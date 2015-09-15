#include "CommonTools/Utils/interface/TFileDirectory.h"

#include "DataFormats/Math/interface/deltaR.h"
#include "DataFormats/PatCandidates/interface/Electron.h"

#include "DisappTrks/TriggerAnalysis/plugins/TriggerEfficiency.h"

TriggerEfficiency::TriggerEfficiency (const edm::ParameterSet &cfg) :
  mets_ (cfg.getParameter<edm::InputTag> ("mets")),
  caloMets_ (cfg.getParameter<edm::InputTag> ("caloMets")),
  muons_ (cfg.getParameter<edm::InputTag> ("muons")),
  electrons_ (cfg.getParameter<edm::InputTag> ("electrons")),
  triggerBits_ (cfg.getParameter<edm::InputTag> ("triggerBits")),
  triggerObjs_ (cfg.getParameter<edm::InputTag> ("triggerObjs")),
  vertices_ (cfg.getParameter<edm::InputTag> ("vertices")),
  genParticles_ (cfg.getParameter<edm::InputTag> ("genParticles")),
  metTriggersList_ ({
    {"hltMet_75"},
    {"hltMETClean75"},
    {"HLT_PFMET120_PFMHT120_IDLoose_v"},
    {"HLT_PFMETNoMu120_NoiseCleaned_PFMHTNoMu120_IDTight_v"},
    {"HLT_PFMET170_NoiseCleaned_v"},
    {"hltMETClean75", "HLT_PFMET120_PFMHT120_IDLoose_v"},
    {"hltMETClean75", "HLT_PFMETNoMu120_NoiseCleaned_PFMHTNoMu120_IDTight_v"},
    {"hltMETClean75", "HLT_PFMET170_NoiseCleaned_v"},
    {"hltMETClean75", "HLT_PFMET120_PFMHT120_IDLoose_v", "HLT_PFMETNoMu120_NoiseCleaned_PFMHTNoMu120_IDTight_v"}
  }),
  metTriggerNames_ ({})
{
  TH1::SetDefaultSumw2 ();
  TFileDirectory MuMETNoMETNoTrigger_metDir = fs_->mkdir ("MuMETNoMETNoTriggerPlotter/Met Plots"),
                 MuMETNoMETNoTrigger_muonDir = fs_->mkdir ("MuMETNoMETNoTriggerPlotter/Muon Plots");
  map<string, TFileDirectory> MuMETNoMET_metDir,
                              MuMETNoMET_muonDir,
                              MuMETNoMuonPt_metDir,
                              MuMETNoMuonPt_muonDir,
                              MuMETNoMuonPtNoTrigger_metDir,
                              MuMETNoMuonPtNoTrigger_muonDir;
  vector<double> bins, wideBins;
  logSpace (1000, 0.0, 3.0, bins);
  logSpace (60, 0.0, 3.0, wideBins);

  oneDHists_["NoTrigger"];
  twoDHists_["NoTrigger"];

  oneDHists_.at ("NoTrigger")["MuMETNoMETNoTrigger_metDir/metPt"] = MuMETNoMETNoTrigger_metDir.make<TH1D> ("metPt", ";E_{T}^{miss} [GeV]", bins.size () - 1, bins.data ());
  oneDHists_.at ("NoTrigger")["MuMETNoMETNoTrigger_metDir/metPhi"] = MuMETNoMETNoTrigger_metDir.make<TH1D> ("metPhi", ";E_{T}^{miss} #phi", 1000, -3.2, 3.2);
  oneDHists_.at ("NoTrigger")["MuMETNoMETNoTrigger_metDir/caloMetPt"] = MuMETNoMETNoTrigger_metDir.make<TH1D> ("caloMetPt", ";calo E_{T}^{miss} [GeV]", bins.size () - 1, bins.data ());
  oneDHists_.at ("NoTrigger")["MuMETNoMETNoTrigger_metDir/caloMetPhi"] = MuMETNoMETNoTrigger_metDir.make<TH1D> ("caloMetPhi", ";calo E_{T}^{miss} #phi", 1000, -3.2, 3.2);
  oneDHists_.at ("NoTrigger")["MuMETNoMETNoTrigger_muonDir/muonPt"] = MuMETNoMETNoTrigger_muonDir.make<TH1D> ("muonPt", ";muon p_{T} [GeV]", bins.size () - 1, bins.data ());
  oneDHists_.at ("NoTrigger")["MuMETNoMETNoTrigger_muonDir/muonPhi"] = MuMETNoMETNoTrigger_muonDir.make<TH1D> ("muonPhi", ";muon #phi", 1000, -3.2, 3.2);
  oneDHists_.at ("NoTrigger")["MuMETNoMETNoTrigger_muonDir/muonEta"] = MuMETNoMETNoTrigger_muonDir.make<TH1D> ("muonEta", ";muon #eta", 1000, -5.0, 5.0);

  twoDHists_.at ("NoTrigger")["MuMETNoMETNoTrigger_metDir/caloMetVsPFMET"] = MuMETNoMETNoTrigger_metDir.make<TH2D> ("caloMetVsPFMET", ";PF E_{T}^{miss} [GeV];calo E_{T}^{miss} [GeV]", wideBins.size () - 1, wideBins.data (), wideBins.size () - 1, wideBins.data ());
  twoDHists_.at ("NoTrigger")["MuMETNoMETNoTrigger_metDir/hltMetVsPFMET"] = MuMETNoMETNoTrigger_metDir.make<TH2D> ("hltMetVsPFMET", ";PF E_{T}^{miss} [GeV];hltMet [GeV]", wideBins.size () - 1, wideBins.data (), wideBins.size () - 1, wideBins.data ());
  twoDHists_.at ("NoTrigger")["MuMETNoMETNoTrigger_metDir/hltMetCleanVsPFMET"] = MuMETNoMETNoTrigger_metDir.make<TH2D> ("hltMetCleanVsPFMET", ";PF E_{T}^{miss} [GeV];hltMetClean [GeV]", wideBins.size () - 1, wideBins.data (), wideBins.size () - 1, wideBins.data ());
  twoDHists_.at ("NoTrigger")["MuMETNoMETNoTrigger_metDir/hltMetVsCaloMET"] = MuMETNoMETNoTrigger_metDir.make<TH2D> ("hltMetVsCaloMET", ";calo E_{T}^{miss} [GeV];hltMet [GeV]", wideBins.size () - 1, wideBins.data (), wideBins.size () - 1, wideBins.data ());
  twoDHists_.at ("NoTrigger")["MuMETNoMETNoTrigger_metDir/hltMetCleanVsCaloMET"] = MuMETNoMETNoTrigger_metDir.make<TH2D> ("hltMetCleanVsCaloMET", ";calo E_{T}^{miss} [GeV];hltMetClean [GeV]", wideBins.size () - 1, wideBins.data (), wideBins.size () - 1, wideBins.data ());

  for (const auto &metTriggers : metTriggersList_)
    {
      string metTriggerName = "";
      for (auto metTrigger = metTriggers.cbegin (); metTrigger != metTriggers.cend (); metTrigger++)
        {
          metTriggerName += *metTrigger;
          if (metTrigger + 1 != metTriggers.cend ())
            metTriggerName += " OR ";
        }
      metTriggerNames_.push_back (metTriggerName);

      MuMETNoMET_metDir[metTriggerName] = fs_->mkdir ("MuMETNoMETPlotter/" + metTriggerName + "/Met Plots"),
      MuMETNoMET_muonDir[metTriggerName] = fs_->mkdir ("MuMETNoMETPlotter/" + metTriggerName + "/Muon Plots"),
      MuMETNoMuonPt_metDir[metTriggerName] = fs_->mkdir ("MuMETNoMuonPtPlotter/" + metTriggerName + "/Met Plots"),
      MuMETNoMuonPt_muonDir[metTriggerName] = fs_->mkdir ("MuMETNoMuonPtPlotter/" + metTriggerName + "/Muon Plots");
      MuMETNoMuonPtNoTrigger_metDir[metTriggerName] = fs_->mkdir ("MuMETNoMuonPtNoTriggerPlotter/" + metTriggerName + "/Met Plots");
      MuMETNoMuonPtNoTrigger_muonDir[metTriggerName] = fs_->mkdir ("MuMETNoMuonPtNoTriggerPlotter/" + metTriggerName + "/Muon Plots");

      oneDHists_[metTriggerName];
      twoDHists_[metTriggerName];

      oneDHists_.at (metTriggerName)["MuMETNoMET_metDir/metPt"] = MuMETNoMET_metDir.at (metTriggerName).make<TH1D> ("metPt", ";E_{T}^{miss} [GeV]", bins.size () - 1, bins.data ());
      oneDHists_.at (metTriggerName)["MuMETNoMET_metDir/metPhi"] = MuMETNoMET_metDir.at (metTriggerName).make<TH1D> ("metPhi", ";E_{T}^{miss} #phi", 1000, -3.2, 3.2);
      oneDHists_.at (metTriggerName)["MuMETNoMET_metDir/caloMetPt"] = MuMETNoMET_metDir.at (metTriggerName).make<TH1D> ("caloMetPt", ";calo E_{T}^{miss} [GeV]", bins.size () - 1, bins.data ());
      oneDHists_.at (metTriggerName)["MuMETNoMET_metDir/caloMetPhi"] = MuMETNoMET_metDir.at (metTriggerName).make<TH1D> ("caloMetPhi", ";calo E_{T}^{miss} #phi", 1000, -3.2, 3.2);
      oneDHists_.at (metTriggerName)["MuMETNoMET_muonDir/muonPt"] = MuMETNoMET_muonDir.at (metTriggerName).make<TH1D> ("muonPt", ";muon p_{T} [GeV]", bins.size () - 1, bins.data ());
      oneDHists_.at (metTriggerName)["MuMETNoMET_muonDir/muonPhi"] = MuMETNoMET_muonDir.at (metTriggerName).make<TH1D> ("muonPhi", ";muon #phi", 1000, -3.2, 3.2);
      oneDHists_.at (metTriggerName)["MuMETNoMET_muonDir/muonEta"] = MuMETNoMET_muonDir.at (metTriggerName).make<TH1D> ("muonEta", ";muon #eta", 1000, -5.0, 5.0);

      twoDHists_.at (metTriggerName)["MuMETNoMET_metDir/caloMetVsPFMET"] = MuMETNoMET_metDir.at (metTriggerName).make<TH2D> ("caloMetVsPFMET", ";PF E_{T}^{miss} [GeV];calo E_{T}^{miss} [GeV]", wideBins.size () - 1, wideBins.data (), wideBins.size () - 1, wideBins.data ());
      twoDHists_.at (metTriggerName)["MuMETNoMET_metDir/hltMetVsPFMET"] = MuMETNoMET_metDir.at (metTriggerName).make<TH2D> ("hltMetVsPFMET", ";PF E_{T}^{miss} [GeV];hltMet [GeV]", wideBins.size () - 1, wideBins.data (), wideBins.size () - 1, wideBins.data ());
      twoDHists_.at (metTriggerName)["MuMETNoMET_metDir/hltMetCleanVsPFMET"] = MuMETNoMET_metDir.at (metTriggerName).make<TH2D> ("hltMetCleanVsPFMET", ";PF E_{T}^{miss} [GeV];hltMetClean [GeV]", wideBins.size () - 1, wideBins.data (), wideBins.size () - 1, wideBins.data ());
      twoDHists_.at (metTriggerName)["MuMETNoMET_metDir/hltMetVsCaloMET"] = MuMETNoMET_metDir.at (metTriggerName).make<TH2D> ("hltMetVsCaloMET", ";calo E_{T}^{miss} [GeV];hltMet [GeV]", wideBins.size () - 1, wideBins.data (), wideBins.size () - 1, wideBins.data ());
      twoDHists_.at (metTriggerName)["MuMETNoMET_metDir/hltMetCleanVsCaloMET"] = MuMETNoMET_metDir.at (metTriggerName).make<TH2D> ("hltMetCleanVsCaloMET", ";calo E_{T}^{miss} [GeV];hltMetClean [GeV]", wideBins.size () - 1, wideBins.data (), wideBins.size () - 1, wideBins.data ());

      oneDHists_.at (metTriggerName)["MuMETNoMuonPt_metDir/metPt"] = MuMETNoMuonPt_metDir.at (metTriggerName).make<TH1D> ("metPt", ";E_{T}^{miss} [GeV]", bins.size () - 1, bins.data ());
      oneDHists_.at (metTriggerName)["MuMETNoMuonPt_metDir/metPhi"] = MuMETNoMuonPt_metDir.at (metTriggerName).make<TH1D> ("metPhi", ";E_{T}^{miss} #phi", 1000, -3.2, 3.2);
      oneDHists_.at (metTriggerName)["MuMETNoMuonPt_metDir/caloMetPt"] = MuMETNoMuonPt_metDir.at (metTriggerName).make<TH1D> ("caloMetPt", ";calo E_{T}^{miss} [GeV]", bins.size () - 1, bins.data ());
      oneDHists_.at (metTriggerName)["MuMETNoMuonPt_metDir/caloMetPhi"] = MuMETNoMuonPt_metDir.at (metTriggerName).make<TH1D> ("caloMetPhi", ";calo E_{T}^{miss} #phi", 1000, -3.2, 3.2);
      oneDHists_.at (metTriggerName)["MuMETNoMuonPt_muonDir/muonPt"] = MuMETNoMuonPt_muonDir.at (metTriggerName).make<TH1D> ("muonPt", ";muon p_{T} [GeV]", bins.size () - 1, bins.data ());
      oneDHists_.at (metTriggerName)["MuMETNoMuonPt_muonDir/muonPhi"] = MuMETNoMuonPt_muonDir.at (metTriggerName).make<TH1D> ("muonPhi", ";muon #phi", 1000, -3.2, 3.2);
      oneDHists_.at (metTriggerName)["MuMETNoMuonPt_muonDir/muonEta"] = MuMETNoMuonPt_muonDir.at (metTriggerName).make<TH1D> ("muonEta", ";muon #eta", 1000, -5.0, 5.0);

      twoDHists_.at (metTriggerName)["MuMETNoMuonPt_metDir/caloMetVsPFMET"] = MuMETNoMuonPt_metDir.at (metTriggerName).make<TH2D> ("caloMetVsPFMET", ";PF E_{T}^{miss} [GeV];calo E_{T}^{miss} [GeV]", wideBins.size () - 1, wideBins.data (), wideBins.size () - 1, wideBins.data ());
      twoDHists_.at (metTriggerName)["MuMETNoMuonPt_metDir/hltMetVsPFMET"] = MuMETNoMuonPt_metDir.at (metTriggerName).make<TH2D> ("hltMetVsPFMET", ";PF E_{T}^{miss} [GeV];hltMet [GeV]", wideBins.size () - 1, wideBins.data (), wideBins.size () - 1, wideBins.data ());
      twoDHists_.at (metTriggerName)["MuMETNoMuonPt_metDir/hltMetCleanVsPFMET"] = MuMETNoMuonPt_metDir.at (metTriggerName).make<TH2D> ("hltMetCleanVsPFMET", ";PF E_{T}^{miss} [GeV];hltMetClean [GeV]", wideBins.size () - 1, wideBins.data (), wideBins.size () - 1, wideBins.data ());
      twoDHists_.at (metTriggerName)["MuMETNoMuonPt_metDir/hltMetVsCaloMET"] = MuMETNoMuonPt_metDir.at (metTriggerName).make<TH2D> ("hltMetVsCaloMET", ";calo E_{T}^{miss} [GeV];hltMet [GeV]", wideBins.size () - 1, wideBins.data (), wideBins.size () - 1, wideBins.data ());
      twoDHists_.at (metTriggerName)["MuMETNoMuonPt_metDir/hltMetCleanVsCaloMET"] = MuMETNoMuonPt_metDir.at (metTriggerName).make<TH2D> ("hltMetCleanVsCaloMET", ";calo E_{T}^{miss} [GeV];hltMetClean [GeV]", wideBins.size () - 1, wideBins.data (), wideBins.size () - 1, wideBins.data ());

      oneDHists_.at (metTriggerName)["MuMETNoMuonPtNoTrigger_metDir/metPt"] = MuMETNoMuonPtNoTrigger_metDir.at (metTriggerName).make<TH1D> ("metPt", ";E_{T}^{miss} [GeV]", bins.size () - 1, bins.data ());
      oneDHists_.at (metTriggerName)["MuMETNoMuonPtNoTrigger_metDir/metPhi"] = MuMETNoMuonPtNoTrigger_metDir.at (metTriggerName).make<TH1D> ("metPhi", ";E_{T}^{miss} #phi", 1000, -3.2, 3.2);
      oneDHists_.at (metTriggerName)["MuMETNoMuonPtNoTrigger_metDir/caloMetPt"] = MuMETNoMuonPtNoTrigger_metDir.at (metTriggerName).make<TH1D> ("caloMetPt", ";calo E_{T}^{miss} [GeV]", bins.size () - 1, bins.data ());
      oneDHists_.at (metTriggerName)["MuMETNoMuonPtNoTrigger_metDir/caloMetPhi"] = MuMETNoMuonPtNoTrigger_metDir.at (metTriggerName).make<TH1D> ("caloMetPhi", ";calo E_{T}^{miss} #phi", 1000, -3.2, 3.2);
      oneDHists_.at (metTriggerName)["MuMETNoMuonPtNoTrigger_muonDir/muonPt"] = MuMETNoMuonPtNoTrigger_muonDir.at (metTriggerName).make<TH1D> ("muonPt", ";muon p_{T} [GeV]", bins.size () - 1, bins.data ());
      oneDHists_.at (metTriggerName)["MuMETNoMuonPtNoTrigger_muonDir/muonPhi"] = MuMETNoMuonPtNoTrigger_muonDir.at (metTriggerName).make<TH1D> ("muonPhi", ";muon #phi", 1000, -3.2, 3.2);
      oneDHists_.at (metTriggerName)["MuMETNoMuonPtNoTrigger_muonDir/muonEta"] = MuMETNoMuonPtNoTrigger_muonDir.at (metTriggerName).make<TH1D> ("muonEta", ";muon #eta", 1000, -5.0, 5.0);

      twoDHists_.at (metTriggerName)["MuMETNoMuonPtNoTrigger_metDir/caloMetVsPFMET"] = MuMETNoMuonPtNoTrigger_metDir.at (metTriggerName).make<TH2D> ("caloMetVsPFMET", ";PF E_{T}^{miss} [GeV];calo E_{T}^{miss} [GeV]", wideBins.size () - 1, wideBins.data (), wideBins.size () - 1, wideBins.data ());
      twoDHists_.at (metTriggerName)["MuMETNoMuonPtNoTrigger_metDir/hltMetVsPFMET"] = MuMETNoMuonPtNoTrigger_metDir.at (metTriggerName).make<TH2D> ("hltMetVsPFMET", ";PF E_{T}^{miss} [GeV];hltMet [GeV]", wideBins.size () - 1, wideBins.data (), wideBins.size () - 1, wideBins.data ());
      twoDHists_.at (metTriggerName)["MuMETNoMuonPtNoTrigger_metDir/hltMetCleanVsPFMET"] = MuMETNoMuonPtNoTrigger_metDir.at (metTriggerName).make<TH2D> ("hltMetCleanVsPFMET", ";PF E_{T}^{miss} [GeV];hltMetClean [GeV]", wideBins.size () - 1, wideBins.data (), wideBins.size () - 1, wideBins.data ());
      twoDHists_.at (metTriggerName)["MuMETNoMuonPtNoTrigger_metDir/hltMetVsCaloMET"] = MuMETNoMuonPtNoTrigger_metDir.at (metTriggerName).make<TH2D> ("hltMetVsCaloMET", ";calo E_{T}^{miss} [GeV];hltMet [GeV]", wideBins.size () - 1, wideBins.data (), wideBins.size () - 1, wideBins.data ());
      twoDHists_.at (metTriggerName)["MuMETNoMuonPtNoTrigger_metDir/hltMetCleanVsCaloMET"] = MuMETNoMuonPtNoTrigger_metDir.at (metTriggerName).make<TH2D> ("hltMetCleanVsCaloMET", ";calo E_{T}^{miss} [GeV];hltMetClean [GeV]", wideBins.size () - 1, wideBins.data (), wideBins.size () - 1, wideBins.data ());
    }
}

