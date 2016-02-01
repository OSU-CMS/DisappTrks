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
  tracksTag_    (iConfig.getParameter<edm::InputTag> ("tracks")),
  electronsTag_ (iConfig.getParameter<edm::InputTag> ("electrons")),
  muonsTag_     (iConfig.getParameter<edm::InputTag> ("muons")),
  tausTag_      (iConfig.getParameter<edm::InputTag> ("taus")),
  beamspotTag_      (iConfig.getParameter<edm::InputTag> ("beamspot")),
  verticesTag_      (iConfig.getParameter<edm::InputTag> ("vertices")),
  conversionsTag_      (iConfig.getParameter<edm::InputTag> ("conversions")),
  rhoTag_       (iConfig.getParameter<edm::InputTag> ("rhoTag")),
  rhoCaloTag_   (iConfig.getParameter<edm::InputTag> ("rhoCaloTag")),
  rhoCentralCaloTag_(iConfig.getParameter<edm::InputTag> ("rhoCentralCaloTag")),
  candMinPt_    (iConfig.getParameter<double> ("candMinPt"))
{
  produces<vector<CandidateTrack> > ();

  tracksToken_          =  consumes<vector<reco::Track> >       (tracksTag_);
  electronsToken_       =  consumes<vector<pat::Electron> >     (electronsTag_);
  muonsToken_           =  consumes<vector<pat::Muon> >         (muonsTag_);
  tausToken_            =  consumes<vector<pat::Tau> >          (tausTag_);
  beamspotToken_        =  consumes<reco::BeamSpot>             (beamspotTag_);
  verticesToken_        =  consumes<vector<reco::Vertex> >      (verticesTag_);
  conversionsToken_     =  consumes<vector<reco::Conversion> >  (conversionsTag_);
  rhoToken_             =  consumes<double>                     (rhoTag_);
  rhoCaloToken_         =  consumes<double>                     (rhoCaloTag_);
  rhoCentralCaloToken_  =  consumes<double>                     (rhoCentralCaloTag_);

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
  iEvent.getByToken (tracksToken_, tracks );
  edm::Handle<vector<pat::Electron> > electrons;
  iEvent.getByToken (electronsToken_, electrons );
  edm::Handle<vector<pat::Muon> > muons;
  iEvent.getByToken (muonsToken_, muons );
  edm::Handle<vector<pat::Tau> > taus;
  iEvent.getByToken (tausToken_, taus );
  edm::Handle<reco::BeamSpot> beamspot;
  iEvent.getByToken (beamspotToken_, beamspot );
  edm::Handle<vector<reco::Vertex> > vertices;
  iEvent.getByToken (verticesToken_, vertices );
  edm::Handle<vector<reco::Conversion> > conversions;
  iEvent.getByToken (conversionsToken_, conversions );
  edm::Handle<double> rhoHandle;
  iEvent.getByToken (rhoToken_, rhoHandle );
  edm::Handle<double> rhoCaloHandle;
  iEvent.getByToken (rhoCaloToken_, rhoCaloHandle );
  edm::Handle<double> rhoCentralCaloHandle;
  iEvent.getByToken (rhoCentralCaloToken_, rhoCentralCaloHandle );

  edm::ESHandle<MagneticField> magneticField;
  iSetup.get<IdealMagneticFieldRecord>().get(magneticField);


  auto_ptr<vector<CandidateTrack> > candTracks (new vector<CandidateTrack> ());
  for (const auto &track : *tracks) {
    if (track.pt () < candMinPt_)
      continue;

    CandidateTrack candTrack(track, *tracks, *electrons, *muons, *taus, *beamspot, *vertices, conversions);
    calculateCaloE(iEvent, iSetup, candTrack, track);
    candTrack.set_rhoPUCorr(*rhoHandle);
    candTrack.set_rhoPUCorrCalo(*rhoCaloHandle);
    candTrack.set_rhoPUCorrCentralCalo(*rhoCentralCaloHandle);
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

  TrackDetMatchInfo info = trackAssociator_.associate(iEvent, iSetup, trackAssociator_.getFreeTrajectoryState(iSetup, candTrack), parameters_);

  candTrack.set_caloEMDRp3 (info.coneEnergy(0.3, TrackDetMatchInfo::EcalRecHits));
  candTrack.set_caloHadDRp3(info.coneEnergy(0.3, TrackDetMatchInfo::HcalRecHits));
  candTrack.set_caloEMDRp5 (info.coneEnergy(0.5, TrackDetMatchInfo::EcalRecHits));
  candTrack.set_caloHadDRp5(info.coneEnergy(0.5, TrackDetMatchInfo::HcalRecHits));

}

//define this as a plug-in
DEFINE_FWK_MODULE (CandidateTrackProducer);
