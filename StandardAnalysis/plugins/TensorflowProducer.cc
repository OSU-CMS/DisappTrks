#ifndef TENSORFLOW_PRODUCER
#define TENSORFLOW_PRODUCER
// -*- C++ -*-
//
// Package:    DisappTrks/StandardAnalysis
// Class:      TensorflowProducer
//
/**\class TensorflowProducer TensorflowProducer.cc DisappTrks/StandardAnalysis/plugins/TensorflowProducer.cc

 Description: [one line class summary]

 Implementation:
     [Notes on implementation]
*/
//
// Original Author:  Michael Carrigan
//         Created:  Thu, 17 Nov 2022 19:04:06 GMT
//
//

// system include files
#include <memory>

// user include files
#include "FWCore/Framework/interface/Frameworkfwd.h"
#include "FWCore/Framework/interface/stream/EDProducer.h"

#include "FWCore/Framework/interface/Event.h"
#include "FWCore/Framework/interface/MakerMacros.h"

#include "FWCore/ParameterSet/interface/ParameterSet.h"
#include "FWCore/Utilities/interface/StreamID.h"

#include "PhysicsTools/TensorFlow/interface/TensorFlow.h"

#include "TTree.h"
#include "CommonTools/UtilAlgos/interface/TFileService.h"

#include "DataFormats/Math/interface/deltaPhi.h"
#include "DataFormats/TrackReco/interface/DeDxHitInfo.h"
#include "RecoTracker/DeDx/interface/DeDxTools.h"
#include "DataFormats/TrackReco/interface/DeDxData.h"
#include "DataFormats/PatCandidates/interface/IsolatedTrack.h"
#include "DataFormats/GeometryVector/interface/LocalPoint.h"

#include "DataFormats/TrackerCommon/interface/TrackerTopology.h"

//Pileup Info
#include "SimDataFormats/PileupSummaryInfo/interface/PileupSummaryInfo.h"

#include "FWCore/ServiceRegistry/interface/Service.h"
#include "FWCore/Utilities/interface/InputTag.h"
#include <map>

#include "DisappTrksML/TreeMaker/interface/Infos.h"

#include "DisappTrks/CandidateTrackProducer/interface/CandidateTrack.h"
#include "OSUT3Analysis/AnaTools/interface/EventVariableProducer.h"
#include "DisappTrks/StandardAnalysis/interface/NetworkOutput.h"

// Tensorflow
#include "PhysicsTools/TensorFlow/interface/TensorFlow.h"

// MINIAOD
#include "DataFormats/HepMCCandidate/interface/GenParticle.h"
#include "DataFormats/PatCandidates/interface/Electron.h"
#include "DataFormats/PatCandidates/interface/Jet.h"
#include "DataFormats/PatCandidates/interface/MET.h"
#include "DataFormats/PatCandidates/interface/Muon.h"
#include "DataFormats/PatCandidates/interface/PackedGenParticle.h"
#include "DataFormats/PatCandidates/interface/Tau.h"
#include "DataFormats/PatCandidates/interface/TriggerObjectStandAlone.h"
#include "DataFormats/VertexReco/interface/Vertex.h"
#include "DataFormats/PatCandidates/interface/PackedCandidate.h"
#include "DataFormats/Common/interface/TriggerResults.h"
#include "FWCore/Common/interface/TriggerNames.h"

// recHits
#include "FWCore/Framework/interface/ESHandle.h"
#include "Geometry/CaloGeometry/interface/CaloGeometry.h"
#include "Geometry/Records/interface/CaloGeometryRecord.h"
#include "Geometry/CaloGeometry/interface/CaloSubdetectorGeometry.h"
#include "Geometry/CaloGeometry/interface/CaloCellGeometry.h"

#include "CondFormats/EcalObjects/interface/EcalChannelStatus.h"
#include "CondFormats/DataRecord/interface/EcalChannelStatusRcd.h"

#include "DataFormats/EcalRecHit/interface/EcalRecHitCollections.h"
#include "DataFormats/HcalRecHit/interface/HcalRecHitCollections.h"

//
// class declaration
//

enum DetType { None, EB, EE, ES, HCAL, CSC, DT, RPC };

struct CacheData {
  CacheData() : graphDef(nullptr) {}
  std::atomic<tensorflow::GraphDef*> graphDef;
};

class TensorflowProducer : public edm::stream::EDProducer<edm::GlobalCache<CacheData>> {
public:
  explicit TensorflowProducer(const edm::ParameterSet &, const CacheData*);

  ~TensorflowProducer() override;

  static void fillDescriptions(edm::ConfigurationDescriptions& descriptions);
  static std::unique_ptr<CacheData> initializeGlobalCache(const edm::ParameterSet&);
  static void globalEndJob(const CacheData*);

private:
  void beginStream(edm::StreamID) override;
  void produce(edm::Event&, const edm::EventSetup&) override;
  void endStream() override;

  int getDetectorIndex(const int) const;

  void getGeometries(const edm::EventSetup &);
  /*void findMatchedIsolatedTrack (const edm::Handle<vector<pat::IsolatedTrack> >&isolatedTracks, 
                                  edm::Ref<vector<pat::IsolatedTrack> >&matchedIsolatedTrack, 
                                  double &dRToMatchedIsolatedTrack, const CandidateTrack &track) const;
  void findMatchedGenTrack (const edm::Handle<vector<reco::Track> >&genTracks,
                                  edm::Ref<vector<reco::Track> >&matchedGenTrack,
                                  double &dRToMatchedGenTrack, const CandidateTrack &track) const;*/
  int countGoodPrimaryVertices(const vector<reco::Vertex> &) const;
  int countGoodJets(const vector<pat::Jet> &) const;
  double getMaxDijetDeltaPhi(const vector<pat::Jet> &) const;
  double getLeadingJetMetPhi(const vector<pat::Jet> &, const pat::MET &) const;

  void getTracks(const reco::Vertex &, 
                  const vector<pat::Jet> &,
                  const vector<pat::Electron> &,
                  const vector<pat::Muon> &,
                  const vector<pat::Tau> &,
                  const vector<pat::Electron> &tagElectrons,
                  const vector<pat::Muon> &tagMuons,
                  const pat::MET &, 
                  const edm::Handle<vector<pat::IsolatedTrack> >, 
                  const edm::Handle<reco::DeDxHitInfoAss>,
                  const edm::Handle<edm::ValueMap<reco::DeDxData> > dEdxStrip,
                  const edm::Handle<edm::ValueMap<reco::DeDxData> > dEdxPixel);

  void getRecHits(const edm::Event &);
  void getGenParticles(const reco::CandidateView &);

  const math::XYZVector getPosition(const DetId &) const;
  //const math::XYZVector getPosition(const CSCSegment&) const;
  //const math::XYZVector getPosition(const CSCRecHit2D&) const;
  //const math::XYZVector getPosition(const DTRecSegment4D&) const;
  //const math::XYZVector getPosition(const DTRecHit1D&) const;
  //const math::XYZVector getPosition(const RPCRecHit&) const;

  vector<pat::Electron> getTagElectrons(const edm::Event &,
                                        const edm::TriggerResults &,
                                        const vector<pat::TriggerObjectStandAlone> &,
                                        const reco::Vertex &,
                                        const vector<pat::Electron> &);

  vector<pat::Muon> getTagMuons(const edm::Event &,
                                const edm::TriggerResults &,
                                const vector<pat::TriggerObjectStandAlone> &,
                                const reco::Vertex &,
                                const vector<pat::Muon> &);

  const bool isProbeTrack(const TrackInfo) const;

  // bit values reflect tag+probe status and charge products:
  //     0b<in same-sign pair><in opposite-sign pair>
  //     So 0 = 0b00 : not in any TP pair
  //        1 = 0b01 : in OS TP pair
  //        2 = 0b10 : in SS TP pair
  //        3 = 0b11 : in both an OS and SS pair
  const unsigned int isTagProbeElePair(const pat::IsolatedTrack &, const pat::Electron &) const;
  const unsigned int isTagProbeMuonPair(const pat::IsolatedTrack &, const pat::Muon &) const;
  const unsigned int isTagProbeTauToElePair(const pat::IsolatedTrack &, const pat::Electron &, const pat::MET &) const;
  const unsigned int isTagProbeTauToMuonPair(const pat::IsolatedTrack &, const pat::Muon &, const pat::MET &) const;

  const double minDRBadEcalChannel(const pat::IsolatedTrack &) const;
  void getChannelStatusMaps();

  std::vector<std::vector<double>> getHitMap(const vector<TrackDeDxInfo>) const;
  std::pair<double, double> getMaxHits(const vector<TrackDeDxInfo>) const;
  unsigned long encodeLayers(const std::vector<std::vector<double>>) const;
  std::pair<std::array<double, 3>, std::array<double, 3>> getClosestVertices(const std::vector<VertexInfo>, float track_vz, float track_vx, float track_vy) const;


  std::string graphPath_;
  std::string inputTensorName_;
  std::string inputTrackTensorName_;
  std::string outputTensorName_;

  tensorflow::GraphDef* graphDef_;
  tensorflow::Session* session_;

  tensorflow::Tensor input_;

