#include "DisappTrks/SignalMC/plugins/CharginoValidator.h"

CharginoValidator::CharginoValidator (const edm::ParameterSet &cfg) :
  tracks_         (cfg.getParameter<edm::InputTag> ("tracks")),
  genParticles_   (cfg.getParameter<edm::InputTag> ("genParticles")),
  pileupInfo_     (cfg.getParameter<edm::InputTag> ("pileupInfo")),
  cutPythia8Flag_ (cfg.getUntrackedParameter<bool>("cutPythia8Flag", false))
{
  TH1::SetDefaultSumw2();
  oneDHists_["nCharginos"] = fs_->make<TH1D> ("nCharginos", ";number of charginos", 5, -0.5, 4.5);
  oneDHists_["genCharge"] = fs_->make<TH1D> ("genCharge", ";generator chargino charge", 3, -1.5, 1.5);
  oneDHists_["genMass"] = fs_->make<TH1D> ("genMass", ";generator chargino mass [GeV]", 1000, -0.5, 999.5);
  oneDHists_["genPt"] = fs_->make<TH1D> ("genPt", ";generator chargino p_{T} [GeV]", 500, 0.0, 1000.0);
  oneDHists_["genPhi"] = fs_->make<TH1D> ("genPhi", ";generator chargino #phi", 100, -3.2, 3.2);
  oneDHists_["genEta"] = fs_->make<TH1D> ("genEta", ";generator chargino #eta", 100, -5.0, 5.0);
  oneDHists_["genP"] = fs_->make<TH1D> ("genP", ";generator chargino p [GeV]", 500, 0.0, 1000.0);
  oneDHists_["genBeta"] = fs_->make<TH1D> ("genBeta", ";generator chargino #beta", 500, 0.0, 1.0);
  oneDHists_["genGamma"] = fs_->make<TH1D> ("genGamma", ";generator chargino #gamma", 500, 0.0, 100.0);
  oneDHists_["genBetaGamma"] = fs_->make<TH1D> ("genBetaGamma", ";generator chargino #beta#gamma", 500, 0.0, 100.0);
  oneDHists_["genBetaGammaM"] = fs_->make<TH1D> ("genBetaGammaM", ";generator chargino #beta#gammam [GeV]", 500, 0.0, 1000.0);

  oneDHists_["genDecayLength_10"] = fs_->make<TH1D> ("genDecayLength_10", ";generator chargino decay length [cm]", 1000, 0.0, 10.0);
  oneDHists_["genDecayLength_100"] = fs_->make<TH1D> ("genDecayLength_100", ";generator chargino decay length [cm]", 1000, 0.0, 100.0);
  oneDHists_["genDecayLength_1000"] = fs_->make<TH1D> ("genDecayLength_1000", ";generator chargino decay length [cm]", 1000, 0.0, 1000.0);
  oneDHists_["genDecayLength_10000"] = fs_->make<TH1D> ("genDecayLength_10000", ";generator chargino decay length [cm]", 1000, 0.0, 10000.0);
  oneDHists_["genDecayLength_100000"] = fs_->make<TH1D> ("genDecayLength_100000", ";generator chargino decay length [cm]", 1000, 0.0, 100000.0);

  oneDHists_["genCTau_10"] = fs_->make<TH1D> ("genCTau_10", ";generator chargino c#tau [cm]", 1000, 0.0, 10.0);
  oneDHists_["genCTau_100"] = fs_->make<TH1D> ("genCTau_100", ";generator chargino c#tau [cm]", 1000, 0.0, 100.0);
  oneDHists_["genCTau_1000"] = fs_->make<TH1D> ("genCTau_1000", ";generator chargino c#tau [cm]", 1000, 0.0, 1000.0);
  oneDHists_["genCTau_10000"] = fs_->make<TH1D> ("genCTau_10000", ";generator chargino c#tau [cm]", 1000, 0.0, 10000.0);
  oneDHists_["genCTau_100000"] = fs_->make<TH1D> ("genCTau_100000", ";generator chargino c#tau [cm]", 1000, 0.0, 100000.0);

  oneDHists_["matchedTrack"] = fs_->make<TH1D> ("matchedTrack", ";matched track found", 2, -0.5, 1.5);
  oneDHists_["charge"] = fs_->make<TH1D> ("charge", ";track charge", 3, -1.5, 1.5);
  oneDHists_["pt"] = fs_->make<TH1D> ("pt", ";track p_{T} [GeV]", 500, 0.0, 1000.0);
  oneDHists_["phi"] = fs_->make<TH1D> ("phi", ";track #phi", 100, -3.2, 3.2);
  oneDHists_["eta"] = fs_->make<TH1D> ("eta", ";track #eta", 100, -5.0, 5.0);

  oneDHists_["numberOfValidHits"] = fs_->make<TH1D> ("numberOfValidHits", ";track number of valid hits", 100, -0.5, 99.5);
  oneDHists_["numberOfMissingInnerHits"] = fs_->make<TH1D> ("numberOfMissingInnerHits", ";track number of missing inner hits", 20, -0.5, 19.5);
  oneDHists_["numberOfMissingMiddleHits"] = fs_->make<TH1D> ("numberOfMissingMiddleHits", ";track number of missing middle hits", 20, -0.5, 19.5);
  oneDHists_["numberOfMissingOuterHits"] = fs_->make<TH1D> ("numberOfMissingOuterHits", ";track number of missing outer hits", 20, -0.5, 19.5);

  twoDHists_["matchedTrackVsPU"] = fs_->make<TH2D> ("matchedTrackVsPU", ";trueNumInteractions;matched track found", 100, 0, 100, 2, -0.5, 1.5);
  twoDHists_["chargeVsPU"] = fs_->make<TH2D> ("chargeVsPU", ";trueNumInteractions;track charge", 100, 0, 100, 3, -1.5, 1.5);
  twoDHists_["ptVsPU"] = fs_->make<TH2D> ("ptVsPU", ";trueNumInteractions;track p_{T} [GeV]", 100, 0, 100, 500, 0.0, 1000.0);
  twoDHists_["etaVsPU"] = fs_->make<TH2D> ("etaVsPU", ";trueNumInteractions;track #eta", 100, 0, 100, 100, -5.0, 5.0);

  twoDHists_["numberOfValidHits"] = fs_->make<TH2D> ("numberOfValidHitsVsPU", ";trueNumInteractions;track number of valid hits", 100, 0, 100, 100, -0.5, 99.5);
  twoDHists_["numberOfMissingInnerHits"] = fs_->make<TH2D> ("numberOfMissingInnerHitsVsPU", ";trueNumInteractions;track number of missing inner hits", 100, 0, 100, 20, -0.5, 19.5);
  twoDHists_["numberOfMissingMiddleHits"] = fs_->make<TH2D> ("numberOfMissingMiddleHitsVsPU", ";trueNumInteractions;track number of missing middle hits", 100, 0, 100, 20, -0.5, 19.5);
  twoDHists_["numberOfMissingOuterHits"] = fs_->make<TH2D> ("numberOfMissingOuterHitsVsPU", ";trueNumInteractions;track number of missing outer hits", 100, 0, 100, 20, -0.5, 19.5);

  tracksToken_       = consumes<vector<reco::Track> >          (tracks_);
  genParticlesToken_ = consumes<vector<reco::GenParticle> >    (genParticles_);
  pileupInfoToken_   = consumes<edm::View<PileupSummaryInfo> > (pileupInfo_);
}

