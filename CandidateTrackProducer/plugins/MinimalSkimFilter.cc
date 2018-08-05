#include "TVector2.h"

#include "OSUT3Analysis/AnaTools/interface/CMSSWVersion.h"

#include "DisappTrks/CandidateTrackProducer/plugins/MinimalSkimFilter.h"

template<MinimalSkim T>
MinimalSkimFilter<T>::MinimalSkimFilter (const edm::ParameterSet& iConfig) :
  triggers_ (iConfig.getParameter<edm::InputTag> ("triggers")),
  vertices_ (iConfig.getParameter<edm::InputTag> ("vertices")),
  met_ (iConfig.getParameter<edm::InputTag> ("met")),
  pfCandidates_ (iConfig.getParameter<edm::InputTag> ("pfCandidates")),
  electrons_ (iConfig.getParameter<edm::InputTag> ("electrons")),
  eleVIDTightIdMap_ (iConfig.getParameter<edm::InputTag> ("eleVIDTightIdMap")),
  muons_ (iConfig.getParameter<edm::InputTag> ("muons")),
  taus_ (iConfig.getParameter<edm::InputTag> ("taus")),
  rho_ (iConfig.getParameter<edm::InputTag> ("rho")),
  triggerNames_ (iConfig.getParameter<vector<string> > ("triggerNames")),
  cutResults_ (new CutResults ())
{
  initializeCutResults ();

#if CMSSW_VERSION_CODE >= CMSSW_VERSION(9,4,0)
  produces<CutResults, edm::Transition::EndRun> ();
#else
  produces<CutResults, edm::InRun> ();
#endif

  triggersToken_ = consumes<edm::TriggerResults> (triggers_);
  verticesToken_ = consumes<vector<reco::Vertex> > (vertices_);
  metToken_ = consumes<vector<pat::MET> > (met_);
  pfCandidatesToken_ = consumes<vector<pat::PackedCandidate> > (pfCandidates_);
  electronsToken_ = consumes<edm::View<pat::Electron> > (electrons_);
  eleVIDTightIdMapToken_ = consumes<edm::ValueMap<bool> > (eleVIDTightIdMap_);
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

  edm::Handle<vector<reco::Vertex> > vertices;
  event.getByToken (verticesToken_, vertices);

  edm::Handle<vector<pat::MET> > met;
  event.getByToken (metToken_, met);
  edm::Handle<vector<pat::PackedCandidate> > pfCandidates;
  event.getByToken (pfCandidatesToken_, pfCandidates);

  edm::Handle<edm::View<pat::Electron> > electrons;
  event.getByToken (electronsToken_, electrons);
  edm::Handle<edm::ValueMap<bool> > eleVIDTightIdMap;
  event.getByToken(eleVIDTightIdMapToken_, eleVIDTightIdMap);

  edm::Handle<vector<pat::Muon> > muons;
  event.getByToken (muonsToken_, muons);

  edm::Handle<vector<pat::Tau> > taus;
  event.getByToken (tausToken_, taus);

  edm::Handle<double> rho;
  event.getByToken (rhoToken_, rho);

  cutResults_->at (0).cumulativePassCount++;
  cutResults_->at (0).accumulativePassCount++;

  return filterDecision (event, 
                         *triggers, 
                         vertices->at (0), 
                         met->at (0), 
                         *pfCandidates,
                         *electrons,
                         *eleVIDTightIdMap,
                         *muons, 
                         *taus, 
                         *rho);
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

template<MinimalSkim T> void
MinimalSkimFilter<T>::initializeCutResults ()
{
  cutResults_->clear ();
  cutResults_->push_back (string ("total"));
}

template<MinimalSkim T> bool
MinimalSkimFilter<T>::filterDecision (const edm::Event &event, 
                                      const edm::TriggerResults &triggers, 
                                      const reco::Vertex &vertex, 
                                      const pat::MET &met,
                                      const vector<pat::PackedCandidate> &pfCandidates, 
                                      const edm::View<pat::Electron> &electrons,
                                      const edm::ValueMap<bool> &eleVIDs,
                                      const vector<pat::Muon> &muons, 
                                      const vector<pat::Tau> &taus, 
                                      const double rho) const
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
MinimalSkimFilter<MET>::filterDecision (const edm::Event &event, 
                                        const edm::TriggerResults &triggers, 
                                        const reco::Vertex &vertex, 
                                        const pat::MET &met,
                                        const vector<pat::PackedCandidate> &pfCandidates, 
                                        const edm::View<pat::Electron> &electrons,
                                        const edm::ValueMap<bool> &eleVIDs,
                                        const vector<pat::Muon> &muons, 
                                        const vector<pat::Tau> &taus, 
                                        const double rho) const
{
  bool decision = true, flag;

  if((flag = passesTrigger(event, triggers))) cutResults_->at(1).accumulativePassCount++;
  if((decision = decision && flag))           cutResults_->at(1).cumulativePassCount++;

  TVector2 metNoMu(met.px (), met.py ());
  for (const auto &pfCandidate : pfCandidates) {
    if (abs (pfCandidate.pdgId ()) != 13) continue;
    TVector2 muon (pfCandidate.px (), pfCandidate.py ());
    metNoMu += muon;
  }
  if((flag = (metNoMu.Mod () > 100.0))) cutResults_->at(2).accumulativePassCount++;
  if((decision = decision && flag))     cutResults_->at(2).cumulativePassCount++;

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
  cutResults_->push_back (string (">= 1 electron passing tight ID + iso (by VID)"));
  cutResults_->push_back (string (">= 1 electron passing |d0| < 0.05, 0.10 (EE, EB)"));
  cutResults_->push_back (string (">= 1 electron passing |dz| < 0.10, 0.417 (EE, EB)"));
  cutResults_->addTriggers (triggerNames_);
}

template<> bool
MinimalSkimFilter<ELECTRON>::filterDecision (const edm::Event &event, 
                                             const edm::TriggerResults &triggers, 
                                             const reco::Vertex &vertex, 
                                             const pat::MET &met,
                                             const vector<pat::PackedCandidate> &pfCandidates,
                                             const edm::View<pat::Electron> &electrons,
                                             const edm::ValueMap<bool> &eleVIDs,
                                             const vector<pat::Muon> &muons, 
                                             const vector<pat::Tau> &taus, 
                                             const double rho) const
{
  bool decision = true, flag;
  unsigned n;

  // trigger
  if((flag = passesTrigger (event, triggers))) cutResults_->at(1).accumulativePassCount++;
  if((decision = decision && flag))            cutResults_->at(1).cumulativePassCount++;

  // pt > 25
  n = 0;
  for(const auto &electron : electrons) {
    if(electron.pt () > 25.0) {
      n++;
      break;
    }
  }
  if((flag = (n > 0)))               cutResults_->at(2).accumulativePassCount++;
  if ((decision = decision && flag)) cutResults_->at(2).cumulativePassCount++;

  // |eta| < 2.1
  n = 0;
  for(const auto &electron : electrons) {
    if(fabs (electron.eta()) < 2.1) {
      n++;
      break;
    }
  }
  if((flag = (n > 0)))              cutResults_->at(3).accumulativePassCount++;
  if((decision = decision && flag)) cutResults_->at(3).cumulativePassCount++;

  // tight ID + iso (by VID)
  n = 0;
  for(unsigned int iEle = 0; iEle < electrons.size(); iEle++) {
    if(eleVIDs[electrons.refAt(iEle)]) {
      n++;
      break;
    }
  }
  if((flag = (n > 0)))              cutResults_->at(4).accumulativePassCount++;
  if((decision = decision && flag)) cutResults_->at(4).cumulativePassCount++;

  // |d0| < 0.10
  // 2015: 0.0111 (EE), 0.0351 (EB)
  // 2016/7: 0.05 (EE), 0.10 (EB)
  n = 0;
  for(const auto &electron : electrons) {
    double eleD0 = fabs(electron.gsfTrack()->dxy(vertex.position()));
    if((fabs(electron.superCluster()->eta()) <= 1.479 && eleD0 < 0.05) ||
       (fabs(electron.superCluster()->eta()) >  1.479 && eleD0 < 0.10)) {
      n++;
      break;
    }
  }
  if((flag = (n > 0)))              cutResults_->at(5).accumulativePassCount++;
  if((decision = decision && flag)) cutResults_->at(5).cumulativePassCount++;

  // |dz| < 0.417
  // 2015: 0.0466 (EE), 0.417 (EB)
  // 2016/7: 0.10 (EE), 0.20 (EB)
  n = 0;
  for(const auto &electron : electrons) {
    double eleDZ = fabs(electron.gsfTrack()->dz(vertex.position()));
    if((fabs(electron.superCluster()->eta()) <= 1.479 && eleDZ < 0.10) ||
       (fabs(electron.superCluster()->eta()) >  1.479 && eleDZ < 0.417)) {
      n++;
      break;
    }
  }
  if((flag = (n > 0)))              cutResults_->at(6).accumulativePassCount++;
  if((decision = decision && flag)) cutResults_->at(6).cumulativePassCount++;

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
MinimalSkimFilter<MUON>::filterDecision (const edm::Event &event, 
                                         const edm::TriggerResults &triggers, 
                                         const reco::Vertex &vertex, 
                                         const pat::MET &met,
                                         const vector<pat::PackedCandidate> &pfCandidates, 
                                         const edm::View<pat::Electron> &electrons,
                                         const edm::ValueMap<bool> &eleVIDs, 
                                         const vector<pat::Muon> &muons, 
                                         const vector<pat::Tau> &taus, 
                                         const double rho) const
{
  bool decision = true, flag;
  unsigned n;

  if ((flag = passesTrigger (event, triggers))) cutResults_->at (1).accumulativePassCount++;
  if ((decision = decision && flag))            cutResults_->at (1).cumulativePassCount++;

  n = 0;
  for (const auto &muon : muons) {
    if (muon.pt () > 26.0) {
      n++;
      break;
    }
  }
  if ((flag = (n > 0)))              cutResults_->at (2).accumulativePassCount++;
  if ((decision = decision && flag)) cutResults_->at (2).cumulativePassCount++;

  n = 0;
  for (const auto &muon : muons) {
    if (fabs (muon.eta ()) < 2.1) {
      n++;
      break;
    }
  }
  if ((flag = (n > 0)))              cutResults_->at (3).accumulativePassCount++;
  if ((decision = decision && flag)) cutResults_->at (3).cumulativePassCount++;

  n = 0;
  for (const auto &muon : muons) {
    if (muon.isTightMuon (vertex)) {
      n++;
      break;
    }
  }
  if ((flag = (n > 0)))              cutResults_->at (4).accumulativePassCount++;
  if ((decision = decision && flag)) cutResults_->at (4).cumulativePassCount++;

  n = 0;
  for (const auto &muon : muons) {
    if ((muon.pfIsolationR04 ().sumChargedHadronPt + 
         max (0.0, 
              muon.pfIsolationR04 ().sumNeutralHadronEt + 
              muon.pfIsolationR04 ().sumPhotonEt - 
              0.5 * muon.pfIsolationR04 ().sumPUPt)) / muon.pt () < 0.15) {
      n++;
      break;
    }
  }
  if ((flag = (n > 0))) cutResults_->at (5).accumulativePassCount++;
  if ((decision = decision && flag)) cutResults_->at (5).cumulativePassCount++;

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
MinimalSkimFilter<TAU>::filterDecision (const edm::Event &event, 
                                        const edm::TriggerResults &triggers, 
                                        const reco::Vertex &vertex, 
                                        const pat::MET &met,
                                        const vector<pat::PackedCandidate> &pfCandidates, 
                                        const edm::View<pat::Electron> &electrons,
                                        const edm::ValueMap<bool> &eleVIDs, 
                                        const vector<pat::Muon> &muons, 
                                        const vector<pat::Tau> &taus, 
                                        const double rho) const
{
  bool decision = true, flag;
  unsigned n;

  if ((flag = passesTrigger (event, triggers))) cutResults_->at (1).accumulativePassCount++;
  if ((decision = decision && flag))            cutResults_->at (1).cumulativePassCount++;

  n = 0;
  for (const auto &tau : taus) {
    if (tau.pt () > 25.0) {
      n++;
      break;
    }
  }
  if ((flag = (n > 0)))              cutResults_->at (2).accumulativePassCount++;
  if ((decision = decision && flag)) cutResults_->at (2).cumulativePassCount++;

  n = 0;
  for (const auto &tau : taus) {
    if (fabs (tau.eta ()) < 2.1) {
      n++;
      break;
    }
  }
  if ((flag = (n > 0)))              cutResults_->at (3).accumulativePassCount++;
  if ((decision = decision && flag)) cutResults_->at (3).cumulativePassCount++;

  n = 0;
  for (const auto &tau : taus) {
    if (tau.isTauIDAvailable ("againstElectronLooseMVA5")) {
      if (tau.tauID ("decayModeFinding") > 0.5 && 
          tau.tauID ("againstElectronLooseMVA5") > 0.5 && 
          tau.tauID ("againstMuonLoose3") > 0.5) {
        n++;
        break;
      }
    }
    else if (tau.isTauIDAvailable ("againstElectronLooseMVA6")) {
      if (tau.tauID ("decayModeFinding") > 0.5 && 
          tau.tauID ("againstElectronLooseMVA6") > 0.5 && 
          tau.tauID ("againstMuonLoose3") > 0.5) {
        n++;
        break;
      }
    }
  }
  if ((flag = (n > 0)))              cutResults_->at (4).accumulativePassCount++;
  if ((decision = decision && flag)) cutResults_->at (4).cumulativePassCount++;

  n = 0;
  for (const auto &tau : taus) {
    if (tau.isTauIDAvailable ("byTightCombinedIsolationDeltaBetaCorr3Hits")) {
      if (tau.tauID ("byTightCombinedIsolationDeltaBetaCorr3Hits") > 0.5) {
        n++;
        break;
      }
    }
    else if (tau.isTauIDAvailable ("byTightIsolationMVArun2v1DBoldDMwLT")) {
      if (tau.tauID ("byTightIsolationMVArun2v1DBoldDMwLT") > 0.5) {
        n++;
        break;
      }
    }
  }
  if ((flag = (n > 0)))              cutResults_->at (5).accumulativePassCount++;
  if ((decision = decision && flag)) cutResults_->at (5).cumulativePassCount++;

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
