#include "DataFormats/Math/interface/deltaR.h"
#include "DataFormats/MuonReco/interface/MuonSelectors.h"

#include "DisappTrks/StandardAnalysis/plugins/CharginoHitAnalyzer.h"

CharginoHitAnalyzer::CharginoHitAnalyzer (const edm::ParameterSet &cfg) :
  tracks_ (cfg.getParameter<edm::InputTag> ("tracks")),
  gsfTracks_ (cfg.getParameter<edm::InputTag> ("gsfTracks")),
  genParticles_ (cfg.getParameter<edm::InputTag> ("genParticles"))
{
  TFileDirectory dir;
  vector<string> dirNames = {"TrackWins", "GsfTrackWins", "GoodTrack", "GoodGsfTrack", "BadTrack", "BadGsfTrack", "AllTrack", "AllGsfTrack"};

  TH1::SetDefaultSumw2();
  oneDHists_["pt"] = fs_->make<TH1D> ("pt", ";p_{T} [GeV]", 100, 0.0, 10000.0);
  oneDHists_["eta"] = fs_->make<TH1D> ("eta", ";#eta", 100, -3.0, 3.0);
  oneDHists_["phi"] = fs_->make<TH1D> ("phi", ";#phi", 100, -3.2, 3.2);
  twoDHists_["etaVsPhi"] = fs_->make<TH2D> ("etaVsPhi", ";#eta;#phi", 100, -3.0, 3.0, 100, -3.2, 3.2);
  oneDHists_["cTau"] = fs_->make<TH1D> ("cTau", ";c#tau [cm]", 100, 0.0, 1000.0);
  oneDHists_["rho"] = fs_->make<TH1D> ("rho", ";#rho [cm]", 100, 0.0, 200.0);
  oneDHists_["expectedHits"] = fs_->make<TH1D> ("expectedHits", ";number of expected hits", 50, 0.0, 50.0);
  twoDHists_["expectedHitsVsTrackHits"] = fs_->make<TH2D> ("expectedHitsVsTrackHits", ";number of expected hits;number of track hits", 50, 0.0, 50.0, 50, 0.0, 50.0);
  twoDHists_["expectedHitsVsGsfTrackHits"] = fs_->make<TH2D> ("expectedHitsVsGsfTrackHits", ";number of expected hits;number of GSF track hits", 50, 0.0, 50.0, 50, 0.0, 50.0);
  oneDHists_["trackHitsMinusExpectedHits"] = fs_->make<TH1D> ("trackHitsMinusExpectedHits", ";number of track hits - number of expected hits", 20, -10.0, 10.0);
  oneDHists_["gsfTrackHitsMinusExpectedHits"] = fs_->make<TH1D> ("gsfTrackHitsMinusExpectedHits", ";number of GSF track hits - number of expected hits", 20, -10.0, 10.0);
  twoDHists_["deltaHits"] = fs_->make<TH2D> ("deltaHits", ";number of track hits - number of expected hits;number of GSF track hits - number of expected hits", 20, -10.0, 10.0, 20, -10.0, 10.0);

  for (const auto &dirName : dirNames)
    {
      dir = fs_->mkdir (dirName);
      oneDHists_[dirName + "/numberOfValidHits"] = dir.make<TH1D> ("numberOfValidHits", ";number of valid hits", 50, 0.0, 50.0);
      oneDHists_[dirName + "/numberOfLayers"] = dir.make<TH1D> ("numberOfLayers", ";number of tracker layers with measurement", 50, 0.0, 50.0);
      oneDHists_[dirName + "/missingInnerHits"] = dir.make<TH1D> ("missingInnerHits", ";number of missing inner hits", 50, 0.0, 50.0);
      oneDHists_[dirName + "/missingMiddleHits"] = dir.make<TH1D> ("missingMiddleHits", ";number of missing middle hits", 50, 0.0, 50.0);
      oneDHists_[dirName + "/normalizedChi2"] = dir.make<TH1D> ("normalizedChi2", ";#chi^{2} / ndof", 100, 0.0, 50.0);
      twoDHists_[dirName + "/generalNumberOfValidHitsVsGSFNumberOfValidHits"] = dir.make<TH2D> ("generalNumberOfValidHitsVsGSFNumberOfValidHits", ";(number of valid hits)_{general};(number of valid hits)_{GSF}", 50, 0.0, 50.0, 50, 0.0, 50.0);
      oneDHists_[dirName + "/deltaNumberOfValidHits"] = dir.make<TH1D> ("deltaNumberOfValidHits", ";(number of valid hits)_{general} - (number of valid hits)_{GSF}", 10, -5.0, 5.0);
      twoDHists_[dirName + "/generalMissingInnerHitsVsGSFMissingInnerHits"] = dir.make<TH2D> ("generalMissingInnerHitsVsGSFMissingInnerHits", ";(number of missing inner hits)_{general};(number of missing inner hits)_{GSF}", 50, 0.0, 50.0, 50, 0.0, 50.0);
      oneDHists_[dirName + "/deltaMissingInnerHits"] = dir.make<TH1D> ("deltaMissingInnerHits", ";(number of missing inner hits)_{general} - (number of missing inner hits)_{GSF}", 10, -5.0, 5.0);
      twoDHists_[dirName + "/generalMissingMiddleHitsVsGSFMissingMiddleHits"] = dir.make<TH2D> ("generalMissingMiddleHitsVsGSFMissingMiddleHits", ";(number of missing middle hits)_{general};(number of missing middle hits)_{GSF}", 50, 0.0, 50.0, 50, 0.0, 50.0);
      oneDHists_[dirName + "/deltaMissingMiddleHits"] = dir.make<TH1D> ("deltaMissingMiddleHits", ";(number of missing middle hits)_{general} - (number of missing middle hits)_{GSF}", 10, -5.0, 5.0);
      twoDHists_[dirName + "/generalChi2VsGSFChi2"] = dir.make<TH2D> ("generalChi2VsGSFChi2", ";(#chi^{2} / ndof)_{general};(#chi^{2} / ndof)_{GSF}", 100, 0.0, 50.0, 100, 0.0, 50.0);
      oneDHists_[dirName + "/deltaChi2"] = dir.make<TH1D> ("deltaChi2", ";(#chi^{2} / ndof)_{general} - (#chi^{2} / ndof)_{GSF}", 100, -5.0, 5.0);
    }

  tracksToken_ = consumes<vector<reco::Track> > (tracks_);
  gsfTracksToken_ = consumes<vector<reco::GsfTrack> > (gsfTracks_);
  genParticlesToken_ = consumes<vector<reco::GenParticle> > (genParticles_);
}