  edm::InputTag triggers_;
  edm::InputTag trigObjs_;
  edm::InputTag genParticles_;
  edm::InputTag met_;
  edm::InputTag electrons_, muons_, taus_;
  edm::InputTag pfCandidates_;
  edm::InputTag vertices_;
  edm::InputTag jets_;
  edm::InputTag rhoCentralCalo_;
  edm::InputTag EBRecHits_, EERecHits_, ESRecHits_;
  edm::InputTag HBHERecHits_;

  edm::InputTag dEdxPixel_;
  edm::InputTag dEdxStrip_;
  edm::InputTag isoTrk2dedxHitInfo_;     
  edm::InputTag isoTracks_;
  edm::InputTag pileupInfo_;

  edm::EDGetTokenT<edm::TriggerResults>                   triggersToken_;
  edm::EDGetTokenT<vector<pat::TriggerObjectStandAlone> > trigObjsToken_;
  edm::EDGetTokenT<reco::CandidateView>                   genParticlesToken_;
  edm::EDGetTokenT<vector<pat::MET> >                     metToken_;
  edm::EDGetTokenT<vector<pat::Electron> >                electronsToken_;
  edm::EDGetTokenT<vector<pat::Muon> >                    muonsToken_;
  edm::EDGetTokenT<vector<pat::Tau> >                     tausToken_;
  edm::EDGetTokenT<vector<pat::PackedCandidate> >         pfCandidatesToken_;
  edm::EDGetTokenT<vector<reco::Vertex> >                 verticesToken_;
  edm::EDGetTokenT<vector<pat::Jet> >                     jetsToken_;

  edm::EDGetTokenT<double> rhoCentralCaloToken_;

  edm::EDGetTokenT<EBRecHitCollection>         EBRecHitsToken_;
  edm::EDGetTokenT<EERecHitCollection>         EERecHitsToken_;
  edm::EDGetTokenT<ESRecHitCollection>         ESRecHitsToken_;
  edm::EDGetTokenT<HBHERecHitCollection>       HBHERecHitsToken_;


  edm::EDGetTokenT<edm::ValueMap<reco::DeDxData> > dEdxPixelToken_;
  edm::EDGetTokenT<edm::ValueMap<reco::DeDxData> > dEdxStripToken_;
  edm::EDGetTokenT<reco::DeDxHitInfoAss> isoTrk2dedxHitInfoToken_;
  edm::EDGetTokenT<vector<pat::IsolatedTrack> >isoTrackToken_;
  edm::EDGetTokenT<edm::View<PileupSummaryInfo> > pileupInfoToken_;
  edm::ESGetToken<CaloGeometry, CaloGeometryRecord> caloGeometryToken_;

  edm::ESGetToken<EcalChannelStatus, EcalChannelStatusRcd> ecalStatusToken_;
  edm::ESGetToken<TrackerTopology, TrackerTopologyRcd> trackerTopologyToken_;


  edm::ESHandle<CaloGeometry> caloGeometry_;


  edm::ESHandle<EcalChannelStatus> ecalStatus_;
  edm::ESHandle<TrackerTopology> trackerTopology_;

  edm::EDPutTokenT<vector<float> > putTokenNetworkScores_;

  //vector<float> networkScores_;
  vector<TrackInfo> trackInfos_;
  vector<RecHitInfo> recHitInfos_;
  vector<GenParticleInfo> genParticleInfos_;
  vector<VertexInfo> vertexInfos_;

  const double minGenParticlePt_;
  const double minTrackPt_;
  const double maxRelTrackIso_;

  const string dataTakingPeriod_;

  // event information  
  int nPV_;
  unsigned long long eventNumber_;
  unsigned int lumiBlockNumber_;
  unsigned int runNumber_;
  vector<float> pileupZPosition_;
  unsigned int numTruePV_;

  // event-wide cut results
  bool firesGrandOrTrigger_;
  bool passMETFilters_;
  int numGoodPVs_;
  double metNoMu_;
  double numGoodJets_;
  double dijetDeltaPhiMax_;
  double leadingJetMetPhi_;

  bool is2017_;

  map<DetId, vector<double> > EcalAllDeadChannelsValMap_;
  map<DetId, vector<int> >    EcalAllDeadChannelsBitMap_;

  vector<string> signalTriggerNames, metFilterNames;

  // recHits range
  double EtaRange_;
  double PhiRange_;
  int maxHits_;

  //void beginRun(edm::Run const&, edm::EventSetup const&) override;
  //virtual void endRun(edm::Run const&, edm::EventSetup const&); 
  //void beginLuminosityBlock(edm::LuminosityBlock const&, edm::EventSetup const&) override;
  //void endLuminosityBlock(edm::LuminosityBlock const&, edm::EventSetup const&) override;

  // ----------member data ---------------------------
};

//
// constants, enums and typedefs
//

//
// static data member definitions
//

//
// constructors and destructor
//
TensorflowProducer::TensorflowProducer(const edm::ParameterSet &config, const CacheData* cacheData)
  : graphPath_(config.getParameter<std::string>("graphPath")),
    inputTensorName_(config.getParameter<std::string>("inputTensorName")),
    inputTrackTensorName_(config.getParameter<std::string>("inputTrackTensorName")),
    outputTensorName_(config.getParameter<std::string>("outputTensorName")),
    session_(tensorflow::createSession(cacheData->graphDef, 4)),
   
    triggers_     (config.getParameter<edm::InputTag> ("triggers")),
    trigObjs_     (config.getParameter<edm::InputTag> ("triggerObjects")),
    genParticles_ (config.getParameter<edm::InputTag> ("genParticles")),
    met_          (config.getParameter<edm::InputTag> ("met")),
    electrons_    (config.getParameter<edm::InputTag> ("electrons")),
    muons_        (config.getParameter<edm::InputTag> ("muons")),
    taus_         (config.getParameter<edm::InputTag> ("taus")),
    pfCandidates_ (config.getParameter<edm::InputTag> ("pfCandidates")),
    vertices_     (config.getParameter<edm::InputTag> ("vertices")),
    jets_         (config.getParameter<edm::InputTag> ("jets")),

    rhoCentralCalo_ (config.getParameter<edm::InputTag> ("rhoCentralCalo")),

    EBRecHits_     (config.getParameter<edm::InputTag> ("EBRecHits")),
    EERecHits_     (config.getParameter<edm::InputTag> ("EERecHits")),
    ESRecHits_     (config.getParameter<edm::InputTag> ("ESRecHits")),
    HBHERecHits_   (config.getParameter<edm::InputTag> ("HBHERecHits")),

    dEdxPixel_ (config.getParameter<edm::InputTag> ("dEdxPixel")),
    dEdxStrip_ (config.getParameter<edm::InputTag> ("dEdxStrip")),
    isoTrk2dedxHitInfo_ (config.getParameter<edm::InputTag> ("isoTrk2dedxHitInfo")),
    isoTracks_ (config.getParameter<edm::InputTag> ("isolatedTracks")),  

    pileupInfo_   (config.getParameter<edm::InputTag>("pileupInfo")),

    minGenParticlePt_   (config.getParameter<double> ("minGenParticlePt")),
    minTrackPt_         (config.getParameter<double> ("minTrackPt")),
    maxRelTrackIso_     (config.getParameter<double> ("maxRelTrackIso")),
    
    dataTakingPeriod_ (config.getParameter<string> ("dataTakingPeriod"))
 {

  //assert(dataTakingPeriod_ == "2017" || dataTakingPeriod_ == "2018" || dataTakingPeriod_ == "2022");
  //is2017_ = (dataTakingPeriod_ == "2017");

  triggersToken_     = consumes<edm::TriggerResults>           (triggers_);
  trigObjsToken_     = consumes<vector<pat::TriggerObjectStandAlone> > (trigObjs_);
  genParticlesToken_ = consumes<reco::CandidateView>           (genParticles_);
  metToken_          = consumes<vector<pat::MET> >             (met_);
  electronsToken_    = consumes<vector<pat::Electron> >        (electrons_);
  muonsToken_        = consumes<vector<pat::Muon> >            (muons_);
  tausToken_         = consumes<vector<pat::Tau> >             (taus_);
  pfCandidatesToken_ = consumes<vector<pat::PackedCandidate> > (pfCandidates_);
  verticesToken_     = consumes<vector<reco::Vertex> >         (vertices_);
  jetsToken_         = consumes<vector<pat::Jet> >             (jets_);

  rhoCentralCaloToken_ = consumes<double> (rhoCentralCalo_);

  EBRecHitsToken_     = consumes<EBRecHitCollection>       (EBRecHits_);
  EERecHitsToken_     = consumes<EERecHitCollection>       (EERecHits_);
  ESRecHitsToken_     = consumes<ESRecHitCollection>       (ESRecHits_);
  HBHERecHitsToken_   = consumes<HBHERecHitCollection>     (HBHERecHits_);
  
  dEdxPixelToken_ = consumes<edm::ValueMap<reco::DeDxData> > (dEdxPixel_);
  dEdxStripToken_ = consumes<edm::ValueMap<reco::DeDxData> > (dEdxStrip_);
  isoTrk2dedxHitInfoToken_ = consumes<reco::DeDxHitInfoAss> (isoTrk2dedxHitInfo_);
  isoTrackToken_ = consumes<vector<pat::IsolatedTrack> > (isoTracks_);
  pileupInfoToken_ = consumes<edm::View<PileupSummaryInfo> > (pileupInfo_);

  caloGeometryToken_    = esConsumes<CaloGeometry, CaloGeometryRecord>();
  ecalStatusToken_         = esConsumes<EcalChannelStatus, EcalChannelStatusRcd>();
  trackerTopologyToken_    = esConsumes<TrackerTopology, TrackerTopologyRcd>();

  signalTriggerNames = config.getParameter<vector<string> >("signalTriggerNames");
  metFilterNames = config.getParameter<vector<string> >("metFilterNames");

  produces<NetworkOutput>("networkScores");
  
  //networkScores_.clear();
  trackInfos_.clear();
  recHitInfos_.clear();
  genParticleInfos_.clear();
  pileupZPosition_.clear();
  vertexInfos_.clear();

}

