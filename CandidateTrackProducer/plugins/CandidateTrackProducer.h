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
#include "FWCore/Framework/interface/EDFilter.h"
#include "FWCore/Framework/interface/Event.h"
#include "FWCore/Framework/interface/MakerMacros.h"
#include "FWCore/ParameterSet/interface/ParameterSet.h"
#include "FWCore/Utilities/interface/InputTag.h"

#include "FWCore/Framework/interface/ESHandle.h"
#include "Geometry/CaloGeometry/interface/CaloGeometry.h"
#include "Geometry/Records/interface/CaloGeometryRecord.h"

#include "DataFormats/EcalRecHit/interface/EcalRecHitCollections.h"
#include "DataFormats/HcalRecHit/interface/HcalRecHitCollections.h"
#include "DataFormats/PatCandidates/interface/IsolatedTrack.h"

using namespace std;

//
// class declaration
//

struct CaloEnergy
{
  double eEM;
  double eHad;
};

class CandidateTrackProducer : public edm::EDFilter {
   public:
      explicit CandidateTrackProducer (const edm::ParameterSet&);
      ~CandidateTrackProducer ();

   private:
      virtual bool filter (edm::Event&, const edm::EventSetup&) override;
      const CaloEnergy calculateCaloE (const CandidateTrack &, const EBRecHitCollection &, const EERecHitCollection &, const HBHERecHitCollection &, const double dR = 0.5) const;


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
      edm::InputTag PackedCandidateCollectionTag_;
      edm::InputTag LostTracksCollectionTag_;
      edm::InputTag IsolatedTracksTag_;
      edm::InputTag generalTracksTag_;            
      edm::InputTag gt2pcTag_;
      edm::InputTag gt2ltTag_;
      edm::InputTag gt2itTag_;

      double candMinPt_;

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
      edm::EDGetTokenT<pat::PackedCandidateCollection> PackedCandidateCollectionToken_;
      edm::EDGetTokenT<pat::PackedCandidateCollection> LostTracksCollectionToken_;
      edm::EDGetTokenT<vector<pat::IsolatedTrack> >    IsolatedTracksToken_;
      edm::EDGetTokenT<reco::TrackCollection>                             generalTracksToken_;
      edm::EDGetTokenT<edm::Association<pat::PackedCandidateCollection> > gt2pc_;
      edm::EDGetTokenT<edm::Association<pat::PackedCandidateCollection> > gt2lt_;
      edm::EDGetTokenT<edm::Association<vector<pat::IsolatedTrack> > >    gt2it_;

  edm::ESHandle<CaloGeometry> caloGeometry_;
  bool insideCone(const CandidateTrack &, const DetId &, const double) const;
  const GlobalPoint getPosition( const DetId &) const;
};
