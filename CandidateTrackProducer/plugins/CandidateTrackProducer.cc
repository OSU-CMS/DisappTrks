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

#include "MagneticField/Engine/interface/MagneticField.h"
#include "MagneticField/Records/interface/IdealMagneticFieldRecord.h"

using namespace std;  

//
// constructors and destructor
//
CandidateTrackProducer::CandidateTrackProducer (const edm::ParameterSet& iConfig) :
  tracksTag_ (iConfig.getParameter<edm::InputTag> ("tracks")), 
  candMinPt_ (iConfig.getParameter<double> ("candMinPt"))
{
  produces<vector<CandidateTrack> > ();

  edm::ParameterSet parameters = iConfig.getParameter<edm::ParameterSet>("TrackAssociatorParameters");
  edm::ConsumesCollector iC = consumesCollector();
  parameters_.loadParameters( parameters, iC);
  trackAssociator_.useDefaultPropagator();

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



  edm::ESHandle<MagneticField> magneticField;
  iSetup.get<IdealMagneticFieldRecord>().get(magneticField);


  auto_ptr<vector<CandidateTrack> > candTracks (new vector<CandidateTrack> ());
  for (const auto &track : *tracks) {

    CandidateTrack candTrack(track);  
    if (candTrack.pt() > candMinPt_) { 
      calculateCaloE(iEvent, iSetup, candTrack, track);  
    }  
    candTracks->push_back (candTrack);  

  }

  // save the vector
  iEvent.put (candTracks);
}


void
CandidateTrackProducer::calculateCaloE (edm::Event& iEvent, const edm::EventSetup& iSetup, CandidateTrack& candTrack, const reco::Track& track) 
{

  // Use as example:
  // https://github.com/cms-sw/cmssw/blob/CMSSW_7_4_X/TrackingTools/TrackAssociator/test/TestTrackAssociator.cc
  // https://github.com/cms-sw/cmssw/blob/CMSSW_7_4_X/TrackingTools/TrackAssociator/test/TestTrackAssociator.py

  std::cout << "Running calculateCaloE" << std::endl;  
  TrackDetMatchInfo info = trackAssociator_.associate(iEvent, iSetup, trackAssociator_.getFreeTrajectoryState(iSetup, candTrack), parameters_);

  candTrack.set_caloEMDeltaRp3 (info.coneEnergy(0.3, TrackDetMatchInfo::EcalRecHits));
  candTrack.set_caloHadDeltaRp3(info.coneEnergy(0.3, TrackDetMatchInfo::HcalRecHits));
  candTrack.set_caloEMDeltaRp5 (info.coneEnergy(0.5, TrackDetMatchInfo::EcalRecHits));
  candTrack.set_caloHadDeltaRp5(info.coneEnergy(0.5, TrackDetMatchInfo::HcalRecHits)); 

}

//define this as a plug-in
DEFINE_FWK_MODULE (CandidateTrackProducer);
