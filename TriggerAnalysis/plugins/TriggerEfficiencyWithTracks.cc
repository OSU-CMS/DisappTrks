#include "CommonTools/Utils/interface/TFileDirectory.h"

#include "DataFormats/Math/interface/deltaR.h"
#include "DataFormats/PatCandidates/interface/Electron.h"

#include "DisappTrks/TriggerAnalysis/plugins/TriggerEfficiencyWithTracks.h"

TriggerEfficiencyWithTracks::TriggerEfficiencyWithTracks (const edm::ParameterSet &cfg) :
  mets_ (cfg.getParameter<edm::InputTag> ("mets")),
  tracks_ (cfg.getParameter<edm::InputTag> ("tracks")),
  triggerBits_ (cfg.getParameter<edm::InputTag> ("triggerBits")),
  triggerObjs_ (cfg.getParameter<edm::InputTag> ("triggerObjs")),
  vertices_ (cfg.getParameter<edm::InputTag> ("vertices")),
  genParticles_ (cfg.getParameter<edm::InputTag> ("genParticles"))
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

TriggerEfficiencyWithTracks::~TriggerEfficiencyWithTracks ()
{
}

void
TriggerEfficiencyWithTracks::analyze (const edm::Event &event, const edm::EventSetup &setup)
{
  edm::Handle<vector<pat::MET> > mets;
  event.getByLabel (mets_, mets);
  edm::Handle<vector<reco::Track> > tracks;
  event.getByLabel (tracks_, tracks);
  edm::Handle<edm::TriggerResults> triggerBits;
  event.getByLabel (triggerBits_, triggerBits);
  edm::Handle<vector<pat::TriggerObjectStandAlone> > triggerObjs;
  event.getByLabel (triggerObjs_, triggerObjs);
  edm::Handle<vector<reco::Vertex> > vertices;
  event.getByLabel (vertices_, vertices);
  edm::Handle<vector<reco::GenParticle> > genParticles;
  event.getByLabel (genParticles_, genParticles);

  const edm::TriggerNames &triggerNames = event.triggerNames (*triggerBits);
  bool passesMETFilter = passesTriggerFilter (triggerNames, *triggerObjs, "hltMETClean75");

  const reco::Vertex &pv = vertices->at (0);

  //////////////////////////////////////////////////////////////////////////////
  // MuMETNoMETNoTrigger channel
  //////////////////////////////////////////////////////////////////////////////
  fillHistograms (*mets, *tracks, "MuMETNoMETNoTrigger");
  //////////////////////////////////////////////////////////////////////////////

  //////////////////////////////////////////////////////////////////////////////
  // MuMETNoMET channel
  //////////////////////////////////////////////////////////////////////////////
  if (passesMETFilter)
    fillHistograms (*mets, *tracks, "MuMETNoMET");
  //////////////////////////////////////////////////////////////////////////////

  //////////////////////////////////////////////////////////////////////////////
  // MuMETNoMuonPtNoTrigger channel
  //////////////////////////////////////////////////////////////////////////////
  vector<const reco::Track *> selectedTracks;
  selectedTracks.clear ();
  for (const auto &track : *tracks)
    {
      if (fabs (track.eta ()) > 2.5)
        continue;
      if (track.normalizedChi2 () > 10.0)
        continue;
      if (fabs (track.dxy (pv.position ())) > 0.2)
        continue;
      if (fabs (track.dz (pv.position ())) > 0.5)
        continue;
      if (track.hitPattern ().numberOfValidPixelHits () == 0)
        continue;
      if (track.hitPattern ().trackerLayersWithMeasurement () <= 5)
        continue;
      if (track.hitPattern ().trackerLayersWithoutMeasurement (reco::HitPattern::MISSING_INNER_HITS) > 0)
        continue;
      if (track.hitPattern ().trackerLayersWithoutMeasurement (reco::HitPattern::TRACK_HITS) > 0)
        continue;
      if (!genMatched (track, *genParticles, 1000024, 3, 0.1))
        continue;
      if (trackIsolation (track, *tracks, 0.3, 1.0e-12) / track.pt () > 0.01)
        continue;
      selectedTracks.push_back (&track);
    }
  sort (selectedTracks.begin (), selectedTracks.end (), ptDescending);
  if (selectedTracks.size () == 1 && passesMETFilter)
    fillHistograms (*mets, *selectedTracks.at (0), "MuMETNoMuonPtNoTrigger");
  //////////////////////////////////////////////////////////////////////////////

  //////////////////////////////////////////////////////////////////////////////
  // MuMETNoMuonPt channel
  //////////////////////////////////////////////////////////////////////////////
  if (selectedTracks.size () == 1 && passesMETFilter && passesTrigger (triggerNames, *triggerBits, "HLT_MET75_IsoTrk50_v"))
    fillHistograms (*mets, *selectedTracks.at (0), "MuMETNoMuonPt");
  //////////////////////////////////////////////////////////////////////////////
}

