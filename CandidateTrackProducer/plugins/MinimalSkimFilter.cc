#include "TVector2.h"

#include "OSUT3Analysis/AnaTools/interface/CMSSWVersion.h"

#include "DisappTrks/CandidateTrackProducer/plugins/MinimalSkimFilter.h"

template<MinimalSkim T>
MinimalSkimFilter<T>::MinimalSkimFilter (const edm::ParameterSet& iConfig) :
  triggers_ (iConfig.getParameter<edm::InputTag> ("triggers")),
  beamspot_ (iConfig.getParameter<edm::InputTag> ("beamspot")),
  vertices_ (iConfig.getParameter<edm::InputTag> ("vertices")),
  met_ (iConfig.getParameter<edm::InputTag> ("met")),
  electrons_ (iConfig.getParameter<edm::InputTag> ("electrons")),
  conversions_ (iConfig.getParameter<edm::InputTag> ("conversions")),
  muons_ (iConfig.getParameter<edm::InputTag> ("muons")),
  taus_ (iConfig.getParameter<edm::InputTag> ("taus")),
  rho_ (iConfig.getParameter<edm::InputTag> ("rho")),
  triggerNames_ (iConfig.getParameter<vector<string> > ("triggerNames")),
  cutResults_ (new CutResults ())
{
  initializeCutResults ();
  produces<CutResults, edm::InRun> ();

  triggersToken_ = consumes<edm::TriggerResults> (triggers_);
  beamspotToken_ = consumes<reco::BeamSpot> (beamspot_);
  verticesToken_ = consumes<vector<reco::Vertex> > (vertices_);
  metToken_ = consumes<vector<pat::MET> > (met_);
  electronsToken_ = consumes<vector<pat::Electron> > (electrons_);
  conversionsToken_ = consumes<vector<reco::Conversion> > (conversions_);
  muonsToken_ = consumes<vector<pat::Muon> > (muons_);
  tausToken_ = consumes<vector<pat::Tau> > (taus_);
  rhoToken_ = consumes<double> (rho_);
}

template<MinimalSkim T>
MinimalSkimFilter<T>::~MinimalSkimFilter ()
{
}

template<MinimalSkim T> void
MinimalSkimFilter<T>::endRunProduce (edm::Run &run, const edm::EventSetup &setup)
{
  run.put (std::move (cutResults_));
  cutResults_.reset (new CutResults ());
  initializeCutResults ();
}

template<MinimalSkim T> bool
MinimalSkimFilter<T>::filter (edm::Event &event, const edm::EventSetup &setup)
{
  edm::Handle<edm::TriggerResults> triggers;
  event.getByToken (triggersToken_, triggers);
  edm::Handle<reco::BeamSpot> beamspot;
  event.getByToken (beamspotToken_, beamspot);
  edm::Handle<vector<reco::Vertex> > vertices;
  event.getByToken (verticesToken_, vertices);
  edm::Handle<vector<pat::MET> > met;
  event.getByToken (metToken_, met);
  edm::Handle<vector<pat::Electron> > electrons;
  event.getByToken (electronsToken_, electrons);
  edm::Handle<vector<reco::Conversion> > conversions;
  event.getByToken (conversionsToken_, conversions);
  edm::Handle<vector<pat::Muon> > muons;
  event.getByToken (muonsToken_, muons);
  edm::Handle<vector<pat::Tau> > taus;
  event.getByToken (tausToken_, taus);
  edm::Handle<double> rho;
  event.getByToken (rhoToken_, rho);

  cutResults_->at (0).cumulativePassCount++;
  cutResults_->at (0).accumulativePassCount++;

  return filterDecision (event, *triggers, *beamspot, vertices->at (0), met->at (0), *electrons, conversions, *muons, *taus, *rho);
}

template<MinimalSkim T> bool
MinimalSkimFilter<T>::passesTrigger (const edm::Event &event, const edm::TriggerResults &triggers) const
{
  bool triggerDecision = cutResults_->triggers ().empty () ? true : false;
  const edm::TriggerNames &triggerNames = event.triggerNames (triggers);

  for (unsigned i = 0; i < triggerNames.size (); i++)
    {
      string name = triggerNames.triggerName (i);
      bool pass = triggers.accept (i);
      for (const auto &trigger : cutResults_->triggers ())
        {
          if (name.find (trigger) == 0)
            triggerDecision = triggerDecision || pass;
        }
    }

  return triggerDecision;
}