TensorflowProducer::~TensorflowProducer() {
  // do anything here that needs to be done at destruction time
  // (e.g. close files, deallocate resources etc.)
  //
  // please remove this method altogether if it would be left empty
}

//
// member functions
//

// ------------ method called to produce the data  ------------
void TensorflowProducer::produce(edm::Event& event, const edm::EventSetup& iSetup) {
  using namespace edm;

   // get collections, setup objects
  std::cout << "In tensorflowPlugin analyze method" << std::endl;

  edm::Handle<edm::TriggerResults> triggers;
  event.getByToken (triggersToken_, triggers);

  edm::Handle<vector<pat::TriggerObjectStandAlone> > trigObjs;
  event.getByToken (trigObjsToken_, trigObjs);

  edm::Handle<reco::CandidateView> genParticles;
  event.getByToken(genParticlesToken_, genParticles);

  edm::Handle<vector<pat::MET> > met;
  event.getByToken (metToken_, met);

  edm::Handle<vector<pat::Electron> > electrons;
  event.getByToken(electronsToken_, electrons);

  edm::Handle<vector<pat::Muon> > muons;
  event.getByToken(muonsToken_, muons);

  edm::Handle<vector<pat::Tau> > taus;
  event.getByToken(tausToken_, taus);

  edm::Handle<vector<pat::PackedCandidate> > pfCandidates;
  event.getByToken(pfCandidatesToken_, pfCandidates);

  edm::Handle<vector<reco::Vertex> > vertices;
  event.getByToken(verticesToken_, vertices);

  edm::Handle<vector<pat::Jet> > jets;
  event.getByToken(jetsToken_, jets);

  edm::Handle<double> rhoCentralCalo;
  event.getByToken(rhoCentralCaloToken_, rhoCentralCalo);

  edm::Handle<edm::ValueMap<reco::DeDxData> > dEdxStrip;
  event.getByToken (dEdxStripToken_, dEdxStrip);

  edm::Handle<edm::ValueMap<reco::DeDxData> > dEdxPixel;
  event.getByToken (dEdxPixelToken_, dEdxPixel);

  edm::Handle<reco::DeDxHitInfoAss> isoTrk2dedxHitInfo;
  event.getByToken(isoTrk2dedxHitInfoToken_, isoTrk2dedxHitInfo);

  edm::Handle<vector<pat::IsolatedTrack> > tracks;
  event.getByToken (isoTrackToken_, tracks);

  edm::Handle<edm::View<PileupSummaryInfo> > pileupInfos;
  event.getByToken(pileupInfoToken_, pileupInfos);
 
  const edm::TriggerNames &allTriggerNames = event.triggerNames(*triggers);

  getGeometries(iSetup);
  getChannelStatusMaps();

  TVector2 metNoMuVec(met->at(0).px(), met->at(0).py()); // Get METNoMu

  // Make cut to ensure there are only muons
  for(const auto &pfCandidate : *pfCandidates) {
    if(abs(pfCandidate.pdgId()) != 13) continue;
    TVector2 muon(pfCandidate.px(), pfCandidate.py());
    metNoMuVec += muon;
  }

  metNoMu_ = metNoMuVec.Mod();

  firesGrandOrTrigger_ = false;
  passMETFilters_ = true;

  // Apply Triggers
  for(unsigned i = 0; i < allTriggerNames.size(); i++) {
    string thisName = allTriggerNames.triggerName(i);

    for(auto name : signalTriggerNames) {
      if(thisName.find(name) == 0 && triggers->accept(i)) {
        firesGrandOrTrigger_ = true;
        break;
      }
    }

    for(auto name : metFilterNames) {
      if(thisName.find(name) == 0 && !triggers->accept(i)) {
        passMETFilters_ = false;
        break;
      }
    }

    if(firesGrandOrTrigger_ && !passMETFilters_) break;
  }
  // Get number of primary vertices
  const reco::Vertex &pv = vertices->at(0);
  nPV_ = vertices->size();
  numGoodPVs_ = countGoodPrimaryVertices(*vertices);

  // Get information of all vertices
  vertexInfos_.clear();
  for(auto vertex : *vertices){
      VertexInfo info;
      
      TLorentzVector vertex_pos(vertex.x(), vertex.y(), vertex.z(), vertex.t());
      TLorentzVector vertex_err(vertex.xError(), vertex.yError(), vertex.zError(), vertex.tError());
      info.vertex = vertex_pos;
      info.vertex_error = vertex_err;
      info.chi2 = vertex.chi2();
      info.ndof = vertex.ndof();
      info.isValid = vertex.isValid();     

      vertexInfos_.push_back(info);
  }

  eventNumber_ = event.id().event();
  lumiBlockNumber_ = event.id().luminosityBlock();
  runNumber_ = event.id().run();

  numGoodJets_      = countGoodJets(*jets);
  dijetDeltaPhiMax_ = getMaxDijetDeltaPhi(*jets);
  leadingJetMetPhi_ = getLeadingJetMetPhi(*jets, met->at(0));

  vector<pat::Electron> tagElectrons = getTagElectrons(event, *triggers, *trigObjs, pv, *electrons);
  vector<pat::Muon> tagMuons = getTagMuons(event, *triggers, *trigObjs, pv, *muons);

  getTracks(pv, *jets, *electrons, *muons, *taus, tagElectrons, tagMuons, met->at(0), tracks, isoTrk2dedxHitInfo, dEdxStrip, dEdxPixel);

  if(trackInfos_.size() == 0) return; // only fill tree with passing tracks
  std::cout << "Number of tracks: " << trackInfos_.size() << "event: " << eventNumber_ << std::endl;

  getRecHits(event);
  if(genParticles.isValid()) getGenParticles(*genParticles);

  // account for pileup in track ecalo
  double caloCorr = (*rhoCentralCalo) * 2. * M_PI_2 * 0.5 * 0.5;
  for(auto &info : trackInfos_) {
    info.ecalo -= caloCorr;
    if(info.ecalo < 0) info.ecalo = 0;
  }

  // Get pileup vertex z positions
  if(pileupInfos.isValid()) {
    edm::View<PileupSummaryInfo>::const_iterator iterPU;
    for(edm::View<PileupSummaryInfo>::const_iterator iterPU = pileupInfos->begin(); iterPU != pileupInfos->end(); iterPU++) {
      // Out of time pileup is also saved -> need to require 0th bunch crossing (in time bunch crossing)
      if(iterPU->getBunchCrossing() == 0){ 
        pileupZPosition_ = iterPU->getPU_zpositions();
        numTruePV_ = iterPU->getTrueNumInteractions();
      }
    }
  }

  //std::sort(recHitInfos_.begin(),recHitInfos_.end(),hitInfoOrder());

 tensorflow::Tensor input(tensorflow::DT_FLOAT, {100,4});
  tensorflow::Tensor inputTrack(tensorflow::DT_FLOAT, {1,4});

  auto networkScores_ = std::make_unique<NetworkOutput>(); //(new std::vector<float> ());
  std::vector<float> v_networkScores_;
  //std::unique_ptr<std::vector<std::vector<tensorflow::Tensor> > > networkScores_(new std::vector<std::vector<tensorflow::Tensor> >());

  for(auto &track : trackInfos_)
  {
    inputTrack.matrix<float>()(0, 0) = nPV_;
    inputTrack.matrix<float>()(0, 1) = track.eta;
    inputTrack.matrix<float>()(0, 2) = track.phi;
    inputTrack.matrix<float>()(0, 3) = track.nValidPixelHits;
    std::vector<std::vector<double>> recHitsNearTrack;
    for (auto &hit : recHitInfos_){
      std::vector<double> hitNearTrack;
      double dEta = track.eta - hit.eta;
      double dPhi = track.phi - hit.phi;
      if( fabs(dPhi) > TMath::Pi() ){
        dPhi -= round(dPhi/(2* TMath::Pi()))*2*TMath::Pi();
      }
      if (fabs(dEta) >= EtaRange_ or fabs(dPhi) >= PhiRange_)
      {
        continue;
      }
      int detIndex = getDetectorIndex(hit.detType);
      double energy = 1;
      if (detIndex != 2)
      {
        energy = hit.energy;
      }
      hitNearTrack.push_back(dEta);
      hitNearTrack.push_back(dPhi);
      hitNearTrack.push_back(energy);
      hitNearTrack.push_back(detIndex);

			recHitsNearTrack.push_back(hitNearTrack);
      std::sort(recHitsNearTrack.begin(),recHitsNearTrack.end(),
                [](const std::vector<double>& a, const std::vector<double>& b) {
                  return a[2] > b[2];
                });

      int numRecHits = recHitsNearTrack.size();
      for (int iHit = 0; iHit < min(maxHits_, numRecHits); iHit++)
      {
        input.matrix<float>()(iHit, 0) = recHitsNearTrack.at(iHit)[0];
        input.matrix<float>()(iHit, 1) = recHitsNearTrack.at(iHit)[1];
        input.matrix<float>()(iHit, 2) = recHitsNearTrack.at(iHit)[2];
        input.matrix<float>()(iHit, 3) = recHitsNearTrack.at(iHit)[3];
      }
      if (numRecHits < maxHits_){
        for (int iHit = numRecHits; iHit < maxHits_; iHit++)
        {
          input.matrix<float>()(iHit, 0) = 0;
          input.matrix<float>()(iHit, 1) = 0;
          input.matrix<float>()(iHit, 2) = 0;
          input.matrix<float>()(iHit, 3) = 0;
        }
      }
    }
    std::vector<tensorflow::Tensor> outputs;
    tensorflow::run(session_, {{inputTensorName_, input},{inputTrackTensorName_, inputTrack}}, {outputTensorName_}, &outputs);

    // print the output
    std::cout << " -> " << outputs[0].matrix<float>()(0, 0) << std::endl << std::endl;
    float score = outputs[0].matrix<float>()(0,0);
    v_networkScores_.push_back(score);
  }
}

