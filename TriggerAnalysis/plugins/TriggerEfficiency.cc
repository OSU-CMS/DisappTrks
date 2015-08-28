#include "CommonTools/Utils/interface/TFileDirectory.h"

#include "DataFormats/PatCandidates/interface/Electron.h"

#include "DisappTrks/TriggerAnalysis/plugins/TriggerEfficiency.h"

TriggerEfficiency::TriggerEfficiency (const edm::ParameterSet &cfg) :
  mets_ (cfg.getParameter<edm::InputTag> ("mets")),
  muons_ (cfg.getParameter<edm::InputTag> ("muons")),
  electrons_ (cfg.getParameter<edm::InputTag> ("electrons")),
  triggerBits_ (cfg.getParameter<edm::InputTag> ("triggerBits")),
  triggerObjs_ (cfg.getParameter<edm::InputTag> ("triggerObjs")),
  vertices_ (cfg.getParameter<edm::InputTag> ("vertices"))
{
  TH1::SetDefaultSumw2 ();
  TFileDirectory MuMETNoMET_metDir = fs_->mkdir ("MuMETNoMETPlotter/Met Plots"),
                 MuMETNoMET_muonDir = fs_->mkdir ("MuMETNoMETPlotter/Muon Plots"),
                 MuMETNoMETNoTrigger_metDir = fs_->mkdir ("MuMETNoMETNoTriggerPlotter/Met Plots"),
                 MuMETNoMETNoTrigger_muonDir = fs_->mkdir ("MuMETNoMETNoTriggerPlotter/Muon Plots"),
                 MuMETNoMuonPt_metDir = fs_->mkdir ("MuMETNoMuonPtPlotter/Met Plots"),
                 MuMETNoMuonPt_muonDir = fs_->mkdir ("MuMETNoMuonPtPlotter/Muon Plots"),
                 MuMETNoMuonPtNoTrigger_metDir = fs_->mkdir ("MuMETNoMuonPtNoTriggerPlotter/Met Plots"),
                 MuMETNoMuonPtNoTrigger_muonDir = fs_->mkdir ("MuMETNoMuonPtNoTriggerPlotter/Muon Plots");

  vector<double> bins;
  logSpace (1000, 0.0, 3.0, bins);

  oneDHists_["MuMETNoMET_metDir/metPt"] = MuMETNoMET_metDir.make<TH1D> ("metPt", ";;E_{T}^{miss} [GeV]", bins.size () - 1, bins.data ());
  oneDHists_["MuMETNoMET_metDir/metPhi"] = MuMETNoMET_metDir.make<TH1D> ("metPhi", ";;E_{T}^{miss} #phi", 1000, -3.2, 3.2);
  oneDHists_["MuMETNoMET_muonDir/muonPt"] = MuMETNoMET_muonDir.make<TH1D> ("muonPt", ";;muon p_{T} [GeV]", bins.size () - 1, bins.data ());
  oneDHists_["MuMETNoMET_muonDir/muonPhi"] = MuMETNoMET_muonDir.make<TH1D> ("muonPhi", ";;muon #phi", 1000, -3.2, 3.2);
  oneDHists_["MuMETNoMET_muonDir/muonEta"] = MuMETNoMET_muonDir.make<TH1D> ("muonEta", ";;muon #eta", 1000, -5.0, 5.0);

  oneDHists_["MuMETNoMETNoTrigger_metDir/metPt"] = MuMETNoMETNoTrigger_metDir.make<TH1D> ("metPt", ";;E_{T}^{miss} [GeV]", bins.size () - 1, bins.data ());
  oneDHists_["MuMETNoMETNoTrigger_metDir/metPhi"] = MuMETNoMETNoTrigger_metDir.make<TH1D> ("metPhi", ";;E_{T}^{miss} #phi", 1000, -3.2, 3.2);
  oneDHists_["MuMETNoMETNoTrigger_muonDir/muonPt"] = MuMETNoMETNoTrigger_muonDir.make<TH1D> ("muonPt", ";;muon p_{T} [GeV]", bins.size () - 1, bins.data ());
  oneDHists_["MuMETNoMETNoTrigger_muonDir/muonPhi"] = MuMETNoMETNoTrigger_muonDir.make<TH1D> ("muonPhi", ";;muon #phi", 1000, -3.2, 3.2);
  oneDHists_["MuMETNoMETNoTrigger_muonDir/muonEta"] = MuMETNoMETNoTrigger_muonDir.make<TH1D> ("muonEta", ";;muon #eta", 1000, -5.0, 5.0);

  oneDHists_["MuMETNoMuonPt_metDir/metPt"] = MuMETNoMuonPt_metDir.make<TH1D> ("metPt", ";;E_{T}^{miss} [GeV]", bins.size () - 1, bins.data ());
  oneDHists_["MuMETNoMuonPt_metDir/metPhi"] = MuMETNoMuonPt_metDir.make<TH1D> ("metPhi", ";;E_{T}^{miss} #phi", 1000, -3.2, 3.2);
  oneDHists_["MuMETNoMuonPt_muonDir/muonPt"] = MuMETNoMuonPt_muonDir.make<TH1D> ("muonPt", ";;muon p_{T} [GeV]", bins.size () - 1, bins.data ());
  oneDHists_["MuMETNoMuonPt_muonDir/muonPhi"] = MuMETNoMuonPt_muonDir.make<TH1D> ("muonPhi", ";;muon #phi", 1000, -3.2, 3.2);
  oneDHists_["MuMETNoMuonPt_muonDir/muonEta"] = MuMETNoMuonPt_muonDir.make<TH1D> ("muonEta", ";;muon #eta", 1000, -5.0, 5.0);

  oneDHists_["MuMETNoMuonPtNoTrigger_metDir/metPt"] = MuMETNoMuonPtNoTrigger_metDir.make<TH1D> ("metPt", ";;E_{T}^{miss} [GeV]", bins.size () - 1, bins.data ());
  oneDHists_["MuMETNoMuonPtNoTrigger_metDir/metPhi"] = MuMETNoMuonPtNoTrigger_metDir.make<TH1D> ("metPhi", ";;E_{T}^{miss} #phi", 1000, -3.2, 3.2);
  oneDHists_["MuMETNoMuonPtNoTrigger_muonDir/muonPt"] = MuMETNoMuonPtNoTrigger_muonDir.make<TH1D> ("muonPt", ";;muon p_{T} [GeV]", bins.size () - 1, bins.data ());
  oneDHists_["MuMETNoMuonPtNoTrigger_muonDir/muonPhi"] = MuMETNoMuonPtNoTrigger_muonDir.make<TH1D> ("muonPhi", ";;muon #phi", 1000, -3.2, 3.2);
  oneDHists_["MuMETNoMuonPtNoTrigger_muonDir/muonEta"] = MuMETNoMuonPtNoTrigger_muonDir.make<TH1D> ("muonEta", ";;muon #eta", 1000, -5.0, 5.0);
}