template<MinimalSkim T> bool
MinimalSkimFilter<T>::passesTightID_noIsolation_2015 (const pat::Electron &electron, const reco::BeamSpot &beamspot, const reco::Vertex &vertex, const edm::Handle<vector<reco::Conversion> > &conversions) const
{
  bool passes = false;

  if (fabs (electron.superCluster ()->eta ()) <= 1.479)
    {
      passes = (electron.full5x5_sigmaIetaIeta ()                                                              <   0.0101
             && fabs (electron.deltaEtaSuperClusterTrackAtVtx ())                                              <   0.00926
             && fabs (electron.deltaPhiSuperClusterTrackAtVtx ())                                              <   0.0336
             && electron.hadronicOverEm ()                                                                     <   0.0597
             && fabs (1.0 / electron.ecalEnergy () - electron.eSuperClusterOverP () / electron.ecalEnergy ())  <   0.012
             && fabs (electron.gsfTrack ()->dxy (vertex.position ()))                                          <   0.0111
             && fabs (electron.gsfTrack ()->dz (vertex.position ()))                                           <   0.0466
#if CMSSW_VERSION_CODE >= CMSSW_VERSION(9,4,0)
             && electron.gsfTrack ()->hitPattern ().numberOfAllHits (reco::HitPattern::MISSING_INNER_HITS)     <=  2
#else
             && electron.gsfTrack ()->hitPattern ().numberOfHits (reco::HitPattern::MISSING_INNER_HITS)        <=  2
#endif
             && !ConversionTools::hasMatchedConversion (electron, conversions, beamspot.position ()));
    }
  else if (fabs (electron.superCluster ()->eta ()) < 2.5)
    {
      passes = (electron.full5x5_sigmaIetaIeta ()                                                              <   0.0279
             && fabs (electron.deltaEtaSuperClusterTrackAtVtx ())                                              <   0.00724
             && fabs (electron.deltaPhiSuperClusterTrackAtVtx ())                                              <   0.0918
             && electron.hadronicOverEm ()                                                                     <   0.0615
             && fabs (1.0 / electron.ecalEnergy () - electron.eSuperClusterOverP () / electron.ecalEnergy ())  <   0.00999
             && fabs (electron.gsfTrack ()->dxy (vertex.position ()))                                          <   0.0351
             && fabs (electron.gsfTrack ()->dz (vertex.position ()))                                           <   0.417
#if CMSSW_VERSION_CODE >= CMSSW_VERSION(9,4,0)
             && electron.gsfTrack ()->hitPattern ().numberOfAllHits (reco::HitPattern::MISSING_INNER_HITS)     <=  1
#else
             && electron.gsfTrack ()->hitPattern ().numberOfHits (reco::HitPattern::MISSING_INNER_HITS)        <=  1
#endif
             && !ConversionTools::hasMatchedConversion (electron, conversions, beamspot.position ()));
    }

  return passes;
}