CharginoHitAnalyzer::~CharginoHitAnalyzer ()
{
}

void
CharginoHitAnalyzer::analyze (const edm::Event &event, const edm::EventSetup &setup)
{
  edm::Handle<vector<reco::Track> > tracks;
  event.getByToken (tracksToken_, tracks);
  edm::Handle<vector<reco::GsfTrack> > gsfTracks;
  event.getByToken (gsfTracksToken_, gsfTracks);
  edm::Handle<vector<reco::GenParticle> > genParticles;
  event.getByToken (genParticlesToken_, genParticles);

  for (const auto &genParticle : *genParticles)
    {
      double cTau = 0.0, rho = 0.0, trackDR = 0.0, gsfTrackDR = 0.0;
      int nHits = 0;
      if (abs (genParticle.pdgId ()) == 1000024 && genParticle.status () == 1 && fabs (genParticle.eta ()) < 0.9)
        {
          cTau = getCTau (genParticle, rho);
          nHits = getExpectedNumberOfHits (rho);

          oneDHists_.at ("pt")->Fill (genParticle.pt ());
          oneDHists_.at ("eta")->Fill (genParticle.eta ());
          oneDHists_.at ("phi")->Fill (genParticle.phi ());
          twoDHists_.at ("etaVsPhi")->Fill (genParticle.eta (), genParticle.phi ());
          oneDHists_.at ("cTau")->Fill (cTau);
          oneDHists_.at ("rho")->Fill (rho);
          oneDHists_.at ("expectedHits")->Fill (nHits);

          const reco::Track * const track = getTrack (genParticle, *tracks, trackDR);
          const reco::GsfTrack * const gsfTrack = getTrack (genParticle, *gsfTracks, gsfTrackDR);

          if (trackDR < 0.1)
            {
              twoDHists_.at ("expectedHitsVsTrackHits")->Fill (nHits, track->hitPattern ().trackerLayersWithMeasurement ());
              oneDHists_.at ("trackHitsMinusExpectedHits")->Fill (track->hitPattern ().trackerLayersWithMeasurement () - nHits);

              fillHistograms (*track, "AllTrack");

              if (abs (track->hitPattern ().trackerLayersWithMeasurement () - nHits) <= 1)
                fillHistograms (*track, "GoodTrack");
              else
                fillHistograms (*track, "BadTrack");
            }
          if (gsfTrackDR < 0.1)
            {
              twoDHists_.at ("expectedHitsVsGsfTrackHits")->Fill (nHits, gsfTrack->hitPattern ().trackerLayersWithMeasurement ());
              oneDHists_.at ("gsfTrackHitsMinusExpectedHits")->Fill (gsfTrack->hitPattern ().trackerLayersWithMeasurement () - nHits);

              fillHistograms (*gsfTrack, "AllGsfTrack");

              if (abs (gsfTrack->hitPattern ().trackerLayersWithMeasurement () - nHits) <= 1)
                fillHistograms (*gsfTrack, "GoodGsfTrack");
              else
                fillHistograms (*gsfTrack, "BadGsfTrack");
            }
          if (trackDR < 0.1 && gsfTrackDR < 0.1)
            {
              twoDHists_.at ("deltaHits")->Fill (track->hitPattern ().trackerLayersWithMeasurement () - nHits, gsfTrack->hitPattern ().trackerLayersWithMeasurement () - nHits);

              fillHistograms (*track, *gsfTrack, "AllTrack");
              fillHistograms (*track, *gsfTrack, "AllGsfTrack");

              if (abs (track->hitPattern ().trackerLayersWithMeasurement () - nHits) <= 1)
                fillHistograms (*track, *gsfTrack, "GoodTrack");
              else
                fillHistograms (*track, *gsfTrack, "BadTrack");
              if (abs (track->hitPattern ().trackerLayersWithMeasurement () - nHits) <= 1 && abs (gsfTrack->hitPattern ().trackerLayersWithMeasurement () - nHits) > 1)
                {
                  fillHistograms (*track, "TrackWins");
                  fillHistograms (*track, *gsfTrack, "TrackWins");
                }

              if (abs (gsfTrack->hitPattern ().trackerLayersWithMeasurement () - nHits) <= 1)
                fillHistograms (*track, *gsfTrack, "GoodGsfTrack");
              else
                fillHistograms (*track, *gsfTrack, "BadGsfTrack");
              if (abs (gsfTrack->hitPattern ().trackerLayersWithMeasurement () - nHits) <= 1 && abs (track->hitPattern ().trackerLayersWithMeasurement () - nHits) > 1)
                {
                  fillHistograms (*gsfTrack, "GsfTrackWins");
                  fillHistograms (*track, *gsfTrack, "GsfTrackWins");
                }
            }
        }
    }
}