TriggerEfficiency::~TriggerEfficiency ()
{
}

void
TriggerEfficiency::analyze (const edm::Event &event, const edm::EventSetup &setup)
{
  edm::Handle<vector<pat::MET> > mets;
  event.getByLabel (mets_, mets);
  edm::Handle<vector<pat::Muon> > muons;
  event.getByLabel (muons_, muons);
  edm::Handle<vector<pat::Electron> > electrons;
  event.getByLabel (electrons_, electrons);
  edm::Handle<edm::TriggerResults> triggerBits;
  event.getByLabel (triggerBits_, triggerBits);
  edm::Handle<vector<pat::TriggerObjectStandAlone> > triggerObjs;
  event.getByLabel (triggerObjs_, triggerObjs);
  edm::Handle<vector<reco::Vertex> > vertices;
  event.getByLabel (vertices_, vertices);

  const edm::TriggerNames &triggerNames = event.triggerNames (*triggerBits);
  bool passesMETFilter = passesTriggerFilter (triggerNames, *triggerObjs, "hltMETClean75");

  const reco::Vertex &pv = vertices->at (0);

  //////////////////////////////////////////////////////////////////////////////
  // MuMETNoMETNoTrigger channel
  //////////////////////////////////////////////////////////////////////////////
  fillHistograms (*mets, *muons, "MuMETNoMETNoTrigger");
  //////////////////////////////////////////////////////////////////////////////

  //////////////////////////////////////////////////////////////////////////////
  // MuMETNoMET channel
  //////////////////////////////////////////////////////////////////////////////
  if (passesMETFilter)
    fillHistograms (*mets, *muons, "MuMETNoMET");
  //////////////////////////////////////////////////////////////////////////////

  //////////////////////////////////////////////////////////////////////////////
  // MuMETNoMuonPtNoTrigger channel
  //////////////////////////////////////////////////////////////////////////////
  vector<const pat::Muon *> selectedMuons;
  selectedMuons.clear ();
  for (const auto &muon : *muons)
    {
      if (fabs (muon.eta ()) > 2.1)
        continue;
      if (!muon.isGlobalMuon ())
        continue;
      if (!muon.isPFMuon ())
        continue;
      if (muon.globalTrack ()->normalizedChi2 () > 10.0)
        continue;
      if (muon.globalTrack ()->hitPattern ().numberOfValidMuonHits () == 0)
        continue;
      if (muon.numberOfMatchedStations () <= 1)
        continue;
      if (fabs (muon.muonBestTrack ()->dxy (pv.position ())) > 0.2)
        continue;
      if (fabs (muon.muonBestTrack ()->dz (pv.position ())) > 0.5)
        continue;
      if (muon.innerTrack ()->hitPattern ().numberOfValidPixelHits () == 0)
        continue;
      if (muon.innerTrack ()->hitPattern ().trackerLayersWithMeasurement () <= 5)
        continue;
      if ((muon.isolationR03 ().sumPt / muon.pt ()) > 0.01)
        continue;
      if (muon.innerTrack ()->hitPattern ().trackerLayersWithoutMeasurement (reco::HitPattern::MISSING_INNER_HITS) > 0)
        continue;
      if (muon.innerTrack ()->hitPattern ().trackerLayersWithoutMeasurement (reco::HitPattern::TRACK_HITS) > 0)
        continue;
      selectedMuons.push_back (&muon);
    }
  bool passesElectronVeto = true;
  for (const auto &electron : *electrons)
    {
      if (electron.pt () < 10.0)
        continue;
      passesElectronVeto = false;
      break;
    }
  if (selectedMuons.size () == 1 && passesElectronVeto && passesMETFilter)
    fillHistograms (*mets, *selectedMuons.at (0), "MuMETNoMuonPtNoTrigger");
  //////////////////////////////////////////////////////////////////////////////

  //////////////////////////////////////////////////////////////////////////////
  // MuMETNoMuonPt channel
  //////////////////////////////////////////////////////////////////////////////
  if (selectedMuons.size () == 1 && passesElectronVeto && passesMETFilter && passesTrigger (triggerNames, *triggerBits, "HLT_MET75_IsoTrk50_v"))
    fillHistograms (*mets, *selectedMuons.at (0), "MuMETNoMuonPt");
  //////////////////////////////////////////////////////////////////////////////
}

