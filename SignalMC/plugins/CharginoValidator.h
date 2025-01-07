#ifndef CHARGINO_VALIDATOR

#define CHARGINO_VALIDATOR

#include <map>
#include <string>

#include "TH1D.h"
#include "TH2D.h"
#include "TLorentzVector.h"

#include <TH1.h>
#include <TH2.h>
#include <TH3.h>
#include "THnSparse.h"
#include "TTree.h"
#include "TGraph.h"
#include "TGraph2D.h"
#include "TVector3.h"

#include "RecoTracker/TrackProducer/plugins/TrackProducer.h"
#include "RecoTracker/TrackProducer/interface/TrackProducerBase.h"
#include <memory>
#include "FWCore/MessageLogger/interface/MessageLogger.h"
#include "TrackingTools/GeomPropagators/interface/Propagator.h"
#include "TrackingTools/PatternTools/interface/Trajectory.h"

#include "TrackingTools/PatternTools/interface/TrajTrackAssociation.h"

#include "DataFormats/TrackerCommon/interface/TrackerTopology.h"
#include "Geometry/Records/interface/TrackerTopologyRcd.h"

#include "FWCore/Framework/interface/Frameworkfwd.h"
#include "FWCore/Framework/interface/stream/EDAnalyzer.h"

#include "FWCore/Framework/interface/ESHandle.h"

#include "DataFormats/TrackReco/interface/TrackBase.h"
#include "DataFormats/TrackReco/interface/TrackExtra.h"
#include "DataFormats/TrackingRecHit/interface/TrackingRecHit.h"
#include "DataFormats/TrackerRecHit2D/interface/BaseTrackerRecHit.h"
#include "DataFormats/TrackingRecHit/interface/TrackingRecHitGlobalState.h"
#include "DataFormats/GeometryCommonDetAlgo/interface/ErrorFrameTransformer.h"
#include "DataFormats/TrackReco/interface/Track.h"
#include "DataFormats/TrackReco/interface/TrackFwd.h"
#include "SimDataFormats/TrackingAnalysis/interface/TrackingParticle.h"
#include "SimDataFormats/TrackingAnalysis/interface/TrackingParticleFwd.h"
#include "CommonTools/UtilAlgos/interface/TFileService.h"
#include "DataFormats/VertexReco/interface/Vertex.h"
#include "DataFormats/VertexReco/interface/VertexFwd.h"
#include "DataFormats/TrackingRecHit/interface/TrackingRecHitFwd.h"
#include "DataFormats/GeometryVector/interface/GlobalPoint.h" 
#include "DataFormats/TrackReco/interface/TrackExtraFwd.h"
#include "DataFormats/DetId/interface/DetId.h" 
#include "Geometry/TrackerGeometryBuilder/interface/TrackerGeometry.h" 
#include "Geometry/Records/interface/TrackerDigiGeometryRecord.h" 
#include "Geometry/TrackerGeometryBuilder/interface/StripGeomDetUnit.h"
#include "DataFormats/TrackerRecHit2D/interface/SiPixelRecHit.h"
#include "DataFormats/SiPixelDetId/interface/PixelSubdetector.h"
#include "Geometry/CommonDetUnit/interface/TrackerGeomDet.h"
#include "DataFormats/GeometrySurface/interface/Surface.h"
#include "DataFormats/HepMCCandidate/interface/GenParticle.h"
#include "DataFormats/Math/interface/deltaR.h"
#include "DataFormats/METReco/interface/GenMET.h"
#include "DataFormats/METReco/interface/GenMETCollection.h"
#include "DataFormats/JetReco/interface/GenJet.h"
#include "DataFormats/JetReco/interface/GenJetCollection.h"
#include "DataFormats/METReco/interface/PFMET.h"
#include "DataFormats/METReco/interface/PFMETCollection.h"
#include "DataFormats/JetReco/interface/PFJet.h"
#include "DataFormats/JetReco/interface/PFJetCollection.h"
#include "DataFormats/MuonReco/interface/Muon.h"
#include "FWCore/Framework/interface/Event.h"
#include "FWCore/Framework/interface/MakerMacros.h"
#include "FWCore/ParameterSet/interface/ParameterSet.h"
#include "FWCore/ServiceRegistry/interface/Service.h"
#include "SimDataFormats/PileupSummaryInfo/interface/PileupSummaryInfo.h"
#include "FWCore/Utilities/interface/InputTag.h"

using namespace std;

class CharginoValidator : public edm::stream::EDAnalyzer<> {
   public:
      explicit CharginoValidator (const edm::ParameterSet &);
      ~CharginoValidator ();

   private:
      void analyze (const edm::Event &, const edm::EventSetup &);

      edm::InputTag genParticles_;
      edm::InputTag genMets_;
      edm::InputTag tracks_;
      edm::InputTag pfmet_;
      edm::InputTag muonsCol_;
      edm::EDGetTokenT<vector<reco::PFMET> > pfmetToken_;
      edm::EDGetTokenT<vector<reco::Track> > tracksToken_;
      edm::EDGetTokenT<vector<reco::GenParticle> > genParticlesToken_;
      edm::EDGetTokenT<reco::GenMETCollection> genMetsToken_;
      edm::EDGetTokenT<vector<reco::Muon> > muonsToken_;

      bool cutPythia8Flag_;

      edm::Service<TFileService> fs_;
      map<string, TH1D *> oneDHists_;
      map<string, TH2D *> twoDHists_;

      void getEndVertex (const reco::GenParticle &, TVector3 &) const;
      const reco::Track * getMatchedTrack (const reco::GenParticle &, const edm::Handle<vector<reco::Track> > &) const;
      unsigned getMatchedTrackNumber (const reco::GenParticle &, const edm::Handle<vector<reco::Track> > &) const;
      const reco::Muon * getMatchedMuon (const reco::GenParticle &, const edm::Handle<vector<reco::Muon> > &) const;
      void logSpace (const unsigned, const double, const double, vector<double> &) const;
};

#endif
