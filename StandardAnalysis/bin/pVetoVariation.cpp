#include <iostream>
#include <random>
#include <chrono>
#include <vector>

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

void
logSpace (const double a, const double b, const unsigned n, vector<double> &bins)
{
  double step = (b - a) / ((double) n);

  bins.clear ();
  for (double i = a; i < b + 0.5 * step; i += step)
    bins.push_back (pow (10.0, i));
}

int
main ()
{
  unsigned events;
  double pVeto, maxContamination, maxTauMisidentification;

  cout << "number of events: ";
  cin >> events;
  cout << "P_veto: ";
  cin >> pVeto;
  cout << "max tau misidentification: ";
  cin >> maxTauMisidentification;
  cout << "max contamination: ";
  cin >> maxContamination;
  cout << endl;

  unsigned seed = std::chrono::system_clock::now().time_since_epoch().count();
  default_random_engine generator (seed);
  uniform_real_distribution<double> distributionPiTau (1.0 - maxTauMisidentification, 1.0),
                                    distributionFE (1.0 - maxContamination, 1.0);
  double piE, piTau, fE;
  unsigned outputEvery = (unsigned) round (events / 62.0);

  vector<double> bins;
  logSpace (-8, -1, 10000, bins);
  TH1D *hPiE = new TH1D ("piE", ";#Pi_{e-veto}^{e}", bins.size () - 1, bins.data ());

  cout << "throwing events";
  cout.flush ();
  for (unsigned i = 0; i < events; i++)
    {
      printDot (i, outputEvery);
      piTau = distributionPiTau (generator);
      fE = distributionFE (generator);

      piE = (pVeto + (fE - 1.0) * piTau) / fE;
      if (piE < 0.0 || piE > 1.0)
        continue;

      if (piE < 1.0e-7)
        cout << "piTau: " << piTau << ", fE: " << fE << " ==> piE: " << piE << endl;

      hPiE->Fill (piE);
    }
  cout << endl << endl;

  TFile *fout = new TFile ("pVetoVariation.root", "recreate");
  fout->cd ();
  hPiE->Write ();
  fout->Close ();

  cout << "Done." << endl;

  return 0;
}
