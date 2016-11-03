#include "DisappTrks/CandidateTrackProducer/plugins/CandidateTrackToRecoTrack.h"

CandidateTrackToRecoTrack::CandidateTrackToRecoTrack (const edm::ParameterSet &cfg) :
  tracks_ (cfg.getParameter<edm::InputTag> ("tracks"))
{
  produces<vector<reco::Track> > ();
  tracksToken_ = consumes<vector<CandidateTrack> > (tracks_);
}

CandidateTrackToRecoTrack::~CandidateTrackToRecoTrack ()
{
}

void
CandidateTrackToRecoTrack::produce (edm::Event &event, const edm::EventSetup &setup)
{
  edm::Handle<vector<CandidateTrack> > tracks;
  event.getByToken (tracksToken_, tracks);

  unique_ptr<vector<reco::Track> > recoTracks (new vector<reco::Track> ());
  for (const auto &track : *tracks)
    recoTracks->push_back (track);

  event.put (std::move (recoTracks));
}

DEFINE_FWK_MODULE (CandidateTrackToRecoTrack);
