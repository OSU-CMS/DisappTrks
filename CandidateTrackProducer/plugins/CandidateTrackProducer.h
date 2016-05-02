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
#include "FWCore/Framework/interface/EDProducer.h"
#include "FWCore/Framework/interface/Event.h"
#include "FWCore/Framework/interface/MakerMacros.h"
#include "FWCore/ParameterSet/interface/ParameterSet.h"
#include "FWCore/Utilities/interface/InputTag.h"

#include "FWCore/Framework/interface/ESHandle.h"
#include "Geometry/CaloGeometry/interface/CaloGeometry.h"
#include "Geometry/Records/interface/CaloGeometryRecord.h"

#include "DataFormats/EcalRecHit/interface/EcalRecHitCollections.h"
#include "DataFormats/HcalRecHit/interface/HcalRecHitCollections.h" 

using namespace std;

//
// class declaration
//

class CandidateTrackProducer : public edm::EDProducer {
   public:
      explicit CandidateTrackProducer (const edm::ParameterSet&);
      ~CandidateTrackProducer ();

   private:
      virtual void produce (edm::Event&, const edm::EventSetup&) override;
void calculateCaloE(edm::Event& iEvent, const edm::EventSetup& iSetup, CandidateTrack& candTrack, const reco::Track& track, edm::Handle<EBRecHitCollection> EBRecHits, edm::Handle<EERecHitCollection> EERecHits, edm::Handle<HBHERecHitCollection> HBHERecHits);


      // ----------member data ---------------------------
      edm::InputTag tracksTag_;
      edm::InputTag electronsTag_;
      edm::InputTag muonsTag_;
      edm::InputTag tausTag_;
      edm::InputTag beamspotTag_;
      edm::InputTag verticesTag_;
      edm::InputTag conversionsTag_;
      edm::InputTag rhoTag_;
      edm::InputTag rhoCaloTag_;
      edm::InputTag rhoCentralCaloTag_;
      edm::InputTag EBRecHitsTag_; 
      edm::InputTag EERecHitsTag_; 
      edm::InputTag HBHERecHitsTag_; 
      double candMinPt_;
      bool verbose_; 

      edm::EDGetTokenT<vector<reco::Track> >       tracksToken_;
      edm::EDGetTokenT<vector<pat::Electron> >     electronsToken_;
      edm::EDGetTokenT<vector<pat::Muon> >         muonsToken_;
      edm::EDGetTokenT<vector<pat::Tau> >          tausToken_;
      edm::EDGetTokenT<reco::BeamSpot>             beamspotToken_;
      edm::EDGetTokenT<vector<reco::Vertex> >      verticesToken_;
      edm::EDGetTokenT<vector<reco::Conversion> >  conversionsToken_;
      edm::EDGetTokenT<double>                     rhoToken_;
      edm::EDGetTokenT<double>                     rhoCaloToken_;
      edm::EDGetTokenT<double>                     rhoCentralCaloToken_;
      edm::EDGetTokenT<EBRecHitCollection>         EBRecHitsToken_;
      edm::EDGetTokenT<EERecHitCollection>         EERecHitsToken_;
      edm::EDGetTokenT<HBHERecHitCollection>       HBHERecHitsToken_;

  edm::ESHandle<CaloGeometry> caloGeometry_;
  bool insideCone(CandidateTrack& candTrack, const DetId& id, const double dR);
  GlobalPoint getPosition( const DetId& id);

};
