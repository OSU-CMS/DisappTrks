#include "DataFormats/TrackReco/interface/Track.h"

using namespace std;

class CandidateTrack : public reco::Track
{
   public:
      CandidateTrack ();
      CandidateTrack (const reco::Track &);
      ~CandidateTrack ();

      const int missingInnerHits () const;
      const int missingMiddleHits () const;
      const int missingOuterHits () const;
};
