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

#include "TrackingTools/TrackAssociator/interface/TrackDetectorAssociator.h"
#include "TrackingTools/TrackAssociator/interface/TrackAssociatorParameters.h"

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
      void calculateCaloE(edm::Event& iEvent, const edm::EventSetup& iSetup, CandidateTrack& candTrack, const reco::Track& track);

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
      double candMinPt_;

      TrackDetectorAssociator trackAssociator_;
      TrackAssociatorParameters parameters_;

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
};
