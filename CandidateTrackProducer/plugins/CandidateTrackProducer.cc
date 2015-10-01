// -*- C++ -*-
//
// Package:    DisappTrks/CandidateTrackProducer
// Class:      CandidateTrackProducer
//
/**\class CandidateTrackProducer CandidateTrackProducer.cc DisappTrks/CandidateTrackProducer/plugins/CandidateTrackProducer.cc

 Description: Calculates quantities of interest for candidate disappearing tracks.

 Implementation:
   Run this producer with AOD as input, to produce MiniAOD output.


*/
//
// Original Author:  Wells Wulsin
//         Created:  Thu, 17 Sep 2015 09:33:32 GMT
//
//

// user include files
#include "DisappTrks/CandidateTrackProducer/interface/CandidateTrack.h"
#include "DisappTrks/CandidateTrackProducer/plugins/CandidateTrackProducer.h"

//
// constructors and destructor
//
CandidateTrackProducer::CandidateTrackProducer (const edm::ParameterSet& iConfig) :
  tracksTag_ (iConfig.getParameter<edm::InputTag> ("tracks"))
{
  produces<vector<CandidateTrack> > ();
}

CandidateTrackProducer::~CandidateTrackProducer ()
{
}

//
// member functions
//

// ------------ method called to produce the data  ------------
void
CandidateTrackProducer::produce (edm::Event& iEvent, const edm::EventSetup& iSetup)
{
  edm::Handle<vector<reco::Track> > tracks;
  iEvent.getByLabel (tracksTag_, tracks );

  auto_ptr<vector<CandidateTrack> > candTracks (new vector<CandidateTrack> ());
  for (const auto &track : *tracks)
    candTracks->push_back (track);

  // save the vector
  iEvent.put (candTracks);
}

//define this as a plug-in
DEFINE_FWK_MODULE (CandidateTrackProducer);