template<MinimalSkim T> bool
MinimalSkimFilter<T>::passesTightID_noIsolation_2016 (const pat::Electron &electron, const reco::BeamSpot &beamspot, const reco::Vertex &vertex, const edm::Handle<vector<reco::Conversion> > &conversions) const
{
  bool passes = false;

  if (fabs (electron.superCluster ()->eta ()) <= 1.479)
    {
      passes = (electron.full5x5_sigmaIetaIeta ()                                                                                                 <   0.00998
             && fabs (electron.deltaEtaSuperClusterTrackAtVtx () - electron.superCluster ()->eta () + electron.superCluster ()->seed ()->eta ())  <   0.00308
             && fabs (electron.deltaPhiSuperClusterTrackAtVtx ())                                                                                 <   0.0816
             && electron.hadronicOverEm ()                                                                                                        <   0.0414
             && fabs (1.0 / electron.ecalEnergy () - electron.eSuperClusterOverP () / electron.ecalEnergy ())                                     <   0.0129
             && fabs (electron.gsfTrack ()->dxy (vertex.position ()))                                                                             <   0.05
             && fabs (electron.gsfTrack ()->dz (vertex.position ()))                                                                              <   0.10
#if CMSSW_VERSION_CODE >= CMSSW_VERSION(9,4,0)
             && electron.gsfTrack ()->hitPattern ().numberOfAllHits (reco::HitPattern::MISSING_INNER_HITS)                                           <=  1
#else
             && electron.gsfTrack ()->hitPattern ().numberOfHits (reco::HitPattern::MISSING_INNER_HITS)                                           <=  1
#endif
             && !ConversionTools::hasMatchedConversion (electron, conversions, beamspot.position ()));
    }
  else if (fabs (electron.superCluster ()->eta ()) < 2.5)
    {
      passes = (electron.full5x5_sigmaIetaIeta ()                                                                                                 <   0.0292
             && fabs (electron.deltaEtaSuperClusterTrackAtVtx () - electron.superCluster ()->eta () + electron.superCluster ()->seed ()->eta ())  <   0.00605
             && fabs (electron.deltaPhiSuperClusterTrackAtVtx ())                                                                                 <   0.0394
             && electron.hadronicOverEm ()                                                                                                        <   0.0641
             && fabs (1.0 / electron.ecalEnergy () - electron.eSuperClusterOverP () / electron.ecalEnergy ())                                     <   0.0129
             && fabs (electron.gsfTrack ()->dxy (vertex.position ()))                                                                             <   0.10
             && fabs (electron.gsfTrack ()->dz (vertex.position ()))                                                                              <   0.20
#if CMSSW_VERSION_CODE >= CMSSW_VERSION(9,4,0)
             && electron.gsfTrack ()->hitPattern ().numberOfAllHits (reco::HitPattern::MISSING_INNER_HITS)                                           <=  1
#else
             && electron.gsfTrack ()->hitPattern ().numberOfHits (reco::HitPattern::MISSING_INNER_HITS)                                           <=  1
#endif
             && !ConversionTools::hasMatchedConversion (electron, conversions, beamspot.position ()));
    }

  return passes;
}

template<MinimalSkim T> double
MinimalSkimFilter<T>::effectiveArea_2015 (const pat::Electron &electron) const
{
  if (fabs (electron.superCluster ()->eta ()) >= 0.0000 && fabs (electron.superCluster ()->eta ()) < 1.0000)
    return 0.1752;
  if (fabs (electron.superCluster ()->eta ()) >= 1.0000 && fabs (electron.superCluster ()->eta ()) < 1.4790)
    return 0.1862;
  if (fabs (electron.superCluster ()->eta ()) >= 1.4790 && fabs (electron.superCluster ()->eta ()) < 2.0000)
    return 0.1411;
  if (fabs (electron.superCluster ()->eta ()) >= 2.0000 && fabs (electron.superCluster ()->eta ()) < 2.2000)
    return 0.1534;
  if (fabs (electron.superCluster ()->eta ()) >= 2.2000 && fabs (electron.superCluster ()->eta ()) < 2.3000)
    return 0.1903;
  if (fabs (electron.superCluster ()->eta ()) >= 2.3000 && fabs (electron.superCluster ()->eta ()) < 2.4000)
    return 0.2243;
  if (fabs (electron.superCluster ()->eta ()) >= 2.4000 && fabs (electron.superCluster ()->eta ()) < 5.0000)
    return 0.2687;
  return 0.0;
}

template<MinimalSkim T> double
MinimalSkimFilter<T>::effectiveArea_2016 (const pat::Electron &electron) const
{
  if (fabs (electron.superCluster ()->eta ()) >= 0.0000 && fabs (electron.superCluster ()->eta ()) < 1.0000)
    return 0.1703;
  if (fabs (electron.superCluster ()->eta ()) >= 1.0000 && fabs (electron.superCluster ()->eta ()) < 1.4790)
    return 0.1715;
  if (fabs (electron.superCluster ()->eta ()) >= 1.4790 && fabs (electron.superCluster ()->eta ()) < 2.0000)
    return 0.1213;
  if (fabs (electron.superCluster ()->eta ()) >= 2.0000 && fabs (electron.superCluster ()->eta ()) < 2.2000)
    return 0.1230;
  if (fabs (electron.superCluster ()->eta ()) >= 2.2000 && fabs (electron.superCluster ()->eta ()) < 2.3000)
    return 0.1635;
  if (fabs (electron.superCluster ()->eta ()) >= 2.3000 && fabs (electron.superCluster ()->eta ()) < 2.4000)
    return 0.1937;
  if (fabs (electron.superCluster ()->eta ()) >= 2.4000 && fabs (electron.superCluster ()->eta ()) < 5.0000)
    return 0.2393;
  return 0.0;
}