// ------------ method called once each stream before processing any runs, lumis or events  ------------
void TensorflowProducer::beginStream(edm::StreamID) {
  // please remove this method if not needed
}

// ------------ method called once each stream after processing all runs, lumis and events  ------------
void TensorflowProducer::endStream() {
  // please remove this method if not needed
}

// ------------ method called when starting to processes a run  ------------
/*
void
TensorflowProducer::beginRun(edm::Run const&, edm::EventSetup const&)
{
}
*/

// ------------ method called when ending the processing of a run  ------------

/*void TensorflowProducer::endRun(const edm::Run& Run, const edm::EventSetup& setup) {
  // close the session
  tensorflow::closeSession(session_);
}*/

// ------------ method called when starting to processes a luminosity block  ------------
/*
void
TensorflowProducer::beginLuminosityBlock(edm::LuminosityBlock const&, edm::EventSetup const&)
{
}
*/

// ------------ method called when ending the processing of a luminosity block  ------------
/*
void
TensorflowProducer::endLuminosityBlock(edm::LuminosityBlock const&, edm::EventSetup const&)
{
}
*/

// ------------ method fills 'descriptions' with the allowed parameters for the module  ------------
void TensorflowProducer::fillDescriptions(edm::ConfigurationDescriptions& descriptions) {
  //The following says we do not know what parameters are allowed so do no validation
  // Please change this to state exactly what you do use, even if it is no parameters
  edm::ParameterSetDescription desc;
  desc.add<std::string>("graphPath");
  desc.add<std::string>("inputTensorName");
  desc.add<std::string>("inputTrackTensorName");
  desc.add<std::string>("outputTensorName");
    
  desc.add<edm::InputTag>("triggers"),
  desc.add<edm::InputTag>("triggerObjects"),
  desc.add<edm::InputTag>("genParticles");
  desc.add<edm::InputTag>("met");
  desc.add<edm::InputTag>("electrons");
  desc.add<edm::InputTag>("muons");
  desc.add<edm::InputTag>("taus");
  desc.add<edm::InputTag>("pfCandidates");
  desc.add<edm::InputTag>("vertices");
  desc.add<edm::InputTag>("jets");

  desc.add<edm::InputTag>("rhoCentralCalo");

  desc.add<edm::InputTag>("EBRecHits");
  desc.add<edm::InputTag>("EERecHits");
  desc.add<edm::InputTag>("ESRecHits");
  desc.add<edm::InputTag>("HBHERecHits");


  desc.add<edm::InputTag>("dEdxPixel");
  desc.add<edm::InputTag>("dEdxStrip");
  desc.add<edm::InputTag>("isoTrk2dedxHitInfo");
  desc.add<edm::InputTag>("isolatedTracks");  

  desc.add<edm::InputTag>("pileupInfo");

  desc.add<double>("minGenParticlePt");
  desc.add<double>("minTrackPt");
  desc.add<double>("maxRelTrackIso");
  
  desc.add<std::string>("dataTakingPeriod");

  desc.add<double>("etaRangeNearTrack");
  desc.add<double>("phiRangeNearTrack");
  desc.add<int>("maxNumOfRecHits");
  desc.add<vector<string>>("signalTriggerNames");
  desc.add<vector<string>>("metFilterNames");

  descriptions.addWithDefaultLabel(desc);
}

std::unique_ptr<CacheData> TensorflowProducer::initializeGlobalCache(const edm::ParameterSet& config) {
  // this method is supposed to create, initialize and return a CacheData instance
 
  std::unique_ptr<CacheData> cache = std::make_unique<CacheData>();

  // load the graph def and save it
  std::string graphPath = config.getParameter<std::string>("graphPath");
  if (!graphPath.empty()) {
    graphPath = edm::FileInPath(graphPath).fullPath();
    cache->graphDef = tensorflow::loadGraphDef(graphPath);
  }

  return cache;
}

void TensorflowProducer::globalEndJob(const CacheData* cacheData) {
  // reset the graphDef
  if (cacheData->graphDef != nullptr) {
    delete cacheData->graphDef;
  }
}

void
TensorflowProducer::getGeometries(const edm::EventSetup &setup) {
  caloGeometry_ = setup.getHandle(caloGeometryToken_);
  if(!caloGeometry_.isValid())
    throw cms::Exception("FatalError") << "Unable to find CaloGeometryRecord in event!\n";
  
  /*cscGeometry_ = setup.getHandle(cscGeometryToken_);
  if(!cscGeometry_.isValid())
    throw cms::Exception("FatalError") << "Unable to find MuonGeometryRecord (CSC) in event!\n";

  dtGeometry_ = setup.getHandle(dtGeometryToken_);
  if(!dtGeometry_.isValid())
    throw cms::Exception("FatalError") << "Unable to find MuonGeometryRecord (DT) in event!\n";

  rpcGeometry_ = setup.getHandle(rpcGeometryToken_);
  if(!rpcGeometry_.isValid())
    throw cms::Exception("FatalError") << "Unable to find MuonGeometryRecord (RPC) in event!\n";*/

  ecalStatus_ = setup.getHandle(ecalStatusToken_);
  trackerTopology_ = setup.getHandle(trackerTopologyToken_);
  
}

int
TensorflowProducer::countGoodPrimaryVertices(const vector<reco::Vertex> &vertices) const
{
  int n = 0;
  for(const auto &v : vertices) {
    if(v.isValid() && v.ndof() >= 4 && fabs(v.z()) < 24.0 && hypot(v.x(), v.y()) < 2.0) n++;
  }
  return n;
}

int
TensorflowProducer::countGoodJets(const vector<pat::Jet> &jets) const
{
  int n = 0;
  vector<double> goodJetPhis;

  for(const auto &jet : jets) {
    // let's not deal with jet smearing for now...
    if(jet.pt() <= 110) continue;
    if(fabs(jet.eta()) >= 2.4) continue;
    if(!anatools::jetPassesTightLepVeto(jet)) continue;

    n++;
  }
  return n;
}

double
TensorflowProducer::getMaxDijetDeltaPhi(const vector<pat::Jet> &jets) const
{
  vector<double> goodJetPhis;
  for(const auto &jet : jets) {
    if(jet.pt() > 30 && fabs(jet.eta()) < 4.5 && anatools::jetPassesTightLepVeto(jet)) goodJetPhis.push_back(jet.phi());
  }

  double maxDeltaPhi = -999.;
  for(unsigned int i = 0; i < goodJetPhis.size(); i++) {
    for(unsigned int j = 0; j < goodJetPhis.size(); j++) {
      if(i == j) continue;
      double dPhi = fabs(deltaPhi(goodJetPhis[i], goodJetPhis[j]));
      if(dPhi > maxDeltaPhi) maxDeltaPhi = dPhi;
    }
  }

  return maxDeltaPhi;
}

double
TensorflowProducer::getLeadingJetMetPhi(const vector<pat::Jet> &jets, const pat::MET &met) const
{
  double deltaPhiMetJetLeading = 999.;
  double ptJetLeading = -1;

  for(const auto &jet : jets) {
    if(jet.pt() > 30 && 
       fabs(jet.eta()) < 4.5 && 
       anatools::jetPassesTightLepVeto(jet)) {
      if(jet.pt() > ptJetLeading) {
        ptJetLeading = jet.pt();
        deltaPhiMetJetLeading = fabs(deltaPhi(jet, met));
      }
    }
  }

  return deltaPhiMetJetLeading;
}

