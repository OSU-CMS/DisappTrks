#include "DataFormats/HepMCCandidate/interface/GenParticle.h"

#include "DisappTrks/SignalMC/plugins/ISRAnalyzer.h"

#include "TLorentzVector.h"

ISRAnalyzer::ISRAnalyzer (const edm::ParameterSet &cfg) :
  genParticles_ (cfg.getParameter<edm::InputTag> ("genParticles"))
{
  TH1::SetDefaultSumw2 ();
  vector<double> bins;
  logSpace (1000, 0.0, 4.0, bins);

  oneDHists_["ewkinoSumPt"] = fs_->make<TH1D> ("ewkinoSumPt", ";p_{T}(#chi^{#pm}#chi^{#pm}/#chi^{#pm}#chi^{0}) [GeV]", bins.size () - 1, bins.data ());
  oneDHists_["isrZPt"] = fs_->make<TH1D> ("isrZPt", ";p_{T}(Z^{0}) [GeV]", bins.size () - 1, bins.data ());
  oneDHists_["isrWPt"] = fs_->make<TH1D> ("isrWPt", ";p_{T}(W^{#pm}) [GeV]", bins.size () - 1, bins.data ());
}

ISRAnalyzer::~ISRAnalyzer ()
{
}

void
ISRAnalyzer::analyze (const edm::Event &event, const edm::EventSetup &setup)
{
  edm::Handle<vector<reco::GenParticle> > genParticles;
  event.getByLabel (genParticles_, genParticles);

  TLorentzVector p (0.0, 0.0, 0.0, 0.0);
  bool foundChargino = false;
  for (const auto &genParticle : *genParticles)
    {
      int pdgId = genParticle.pdgId ();
      unsigned status = genParticle.status ();

      if (abs (pdgId) != 23 && abs (pdgId) != 24 && abs (pdgId) != 1000022 && abs (pdgId) != 1000024)
        continue;
      if (abs (pdgId) == 23)
        clog << "event contains a Z boson" << endl;
      if (abs (pdgId) == 24)
        clog << "event contains a W boson" << endl;
      if (status != 1 && status != 62)
        continue;
      switch (abs (pdgId))
        {
          case 23:
            if (status == 62)
              oneDHists_.at ("isrZPt")->Fill (genParticle.pt ());
            break;
          case 24:
            if (status == 62)
              oneDHists_.at ("isrWPt")->Fill (genParticle.pt ());
            break;
          case 1000022:
            if (status == 1)
              p += TLorentzVector (genParticle.px (), genParticle.py (), genParticle.pz (), genParticle.energy ());
            break;
          case 1000024:
            if (status == 1)
              {
                p += TLorentzVector (genParticle.px (), genParticle.py (), genParticle.pz (), genParticle.energy ());
                foundChargino = true;
              }
            break;
          default:
            break;
        }
    }
  if (foundChargino)
    oneDHists_.at ("ewkinoSumPt")->Fill (p.Pt ());
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