template<MinimalSkim T> void
MinimalSkimFilter<T>::initializeCutResults ()
{
  cutResults_->clear ();
  cutResults_->push_back (string ("total"));
}

template<MinimalSkim T> bool
MinimalSkimFilter<T>::filterDecision (const edm::Event &event, const edm::TriggerResults &triggers, const reco::BeamSpot &beamspot, const reco::Vertex &vertex, const pat::MET &met, const vector<pat::Electron> &electrons, const edm::Handle<vector<reco::Conversion> > &conversions, const vector<pat::Muon> &muons, const vector<pat::Tau> &taus, const double rho) const
{
  return true;
}

template<> void
MinimalSkimFilter<MET>::initializeCutResults ()
{
  cutResults_->clear ();
  cutResults_->push_back (string ("total"));
  cutResults_->push_back (string ("trigger"));
  cutResults_->push_back (string ("metNoMu > 100 GeV"));
  cutResults_->addTriggers (triggerNames_);
}

template<> bool
MinimalSkimFilter<MET>::filterDecision (const edm::Event &event, const edm::TriggerResults &triggers, const reco::BeamSpot &beamspot, const reco::Vertex &vertex, const pat::MET &met, const vector<pat::Electron> &electrons, const edm::Handle<vector<reco::Conversion> > &conversions, const vector<pat::Muon> &muons, const vector<pat::Tau> &taus, const double rho) const
{
  bool decision = true, flag;

  if ((flag = passesTrigger (event, triggers)))
    cutResults_->at (1).accumulativePassCount++;
  if ((decision = decision && flag))
    cutResults_->at (1).cumulativePassCount++;

  TVector2 metNoMu (met.px (), met.py ());
  for (const auto &muon : muons)
    {
      TVector2 muonPt (muon.px (), muon.py ());
      metNoMu += muonPt;
    }
  if ((flag = (metNoMu.Mod () > 100.0)))
    cutResults_->at (2).accumulativePassCount++;
  if ((decision = decision && flag))
    cutResults_->at (2).cumulativePassCount++;

  return decision;
}

template<> void
MinimalSkimFilter<ELECTRON>::initializeCutResults ()
{
  cutResults_->clear ();
  cutResults_->push_back (string ("total"));
  cutResults_->push_back (string ("trigger"));
  cutResults_->push_back (string (">= 1 electron with pt > 25"));
  cutResults_->push_back (string (">= 1 electron with |eta| < 2.1"));
  cutResults_->push_back (string (">= 1 electron passing tight ID"));
  cutResults_->push_back (string (">= 1 electron passing tight isolation"));
  cutResults_->addTriggers (triggerNames_);
}

