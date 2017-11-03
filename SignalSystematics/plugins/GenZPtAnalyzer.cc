#include "DisappTrks/SignalSystematics/plugins/GenZPtAnalyzer.h"

GenZPtAnalyzer::GenZPtAnalyzer (const edm::ParameterSet &cfg) :
  genParticles_ (cfg.getParameter<edm::InputTag> ("genParticles"))
{
  TH1::SetDefaultSumw2 ();

  vector<double> bins;
  anatools::logSpace (0.0, 3.0, 1000, bins);

  oneDHists_["genZPtLin"] = fs_->make<TH1D> ("genZPtLin",";generator Z p_{T} [GeV]", 1000, 0.0, 1000.0);
  oneDHists_["genZPtLog"] = fs_->make<TH1D> ("genZPtLog",";generator Z p_{T} [GeV]", bins.size () - 1, bins.data ());

  genParticlesToken_ = consumes<edm::View<reco::GenParticle> > (genParticles_);
}

GenZPtAnalyzer::~GenZPtAnalyzer ()
{
}

void
GenZPtAnalyzer::analyze (const edm::Event &event, const edm::EventSetup &setup)
{
  edm::Handle<edm::View<reco::GenParticle> > genParticles;
  event.getByToken (genParticlesToken_, genParticles);

  const reco::GenParticle * const finalZ = getFinalZ (*genParticles);

  if (!finalZ)
    {
      edm::LogWarning ("GenZPtAnalyzer") << "No Z->mumu found!";
      return;
    }

  oneDHists_["genZPtLin"]->Fill (finalZ->pt ());
  oneDHists_["genZPtLog"]->Fill (finalZ->pt ());
}

const reco::GenParticle * const
GenZPtAnalyzer::getFinalZ (const edm::View<reco::GenParticle> &genParticles) const
{
  const reco::GenParticle *finalZ = NULL;
  for (int i = min (20, (int) (genParticles.size () - 1)); i >= 0; i--)
    {
      const reco::GenParticle *genParticle = &genParticles.at (i);
      if (!isFinalZ (*genParticle))
        continue;

      finalZ = genParticle;
      break;
    }
  return finalZ;
}

bool
GenZPtAnalyzer::isFinalZ (const reco::GenParticle &genParticle) const
{
  if (abs (genParticle.pdgId ()) != 23)
    return false;
  unsigned decaysToMuMu = 0;
  for (const auto &daughter : genParticle.daughterRefVector ())
    {
      if (abs (daughter->pdgId ()) != 13)
        continue;
      decaysToMuMu++;
    }

  return (decaysToMuMu >= 2);
}

#include "FWCore/Framework/interface/MakerMacros.h"
DEFINE_FWK_MODULE(GenZPtAnalyzer);