bool
TriggerEfficiencyWithTracks::ptDescending (const reco::Track *a, const reco::Track *b)
{
  return (a->pt () > b->pt ());
}

void
TriggerEfficiencyWithTracks::logSpace (const unsigned n, const double a, const double b, vector<double> &bins) const
{
  double step = (b - a) / ((double) n);

  bins.clear ();
  for (double i = a; i < b + 0.5 * step; i += step)
    bins.push_back (pow (10.0, i));
}

void
TriggerEfficiencyWithTracks::linSpace (const unsigned n, const double a, const double b, vector<double> &bins) const
{
  double step = (b - a) / ((double) n);

  bins.clear ();
  for (double i = a; i < b + 0.5 * step; i += step)
    bins.push_back (i);
}

void
TriggerEfficiencyWithTracks::fillHistograms (const vector<pat::MET> &mets, const vector<reco::Track> &tracks, const string &channel) const
{
  for (const auto &met : mets)
    {
      oneDHists_.at (channel + "_metDir/metPt")->Fill (met.pt ());
      oneDHists_.at (channel + "_metDir/metPhi")->Fill (met.phi ());
    }
  for (const auto &track : tracks)
    {
      oneDHists_.at (channel + "_muonDir/muonPt")->Fill (track.pt ());
      oneDHists_.at (channel + "_muonDir/muonPhi")->Fill (track.phi ());
      oneDHists_.at (channel + "_muonDir/muonEta")->Fill (track.eta ());
    }
}

void
TriggerEfficiencyWithTracks::fillHistograms (const vector<pat::MET> &mets, const reco::Track &track, const string &channel) const
{
  for (const auto &met : mets)
    {
      oneDHists_.at (channel + "_metDir/metPt")->Fill (met.pt ());
      oneDHists_.at (channel + "_metDir/metPhi")->Fill (met.phi ());
    }
  oneDHists_.at (channel + "_muonDir/muonPt")->Fill (track.pt ());
  oneDHists_.at (channel + "_muonDir/muonPhi")->Fill (track.phi ());
  oneDHists_.at (channel + "_muonDir/muonEta")->Fill (track.eta ());
}

bool
TriggerEfficiencyWithTracks::passesTriggerFilter (const edm::TriggerNames &triggerNames, const vector<pat::TriggerObjectStandAlone> &triggerObjs, const string &filter) const
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
TriggerEfficiencyWithTracks::passesTrigger (const edm::TriggerNames &triggerNames, const edm::TriggerResults &triggerBits, const string &path) const
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

double
TriggerEfficiencyWithTracks::trackIsolation (const reco::Track &track, const vector<reco::Track> &tracks, const double outerDeltaR, const double innerDeltaR) const
{
  double sumPt = 0.0;

  for (const auto &t : tracks)
    {
      double dR = deltaR (track, t);
      if (dR < outerDeltaR && dR > innerDeltaR)
        sumPt += t.pt ();
    }

  return sumPt;
}

bool
TriggerEfficiencyWithTracks::genMatched (const reco::Track &track, const vector<reco::GenParticle> &genParticles, const int pdgId, const int status, const double maxDeltaR) const
{
  for (const auto &genParticle : genParticles)
    {
      if (abs (genParticle.pdgId ()) != abs (pdgId))
        continue;
      if (genParticle.status () != status)
        break;
      if (deltaR (track, genParticle) > maxDeltaR)
        continue;
      return true;
    }
  return false;
}

#include "FWCore/Framework/interface/MakerMacros.h"
DEFINE_FWK_MODULE(TriggerEfficiencyWithTracks);
