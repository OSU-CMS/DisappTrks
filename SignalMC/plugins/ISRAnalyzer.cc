//#include "CommonTools/Utils/interface/TFileDirectory.h"

#include "DataFormats/HepMCCandidate/interface/GenParticle.h"

#include "DisappTrks/SignalMC/plugins/ISRAnalyzer.h"

ISRAnalyzer::ISRAnalyzer (const edm::ParameterSet &cfg) :
  genParticles_ (cfg.getParameter<edm::InputTag> ("genParticles"))
{
  TH1::SetDefaultSumw2 ();
/*  TFileDirectory MuMETNoMET_metDir = fs_->mkdir ("MuMETNoMETPlotter/Met Plots"),
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
  oneDHists_["MuMETNoMuonPtNoTrigger_muonDir/muonEta"] = MuMETNoMuonPtNoTrigger_muonDir.make<TH1D> ("muonEta", ";;muon #eta", 1000, -5.0, 5.0);*/
}

ISRAnalyzer::~ISRAnalyzer ()
{
}

void
ISRAnalyzer::analyze (const edm::Event &event, const edm::EventSetup &setup)
{
  edm::Handle<vector<reco::GenParticle> > genParticles;
  event.getByLabel (genParticles_, genParticles);

  for (const auto &genParticle : *genParticles)
    {
      if (abs (genParticle.pdgId ()) != 23 && abs (genParticle.pdgId ()) != 24)
        continue;
      switch (abs (genParticle.pdgId ()))
        {
          case 23:
            clog << "event contains a Z boson" << endl;
            break;
          case 24:
            clog << "event contains a W boson" << endl;
            break;
          default:
            break;
        }
    }
}

void
ISRAnalyzer::logSpace (const unsigned n, const double a, const double b, vector<double> &bins) const
{
  double step = (b - a) / ((double) n);

  bins.clear ();
  for (double i = a; i < b + 0.5 * step; i += step)
    bins.push_back (pow (10.0, i));
}

void
ISRAnalyzer::linSpace (const unsigned n, const double a, const double b, vector<double> &bins) const
{
  double step = (b - a) / ((double) n);

  bins.clear ();
  for (double i = a; i < b + 0.5 * step; i += step)
    bins.push_back (i);
}

#include "FWCore/Framework/interface/MakerMacros.h"
DEFINE_FWK_MODULE(ISRAnalyzer);
