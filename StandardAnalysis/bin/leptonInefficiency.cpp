#include <iostream>
#include <random>

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
  unsigned events;

  cout << "input inefficiency: ";
  cin >> leptonInefficiency;
  cout << "number of events to generate: ";
  cin >> events;
  cout << endl;

  default_random_engine generator (time (NULL));
  uniform_real_distribution<double> distribution (0.0, 1.0);
  double x = 0.0, y = 0.0, dx, dy, measuredInefficiency, measuredInefficiencyError, correctedInefficiency, correctedInefficiencyError;
  unsigned outputEvery = (unsigned) round (events / 62.0);

  cout << "generating events";
  cout.flush ();
  for (unsigned i = 0; i < events; i++)
    {
      printDot (i, outputEvery);

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
  cout << endl << endl;

  dx = sqrt (x);
  dy = sqrt (y);

  measuredInefficiency = x / y;
  measuredInefficiencyError = hypot (dx * y, x * dy) / (y * y);
  correctedInefficiency = x / (2.0 * y - x);
  correctedInefficiencyError = 2.0 * hypot (dx * y, x * dy) / ((2.0 * y - x) * (2.0 * y - x));

  cout << "input inefficiency:     " << leptonInefficiency << endl;
  cout << "measured inefficiency:  " << x << " / " << y << " = " << measuredInefficiency << " +- " << measuredInefficiencyError << endl;
  cout << "|input - measured|:     " << fabs (measuredInefficiency - leptonInefficiency) / measuredInefficiencyError << " sigma" << endl;
  cout << "corrected inefficiency: " << x << " / " << (2.0 * y - x) << " = " << correctedInefficiency << " +- " << correctedInefficiencyError << endl;
  cout << "|input - corrected|:    " << fabs (correctedInefficiency - leptonInefficiency) / correctedInefficiencyError << " sigma" << endl;

  return 0;
}