void
TensorflowProducer::getTracks(const reco::Vertex &pv, 
                                const vector<pat::Jet> &jets,
                                const vector<pat::Electron> &electrons,
                                const vector<pat::Muon> &muons,
                                const vector<pat::Tau> &taus,
                                const vector<pat::Electron> &tagElectrons,
                                const vector<pat::Muon> &tagMuons,
                                const pat::MET &met,
                                const edm::Handle<vector<pat::IsolatedTrack> > tracks, 
                                const edm::Handle<reco::DeDxHitInfoAss> isoTrk2dedxHitInfo,
                                const edm::Handle<edm::ValueMap<reco::DeDxData> > dEdxStrip,
                                const edm::Handle<edm::ValueMap<reco::DeDxData> > dEdxPixel)
{
  trackInfos_.clear();


  for(vector<pat::IsolatedTrack>::const_iterator it_track = tracks->begin(); it_track != tracks->end(); it_track++) {

    pat::IsolatedTrack track = *it_track;    
    TrackInfo info;
    
    //apply track pt cut
    if(minTrackPt_ > 0 && track.pt() <= minTrackPt_) continue;

    info.trackIso = 0.0;
    for(const auto &t : *tracks) {
      const auto theptinv2 = 1 / pow(track.pt(),2);
      float dz_track = (track.vz() - t.vz()) - ((track.vx() - t.vx()) * track.px() + (track.vy() - t.vy()) * track.py()) * track.pz() * theptinv2;
      if(fabs(dz_track) > 3.0 * hypot(track.dzError(), t.dzError())) continue;
      double dR = deltaR(track, t);
      if(dR < 0.3 && dR > 1.0e-12) info.trackIso += t.pt();
    }

    // apply relative track isolation cut
    if(maxRelTrackIso_ > 0 && info.trackIso / track.pt() >= maxRelTrackIso_) continue;

    info.px = track.px();
    info.py = track.py();
    info.pz = track.pz();
    info.vx = track.vx();
    info.vy = track.vy();
    info.vz = track.vz();
    info.eta = track.eta();
    info.pt = track.pt();
    //info.ptError = track.ptError();
    info.phi = track.phi();
    info.charge = track.charge();

    info.dEdxInfo.clear();

    //edm::Ref<vector<pat::IsolatedTrack> > matchedIsolatedTrack;
    //double dRToMatchedIsolatedTrack;
    //findMatchedIsolatedTrack(tracks, matchedIsolatedTrack, dRToMatchedIsolatedTrack, track);

    /*if(dRToMatchedIsolatedTrack == INVALID_VALUE) {
      info.dEdxInfo.push_back(TrackDeDxInfo());
    }
    else {
      if(isoTrk2dedxHitInfo->contains(matchedIsolatedTrack.id())) {
        const reco::DeDxHitInfo * hitInfo = (*isoTrk2dedxHitInfo)[matchedIsolatedTrack].get();
        if(hitInfo == nullptr) {
          //edm::LogWarning ("disappTrks_DeDxHitInfoVarProducer") << "Encountered a null DeDxHitInfo object from a pat::IsolatedTrack? Skipping this track...";
          continue;
        }*/

    edm::Ref<vector<pat::IsolatedTrack> > matchedIsolatedTrack = edm::Ref<vector<pat::IsolatedTrack> >(tracks, it_track - tracks->begin());

    if(isoTrk2dedxHitInfo->contains(matchedIsolatedTrack.id())) {
      const reco::DeDxHitInfo * hitInfo = (*isoTrk2dedxHitInfo)[matchedIsolatedTrack].get();
      if(hitInfo == nullptr) {
        //edm::LogWarning ("disappTrks_DeDxHitInfoVarProducer") << "Encountered a null DeDxHitInfo object from a pat::IsolatedTrack? Skipping this track...";
        continue;
      }

      for(unsigned int iHit = 0; iHit < hitInfo->size(); iHit++) {
        bool isPixel = (hitInfo->pixelCluster(iHit) != nullptr);
        bool isStrip = (hitInfo->stripCluster(iHit) != nullptr);
        if(!isPixel && !isStrip) continue; // probably shouldn't happen
        if(isPixel && isStrip) continue;
        
        //subdet Id = {1, pbx}, {2, pxf}, {3, tib}, {4, tid}, {5, tob}, {6, tec}
        int subDet = hitInfo->detId(iHit).subdetId();
        if(subDet == PixelSubdetector::PixelBarrel) subDet = 1;
        else if (subDet == PixelSubdetector::PixelEndcap) subDet = 2;
        else if(subDet == StripSubdetector::TIB) subDet = 3;  //N.B. in CMSSW_11 StripSubdetector -> SiStripSubdetector
        else if (subDet == StripSubdetector::TID) subDet = 4;
        else if (subDet == StripSubdetector::TOB) subDet = 5;
        else if (subDet == StripSubdetector::TEC) subDet = 6;

        float norm = isPixel ? 3.61e-06 : 3.61e-06 * 265;

        info.dEdxInfo.push_back(
          TrackDeDxInfo(subDet,
                        norm * hitInfo->charge(iHit) / hitInfo->pathlength(iHit),
                        isPixel ? hitInfo->pixelCluster(iHit)->size()  : -1,
                        isPixel ? hitInfo->pixelCluster(iHit)->sizeX() : -1,
                        isPixel ? hitInfo->pixelCluster(iHit)->sizeY() : -1,
#if CMSSW_VERSION_CODE >= CMSSW_VERSION(12,4,0)
                        isStrip ? deDxTools::shapeSelection(*(hitInfo->stripCluster(iHit))) : false,
#else
                        isStrip ? deDxTools::shapeSelection(*(hitInfo->stripCluster(iHit))) : false,
#endif
                        hitInfo->pos(iHit).x(),
                        hitInfo->pos(iHit).y(),
                        hitInfo->pos(iHit).z(),
                        trackerTopology_->layer(hitInfo->detId(iHit)))); // gives layer within sub detector
      }
    } // if isoTrk in association map
    else {
      info.dEdxInfo.push_back(TrackDeDxInfo()); // if somehow the matched isoTrk isn't in the hitInfo?
    }
    //} //if dRToMatchedIsoTrk != invalid

    /*edm::Ref<vector<reco::Track> > matchedGenTrack;
    double dRToMatchedGenTrack;
    findMatchedGenTrack(genTracks, matchedGenTrack, dRToMatchedGenTrack, track);
    if(dRToMatchedGenTrack == INVALID_VALUE){
      info.dEdxPixel = -10;
      info.numMeasurementsPixel = -10;
      info.numSatMeasurementsPixel = -10;
      info.dEdxStrip = -10;
      info.numMeasurementsStrip = -10;
      info.numSatMeasurementsStrip = -10;
    }
    else{
      const reco::DeDxData &dEdxDataPixel = (*dEdxPixel)[matchedGenTrack];
      const reco::DeDxData &dEdxDataStrip = (*dEdxStrip)[matchedGenTrack];

      info.dEdxPixel = dEdxDataPixel.dEdx();
      info.numMeasurementsPixel = dEdxDataPixel.numberOfMeasurements();
      info.numSatMeasurementsPixel = dEdxDataPixel.numberOfSaturatedMeasurements();
      info.dEdxStrip = dEdxDataStrip.dEdx();
      info.numMeasurementsStrip = dEdxDataStrip.numberOfMeasurements();
      info.numSatMeasurementsStrip = dEdxDataStrip.numberOfSaturatedMeasurements();
    }*/

    info.dEdxPixel = track.dEdxPixel();
    info.dEdxStrip = track.dEdxStrip();
    info.numMeasurementsPixel = track.hitPattern().numberOfValidPixelHits();
    info.numMeasurementsStrip = track.hitPattern().numberOfValidStripHits();


    info.dRMinJet = -1;
    for(const auto &jet : jets) {
      if(jet.pt() > 30 &&
         fabs(jet.eta()) < 4.5 &&
         (((jet.neutralHadronEnergyFraction()<0.90 && jet.neutralEmEnergyFraction()<0.90 && (jet.chargedMultiplicity() + jet.neutralMultiplicity())>1 && jet.muonEnergyFraction()<0.8) && ((fabs(jet.eta())<=2.4 && jet.chargedHadronEnergyFraction()>0 && jet.chargedMultiplicity()>0 && jet.chargedEmEnergyFraction()<0.90) || fabs(jet.eta())>2.4) && fabs(jet.eta())<=3.0)
            || (jet.neutralEmEnergyFraction()<0.90 && jet.neutralMultiplicity()>10 && fabs(jet.eta())>3.0))) {
        double dR = deltaR(track, jet);
        if(info.dRMinJet < 0 || dR < info.dRMinJet) info.dRMinJet = dR;
      }
    }

    bool inTOBCrack = (fabs(track.dz()) < 0.5 && fabs(M_PI_2 - track.theta()) < 1.0e-3);
    bool inECALCrack = (fabs(track.eta()) >= 1.42 && fabs(track.eta()) <= 1.65);
    bool inDTWheelGap = (fabs(track.eta()) >= 0.15 && fabs(track.eta()) <= 0.35);
    bool inCSCTransitionRegion = (fabs(track.eta()) >= 1.55 && fabs(track.eta()) <= 1.85);
    info.inGap = (inTOBCrack || inECALCrack || inDTWheelGap || inCSCTransitionRegion);

    info.dRMinBadEcalChannel = minDRBadEcalChannel(track);

    info.nValidPixelHits        = track.hitPattern().numberOfValidPixelHits();
    info.nValidHits             = track.hitPattern().numberOfValidHits();
    info.numberOfValidMuonHits  = track.hitPattern().numberOfValidMuonHits();
    info.missingInnerHits       = track.hitPattern().trackerLayersWithoutMeasurement(reco::HitPattern::MISSING_INNER_HITS);
    info.missingMiddleHits      = track.hitPattern().trackerLayersWithoutMeasurement(reco::HitPattern::TRACK_HITS);
    info.missingOuterHits       = track.hitPattern().trackerLayersWithoutMeasurement(reco::HitPattern::MISSING_OUTER_HITS);
    info.nLayersWithMeasurement = track.hitPattern().trackerLayersWithMeasurement();
    info.pixelLayersWithMeasurement = track.hitPattern().pixelLayersWithMeasurement();

    // d0 wrt pv (2d) = (vertex - pv) cross p / |p|
    info.d0 = ((track.vx() - pv.x()) * track.py() - (track.vy() - pv.y()) * track.px()) / track.pt(); 
  
    // dz wrt pv (2d) = (v_z - pv_z) - p_z * [(vertex - pv) dot p / |p|^2]
    info.dz = track.vz() - pv.z() -
      ((track.vx() - pv.x()) * track.px() + (track.vy() - pv.y()) * track.py()) * track.pz() / track.pt() / track.pt();

    //info.normalizedChi2 = track.normalizedChi2();
    info.highPurityFlag = track.isHighPurityTrack();

    info.deltaRToClosestElectron = -1;
    for(const auto &electron : electrons) {
      double thisDR = deltaR(electron, track);
      if(info.deltaRToClosestElectron < 0 || thisDR < info.deltaRToClosestElectron) info.deltaRToClosestElectron = thisDR;
    }

    info.deltaRToClosestMuon = -1;
    for(const auto &muon : muons) {
      double thisDR = deltaR(muon, track);
      if(info.deltaRToClosestMuon < 0 || thisDR < info.deltaRToClosestMuon) info.deltaRToClosestMuon = thisDR;
    }

    info.deltaRToClosestTauHad = -1;
    for(const auto &tau : taus) {
      if(tau.isTauIDAvailable("againstElectronLooseMVA5")) {
        if(tau.tauID("decayModeFinding") <= 0.5 ||
           tau.tauID("againstElectronLooseMVA5") <= 0.5 ||
           tau.tauID("againstMuonLoose3") <= 0.5) {
          continue;
        }
      }
      else if(tau.isTauIDAvailable("againstElectronLooseMVA6")) {
        if(tau.tauID("decayModeFinding") <= 0.5 ||
           tau.tauID("againstElectronLooseMVA6") <= 0.5 ||
           tau.tauID("againstMuonLoose3") <= 0.5) {
          continue;
        }
      }
      else {
        continue;
      }

      double thisDR = deltaR(tau, track);
      if(info.deltaRToClosestTauHad < 0 || thisDR < info.deltaRToClosestTauHad) info.deltaRToClosestTauHad = thisDR;
    }

    info.passesProbeSelection = isProbeTrack(info);

    info.deltaRToClosestTagElectron = -1;
    info.deltaRToClosestTagMuon = -1;

    info.isTagProbeElectron = 0;
    info.isTagProbeTauToElectron = 0;

    info.isTagProbeMuon = 0;
    info.isTagProbeTauToMuon = 0;

    if(info.passesProbeSelection) {
      for(const auto tag : tagElectrons) {
        double thisDR = deltaR(tag, track);
        if(info.deltaRToClosestTagElectron < 0 || thisDR < info.deltaRToClosestTagElectron) {
          info.deltaRToClosestTagElectron = thisDR;
        }
        info.isTagProbeElectron |= isTagProbeElePair(track, tag);
        info.isTagProbeTauToElectron |= isTagProbeTauToElePair(track, tag, met);
      }

      for(const auto tag : tagMuons) {
        double thisDR = deltaR(tag, track);
        if(info.deltaRToClosestTagMuon < 0 || thisDR < info.deltaRToClosestTagMuon) {
          info.deltaRToClosestTagMuon = thisDR;
        }
        info.isTagProbeMuon |= isTagProbeMuonPair(track, tag);
        info.isTagProbeTauToMuon |= isTagProbeTauToMuonPair(track, tag, met);
      }
    }

    info.ecalo = 0; // calculated in getRecHits

    trackInfos_.push_back(info);
  }

  return;
}

