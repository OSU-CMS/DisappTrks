#include "DataFormats/Common/interface/Wrapper.h"

#include "DisappTrks/CandidateTrackProducer/interface/CandidateTrack.h"

namespace {
  struct DisappTrks_CandidateTrackProducer {
    CandidateTrack                         candidateTrack0;
    vector<CandidateTrack>                 candidateTrack1;
    edm::Wrapper<CandidateTrack>           candidateTrack2;
    edm::Wrapper<vector<CandidateTrack> >  candidateTrack3;
  };
}
