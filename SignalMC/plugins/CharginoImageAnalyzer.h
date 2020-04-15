#ifndef CHARGINO_IMAGE_ANALYZER

#define CHARGINO_IMAGE_ANALYZER

#include <map>
#include <string>

#include "TTree.h"

#include "TH1D.h"
#include "TH2D.h"
#include "TVector3.h"
#include "TLorentzVector.h"

#include "CommonTools/UtilAlgos/interface/TFileService.h"

#include "DataFormats/HepMCCandidate/interface/GenParticle.h"
#include "DataFormats/PatCandidates/interface/PackedCandidate.h"

#include "FWCore/Framework/interface/ESHandle.h"
#include "Geometry/CaloGeometry/interface/CaloGeometry.h"
#include "Geometry/Records/interface/CaloGeometryRecord.h"
#include "DataFormats/EcalRecHit/interface/EcalRecHitCollections.h"
#include "DataFormats/HcalRecHit/interface/HcalRecHitCollections.h"

#include "DataFormats/Math/interface/deltaPhi.h"

#include "FWCore/Framework/interface/EDAnalyzer.h"
#include "FWCore/Framework/interface/Event.h"
#include "FWCore/Framework/interface/MakerMacros.h"
#include "FWCore/ParameterSet/interface/ParameterSet.h"
#include "FWCore/ServiceRegistry/interface/Service.h"
#include "FWCore/Utilities/interface/InputTag.h"

using namespace std;

class CharginoImageAnalyzer : public edm::EDAnalyzer {
   public:
      explicit CharginoImageAnalyzer (const edm::ParameterSet &);
      ~CharginoImageAnalyzer ();

   private:
      void analyze (const edm::Event &, const edm::EventSetup &);

      void getImage(const reco::GenParticle &, const EBRecHitCollection &, const EERecHitCollection &, const HBHERecHitCollection &, vector<vector<double> > &, vector<vector<double> > &) const;
      const math::XYZVector getPosition(const DetId &) const;

      edm::InputTag genParticles_;
      edm::InputTag EBRecHitsTag_;
      edm::InputTag EERecHitsTag_;
      edm::InputTag HBHERecHitsTag_;

      edm::EDGetTokenT<vector<reco::GenParticle> > genParticlesToken_;

      edm::EDGetTokenT<EBRecHitCollection>         EBRecHitsToken_;
      edm::EDGetTokenT<EERecHitCollection>         EERecHitsToken_;
      edm::EDGetTokenT<HBHERecHitCollection>       HBHERecHitsToken_;

      edm::ESHandle<CaloGeometry> caloGeometry_;

      edm::Service<TFileService> fs_;
      TTree * tree_;
      TH2D * averageImage_;

      double x_lo, x_hi, y_lo, y_hi;
      int n_x, n_y;
};

#endif