void 
TensorflowProducer::getRecHits(const edm::Event &event)
{
  recHitInfos_.clear();

  edm::Handle<EBRecHitCollection> EBRecHits;
  event.getByToken(EBRecHitsToken_, EBRecHits);
  for(const auto &hit : *EBRecHits) {
    math::XYZVector pos = getPosition(hit.detid());
    recHitInfos_.push_back(RecHitInfo(pos.eta(), pos.phi(), hit.energy(), -999., DetType::EB));

    for(auto &info : trackInfos_) {
      double dR2 = deltaR2(pos.eta(), pos.phi(), info.eta, info.phi);
      if(dR2 < 0.5*0.5) info.ecalo += hit.energy();
    }
  }

  edm::Handle<EERecHitCollection> EERecHits;
  event.getByToken(EERecHitsToken_, EERecHits);
  for(const auto &hit : *EERecHits) {
    math::XYZVector pos = getPosition(hit.detid());
    recHitInfos_.push_back(RecHitInfo(pos.eta(), pos.phi(), hit.energy(), -999., DetType::EE));

    for(auto &info : trackInfos_) {
      double dR2 = deltaR2(pos.eta(), pos.phi(), info.eta, info.phi);
      if(dR2 < 0.5*0.5) info.ecalo += hit.energy();
    }
  }

  edm::Handle<ESRecHitCollection> ESRecHits;
  event.getByToken(ESRecHitsToken_, ESRecHits);
  for(const auto &hit : *ESRecHits) {
    math::XYZVector pos = getPosition(hit.detid());
    recHitInfos_.push_back(RecHitInfo(pos.eta(), pos.phi(), hit.energy(), -999., DetType::ES));
  }

  edm::Handle<HBHERecHitCollection> HBHERecHits;
  event.getByToken(HBHERecHitsToken_, HBHERecHits);
  for(const auto &hit : *HBHERecHits) {
    math::XYZVector pos = getPosition(hit.detid());
    recHitInfos_.push_back(RecHitInfo(pos.eta(), pos.phi(), hit.energy(), -999., DetType::HCAL));

    for(auto &info : trackInfos_) {
      double dR2 = deltaR2(pos.eta(), pos.phi(), info.eta, info.phi);
      if(dR2 < 0.5*0.5) info.ecalo += hit.energy();
    }
  }
}

void
TensorflowProducer::getGenParticles(const reco::CandidateView &genParticles){
                                          
  
  genParticleInfos_.clear();

  vector<const reco::Candidate*> cands;
  vector<const reco::Candidate*>::const_iterator found = cands.begin();
  for(reco::CandidateView::const_iterator p = genParticles.begin(); p != genParticles.end(); ++p) cands.push_back(&*p);

  for(reco::CandidateView::const_iterator p = genParticles.begin(); p != genParticles.end(); p++) {
    GenParticleInfo info;
    info.px = p->px();
    info.py = p->py();
    info.pz = p->pz();
    info.e  = p->energy();

    info.eta = p->eta();
    info.phi = p->phi();
    info.pt  = p->pt();

    info.vx = p->vx();
    info.vy = p->vy();
    info.vz = p->vz();

    info.pdgId = p->pdgId();
    info.status = p->status();

    info.mother1_index = -1;
    info.mother2_index = -1;

    info.daughter1_index = -1;
    info.daughter2_index = -1;

    info.nMothers = p->numberOfMothers();
    info.nDaughters = p->numberOfDaughters();

    found = find(cands.begin(), cands.end(), p->mother(0));
    if(found != cands.end()) info.mother1_index = found - cands.begin();

    found = find(cands.begin(), cands.end(), p->mother(p->numberOfMothers() - 1));
    if(found != cands.end()) info.mother2_index = found - cands.begin();

    found = find(cands.begin(), cands.end(), p->daughter(0));
    if(found != cands.end()) info.daughter1_index = found - cands.begin();

    found = find(cands.begin(), cands.end(), p->daughter(p->numberOfDaughters() - 1));
    if(found != cands.end()) info.daughter2_index = found - cands.begin();

    const reco::GenParticle* gp = dynamic_cast<const reco::GenParticle*>(&*p);

    info.isPromptFinalState = gp->isPromptFinalState();
    info.isDirectPromptTauDecayProductFinalState = gp->isDirectPromptTauDecayProductFinalState();
    info.isHardProcess = gp->isHardProcess();
    info.fromHardProcessFinalState = gp->fromHardProcessFinalState();
    info.fromHardProcessBeforeFSR = gp->fromHardProcessBeforeFSR();
    info.isFirstCopy = gp->statusFlags().isFirstCopy();
    info.isLastCopy = gp->isLastCopy();
    info.isLastCopyBeforeFSR = gp->isLastCopyBeforeFSR();

    genParticleInfos_.push_back(info);
  }
}

