#include "DataFormats/Math/interface/deltaR.h"
#include "DataFormats/MuonReco/interface/MuonSelectors.h"

#include "DisappTrks/StandardAnalysis/plugins/DEdxAnalyzer.h"

DEdxAnalyzer::DEdxAnalyzer (const edm::ParameterSet &cfg) :
  tracks_ (cfg.getParameter<edm::InputTag> ("tracks")),
  electrons_ (cfg.getParameter<edm::InputTag> ("electrons")),
  muons_ (cfg.getParameter<edm::InputTag> ("muons")),
  dEdxPixel_ (cfg.getParameter<edm::InputTag> ("dEdxPixel")),
  dEdxStrip_ (cfg.getParameter<edm::InputTag> ("dEdxStrip")),
  minPt_ (cfg.getParameter<double> ("minPt")),
  minNMissOut_ (cfg.getParameter<int> ("minNMissOut")),
  requiredNumLayers_ (cfg.getParameter<int> ("requiredNumLayers")),
  vetoElectronsOrMuons_ (cfg.getParameter<string> ("vetoElectronsOrMuons"))
{
  vector<double> pLogBins, dEdxLogBins;
  logSpace (200, 1.0, 3.3, pLogBins);
  logSpace (200, -1.0, 1.0, dEdxLogBins);

  TH1::SetDefaultSumw2();
  twoDHists_["dedxPixelVsP"]       = fs_->make<TH2D> ("dedxPixelVsP", ";p [GeV];#LTdE/dx#GT (pixels) [MeV/cm]", 200, 0.0, 200.0, 200, 0.0, 10.0);
  twoDHists_["dedxPixelVsPLog"]    = fs_->make<TH2D> ("dedxPixelVsPLog", ";p [GeV];#LTdE/dx#GT (pixels) [MeV/cm]", pLogBins.size () - 1, pLogBins.data (), 200, 0.0, 10.0);
  twoDHists_["dedxPixelLogVsP"]    = fs_->make<TH2D> ("dedxPixelLogVsP", ";p [GeV];#LTdE/dx#GT (pixels) [MeV/cm]", 200, 0.0, 200.0, dEdxLogBins.size () - 1, dEdxLogBins.data ());
  twoDHists_["dedxPixelLogVsPLog"] = fs_->make<TH2D> ("dedxPixelLogVsPLog", ";p [GeV];#LTdE/dx (pixels)#GT [MeV/cm]", pLogBins.size () - 1, pLogBins.data (), dEdxLogBins.size () - 1, dEdxLogBins.data ());

  twoDHists_["dedxStripVsP"]       = fs_->make<TH2D> ("dedxStripVsP", ";p [GeV];#LTdE/dx#GT (strips) [MeV/cm]", 200, 0.0, 200.0, 200, 0.0, 10.0);
  twoDHists_["dedxStripVsPLog"]    = fs_->make<TH2D> ("dedxStripVsPLog", ";p [GeV];#LTdE/dx#GT (strips) [MeV/cm]", pLogBins.size () - 1, pLogBins.data (), 200, 0.0, 10.0);
  twoDHists_["dedxStripLogVsP"]    = fs_->make<TH2D> ("dedxStripLogVsP", ";p [GeV];#LTdE/dx#GT (strips) [MeV/cm]", 200, 0.0, 200.0, dEdxLogBins.size () - 1, dEdxLogBins.data ());
  twoDHists_["dedxStripLogVsPLog"] = fs_->make<TH2D> ("dedxStripLogVsPLog", ";p [GeV];#LTdE/dx (strips#GT [MeV/cm]", pLogBins.size () - 1, pLogBins.data (), dEdxLogBins.size () - 1, dEdxLogBins.data ());

  twoDHists_["dedxStripVsPixel"] = fs_->make<TH2D> ("dedxStripVsPixel", ";#LTdE/dx#GT (pixels) [MeV/cm];#LTdE/dx#GT (strip) [MeV/cm]", 200, 0, 10, 200, 0, 10);

  oneDHists_["massEstimatePixel"] = fs_->make<TH1D> ("massEstimatePixel", ";Mass [GeV];Tracks", 500, 0.0, 2000.0);
  oneDHists_["massEstimateStrip"] = fs_->make<TH1D> ("massEstimateStrip", ";Mass [GeV];Tracks", 500, 0.0, 2000.0);

  tracksToken_ = consumes<vector<reco::Track> > (tracks_);
  electronsToken_ = consumes<vector<reco::GsfElectron> > (electrons_);
  muonsToken_ = consumes<vector<reco::Muon> > (muons_);
  dEdxPixelToken_ = consumes<edm::ValueMap<reco::DeDxData> > (dEdxPixel_);
  dEdxStripToken_ = consumes<edm::ValueMap<reco::DeDxData> > (dEdxStrip_);
}

DEdxAnalyzer::~DEdxAnalyzer ()
{
}

