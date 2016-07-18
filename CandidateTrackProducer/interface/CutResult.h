#include <string>
#include <vector>

using namespace std;

struct CutResult {
  string name;
  unsigned cumulativePassCount;
  unsigned accumulativePassCount;

  CutResult ():
    name (""),
    cumulativePassCount (0),
    accumulativePassCount (0)
  {
  }

  CutResult (const string &cutName) :
    name (cutName),
    cumulativePassCount (0),
    accumulativePassCount (0)
  {
  }
};

class CutResults : public vector<CutResult>
{
  public:
    CutResults () : triggers_ () {};
    ~CutResults () {};

    const vector<string> &triggers () const { return triggers_; }
    void addTrigger (const string &trigger) { triggers_.push_back (trigger); }
    void addTriggers (const vector<string> &triggers) { triggers_.insert (triggers_.end (), triggers.begin (), triggers.end ()); }

  private:
    vector<string> triggers_;
};
