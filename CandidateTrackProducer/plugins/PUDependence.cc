#include "CommonTools/Utils/interface/TFileDirectory.h"

#include "DataFormats/Math/interface/deltaR.h"
#include "DataFormats/PatCandidates/interface/Electron.h"

#include "DisappTrks/CandidateTrackProducer/interface/CandidateTrack.h"
#include "DisappTrks/CandidateTrackProducer/plugins/PUDependence.h"

PUDependence::PUDependence (const edm::ParameterSet &cfg) :
  tracks_        (cfg.getParameter<edm::InputTag>  ("tracks")),
  vertices_      (cfg.getParameter<edm::InputTag>  ("vertices")),
  genParticles_  (cfg.getParameter<edm::InputTag>  ("genParticles"))
{
  TH1::SetDefaultSumw2 ();

  oneDHists_["nVertices"] = fs_->make<TH1D> ("nVertices", ";number of primary vertices", 100, 0.0, 100.0);
  oneDHists_["isoTrack"] = fs_->make<TH1D> ("isoTrack", ";number of primary vertices", 100, 0.0, 100.0);
  oneDHists_["isoNoPUTrack"] = fs_->make<TH1D> ("isoNoPUTrack", ";number of primary vertices", 100, 0.0, 100.0);
  twoDHists_["rhoPUCorr"]     = fs_->make<TH2D> ("rhoPUCorr",     ";number of primary vertices;rho [GeV]", 100, 0.0, 50.0, 100, 0, 50);
  twoDHists_["rhoPUCorrCalo"]     = fs_->make<TH2D> ("rhoPUCorrCalo",     ";number of primary vertices;rho [GeV]", 100, 0.0, 50.0, 100, 0, 50);
  twoDHists_["rhoPUCorrCentralCalo"]     = fs_->make<TH2D> ("rhoPUCorrCentralCalo",     ";number of primary vertices;rho [GeV]", 100, 0.0, 50.0, 100, 0, 50);
  twoDHists_["caloTot"]     = fs_->make<TH2D> ("caloTot",     ";number of primary vertices;assoc. calorimeter energy [GeV]", 100, 0.0, 50.0, 100, 0, 50);
  twoDHists_["caloTotNoPU"] = fs_->make<TH2D> ("caloTotNoPU", ";number of primary vertices;assoc. calorimeter energy (with PU corr.) [GeV]", 100, 0.0, 50.0, 100, 0, 50);
  twoDHists_["caloTotNoPUCalo"] = fs_->make<TH2D> ("caloTotNoPUCalo", ";number of primary vertices;assoc. calorimeter energy (with PU corr., calo) [GeV]", 100, 0.0, 50.0, 100, 0, 50);
  twoDHists_["caloTotNoPUCentralCalo"] = fs_->make<TH2D> ("caloTotNoPUCentralCalo", ";number of primary vertices;assoc. calorimeter energy (with PU corr., central calo) [GeV]", 100, 0.0, 50.0, 100, 0, 50);
  oneDHists_["passCaloTot"]     = fs_->make<TH1D> ("passCaloTot",     ";number of primary vertices", 100, 0.0, 100.0);
  oneDHists_["passCaloTotNoPU"] = fs_->make<TH1D> ("passCaloTotNoPU", ";number of primary vertices", 100, 0.0, 100.0);
}

PUDependence::~PUDependence ()
{
}

void
PUDependence::analyze (const edm::Event &event, const edm::EventSetup &setup)
{
  edm::Handle<vector<CandidateTrack> > tracks;
  event.getByLabel (tracks_, tracks);
  edm::Handle<vector<reco::Vertex> > vertices;
  event.getByLabel (vertices_, vertices);
  edm::Handle<vector<reco::GenParticle> > genParticles;
  event.getByLabel (genParticles_, genParticles);

  for (const auto &track : *tracks)
    {
      if (fabs(track.eta()) > 2.5)
        continue;
      if (!genMatched (track, *genParticles, 1000024, 3, 0.1))
        continue;
      oneDHists_.at ("nVertices")->Fill (vertices->size ());
      twoDHists_.at ("caloTot")    ->Fill (vertices->size (), track.caloNewDRp5());
      twoDHists_.at ("caloTotNoPU")->Fill (vertices->size (), track.caloNewNoPUDRp5());
      twoDHists_.at ("caloTotNoPUCalo")->Fill (vertices->size (), track.caloNewNoPUDRp5Calo());
      twoDHists_.at ("caloTotNoPUCentralCalo")->Fill (vertices->size (), track.caloNewNoPUDRp5CentralCalo());
      twoDHists_.at ("rhoPUCorr")->Fill (vertices->size (), track.rhoPUCorr());
      twoDHists_.at ("rhoPUCorrCalo")->Fill (vertices->size (), track.rhoPUCorrCalo());
      twoDHists_.at ("rhoPUCorrCentralCalo")->Fill (vertices->size (), track.rhoPUCorrCentralCalo());

      if (track.caloNewDRp5 () < 10)
        oneDHists_.at ("passCaloTot")    ->Fill (vertices->size ());
      if (track.caloNewNoPUDRp5 () < 10)
        oneDHists_.at ("passCaloTotNoPU")->Fill (vertices->size ());
      if (track.trackIsoDRp5 () < 0.05 * track.pt ())
        oneDHists_.at ("isoTrack")->Fill (vertices->size ());
      if (track.trackIsoNoPUDRp5 () < 0.05 * track.pt ())
        oneDHists_.at ("isoNoPUTrack")->Fill (vertices->size ());
    }
}

void
PUDependence::logSpace (const unsigned n, const double a, const double b, vector<double> &bins) const
{
  double step = (b - a) / ((double) n);

  bins.clear ();
  for (double i = a; i < b + 0.5 * step; i += step)
    bins.push_back (pow (10.0, i));
}

void
PUDependence::linSpace (const unsigned n, const double a, const double b, vector<double> &bins) const
{
  double step = (b - a) / ((double) n);

  bins.clear ();
  for (double i = a; i < b + 0.5 * step; i += step)
    bins.push_back (i);
}

template<class T> bool
PUDependence::genMatched (const T &track, const vector<reco::GenParticle> &genParticles, const int pdgId, const int status, const double maxDeltaR) const
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
DEFINE_FWK_MODULE(PUDependence);