const math::XYZVector 
TensorflowProducer::getPosition(const DetId& id) const
{
   if(!caloGeometry_->getSubdetectorGeometry(id) || !caloGeometry_->getSubdetectorGeometry(id)->getGeometry(id) ) {
      throw cms::Exception("FatalError") << "Failed to access geometry for DetId: " << id.rawId();
      return math::XYZVector(0,0,0);
   }
   const GlobalPoint idPosition = caloGeometry_->getSubdetectorGeometry(id)->getGeometry(id)->getPosition();
   math::XYZVector idPositionRoot(idPosition.x(), idPosition.y(), idPosition.z());
   return idPositionRoot;
}

vector<pat::Electron>
TensorflowProducer::getTagElectrons(const edm::Event &event,
                                           const edm::TriggerResults &triggers,
                                           const vector<pat::TriggerObjectStandAlone> &trigObjs,
                                           const reco::Vertex &vertex,
                                           const vector<pat::Electron> &electrons)
{
  vector<pat::Electron> tagElectrons;

  for(const auto &electron : electrons) {
    if(electron.pt() <= (is2017_ ? 35 : 32)) continue;

    if(!anatools::isMatchedToTriggerObject(event,
                                           triggers,
                                           electron,
                                           trigObjs,
                                           "hltEgammaCandidates::HLT", 
                                           (is2017_ ? "hltEle35noerWPTightGsfTrackIsoFilter" : "hltEle32WPTightGsfTrackIsoFilter"))) {
      continue; // cutElectronMatchToTrigObj
    }

    if(fabs(electron.eta()) >= 2.1) continue;
    if(!electron.electronID(is2017_ ? "cutBasedElectronID-Fall17-94X-V1-tight" : "cutBasedElectronID-Fall17-94X-V2-tight")) continue;
    
    if(fabs(electron.superCluster()->eta()) <= 1.479) {
      if(fabs(electron.gsfTrack()->dxy(vertex.position())) >= 0.05) continue;
      if(fabs(electron.gsfTrack()->dz(vertex.position())) >= 0.10) continue;
    }
    else {
      if(fabs(electron.gsfTrack()->dxy(vertex.position())) >= 0.10) continue;
      if(fabs(electron.gsfTrack()->dz(vertex.position())) >= 0.20) continue;
    }

    tagElectrons.push_back(electron);
  }

  return tagElectrons;
}

vector<pat::Muon>
TensorflowProducer::getTagMuons(const edm::Event &event,
                                       const edm::TriggerResults &triggers,
                                       const vector<pat::TriggerObjectStandAlone> &trigObjs,
                                       const reco::Vertex &vertex,
                                       const vector<pat::Muon> &muons)
{
  vector<pat::Muon> tagMuons;

  for(const auto &muon : muons) {
    if(muon.pt() <= (is2017_ ? 29 : 26)) continue;
    if(fabs(muon.eta()) >= 2.1) continue;
    if(!muon.isTightMuon(vertex)) continue;

    double iso = muon.pfIsolationR04().sumNeutralHadronEt +
                 muon.pfIsolationR04().sumPhotonEt +
                 -0.5 * muon.pfIsolationR04().sumPUPt;
    iso = muon.pfIsolationR04().sumChargedHadronPt + max(0.0, iso);
    if(iso / muon.pt() >= 0.15) continue;

    if(!anatools::isMatchedToTriggerObject(event,
                                           triggers,
                                           muon,
                                           trigObjs,
                                           (is2017_ ? "hltIterL3MuonCandidates::HLT" : "hltHighPtTkMuonCands::HLT"),
                                           (is2017_ ? "hltL3crIsoL1sMu22Or25L1f0L2f10QL3f27QL3trkIsoFiltered0p07" : "hltL3crIsoL1sMu22Or25L1f0L2f10QL3f27QL3trkIsoFiltered0p07"))) {
      continue; // cutMuonMatchToTrigObj
    }
    
    tagMuons.push_back(muon);
  }

  return tagMuons;
}

const bool
TensorflowProducer::isProbeTrack(const TrackInfo info) const
{
  if(info.pt <= 30 ||
     fabs(info.eta) >= 2.1 ||
     // skip fiducial sElectrons
     info.nValidPixelHits < 4 ||
     info.nValidHits < 4 ||
     info.missingInnerHits != 0 ||
     info.missingMiddleHits != 0 ||
     info.trackIso / info.pt >= 0.05 ||
     fabs(info.d0) >= 0.02 ||
     fabs(info.dz) >= 0.5 ||
     // skip lepton vetoes
     fabs(info.dRMinJet) <= 0.5) {
    return false;
  }

  return true;
}

const unsigned int
TensorflowProducer::isTagProbeElePair(const pat::IsolatedTrack &probe, const pat::Electron &tag) const 
{
  TLorentzVector t(tag.px(), tag.py(), tag.pz(), tag.energy());
  TLorentzVector p(probe.px(), 
                   probe.py(), 
                   probe.pz(), 
                   sqrt(probe.px() * probe.px() + 
                        probe.py() * probe.py() + 
                        probe.pz() * probe.pz() + 
                        0.000510998928 * 0.000510998928)); // energyOfElectron()

  if(fabs((t + p).M() - 91.1876) >= 10.0) return 0b00;
  return (tag.charge() * probe.charge() < 0) ? 0b01 : 0b10;
}

const unsigned int
TensorflowProducer::isTagProbeTauToElePair(const pat::IsolatedTrack &probe, 
                                                  const pat::Electron &tag, 
                                                  const pat::MET &met) const 
{
  double dPhi = deltaPhi(tag.phi(), probe.phi());
  if(sqrt(2.0 * tag.pt() * probe.pt() * (1 - cos(dPhi))) >= 40) return false; // cutElectronLowMT

  TLorentzVector t(tag.px(), tag.py(), tag.pz(), tag.energy());
  TLorentzVector p(probe.px(), 
                   probe.py(), 
                   probe.pz(), 
                   sqrt(probe.px() * probe.px() + 
                        probe.py() * probe.py() + 
                        probe.pz() * probe.pz() + 
                        0.000510998928 * 0.000510998928)); // energyOfElectron()

  double invMass = (t + p).M();

  if(invMass <= 91.1876 - 50 || invMass >= 91.1876 - 15) return 0b00;
  return (tag.charge() * probe.charge() < 0) ? 0b01 : 0b10;
}

const unsigned int
TensorflowProducer::isTagProbeMuonPair(const pat::IsolatedTrack &probe, const pat::Muon &tag) const 
{
  TLorentzVector t(tag.px(), tag.py(), tag.pz(), tag.energy());
  TLorentzVector p(probe.px(), 
                   probe.py(), 
                   probe.pz(), 
                   sqrt(probe.px() * probe.px() + 
                        probe.py() * probe.py() + 
                        probe.pz() * probe.pz() + 
                        0.1056583715 * 0.1056583715)); // energyOfMuon()

  if(fabs((t + p).M() - 91.1876) >= 10.0) return 0b00;
  return (tag.charge() * probe.charge() < 0) ? 0b01 : 0b10;
}

const unsigned int
TensorflowProducer::isTagProbeTauToMuonPair(const pat::IsolatedTrack &probe, 
                                                   const pat::Muon &tag, 
                                                   const pat::MET &met) const 
{
  double dPhi = deltaPhi(tag.phi(), probe.phi());
  if(sqrt(2.0 * tag.pt() * probe.pt() * (1 - cos(dPhi))) >= 40) return false; // cutMuonLowMT

  TLorentzVector t(tag.px(), tag.py(), tag.pz(), tag.energy());
  TLorentzVector p(probe.px(), 
                   probe.py(), 
                   probe.pz(), 
                   sqrt(probe.px() * probe.px() + 
                        probe.py() * probe.py() + 
                        probe.pz() * probe.pz() + 
                        0.1056583715 * 0.1056583715)); // energyOfMuon()

  double invMass = (t + p).M();

  if(invMass <= 91.1876 - 50 || invMass >= 91.1876 - 15) return 0b00;
  return (tag.charge() * probe.charge() < 0) ? 0b01 : 0b10;
}

const double
TensorflowProducer::minDRBadEcalChannel(const pat::IsolatedTrack &track) const
{
   double trackEta = track.eta(), trackPhi = track.phi();

   double min_dist = -1;
   DetId min_detId;

   map<DetId, vector<int> >::const_iterator bitItor;
   for(bitItor = EcalAllDeadChannelsBitMap_.begin(); bitItor != EcalAllDeadChannelsBitMap_.end(); bitItor++) {
      DetId maskedDetId = bitItor->first;
      map<DetId, std::vector<double> >::const_iterator valItor = EcalAllDeadChannelsValMap_.find(maskedDetId);
      if(valItor == EcalAllDeadChannelsValMap_.end()){ 
        cout << "Error cannot find maskedDetId in EcalAllDeadChannelsValMap_ ?!" << endl;
        continue;
      }

      double eta = (valItor->second)[0], phi = (valItor->second)[1];
      double dist = reco::deltaR(eta, phi, trackEta, trackPhi);

      if(min_dist > dist || min_dist < 0) {
        min_dist = dist;
        min_detId = maskedDetId;
      }
   }

   return min_dist;
}