void
TriggerEfficiency::logSpace (const unsigned n, const double a, const double b, vector<double> &bins) const
{
  double step = (b - a) / ((double) n);

  bins.clear ();
  for (double i = a; i < b + 0.5 * step; i += step)
    bins.push_back (pow (10.0, i));
}

void
TriggerEfficiency::linSpace (const unsigned n, const double a, const double b, vector<double> &bins) const
{
  double step = (b - a) / ((double) n);

  bins.clear ();
  for (double i = a; i < b + 0.5 * step; i += step)
    bins.push_back (i);
}

void
TriggerEfficiency::fillHistograms (const vector<pat::MET> &mets, const vector<pat::Muon> &muons, const string &channel) const
{
  for (const auto &met : mets)
    {
      oneDHists_.at (channel + "_metDir/metPt")->Fill (met.pt ());
      oneDHists_.at (channel + "_metDir/metPhi")->Fill (met.phi ());
    }
  for (const auto &muon : muons)
    {
      oneDHists_.at (channel + "_muonDir/muonPt")->Fill (muon.pt ());
      oneDHists_.at (channel + "_muonDir/muonPhi")->Fill (muon.phi ());
      oneDHists_.at (channel + "_muonDir/muonEta")->Fill (muon.eta ());
    }
}

void
TriggerEfficiency::fillHistograms (const vector<pat::MET> &mets, const pat::Muon &muon, const string &channel) const
{
  for (const auto &met : mets)
    {
      oneDHists_.at (channel + "_metDir/metPt")->Fill (met.pt ());
      oneDHists_.at (channel + "_metDir/metPhi")->Fill (met.phi ());
    }
  oneDHists_.at (channel + "_muonDir/muonPt")->Fill (muon.pt ());
  oneDHists_.at (channel + "_muonDir/muonPhi")->Fill (muon.phi ());
  oneDHists_.at (channel + "_muonDir/muonEta")->Fill (muon.eta ());
}

bool
TriggerEfficiency::passesTriggerFilter (const edm::TriggerNames &triggerNames, const vector<pat::TriggerObjectStandAlone> &triggerObjs, const string &filter) const
{
  for (auto triggerObj : triggerObjs)
    {
      triggerObj.unpackPathNames (triggerNames);
      for (const auto &filterLabel : triggerObj.filterLabels ())
        {
          if (filterLabel == filter)
            return true;
        }
    }
  return false;
}

bool
TriggerEfficiency::passesTrigger (const edm::TriggerNames &triggerNames, const edm::TriggerResults &triggerBits, const string &path) const
{
  for (unsigned i = 0; i < triggerNames.size (); i++)
    {
      string name = triggerNames.triggerName (i);
      bool pass = triggerBits.accept (i);
      if (name.find (path) == 0)
        return pass;
    }
  return false;
}

#include "FWCore/Framework/interface/MakerMacros.h"
DEFINE_FWK_MODULE(TriggerEfficiency);