template<> bool
MinimalSkimFilter<ELECTRON>::filterDecision (const edm::Event &event, const edm::TriggerResults &triggers, const reco::BeamSpot &beamspot, const reco::Vertex &vertex, const pat::MET &met, const vector<pat::Electron> &electrons, const edm::Handle<vector<reco::Conversion> > &conversions, const vector<pat::Muon> &muons, const vector<pat::Tau> &taus, const double rho) const
{
  bool decision = true, flag;
  unsigned n;

  if ((flag = passesTrigger (event, triggers)))
    cutResults_->at (1).accumulativePassCount++;
  if ((decision = decision && flag))
    cutResults_->at (1).cumulativePassCount++;

  n = 0;
  for (const auto &electron : electrons)
    {
      if (electron.pt () > 25.0)
        {
          n++;
          break;
        }
    }
  if ((flag = (n > 0)))
    cutResults_->at (2).accumulativePassCount++;
  if ((decision = decision && flag))
    cutResults_->at (2).cumulativePassCount++;

  n = 0;
  for (const auto &electron : electrons)
    {
      if (fabs (electron.eta ()) < 2.1)
        {
          n++;
          break;
        }
    }
  if ((flag = (n > 0)))
    cutResults_->at (3).accumulativePassCount++;
  if ((decision = decision && flag))
    cutResults_->at (3).cumulativePassCount++;

  n = 0;
  for (const auto &electron : electrons)
    {
      if (passesTightID_noIsolation_2015 (electron, beamspot, vertex, conversions) || passesTightID_noIsolation_2016 (electron, beamspot, vertex, conversions))
        {
          n++;
          break;
        }
    }
  if ((flag = (n > 0)))
    cutResults_->at (4).accumulativePassCount++;
  if ((decision = decision && flag))
    cutResults_->at (4).cumulativePassCount++;

  n = 0;
  for (const auto &electron : electrons)
    {
      bool passesTightIso_2015 = ((fabs (electron.superCluster ()->eta ()) <= 1.479) && (((electron.pfIsolationVariables ().sumChargedHadronPt + max (0.0, electron.pfIsolationVariables ().sumNeutralHadronEt + electron.pfIsolationVariables ().sumPhotonEt - rho * effectiveArea_2015 (electron))) / electron.pt ()) < 0.0591)) \
                              || ((fabs (electron.superCluster ()->eta ()) >  1.479) && (((electron.pfIsolationVariables ().sumChargedHadronPt + max (0.0, electron.pfIsolationVariables ().sumNeutralHadronEt + electron.pfIsolationVariables ().sumPhotonEt - rho * effectiveArea_2015 (electron))) / electron.pt ()) < 0.0759)),
           passesTightIso_2016 = ((fabs (electron.superCluster ()->eta ()) <= 1.479) && (((electron.pfIsolationVariables ().sumChargedHadronPt + max (0.0, electron.pfIsolationVariables ().sumNeutralHadronEt + electron.pfIsolationVariables ().sumPhotonEt - rho * effectiveArea_2016 (electron))) / electron.pt ()) < 0.0588)) \
                              || ((fabs (electron.superCluster ()->eta ()) >  1.479) && (((electron.pfIsolationVariables ().sumChargedHadronPt + max (0.0, electron.pfIsolationVariables ().sumNeutralHadronEt + electron.pfIsolationVariables ().sumPhotonEt - rho * effectiveArea_2016 (electron))) / electron.pt ()) < 0.0571));

      if (passesTightIso_2015 || passesTightIso_2016)
        {
          n++;
          break;
        }
    }
  if ((flag = (n > 0)))
    cutResults_->at (5).accumulativePassCount++;
  if ((decision = decision && flag))
    cutResults_->at (5).cumulativePassCount++;

  return decision;
}

template<> void
MinimalSkimFilter<MUON>::initializeCutResults ()
{
  cutResults_->clear ();
  cutResults_->push_back (string ("total"));
  cutResults_->push_back (string ("trigger"));
  cutResults_->push_back (string (">= 1 muon with pt > 26"));
  cutResults_->push_back (string (">= 1 muon with |eta| < 2.1"));
  cutResults_->push_back (string (">= 1 muon passing tight ID"));
  cutResults_->push_back (string (">= 1 muon passing tight isolation"));
  cutResults_->addTriggers (triggerNames_);
}

template<> bool
MinimalSkimFilter<MUON>::filterDecision (const edm::Event &event, const edm::TriggerResults &triggers, const reco::BeamSpot &beamspot, const reco::Vertex &vertex, const pat::MET &met, const vector<pat::Electron> &electrons, const edm::Handle<vector<reco::Conversion> > &conversions, const vector<pat::Muon> &muons, const vector<pat::Tau> &taus, const double rho) const
{
  bool decision = true, flag;
  unsigned n;

  if ((flag = passesTrigger (event, triggers)))
    cutResults_->at (1).accumulativePassCount++;
  if ((decision = decision && flag))
    cutResults_->at (1).cumulativePassCount++;

  n = 0;
  for (const auto &muon : muons)
    {
      if (muon.pt () > 26.0)
        {
          n++;
          break;
        }
    }
  if ((flag = (n > 0)))
    cutResults_->at (2).accumulativePassCount++;
  if ((decision = decision && flag))
    cutResults_->at (2).cumulativePassCount++;

  n = 0;
  for (const auto &muon : muons)
    {
      if (fabs (muon.eta ()) < 2.1)
        {
          n++;
          break;
        }
    }
  if ((flag = (n > 0)))
    cutResults_->at (3).accumulativePassCount++;
  if ((decision = decision && flag))
    cutResults_->at (3).cumulativePassCount++;

  n = 0;
  for (const auto &muon : muons)
    {
      if (muon.isTightMuon (vertex))
        {
          n++;
          break;
        }
    }
  if ((flag = (n > 0)))
    cutResults_->at (4).accumulativePassCount++;
  if ((decision = decision && flag))
    cutResults_->at (4).cumulativePassCount++;

  n = 0;
  for (const auto &muon : muons)
    {
      if ((muon.pfIsolationR04 ().sumChargedHadronPt + max (0.0, muon.pfIsolationR04 ().sumNeutralHadronEt + muon.pfIsolationR04 ().sumPhotonEt - 0.5 * muon.pfIsolationR04 ().sumPUPt)) / muon.pt () < 0.15)
        {
          n++;
          break;
        }
    }
  if ((flag = (n > 0)))
    cutResults_->at (5).accumulativePassCount++;
  if ((decision = decision && flag))
    cutResults_->at (5).cumulativePassCount++;

  return decision;
}