void
DEdxAnalyzer::analyze (const edm::Event &event, const edm::EventSetup &setup)
{
  edm::Handle<vector<reco::Track> > tracks;
  event.getByToken (tracksToken_, tracks);

  edm::Handle<vector<reco::GsfElectron> > electrons;
  event.getByToken (electronsToken_, electrons);
  
  edm::Handle<vector<reco::Muon> > muons;
  event.getByToken (muonsToken_, muons);
  
  edm::Handle<edm::ValueMap<reco::DeDxData> > dEdxPixel;
  event.getByToken (dEdxPixelToken_, dEdxPixel);

  edm::Handle<edm::ValueMap<reco::DeDxData> > dEdxStrip;
  event.getByToken (dEdxStripToken_, dEdxStrip);

  vector<SlimTrack> selectedTracks;
  for (unsigned i = 0; i < tracks->size (); i++) {
    const edm::Ref<vector<reco::Track> > trackRef (tracks, i);
    const reco::DeDxData &dEdxDataPixel = (*dEdxPixel)[trackRef];
    const reco::DeDxData &dEdxDataStrip = (*dEdxStrip)[trackRef];

    if (trackRef->pt () < minPt_) continue;
    if (requiredNumLayers_ > 0) {
      if(requiredNumLayers_ == 6 && trackRef->hitPattern().trackerLayersWithMeasurement() < requiredNumLayers_) continue;
      else if(trackRef->hitPattern().trackerLayersWithMeasurement() != requiredNumLayers_) continue;
    }
    if (vetoElectronsOrMuons_ == "electrons" && isNearElectron (*trackRef, *electrons)) continue;
    if (vetoElectronsOrMuons_ == "muons" && isNearMuon (*trackRef, *muons)) continue;
    if (vetoElectronsOrMuons_ == "both" && 
        (isNearElectron (*trackRef, *electrons) || isNearMuon (*trackRef, *muons))) continue;
    if (minNMissOut_ > 0 && trackRef->hitPattern().trackerLayersWithoutMeasurement(reco::HitPattern::MISSING_OUTER_HITS) < minNMissOut_) continue;

    selectedTracks.push_back (SlimTrack (*trackRef, 
                                         dEdxDataPixel.dEdx(), dEdxDataStrip.dEdx(),
                                         dEdxDataPixel.numberOfMeasurements(), dEdxDataStrip.numberOfMeasurements(),
                                         dEdxDataPixel.numberOfSaturatedMeasurements(), dEdxDataStrip.numberOfSaturatedMeasurements()));
  }
  clog << "found " << selectedTracks.size () << " tracks in " << event.id () << endl;
  if (selectedTracks.empty ()) return;

  for (const auto &selectedTrack : selectedTracks) {
    twoDHists_.at ("dedxPixelVsP")->Fill       (selectedTrack.p, selectedTrack.dEdxPixel);
    twoDHists_.at ("dedxPixelVsPLog")->Fill    (selectedTrack.p, selectedTrack.dEdxPixel);
    twoDHists_.at ("dedxPixelLogVsP")->Fill    (selectedTrack.p, selectedTrack.dEdxPixel);
    twoDHists_.at ("dedxPixelLogVsPLog")->Fill (selectedTrack.p, selectedTrack.dEdxPixel);

    twoDHists_.at ("dedxStripVsP")->Fill       (selectedTrack.p, selectedTrack.dEdxStrip);
    twoDHists_.at ("dedxStripVsPLog")->Fill    (selectedTrack.p, selectedTrack.dEdxStrip);
    twoDHists_.at ("dedxStripLogVsP")->Fill    (selectedTrack.p, selectedTrack.dEdxStrip);
    twoDHists_.at ("dedxStripLogVsPLog")->Fill (selectedTrack.p, selectedTrack.dEdxStrip);

    twoDHists_.at ("dedxStripVsPixel")->Fill (selectedTrack.dEdxPixel, selectedTrack.dEdxStrip);

    oneDHists_.at ("massEstimatePixel")->Fill  (sqrt((selectedTrack.dEdxPixel - 3.375) / 2.684 * selectedTrack.p * selectedTrack.p));
    oneDHists_.at ("massEstimateStrip")->Fill  (sqrt((selectedTrack.dEdxStrip - 3.375) / 2.684 * selectedTrack.p * selectedTrack.p));

    cout << "\tp = " << selectedTrack.p << ", pixels = " << selectedTrack.dEdxPixel << ", strips = " << selectedTrack.dEdxStrip << endl;
    cout << "\t\t(eta, phi) = (" << selectedTrack.eta << ", " << selectedTrack.phi << ")" << endl;
    cout << "\t\tnumMeasurements pixels = " << selectedTrack.numMeasurementsPixels << " (" << selectedTrack.numSaturatedMeasurementsPixels << " saturated)" << endl;
    cout << "\t\tnumMeasurements strips = " << selectedTrack.numMeasurementsStrips << " (" << selectedTrack.numSaturatedMeasurementsStrips << " saturated)" << endl;
  }
}

void
DEdxAnalyzer::logSpace (const unsigned n, const double a, const double b, vector<double> &bins) const
{
  double step = (b - a) / ((double) n);

  bins.clear ();
  for (double i = a; i < b + 0.5 * step; i += step)
    bins.push_back (pow (10.0, i));
}

bool
DEdxAnalyzer::isNearElectron (const reco::Track &track, const vector<reco::GsfElectron> &leptons) const
{
  for (const auto &lepton : leptons)
    {
      if (deltaR (track, lepton) < 0.15)
        return true;
    }
  return false;
}

bool
DEdxAnalyzer::isNearMuon (const reco::Track &track, const vector<reco::Muon> &leptons) const
{
  for (const auto &lepton : leptons)
    {
      if (!muon::isLooseMuon (lepton))
        continue;
      if (deltaR (track, lepton) < 0.15)
        return true;
    }
  return false;
}

DEFINE_FWK_MODULE (DEdxAnalyzer);