void
CharginoHitAnalyzer::logSpace (const unsigned n, const double a, const double b, vector<double> &bins) const
{
  double step = (b - a) / ((double) n);

  bins.clear ();
  for (double i = a; i < b + 0.5 * step; i += step)
    bins.push_back (pow (10.0, i));
}

double
CharginoHitAnalyzer::getCTau (const reco::GenParticle &genParticle, double &rho) const
{
  math::XYZPoint v0 = genParticle.vertex (), v1;
  double boost = 1.0 / (genParticle.p4 ().Beta () * genParticle.p4 ().Gamma ());

  getFinalPosition (genParticle, genParticle.pdgId (), true, v1);
  rho = (v1 - v0).rho ();
  return ((v1 - v0).r () * boost);
}

void
CharginoHitAnalyzer::getFinalPosition (const reco::Candidate &genParticle, const int pdgId, bool firstDaughter, math::XYZPoint &v1) const
{
  if (genParticle.pdgId () == pdgId)
    {
      v1 = genParticle.vertex ();
      firstDaughter = true;
    }
  else if (firstDaughter)
    {
      v1 = genParticle.vertex ();
      firstDaughter = false;
    }
  for (const auto &daughter : genParticle)
    getFinalPosition (daughter, pdgId, firstDaughter, v1);
}