void
TensorflowProducer::getChannelStatusMaps()
{
  EcalAllDeadChannelsValMap_.clear();
  EcalAllDeadChannelsBitMap_.clear();

  // Loop over EB ...
  for(int ieta = -85; ieta <= 85; ieta++) {
    for(int iphi = 0; iphi <= 360; iphi++) {
      if(!EBDetId::validDetId(ieta, iphi)) continue;

      const EBDetId detid = EBDetId(ieta, iphi, EBDetId::ETAPHIMODE);
      EcalChannelStatus::const_iterator chit = ecalStatus_->find(detid);
      // refer https://twiki.cern.ch/twiki/bin/viewauth/CMS/EcalChannelStatus
      int status = (chit != ecalStatus_->end()) ? chit->getStatusCode() & 0x1F : -1;

      const CaloSubdetectorGeometry * subGeom = caloGeometry_->getSubdetectorGeometry(detid);
      auto cellGeom = subGeom->getGeometry(detid);
      double eta = cellGeom->getPosition().eta();
      double phi = cellGeom->getPosition().phi();
      double theta = cellGeom->getPosition().theta();

      if(status >= 3) { // maskedEcalChannelStatusThreshold_
        vector<double> valVec;
        vector<int> bitVec;
        
        valVec.push_back(eta);
        valVec.push_back(phi);
        valVec.push_back(theta);
        
        bitVec.push_back(1);
        bitVec.push_back(ieta);
        bitVec.push_back(iphi);
        bitVec.push_back(status);
        
        EcalAllDeadChannelsValMap_.insert(make_pair(detid, valVec));
        EcalAllDeadChannelsBitMap_.insert(make_pair(detid, bitVec));
      }
    } // end loop iphi
  } // end loop ieta

  // Loop over EE detid
  for(int ix = 0; ix <= 100; ix++) {
    for(int iy = 0; iy <= 100; iy++) {
      for(int iz = -1; iz <= 1; iz++) {
        if(iz == 0) continue;
        if(!EEDetId::validDetId(ix, iy, iz)) continue;

        const EEDetId detid = EEDetId(ix, iy, iz, EEDetId::XYMODE);
        EcalChannelStatus::const_iterator chit = ecalStatus_->find(detid);
        int status = (chit != ecalStatus_->end()) ? chit->getStatusCode() & 0x1F : -1;

        const CaloSubdetectorGeometry * subGeom = caloGeometry_->getSubdetectorGeometry(detid);
        auto cellGeom = subGeom->getGeometry(detid);
        double eta = cellGeom->getPosition().eta();
        double phi = cellGeom->getPosition().phi();
        double theta = cellGeom->getPosition().theta();

        if(status >= 3) { // maskedEcalChannelStatusThreshold_
          vector<double> valVec;
          vector<int> bitVec;
          
          valVec.push_back(eta);
          valVec.push_back(phi);
          valVec.push_back(theta);
          
          bitVec.push_back(2);
          bitVec.push_back(ix);
          bitVec.push_back(iy);
          bitVec.push_back(iz);
          bitVec.push_back(status);

          EcalAllDeadChannelsValMap_.insert(make_pair(detid, valVec));
          EcalAllDeadChannelsBitMap_.insert(make_pair(detid, bitVec));
        }
      } // end loop iz
    } // end loop iy
  } // end loop ix
}

std::vector<std::vector<double>>
TensorflowProducer::getHitMap(const vector<TrackDeDxInfo> trackDeDxInfos) const {

  //hit.hitLayerId, hit.charge, hit.subDet, hit.pixelHitSize, 
  //hit.pixelHitSizeX, hit.pixelHitSizeY, hit.stripShapeSelection, hit.hitPosX, hit.hitPosY]

  int hitsWanted = 16;
  int numHitVar = 9;
  int numHits = 0;
  bool newLayer = true;
  std::vector<std::vector<double>> layerHits(hitsWanted, vector<double>(numHitVar));

  for(auto &hit : trackDeDxInfos){

    newLayer = true;

    //std::cout << "Get Hit Map, sub detector: " << hit.subDet << ", layer: " << hit.hitLayerId << ", energy: " << hit.charge << ", num hits: " << numHits<< std::endl;

    //if(numHits == hitsWanted-1) break; //check if greater hits then break

    for(int i=0; i < numHits; i++){
      //check to see if this detector/layer already has a hit
      if(hit.subDet == layerHits[i][2] && hit.hitLayerId == layerHits[i][0]){
        newLayer = false;
        //check if the hit has more energy, want to have max energy hit in detector/layer
        if(hit.charge > layerHits[i][1]){
          std::vector<double> thisLayer = {(double)hit.hitLayerId, (double)hit.charge, (double)hit.subDet, (double)hit.pixelHitSize, (double)hit.pixelHitSizeX, (double)hit.pixelHitSizeY,
                                          (double)hit.stripShapeSelection, (double)hit.hitPosX, (double)hit.hitPosY};
          layerHits[i] = thisLayer;
        }
        break;
      }
    } //end loop over existing hits
    if(newLayer && numHits < hitsWanted-1){
      std::vector<double> thisLayer = {(double)hit.hitLayerId, (double)hit.charge, (double)hit.subDet, (double)hit.pixelHitSize, (double)hit.pixelHitSizeX, (double)hit.pixelHitSizeY,
                                      (double)hit.stripShapeSelection, (double)hit.hitPosX, (double)hit.hitPosY};
      layerHits[numHits] = thisLayer;
      numHits++;
    }
    
  }//end loop over dedxInfos

  return layerHits;

}

std::pair<double, double>
TensorflowProducer::getMaxHits(const vector<TrackDeDxInfo> trackDeDxInfos) const {

  double maxEnergy = 0;
  double totalEnergy = 0;

  for(auto &hit : trackDeDxInfos){
    totalEnergy += hit.charge;
    if(hit.charge > maxEnergy) maxEnergy = hit.charge;
  }

  std::pair<double, double> hitEnergy(maxEnergy, totalEnergy);
  return hitEnergy;
}

//std::bitset<29> 
unsigned long
TensorflowProducer::encodeLayers(const std::vector<std::vector<double>> layerHits) const {
  
  //number of layers in each sub detector {pbx, pex, TIB, TOB, TID, TEC}
  int numLayers[6] = {4, 3, 4, 6, 3, 9};

  std::bitset<29> encodedHits;


  for(unsigned int i=0; i < layerHits.size(); i++){
    
    int thisLayer = layerHits[i][0];
    int thisDet = layerHits[i][2];
    int bit = thisLayer-1;

    for(int det = 0; det < thisDet-1; det++){
      bit += numLayers[det];
    }

    std::bitset<29> thisHit = 1<<bit;
    encodedHits = encodedHits | thisHit;

  }

  unsigned long encodedHitsInt = encodedHits.to_ulong();

  return encodedHitsInt;

}

std::pair<std::array<double, 3>, std::array<double, 3>>
TensorflowProducer::getClosestVertices(const std::vector<VertexInfo> v_info, float track_vz, float track_vx, float track_vy) const {

  std::array<double, 3> d0 {{10e3, 10e3, 10e3}};
  std::array<double, 3> dz {{10e3, 10e3, 10e3}};

  for(auto &info : v_info){
    float deltaZ = abs(info.vertex.Z() - track_vz);
    float delta0 = abs(sqrt(pow(info.vertex.X()-track_vx,2) + pow(info.vertex.Y()-track_vy,2)));
    //std::cout << "delta0: " << delta0 << " , deltaZ: " << deltaZ << std::endl;
    int size = sizeof(dz)/sizeof(dz[0]);
    //std::cout << "size: " << size << std::endl;
    if(abs(deltaZ) < abs(dz[size-1])) dz[size-1] = deltaZ;
    std::sort(dz.begin(), dz.end(), [](float i, float j){ return abs(i) < abs(j); });
    if(abs(delta0) < abs(d0[size-1])) d0[size-1] = delta0;
    std::sort(d0.begin(), d0.end(), [](float i, float j){ return abs(i) < abs(j); });
    //std::cout << "d0: " << d0[0] << " " << d0[1] << " " << d0[2] << ", dz: " << dz[0] << " " << dz[1] << " " << dz[2] << std::endl;
  }

  std::pair<std::array<double, 3>, std::array<double, 3>> closestVertices(dz, d0);
  return closestVertices;

}
int
TensorflowProducer::getDetectorIndex(const int detectorIndex) const
{
  if(detectorIndex == DetType::EB or detectorIndex == DetType::EE)
  {
    return 0;
  }
  else if (detectorIndex == DetType::HCAL)
  {
    return 1;
  }
  else if (detectorIndex >= DetType::CSC and detectorIndex <= DetType::RPC)
  {
    return 2;
  }
  else
  {
    return -1;
  }

}
//define this as a plug-in
DEFINE_FWK_MODULE(TensorflowProducer);

#endif
