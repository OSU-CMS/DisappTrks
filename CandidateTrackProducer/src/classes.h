#include "DataFormats/Common/interface/Wrapper.h"

#include "DisappTrks/CandidateTrackProducer/interface/CandidateTrack.h"
#include "DisappTrks/CandidateTrackProducer/interface/CutResult.h"

namespace {
  struct DisappTrks_CandidateTrackProducer {
    CandidateTrack                         candidateTrack0;
    vector<CandidateTrack>                 candidateTrack1;
    edm::Wrapper<CandidateTrack>           candidateTrack2;
    edm::Wrapper<vector<CandidateTrack> >  candidateTrack3;

    CutResult                         cutResult0;
    vector<CutResult>                 cutResult1;
    edm::Wrapper<CutResult>           cutResult2;
    edm::Wrapper<vector<CutResult> >  cutResult3;

    CutResults                         cutResults0;
    vector<CutResults>                 cutResults1;
    edm::Wrapper<CutResults>           cutResults2;
    edm::Wrapper<vector<CutResults> >  cutResults3;

    edm::Association<std::vector<pat::IsolatedTrack> > 		association0;
    edm::Wrapper<edm::Association<std::vector<pat::IsolatedTrack> > > association1;

  };
}