CharginoValidator::~CharginoValidator ()
{
}

void
CharginoValidator::analyze (const edm::Event &event, const edm::EventSetup &setup)
{
  edm::Handle<vector<reco::Track> > tracks;
  event.getByToken (tracksToken_, tracks);

  edm::Handle<vector<reco::GenParticle> > genParticles;
  event.getByToken (genParticlesToken_, genParticles);

  edm::Handle<edm::View<PileupSummaryInfo> > pileupInfos;
  event.getByToken (pileupInfoToken_, pileupInfos);

  unsigned nCharginos = 0;
  for (const auto &genParticle : *genParticles)
    {
      if (abs (genParticle.pdgId ()) != 1000024)
        continue;
      if (genParticle.numberOfDaughters () == 1)
        continue;
      if (cutPythia8Flag_ && !genParticle.fromHardProcessBeforeFSR ())
        continue;

      nCharginos++;

      TVector3 x (genParticle.vx (), genParticle.vy (), genParticle.vz ()),
               y (0.0, 0.0, 0.0);
      double boost = 1.0 / (genParticle.p4 ().Beta (), genParticle.p4 ().Gamma ());
      getEndVertex (genParticle, y);

      oneDHists_.at ("genCharge")->Fill (genParticle.charge ());
      oneDHists_.at ("genMass")->Fill (genParticle.mass ());
      oneDHists_.at ("genPt")->Fill (genParticle.pt ());
      oneDHists_.at ("genPhi")->Fill (genParticle.phi ());
      oneDHists_.at ("genEta")->Fill (genParticle.eta ());
      oneDHists_.at ("genP")->Fill (genParticle.p ());
      oneDHists_.at ("genBeta")->Fill (genParticle.p4 ().Beta ());
      oneDHists_.at ("genGamma")->Fill (genParticle.p4 ().Gamma ());
      oneDHists_.at ("genBetaGamma")->Fill (genParticle.p4 ().Beta () * genParticle.p4 ().Gamma ());
      oneDHists_.at ("genBetaGammaM")->Fill (genParticle.p4 ().Beta () * genParticle.p4 ().Gamma () * genParticle.mass ());

      oneDHists_.at ("genDecayLength_10")->Fill ((x - y).Mag ());
      oneDHists_.at ("genDecayLength_100")->Fill ((x - y).Mag ());
      oneDHists_.at ("genDecayLength_1000")->Fill ((x - y).Mag ());
      oneDHists_.at ("genDecayLength_10000")->Fill ((x - y).Mag ());
      oneDHists_.at ("genDecayLength_100000")->Fill ((x - y).Mag ());

      oneDHists_.at ("genCTau_10")->Fill ((x - y).Mag () * boost);
      oneDHists_.at ("genCTau_100")->Fill ((x - y).Mag () * boost);
      oneDHists_.at ("genCTau_1000")->Fill ((x - y).Mag () * boost);
      oneDHists_.at ("genCTau_10000")->Fill ((x - y).Mag () * boost);
      oneDHists_.at ("genCTau_100000")->Fill ((x - y).Mag () * boost);

      if (genParticle.pt () < 10.0)
        {
          oneDHists_.at ("matchedTrack")->Fill (-1.0);
          continue;
        }

      edm::View<PileupSummaryInfo>::const_iterator iterPU;
      double truePV = -1;
      for(edm::View<PileupSummaryInfo>::const_iterator iterPU = pileupInfos->begin(); iterPU != pileupInfos->end(); iterPU++) {
        if(iterPU->getBunchCrossing() == 0) truePV = iterPU->getTrueNumInteractions();
      }

      const reco::Track *track = getMatchedTrack (genParticle, tracks);

      if (track)
        {
          oneDHists_.at ("matchedTrack")->Fill (1.0);
          oneDHists_.at ("charge")->Fill (track->charge ());
          oneDHists_.at ("pt")->Fill (track->pt ());
          oneDHists_.at ("phi")->Fill (track->phi ());
          oneDHists_.at ("eta")->Fill (track->eta ());

          oneDHists_.at ("numberOfValidHits")->Fill (track->numberOfValidHits ());
          oneDHists_.at ("numberOfMissingInnerHits")->Fill (track->hitPattern ().trackerLayersWithoutMeasurement (reco::HitPattern::MISSING_INNER_HITS));
          oneDHists_.at ("numberOfMissingMiddleHits")->Fill (track->hitPattern ().trackerLayersWithoutMeasurement (reco::HitPattern::TRACK_HITS));
          oneDHists_.at ("numberOfMissingOuterHits")->Fill (track->hitPattern ().trackerLayersWithoutMeasurement (reco::HitPattern::MISSING_OUTER_HITS));

          twoDHists_.at ("matchedTrackVsPU")->Fill (truePV, 1.0);

          twoDHists_["chargeVsPU"]->Fill (truePV, track->charge ());
          twoDHists_["ptVsPU"]->Fill (truePV, track->pt ());
          twoDHists_["etaVsPU"]->Fill (truePV, track->eta ());

          twoDHists_["numberOfValidHits"]->Fill (truePV, track->numberOfValidHits ());
          twoDHists_["numberOfMissingInnerHits"]->Fill (truePV, track->hitPattern ().trackerLayersWithoutMeasurement (reco::HitPattern::MISSING_INNER_HITS));
          twoDHists_["numberOfMissingMiddleHits"]->Fill (truePV, track->hitPattern ().trackerLayersWithoutMeasurement (reco::HitPattern::TRACK_HITS));
          twoDHists_["numberOfMissingOuterHits"]->Fill (truePV, track->hitPattern ().trackerLayersWithoutMeasurement (reco::HitPattern::MISSING_OUTER_HITS));
        }
      else {
        oneDHists_.at ("matchedTrack")->Fill (0.0);
        twoDHists_.at ("matchedTrackVsPU")->Fill (truePV, 0.0);
      }
    }
  oneDHists_.at ("nCharginos")->Fill (nCharginos);
  if (!nCharginos)
    clog << "[" << event.id () << "] No charginos found!" << endl;
}

void
CharginoValidator::getEndVertex (const reco::GenParticle &genParticle, TVector3 &y) const
{
  if (!genParticle.numberOfDaughters ())
    y.SetXYZ (99999.0, 99999.0, 99999.0);
  else
    for (const auto &daughter : genParticle)
      {
        if (abs (daughter.pdgId ()) != 1000022)
          continue;

        y.SetXYZ (daughter.vx (), daughter.vy (), daughter.vz ());
        break;
      }
}

const reco::Track *
CharginoValidator::getMatchedTrack (const reco::GenParticle &genParticle, const edm::Handle<vector<reco::Track> > &tracks) const
{
  const reco::Track *matchedTrack = NULL;
  double minDR = -1.0;
  int i = -1;
  for (const auto &track : *tracks)
    {
      i++;
      if (track.pt () < 10.0)
        continue;

      const double dR = deltaR (genParticle, track);
      if (dR > 0.1)
        continue;

      if (!matchedTrack || dR < minDR)
        {
          matchedTrack = &(tracks->at (i));
          minDR = dR;
        }
    }

  return matchedTrack;
}

DEFINE_FWK_MODULE (CharginoValidator);
