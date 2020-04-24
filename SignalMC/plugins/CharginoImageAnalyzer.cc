#include "DisappTrks/SignalMC/plugins/CharginoImageAnalyzer.h"

#include "MagneticField/Engine/interface/MagneticField.h"
#include "MagneticField/Records/interface/IdealMagneticFieldRecord.h"
#include "Geometry/CaloGeometry/interface/CaloSubdetectorGeometry.h"
#include "Geometry/CaloGeometry/interface/CaloCellGeometry.h"

CharginoImageAnalyzer::CharginoImageAnalyzer(const edm::ParameterSet &cfg) :
  genParticles_     (cfg.getParameter<edm::InputTag> ("genParticles")),
  EBRecHitsTag_     (cfg.getParameter<edm::InputTag> ("EBRecHits")),
  EERecHitsTag_     (cfg.getParameter<edm::InputTag> ("EERecHits")),
  HBHERecHitsTag_   (cfg.getParameter<edm::InputTag> ("HBHERecHits")),
  matchingID_       (cfg.getParameter<int>           ("matchingID")),
  matchingMotherID_ (cfg.getParameter<int>           ("matchingMotherID")),
  matchingStatus_   (cfg.getParameter<int>           ("matchingStatus")),
  x_lo              (cfg.getParameter<double>        ("x_lo")),
  x_hi              (cfg.getParameter<double>        ("x_hi")),
  y_lo              (cfg.getParameter<double>        ("y_lo")),
  y_hi              (cfg.getParameter<double>        ("y_hi")),
  n_x               (cfg.getParameter<int>           ("n_x")),
  n_y               (cfg.getParameter<int>           ("n_y"))
{
  genParticlesToken_ = consumes<vector<reco::GenParticle> > (genParticles_);

  EBRecHitsToken_       = consumes<EBRecHitCollection>   (EBRecHitsTag_);
  EERecHitsToken_       = consumes<EERecHitCollection>   (EERecHitsTag_);
  HBHERecHitsToken_     = consumes<HBHERecHitCollection> (HBHERecHitsTag_);

  for(int i = 0; i < n_x; i++) {
    image_ecal.push_back(vector<double>(n_y, 0.0));
    image_hcal.push_back(vector<double>(n_y, 0.0));
  }

  tree_ = fs_->make<TTree>("tree", "tree");
  tree_->Branch("ecal", &image_ecal);
  tree_->Branch("hcal", &image_hcal);

}

CharginoImageAnalyzer::~CharginoImageAnalyzer()
{
}

void
CharginoImageAnalyzer::analyze(const edm::Event &event, const edm::EventSetup &setup)
{
  edm::Handle<vector<reco::GenParticle> > genParticles;
  event.getByToken(genParticlesToken_, genParticles);

  edm::Handle<EBRecHitCollection> EBRecHits;
  event.getByToken(EBRecHitsToken_, EBRecHits);
  
  edm::Handle<EERecHitCollection> EERecHits;
  event.getByToken(EERecHitsToken_, EERecHits);
  
  edm::Handle<HBHERecHitCollection> HBHERecHits;
  event.getByToken(HBHERecHitsToken_, HBHERecHits);

  setup.get<CaloGeometryRecord>().get(caloGeometry_);
  if (!caloGeometry_.isValid())
    throw cms::Exception("FatalError") << "Unable to find CaloGeometryRecord in event!\n";

  for(const auto &genParticle : *genParticles) {
    if(abs(genParticle.pdgId()) != matchingID_) continue;
    if(matchingMotherID_ != 0 && abs(genParticle.motherRef()->pdgId()) != matchingMotherID_) continue;
    if(matchingStatus_ != 0 && genParticle.status() != matchingStatus_) continue;

    getImage(genParticle, *EBRecHits, *EERecHits, *HBHERecHits);

    tree_->Fill();
  }

}

void 
CharginoImageAnalyzer::getImage(
  const reco::GenParticle &genParticle,
  const EBRecHitCollection &EBRecHits,
  const EERecHitCollection &EERecHits,
  const HBHERecHitCollection &HBHERecHits)
{

  for(int i = 0; i < n_x; i++) {
    for(int j = 0; j < n_y; j++) {
      image_ecal[i][j] = 0.0;
      image_hcal[i][j] = 0.0;
    }
  }

  for(const auto &hit : EBRecHits) {
    math::XYZVector pos = getPosition(hit.detid());
    double dEta = genParticle.eta() - pos.eta();
    if(dEta < x_lo || dEta >= x_hi) continue;
    double dPhi = deltaPhi(genParticle, pos);
    if(dPhi < y_lo || dPhi >= y_hi) continue;

    const unsigned int ix = (dEta - x_lo) * n_x / (x_hi - x_lo);
    const unsigned int iy = (dPhi - y_lo) * n_y / (y_hi - y_lo);
    image_ecal[ix][iy] += hit.energy();
  }

  for(const auto &hit : EERecHits) {
    math::XYZVector pos = getPosition(hit.detid());
    double dEta = genParticle.eta() - pos.eta();
    if(dEta < x_lo || dEta >= x_hi) continue;
    double dPhi = deltaPhi(genParticle, pos);
    if(dPhi < y_lo || dPhi >= y_hi) continue;

    const unsigned int ix = (dEta - x_lo) * n_x / (x_hi - x_lo);
    const unsigned int iy = (dPhi - y_lo) * n_y / (y_hi - y_lo);
    image_ecal[ix][iy] += hit.energy();
  }

  for(const auto &hit : HBHERecHits) {
    math::XYZVector pos = getPosition(hit.detid());
    double dEta = genParticle.eta() - pos.eta();
    if(dEta < x_lo || dEta >= x_hi) continue;
    double dPhi = deltaPhi(genParticle, pos);
    if(dPhi < y_lo || dPhi >= y_hi) continue;

    const unsigned int ix = (dEta - x_lo) * n_x / (x_hi - x_lo);
    const unsigned int iy = (dPhi - y_lo) * n_y / (y_hi - y_lo);
    image_hcal[ix][iy] += hit.energy();
  }

}

const math::XYZVector 
CharginoImageAnalyzer::getPosition(const DetId& id) const
{
   if ( ! caloGeometry_.isValid() ||
        ! caloGeometry_->getSubdetectorGeometry(id) ||
        ! caloGeometry_->getSubdetectorGeometry(id)->getGeometry(id) ) {
      throw cms::Exception("FatalError") << "Failed to access geometry for DetId: " << id.rawId();
      return math::XYZVector(0,0,0);
   }
   const GlobalPoint idPosition = caloGeometry_->getSubdetectorGeometry(id)->getGeometry(id)->getPosition();
   math::XYZVector idPositionRoot(idPosition.x(), idPosition.y(), idPosition.z());
   return idPositionRoot;
}

DEFINE_FWK_MODULE(CharginoImageAnalyzer);
