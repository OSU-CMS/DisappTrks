#include "DataFormats/PatCandidates/interface/Electron.h"
#include "DataFormats/PatCandidates/interface/Muon.h"
#include "DataFormats/PatCandidates/interface/Tau.h"

#include "DataFormats/TrackReco/interface/Track.h"

using namespace std;

class CandidateTrack : public reco::Track
{
  public:
    CandidateTrack ();
    CandidateTrack (const reco::Track &);
    CandidateTrack (const reco::Track &, const vector<pat::Electron> &, const vector<pat::Muon> &, const vector<pat::Tau> &);
    ~CandidateTrack ();

    const int missingInnerHits () const;
    const int missingMiddleHits () const;
    const int missingOuterHits () const;

    const double deltaRToClosestElectron () const;
    const double deltaRToClosestMuon () const;
    const double deltaRToClosestTau () const;

  private:
    double deltaRToClosestElectron_;
    double deltaRToClosestMuon_;
    double deltaRToClosestTau_;

    template<class T> const double getMinDeltaR (const vector<T> &) const;
};