TriggerEfficiency::~TriggerEfficiency ()
{
}

void
TriggerEfficiency::analyze (const edm::Event &event, const edm::EventSetup &setup)
{
  edm::Handle<vector<pat::MET> > mets;
  event.getByLabel (mets_, mets);
  edm::Handle<vector<reco::CaloMET> > caloMets;
  event.getByLabel (caloMets_, caloMets);
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
  edm::Handle<vector<reco::GenParticle> > genParticles;
  event.getByLabel (genParticles_, genParticles);

  const edm::TriggerNames &triggerNames = event.triggerNames (*triggerBits);
  const reco::Vertex &pv = vertices->at (0);
  const pat::TriggerObjectStandAlone &hltMet = getHLTMET (triggerNames, *triggerObjs, "hltMet");
  const pat::TriggerObjectStandAlone &hltMetClean = getHLTMET (triggerNames, *triggerObjs, "hltMetClean");

  //////////////////////////////////////////////////////////////////////////////
  // MuMETNoMETNoTrigger channel
  //////////////////////////////////////////////////////////////////////////////
  fillHistograms (*mets, *caloMets, hltMet, hltMetClean, *muons, "MuMETNoMETNoTrigger");
  //////////////////////////////////////////////////////////////////////////////

  for (unsigned i = 0; i < metTriggersList_.size (); i++)
    {
      bool passesMETTriggers = false;
      for (const auto &metTrigger : metTriggersList_.at (i))
        {
          if (metTrigger == "hltMet_75")
            passesMETTriggers = passesMETTriggers || (hltMet.pt () > 75.0);
          else
            passesMETTriggers = passesMETTriggers || (metTrigger.find ("HLT") == 0 ? passesTrigger (triggerNames, *triggerBits, metTrigger) : passesTriggerFilter (triggerNames, *triggerObjs, metTrigger));
          if (passesMETTriggers)
            break;
        }

      //////////////////////////////////////////////////////////////////////////////
      // MuMETNoMET channel
      //////////////////////////////////////////////////////////////////////////////
      if (passesMETTriggers)
        fillHistograms (*mets, *caloMets, hltMet, hltMetClean, *muons, "MuMETNoMET", metTriggerNames_.at (i));
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
          if (muon.innerTrack ()->hitPattern ().trackerLayersWithoutMeasurement (reco::HitPattern::MISSING_INNER_HITS) > 0)
            continue;
          if (muon.innerTrack ()->hitPattern ().trackerLayersWithoutMeasurement (reco::HitPattern::TRACK_HITS) > 0)
            continue;
          if ((muon.isolationR03 ().sumPt / muon.pt ()) > 0.01)
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
      if (selectedMuons.size () == 1 && passesElectronVeto && passesMETTriggers)
        fillHistograms (*mets, *caloMets, hltMet, hltMetClean, *selectedMuons.at (0), "MuMETNoMuonPtNoTrigger", metTriggerNames_.at (i));
      //////////////////////////////////////////////////////////////////////////////

      //////////////////////////////////////////////////////////////////////////////
      // MuMETNoMuonPt channel
      //////////////////////////////////////////////////////////////////////////////
      if (selectedMuons.size () == 1 && passesElectronVeto && passesMETTriggers && passesTrigger (triggerNames, *triggerBits, "HLT_MET75_IsoTrk50_v"))
        fillHistograms (*mets, *caloMets, hltMet, hltMetClean, *selectedMuons.at (0), "MuMETNoMuonPt", metTriggerNames_.at (i));
      //////////////////////////////////////////////////////////////////////////////
    }
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
TriggerEfficiency::fillHistograms (const vector<pat::MET> &mets, const vector<reco::CaloMET> &caloMets, const pat::TriggerObjectStandAlone &hltMet, const pat::TriggerObjectStandAlone &hltMetClean, const vector<pat::Muon> &muons, const string &channel, const string &trigger) const
{
  for (const auto &met : mets)
    {
      oneDHists_.at (trigger).at (channel + "_metDir/metPt")->Fill (met.pt ());
      oneDHists_.at (trigger).at (channel + "_metDir/metPhi")->Fill (met.phi ());

      for (const auto &caloMet : caloMets)
        twoDHists_.at (trigger).at (channel + "_metDir/caloMetVsPFMET")->Fill (met.pt (), caloMet.pt ());
      twoDHists_.at (trigger).at (channel + "_metDir/hltMetVsPFMET")->Fill (met.pt (), hltMet.pt ());
      twoDHists_.at (trigger).at (channel + "_metDir/hltMetCleanVsPFMET")->Fill (met.pt (), hltMetClean.pt ());
    }
  for (const auto &caloMet : caloMets)
    {
      oneDHists_.at (trigger).at (channel + "_metDir/caloMetPt")->Fill (caloMet.pt ());
      oneDHists_.at (trigger).at (channel + "_metDir/caloMetPhi")->Fill (caloMet.phi ());

      twoDHists_.at (trigger).at (channel + "_metDir/hltMetVsCaloMET")->Fill (caloMet.pt (), hltMet.pt ());
      twoDHists_.at (trigger).at (channel + "_metDir/hltMetCleanVsCaloMET")->Fill (caloMet.pt (), hltMetClean.pt ());
    }
  for (const auto &muon : muons)
    {
      oneDHists_.at (trigger).at (channel + "_muonDir/muonPt")->Fill (muon.pt ());
      oneDHists_.at (trigger).at (channel + "_muonDir/muonPhi")->Fill (muon.phi ());
      oneDHists_.at (trigger).at (channel + "_muonDir/muonEta")->Fill (muon.eta ());
    }
}

void
TriggerEfficiency::fillHistograms (const vector<pat::MET> &mets, const vector<reco::CaloMET> &caloMets, const pat::TriggerObjectStandAlone &hltMet, const pat::TriggerObjectStandAlone &hltMetClean, const pat::Muon &muon, const string &channel, const string &trigger) const
{
  for (const auto &met : mets)
    {
      oneDHists_.at (trigger).at (channel + "_metDir/metPt")->Fill (met.pt ());
      oneDHists_.at (trigger).at (channel + "_metDir/metPhi")->Fill (met.phi ());

      for (const auto &caloMet : caloMets)
        twoDHists_.at (trigger).at (channel + "_metDir/caloMetVsPFMET")->Fill (met.pt (), caloMet.pt ());
      twoDHists_.at (trigger).at (channel + "_metDir/hltMetVsPFMET")->Fill (met.pt (), hltMet.pt ());
      twoDHists_.at (trigger).at (channel + "_metDir/hltMetCleanVsPFMET")->Fill (met.pt (), hltMetClean.pt ());
    }
  for (const auto &caloMet : caloMets)
    {
      oneDHists_.at (trigger).at (channel + "_metDir/caloMetPt")->Fill (caloMet.pt ());
      oneDHists_.at (trigger).at (channel + "_metDir/caloMetPhi")->Fill (caloMet.phi ());

      twoDHists_.at (trigger).at (channel + "_metDir/hltMetVsCaloMET")->Fill (caloMet.pt (), hltMet.pt ());
      twoDHists_.at (trigger).at (channel + "_metDir/hltMetCleanVsCaloMET")->Fill (caloMet.pt (), hltMetClean.pt ());
    }
  oneDHists_.at (trigger).at (channel + "_muonDir/muonPt")->Fill (muon.pt ());
  oneDHists_.at (trigger).at (channel + "_muonDir/muonPhi")->Fill (muon.phi ());
  oneDHists_.at (trigger).at (channel + "_muonDir/muonEta")->Fill (muon.eta ());
}

const pat::TriggerObjectStandAlone &
TriggerEfficiency::getHLTMET (const edm::TriggerNames &triggerNames, const vector<pat::TriggerObjectStandAlone> &triggerObjs, const string &collection) const
{
  unsigned i = 0;
  for (auto triggerObj : triggerObjs)
    {
      triggerObj.unpackPathNames (triggerNames);
      if (triggerObj.collection () == (collection + "::HLT"))
        return triggerObjs.at (i);
      i++;
    }

  pat::TriggerObjectStandAlone *dummy = new pat::TriggerObjectStandAlone ();
  return *dummy;
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

bool
TriggerEfficiency::genMatched (const pat::Muon &muon, const vector<reco::GenParticle> &genParticles, const int pdgId, const int status, const double maxDeltaR) const
{
  for (const auto &genParticle : genParticles)
    {
      if (abs (genParticle.pdgId ()) != abs (pdgId))
        continue;
      if (genParticle.status () != status)
        break;
      if (deltaR (muon, genParticle) > maxDeltaR)
        continue;
      return true;
    }
  return false;
}

#include "FWCore/Framework/interface/MakerMacros.h"
DEFINE_FWK_MODULE(TriggerEfficiency);
