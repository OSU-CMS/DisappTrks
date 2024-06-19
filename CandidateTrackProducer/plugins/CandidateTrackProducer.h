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
#include "FWCore/Framework/interface/stream/EDFilter.h"
#include "FWCore/Framework/interface/Event.h"
#include "FWCore/Framework/interface/MakerMacros.h"
#include "FWCore/ParameterSet/interface/ParameterSet.h"
#include "FWCore/Utilities/interface/InputTag.h"

#include "FWCore/Framework/interface/ESHandle.h"
#include "Geometry/CaloGeometry/interface/CaloGeometry.h"
#include "Geometry/Records/interface/CaloGeometryRecord.h"

#include "DataFormats/TrackReco/interface/DeDxData.h"
#include "DataFormats/EcalRecHit/interface/EcalRecHitCollections.h"
#include "DataFormats/HcalRecHit/interface/HcalRecHitCollections.h"
#include "DataFormats/Common/interface/ValueMap.h"

#include "MagneticField/Engine/interface/MagneticField.h"
#include "MagneticField/Records/interface/IdealMagneticFieldRecord.h"

using namespace std;

//
// class declaration
//

struct CaloEnergy
{
  double eEM;
  double eHad;
};

class CandidateTrackProducer : public edm::stream::EDFilter<> {
   public:
      explicit CandidateTrackProducer (const edm::ParameterSet&);
      ~CandidateTrackProducer ();

   private:
      virtual bool filter (edm::Event&, const edm::EventSetup&) override;
      const CaloEnergy calculateCaloE (const CandidateTrack &, const EBRecHitCollection &, const EERecHitCollection &, const HBHERecHitCollection &, const double dR = 0.5) const;


      // ----------member data ---------------------------
      edm::InputTag tracksTag_;
      edm::InputTag rhoTag_;
      edm::InputTag rhoCaloTag_;
      edm::InputTag rhoCentralCaloTag_;
      edm::InputTag EBRecHitsTag_;
      edm::InputTag EERecHitsTag_;
      edm::InputTag HBHERecHitsTag_;
      edm::InputTag gt2dedxPixelTag_;
      edm::InputTag gt2dedxStripTag_;
      double candMinPt_;
      bool use_dEdx_;

      edm::EDGetTokenT<vector<reco::Track> >       tracksToken_;
      edm::EDGetTokenT<double>                     rhoToken_;
      edm::EDGetTokenT<double>                     rhoCaloToken_;
      edm::EDGetTokenT<double>                     rhoCentralCaloToken_;
      edm::EDGetTokenT<EBRecHitCollection>         EBRecHitsToken_;
      edm::EDGetTokenT<EERecHitCollection>         EERecHitsToken_;
      edm::EDGetTokenT<HBHERecHitCollection>       HBHERecHitsToken_;
      edm::EDGetTokenT<edm::ValueMap<reco::DeDxData> > gt2dedxStripToken_;
      edm::EDGetTokenT<edm::ValueMap<reco::DeDxData> > gt2dedxPixelToken_;
      edm::ESGetToken<MagneticField, IdealMagneticFieldRecord> magFieldToken_;
      edm::ESGetToken<CaloGeometry, CaloGeometryRecord> caloGeometryToken_;

      edm::ESHandle<CaloGeometry> caloGeometry_;
      bool insideCone(const CandidateTrack &, const DetId &, const double) const;
      const GlobalPoint getPosition( const DetId &) const;
};
