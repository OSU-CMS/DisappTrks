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
      if (!genMatched (track, *genParticles, 1000024, 3, 0.1))
        continue;
      oneDHists_.at ("nVertices")->Fill (vertices->size ());
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
