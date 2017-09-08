#include <iostream>
#include <random>
#include <chrono>

#include "TH1D.h"
#include "TFile.h"

using namespace std;

inline void
printDot (const unsigned i, const unsigned outputEvery)
{
  if (outputEvery > 0)
    {
      if (!(i % outputEvery))
        cout << ".";
    }
  else
    cout << ".";
  cout.flush ();
}

int
main ()
{
  double leptonInefficiency;
  unsigned trials, events;

  cout << "input inefficiency: ";
  cin >> leptonInefficiency;
  cout << "number of experiments to run: ";
  cin >> trials;
  cout << "number of events per experiment: ";
  cin >> events;
  cout << endl;

  unsigned seed = std::chrono::system_clock::now().time_since_epoch().count();
  default_random_engine generator (seed);
  uniform_real_distribution<double> distribution (0.0, 1.0);
  double x, y, dx, dy, measuredInefficiency, measuredInefficiencyError, correctedInefficiency, correctedInefficiencyError;
  unsigned outputEvery = (unsigned) round (trials / 62.0);

  TH1D *measured = new TH1D ("measuredInefficiency", ";measured inefficiency", 1000, 0.0, 1.0),
       *measuredPull = new TH1D ("measuredInefficiencyPull", ";pull measured inefficiency", 1000, -100.0, 100.0),
       *corrected = new TH1D ("correctedInefficiency", ";measured inefficiency with correction", 1000, 0.0, 1.0),
       *correctedPull = new TH1D ("correctedInefficiencyPull", ";pull of measured inefficiency with correction", 1000, -100.0, 100.0);

  cout << "running experiments";
  cout.flush ();
  for (unsigned i = 0; i < trials; i++)
    {
      x = y = 0.0;
      printDot (i, outputEvery);
      for (unsigned j = 0; j < events; j++)
        {
          double lepton0 = distribution (generator),
                 lepton1 = distribution (generator);
          if (lepton0 > leptonInefficiency && lepton1 > leptonInefficiency) // both leptons reconstructed
            y++;
          else if (lepton0 < leptonInefficiency && lepton1 < leptonInefficiency); // neither lepton reconstructed
          else // exactly one lepton reconstructed
            {
              x++;
              y++;
            }
        }
      dx = sqrt (x);
      dy = sqrt (y);

      measuredInefficiency = x / y;
      measuredInefficiencyError = hypot (dx * y, x * dy) / (y * y);
      correctedInefficiency = x / (2.0 * y - x);
      correctedInefficiencyError = 2.0 * hypot (dx * y, x * dy) / ((2.0 * y - x) * (2.0 * y - x));

      measured->Fill (measuredInefficiency);
      measuredPull->Fill ((measuredInefficiency - leptonInefficiency) / measuredInefficiencyError);
      corrected->Fill (correctedInefficiency);
      correctedPull->Fill ((correctedInefficiency - leptonInefficiency) / correctedInefficiencyError);
    }
  cout << endl << endl;

  TFile *fout = new TFile ("leptonInefficiency.root", "recreate");
  fout->cd ();
  measured->Write ();
  measuredPull->Write ();
  corrected->Write ();
  correctedPull->Write ();
  fout->Close ();

  cout << "Done." << endl;

  return 0;
}