int
CharginoHitAnalyzer::getExpectedNumberOfHits (const double rho) const
{
  int n = 0;

  // BPIX
  if (rho > 4.4)
    n++;
  if (rho > 7.3)
    n++;
  if (rho > 10.2)
    n++;

  // TIB
  if (rho > 26.0)
    n++;
  if (rho > 34.0)
    n++;
  if (rho > 42.0)
    n++;
  if (rho > 50.0)
    n++;

  // TOB
  if (rho > 61.0)
    n++;
  if (rho > 69.0)
    n++;
  if (rho > 78.0)
    n++;
  if (rho > 87.0)
    n++;
  if (rho > 96.0)
    n++;
  if (rho > 108.0)
    n++;

  return n;
}

template<class T> const T * const
CharginoHitAnalyzer::getTrack (const reco::GenParticle &genParticle, const vector<T> &tracks, double &minDR) const
{
  minDR = numeric_limits<double>::max ();
  int i = 0, iTrack = 0;

  for (const auto &track : tracks)
    {
      double dR = deltaR (genParticle, track);

      if (dR < minDR)
        {
          minDR = dR;
          iTrack = i;
        }
      i++;
    }

  return (iTrack < (int) tracks.size () ? &tracks.at (iTrack) : NULL);
}

template<class T> void
CharginoHitAnalyzer::fillHistograms (const T &track, const string &dir)
{
  oneDHists_.at (dir + "/numberOfValidHits")->Fill (track.numberOfValidHits ());
  oneDHists_.at (dir + "/numberOfLayers")->Fill (track.hitPattern ().trackerLayersWithMeasurement ());
  oneDHists_.at (dir + "/missingInnerHits")->Fill (track.hitPattern ().trackerLayersWithoutMeasurement (reco::HitPattern::MISSING_INNER_HITS));
  oneDHists_.at (dir + "/missingMiddleHits")->Fill (track.hitPattern ().trackerLayersWithoutMeasurement (reco::HitPattern::TRACK_HITS));
  oneDHists_.at (dir + "/normalizedChi2")->Fill (track.normalizedChi2 ());
}

template<class T0, class T1> void
CharginoHitAnalyzer::fillHistograms (const T0 &track0, const T1 &track1, const string &dir)
{
  twoDHists_.at (dir + "/generalNumberOfValidHitsVsGSFNumberOfValidHits")->Fill (track0.numberOfValidHits (), track1.numberOfValidHits ());
  oneDHists_.at (dir + "/deltaNumberOfValidHits")->Fill (track0.numberOfValidHits () - track1.numberOfValidHits ());
  twoDHists_.at (dir + "/generalMissingInnerHitsVsGSFMissingInnerHits")->Fill (track0.hitPattern ().trackerLayersWithoutMeasurement (reco::HitPattern::MISSING_INNER_HITS), track1.hitPattern ().trackerLayersWithoutMeasurement (reco::HitPattern::MISSING_INNER_HITS));
  oneDHists_.at (dir + "/deltaMissingInnerHits")->Fill (track0.hitPattern ().trackerLayersWithoutMeasurement (reco::HitPattern::MISSING_INNER_HITS) - track1.hitPattern ().trackerLayersWithoutMeasurement (reco::HitPattern::MISSING_INNER_HITS));
  twoDHists_.at (dir + "/generalMissingMiddleHitsVsGSFMissingMiddleHits")->Fill (track0.hitPattern ().trackerLayersWithoutMeasurement (reco::HitPattern::TRACK_HITS), track1.hitPattern ().trackerLayersWithoutMeasurement (reco::HitPattern::TRACK_HITS));
  oneDHists_.at (dir + "/deltaMissingMiddleHits")->Fill (track0.hitPattern ().trackerLayersWithoutMeasurement (reco::HitPattern::TRACK_HITS) - track1.hitPattern ().trackerLayersWithoutMeasurement (reco::HitPattern::TRACK_HITS));
  twoDHists_.at (dir + "/generalChi2VsGSFChi2")->Fill (track0.normalizedChi2 (), track1.normalizedChi2 ());
  oneDHists_.at (dir + "/deltaChi2")->Fill (track0.normalizedChi2 () - track1.normalizedChi2 ());
}

DEFINE_FWK_MODULE (CharginoHitAnalyzer);