template<> void
MinimalSkimFilter<TAU>::initializeCutResults ()
{
  cutResults_->clear ();
  cutResults_->push_back (string ("total"));
  cutResults_->push_back (string ("trigger"));
  cutResults_->push_back (string (">= 1 tau with pt > 25"));
  cutResults_->push_back (string (">= 1 tau with |eta| < 2.1"));
  cutResults_->push_back (string (">= 1 tau passing decay mode reconstruction && light flavor rejection"));
  cutResults_->push_back (string (">= 1 tau passing tight isolation"));
  cutResults_->addTriggers (triggerNames_);
}

template<> bool
MinimalSkimFilter<TAU>::filterDecision (const edm::Event &event, const edm::TriggerResults &triggers, const reco::BeamSpot &beamspot, const reco::Vertex &vertex, const pat::MET &met, const vector<pat::Electron> &electrons, const edm::Handle<vector<reco::Conversion> > &conversions, const vector<pat::Muon> &muons, const vector<pat::Tau> &taus, const double rho) const
{
  bool decision = true, flag;
  unsigned n;

  if ((flag = passesTrigger (event, triggers)))
    cutResults_->at (1).accumulativePassCount++;
  if ((decision = decision && flag))
    cutResults_->at (1).cumulativePassCount++;

  n = 0;
  for (const auto &tau : taus)
    {
      if (tau.pt () > 25.0)
        {
          n++;
          break;
        }
    }
  if ((flag = (n > 0)))
    cutResults_->at (2).accumulativePassCount++;
  if ((decision = decision && flag))
    cutResults_->at (2).cumulativePassCount++;

  n = 0;
  for (const auto &tau : taus)
    {
      if (fabs (tau.eta ()) < 2.1)
        {
          n++;
          break;
        }
    }
  if ((flag = (n > 0)))
    cutResults_->at (3).accumulativePassCount++;
  if ((decision = decision && flag))
    cutResults_->at (3).cumulativePassCount++;

  n = 0;
  for (const auto &tau : taus)
    {
      if (tau.isTauIDAvailable ("againstElectronLooseMVA5"))
        {
          if (tau.tauID ("decayModeFinding") > 0.5 && tau.tauID ("againstElectronLooseMVA5") > 0.5 && tau.tauID ("againstMuonLoose3") > 0.5)
            {
              n++;
              break;
            }
        }
      else if (tau.isTauIDAvailable ("againstElectronLooseMVA6"))
        {
          if (tau.tauID ("decayModeFinding") > 0.5 && tau.tauID ("againstElectronLooseMVA6") > 0.5 && tau.tauID ("againstMuonLoose3") > 0.5)
            {
              n++;
              break;
            }
        }
    }
  if ((flag = (n > 0)))
    cutResults_->at (4).accumulativePassCount++;
  if ((decision = decision && flag))
    cutResults_->at (4).cumulativePassCount++;

  n = 0;
  for (const auto &tau : taus)
    {
      if (tau.tauID ("byTightCombinedIsolationDeltaBetaCorr3Hits") > 0.5)
        {
          n++;
          break;
        }
    }
  if ((flag = (n > 0)))
    cutResults_->at (5).accumulativePassCount++;
  if ((decision = decision && flag))
    cutResults_->at (5).cumulativePassCount++;

  return decision;
}

typedef  MinimalSkimFilter<MET>       METSkimFilter;
typedef  MinimalSkimFilter<ELECTRON>  ElectronSkimFilter;
typedef  MinimalSkimFilter<MUON>      MuonSkimFilter;
typedef  MinimalSkimFilter<TAU>       TauSkimFilter;

DEFINE_FWK_MODULE (METSkimFilter);
DEFINE_FWK_MODULE (ElectronSkimFilter);
DEFINE_FWK_MODULE (MuonSkimFilter);
DEFINE_FWK_MODULE (TauSkimFilter);
