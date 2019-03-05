#include "TVector2.h"

#include "OSUT3Analysis/AnaTools/interface/CMSSWVersion.h"

#include "DisappTrks/CandidateTrackProducer/plugins/MinimalSkimFilter.h"

template<MinimalSkim T>
MinimalSkimFilter<T>::MinimalSkimFilter (const edm::ParameterSet& iConfig) :
  triggers_ (iConfig.getParameter<edm::InputTag> ("triggers")),
  beamspot_ (iConfig.getParameter<edm::InputTag> ("beamspot")),
  vertices_ (iConfig.getParameter<edm::InputTag> ("vertices")),
  met_ (iConfig.getParameter<edm::InputTag> ("met")),
  pfCandidates_ (iConfig.getParameter<edm::InputTag> ("pfCandidates")),
  electrons_ (iConfig.getParameter<edm::InputTag> ("electrons")),
  conversions_ (iConfig.getParameter<edm::InputTag> ("conversions")),
  muons_ (iConfig.getParameter<edm::InputTag> ("muons")),
  taus_ (iConfig.getParameter<edm::InputTag> ("taus")),
  rho_ (iConfig.getParameter<edm::InputTag> ("rho")),
  etaCut_ (iConfig.getParameter<double> ("etaCut")),
  ptCut_ (iConfig.getParameter<double> ("ptCut")),
  eleVIDid_ (iConfig.getParameter<string> ("eleVIDid")),
  d0Cuts_ (iConfig.getParameter<vector<double> > ("d0Cuts")),
  dZCuts_ (iConfig.getParameter<vector<double> > ("dZCuts")),
  triggerNames_ (iConfig.getParameter<vector<string> > ("triggerNames")),
  cutResults_ (new CutResults ())
{
  assert(d0Cuts_.size() == 2 && dZCuts_.size() == 2);

  initializeCutResults ();

#if CMSSW_VERSION_CODE >= CMSSW_VERSION(9,4,0)
  produces<CutResults, edm::Transition::EndRun> ();
#else
  produces<CutResults, edm::InRun> ();
#endif

  triggersToken_ = consumes<edm::TriggerResults> (triggers_);
  beamspotToken_ = consumes<reco::BeamSpot> (beamspot_);
  verticesToken_ = consumes<vector<reco::Vertex> > (vertices_);
  metToken_ = consumes<vector<pat::MET> > (met_);
  pfCandidatesToken_ = consumes<vector<pat::PackedCandidate> > (pfCandidates_);
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
  edm::Handle<vector<pat::PackedCandidate> > pfCandidates;
  event.getByToken (pfCandidatesToken_, pfCandidates);

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

  return filterDecision (event,
                         *triggers,
                         *beamspot,
                         vertices->at (0),
                         met->at (0),
                         *pfCandidates,
                         *electrons,
                         conversions,
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
                                      const reco::BeamSpot &beamspot,
                                      const reco::Vertex &vertex,
                                      const pat::MET &met,
                                      const vector<pat::PackedCandidate> &pfCandidates,
                                      const vector<pat::Electron> &electrons,
                                      const edm::Handle<vector<reco::Conversion> > &conversions,
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
  cutResults_->push_back ("metNoMu > " + to_string(ptCut_) + " GeV");
  cutResults_->addTriggers (triggerNames_);
}

template<> bool
MinimalSkimFilter<MET>::filterDecision (const edm::Event &event,
                                        const edm::TriggerResults &triggers,
                                        const reco::BeamSpot &beamspot,
                                        const reco::Vertex &vertex,
                                        const pat::MET &met,
                                        const vector<pat::PackedCandidate> &pfCandidates,
                                        const vector<pat::Electron> &electrons,
                                        const edm::Handle<vector<reco::Conversion> > &conversions,
                                        const vector<pat::Muon> &muons,
                                        const vector<pat::Tau> &taus,
                                        const double rho) const
{
  bool decision = true;

  // trigger
  if(passesTrigger(event, triggers)) cutResults_->at(1).accumulativePassCount++;
  if((decision = decision && passesTrigger(event, triggers))) cutResults_->at(1).cumulativePassCount++;

  // pt > cut
  TVector2 metNoMu(met.px (), met.py ());
  for (const auto &pfCandidate : pfCandidates) {
    if (abs (pfCandidate.pdgId ()) != 13) continue;
    TVector2 muon (pfCandidate.px (), pfCandidate.py ());
    metNoMu += muon;
  }
  if(metNoMu.Mod() > ptCut_) cutResults_->at(2).accumulativePassCount++;
  if((decision = decision && metNoMu.Mod() > ptCut_)) cutResults_->at(2).cumulativePassCount++;

  return decision;
}

template<> void
MinimalSkimFilter<ELECTRON>::initializeCutResults ()
{
  cutResults_->clear ();
  cutResults_->push_back (string ("total"));
  cutResults_->push_back (string ("trigger"));
  cutResults_->push_back (">= 1 electron with pt > " + to_string(ptCut_));
  cutResults_->push_back (">= 1 electron with |eta| < " + to_string(etaCut_));
  cutResults_->push_back (string (">= 1 electron passing tight ID + Iso (VID)"));
  cutResults_->push_back (">= 1 electron passing d0 < " + to_string(d0Cuts_[0]) + " EB (" + to_string(d0Cuts_[1]) + " EE) wrt PV");
  cutResults_->push_back (">= 1 electron passing dZ < " + to_string(dZCuts_[0]) + " EB (" + to_string(dZCuts_[1]) + " EE) wrt PV");
  cutResults_->addTriggers (triggerNames_);
}

template<> bool
MinimalSkimFilter<ELECTRON>::filterDecision (const edm::Event &event,
                                             const edm::TriggerResults &triggers,
                                             const reco::BeamSpot &beamspot,
                                             const reco::Vertex &vertex,
                                             const pat::MET &met,
                                             const vector<pat::PackedCandidate> &pfCandidates,
                                             const vector<pat::Electron> &electrons,
                                             const edm::Handle<vector<reco::Conversion> > &conversions,
                                             const vector<pat::Muon> &muons,
                                             const vector<pat::Tau> &taus,
                                             const double rho) const
{
  bool decision = true;
  unsigned n, i;

  // trigger
  if(passesTrigger (event, triggers)) cutResults_->at(1).accumulativePassCount++;
  if((decision = decision && passesTrigger (event, triggers))) cutResults_->at(1).cumulativePassCount++;

  vector<bool> elePasses(true, electrons.size());

  // pt > cut
  n = i = 0;
  for(const auto &electron : electrons) {
    if(electron.pt() > ptCut_) n++;
    else elePasses[i] = false;
    i++;
  }
  if(n > 0) cutResults_->at(2).accumulativePassCount++;
  if((decision = decision && count(elePasses.begin(), elePasses.end(), true) > 0)) cutResults_->at(2).cumulativePassCount++;

  // |eta| < cut
  n = i = 0;
  for(const auto &electron : electrons) {
    if(fabs (electron.eta()) < etaCut_) n++;
    else elePasses[i] = false;
    i++;
  }
  if(n > 0) cutResults_->at(3).accumulativePassCount++;
  if((decision = decision && count(elePasses.begin(), elePasses.end(), true) > 0)) cutResults_->at(3).cumulativePassCount++;

  // tight ID + Iso (VID)
  n = i = 0;
  for(const auto &electron : electrons) {
    if(electron.electronID(eleVIDid_)) n++;
    else elePasses[i] = false;
    i++;
  }
  if(n > 0) cutResults_->at(4).accumulativePassCount++;
  if((decision = decision && count(elePasses.begin(), elePasses.end(), true) > 0)) cutResults_->at(4).cumulativePassCount++;

  // d0 < cut
  n = i = 0;
  for(const auto &electron : electrons) {
    if((fabs(electron.superCluster()->eta()) <= 1.479 && fabs(electron.gsfTrack()->dxy(vertex.position())) < d0Cuts_[0]) ||
       (fabs(electron.superCluster()->eta()) > 1.479 && fabs(electron.gsfTrack()->dxy(vertex.position())) < d0Cuts_[1])) {
      n++;
    }
    else elePasses[i] = false;
    i++;
  }
  if(n > 0) cutResults_->at(5).accumulativePassCount++;
  if((decision = decision && count(elePasses.begin(), elePasses.end(), true) > 0)) cutResults_->at(5).cumulativePassCount++;

  // dZ < cut
  n = i = 0;
  for(const auto &electron : electrons) {
    if((fabs(electron.superCluster()->eta()) <= 1.479 && fabs(electron.gsfTrack()->dz(vertex.position())) < dZCuts_[0]) ||
       (fabs(electron.superCluster()->eta()) > 1.479 && fabs(electron.gsfTrack()->dz(vertex.position())) < dZCuts_[1])) {
      n++;
    }
    else elePasses[i] = false;
    i++;
  }
  if(n > 0) cutResults_->at(6).accumulativePassCount++;
  if((decision = decision && count(elePasses.begin(), elePasses.end(), true) > 0)) cutResults_->at(6).cumulativePassCount++;

  return decision;
}

template<> void
MinimalSkimFilter<MUON>::initializeCutResults ()
{
  cutResults_->clear ();
  cutResults_->push_back (string ("total"));
  cutResults_->push_back (string ("trigger"));
  cutResults_->push_back (">= 1 muon with pt > " + to_string(ptCut_));
  cutResults_->push_back (">= 1 muon with |eta| < " + to_string(etaCut_));
  cutResults_->push_back (string (">= 1 muon passing tight ID"));
  cutResults_->push_back (string (">= 1 muon passing tight isolation"));
  cutResults_->addTriggers (triggerNames_);
}

template<> bool
MinimalSkimFilter<MUON>::filterDecision (const edm::Event &event,
                                         const edm::TriggerResults &triggers,
                                         const reco::BeamSpot &beamspot,
                                         const reco::Vertex &vertex,
                                         const pat::MET &met,
                                         const vector<pat::PackedCandidate> &pfCandidates,
                                         const vector<pat::Electron> &electrons,
                                         const edm::Handle<vector<reco::Conversion> > &conversions,
                                         const vector<pat::Muon> &muons,
                                         const vector<pat::Tau> &taus,
                                         const double rho) const
{
  bool decision = true;
  unsigned n, i;

  // trigger
  if(passesTrigger (event, triggers)) cutResults_->at(1).accumulativePassCount++;
  if((decision = decision && passesTrigger (event, triggers))) cutResults_->at(1).cumulativePassCount++;

  vector<bool> muPasses(true, muons.size());

  // pt > cut
  n = i = 0;
  for (const auto &muon : muons) {
    if (muon.pt () > ptCut_) n++;
    else muPasses[i] = false;
    i++;
  }
  if(n > 0) cutResults_->at (2).accumulativePassCount++;
  if((decision = decision && count(muPasses.begin(), muPasses.end(), true) > 0)) cutResults_->at (2).cumulativePassCount++;

  // eta < cut
  n = i = 0;
  for (const auto &muon : muons) {
    if (fabs (muon.eta ()) < etaCut_) n++;
    else muPasses[i] = false;
    i++;
  }
  if(n > 0) cutResults_->at (3).accumulativePassCount++;
  if((decision = decision && count(muPasses.begin(), muPasses.end(), true) > 0)) cutResults_->at (3).cumulativePassCount++;

  // tight ID
  n = i = 0;
  for (const auto &muon : muons) {
    if (muon.isTightMuon (vertex)) n++;
    else muPasses[i] = false;
    i++;
  }
  if(n > 0) cutResults_->at (4).accumulativePassCount++;
  if((decision = decision && count(muPasses.begin(), muPasses.end(), true) > 0)) cutResults_->at (4).cumulativePassCount++;

  // tight PF iso
  n = i = 0;
  for (const auto &muon : muons) {
    if ((muon.pfIsolationR04 ().sumChargedHadronPt + 
         max (0.0, 
              muon.pfIsolationR04 ().sumNeutralHadronEt + 
              muon.pfIsolationR04 ().sumPhotonEt - 
              0.5 * muon.pfIsolationR04 ().sumPUPt)) / muon.pt () < 0.15) {
      n++;
    }
    else muPasses[i] = false;
    i++;
  }
  if(n > 0) cutResults_->at (5).accumulativePassCount++;
  if((decision = decision && count(muPasses.begin(), muPasses.end(), true) > 0)) cutResults_->at (5).cumulativePassCount++;

  return decision;
}

template<> void
MinimalSkimFilter<TAU>::initializeCutResults ()
{
  cutResults_->clear ();
  cutResults_->push_back (string ("total"));
  cutResults_->push_back (string ("trigger"));
  cutResults_->push_back (">= 1 tau with pt > " + to_string(ptCut_));
  cutResults_->push_back (">= 1 tau with |eta| < " + to_string(etaCut_));
  cutResults_->push_back (string (">= 1 tau passing decay mode reconstruction && light flavor rejection"));
  cutResults_->push_back (string (">= 1 tau passing tight isolation"));
  cutResults_->addTriggers (triggerNames_);
}

template<> bool
MinimalSkimFilter<TAU>::filterDecision (const edm::Event &event,
                                        const edm::TriggerResults &triggers,
                                        const reco::BeamSpot &beamspot,
                                        const reco::Vertex &vertex,
                                        const pat::MET &met,
                                        const vector<pat::PackedCandidate> &pfCandidates,
                                        const vector<pat::Electron> &electrons,
                                        const edm::Handle<vector<reco::Conversion> > &conversions,
                                        const vector<pat::Muon> &muons,
                                        const vector<pat::Tau> &taus,
                                        const double rho) const
{
  bool decision = true;
  unsigned n, i;

  // trigger
  if(passesTrigger (event, triggers)) cutResults_->at(1).accumulativePassCount++;
  if((decision = decision && passesTrigger (event, triggers))) cutResults_->at(1).cumulativePassCount++;

  vector<bool> tauPasses(true, taus.size());

  // pt > cut
  n = i = 0;
  for (const auto &tau : taus) {
    if (tau.pt () > ptCut_) n++;
    else tauPasses[i] = false;
    i++;
  }
  if(n > 0) cutResults_->at (2).accumulativePassCount++;
  if((decision = decision && count(tauPasses.begin(), tauPasses.end(), true) > 0)) cutResults_->at (2).cumulativePassCount++;

  // eta < cut
  n = i = 0;
  for (const auto &tau : taus) {
    if (fabs (tau.eta ()) < etaCut_) n++;
    else tauPasses[i] = false;
    i++;
  }
  if(n > 0) cutResults_->at (3).accumulativePassCount++;
  if((decision = decision && count(tauPasses.begin(), tauPasses.end(), true) > 0)) cutResults_->at (3).cumulativePassCount++;

  // tight ID
  n = i = 0;
  for (const auto &tau : taus) {
    if (tau.isTauIDAvailable ("againstElectronLooseMVA5")) {
      if (tau.tauID ("decayModeFinding") > 0.5 && 
          tau.tauID ("againstElectronLooseMVA5") > 0.5 && 
          tau.tauID ("againstMuonLoose3") > 0.5) {
        n++;
      }
      else tauPasses[i] = false;
      i++;
    }
    else if (tau.isTauIDAvailable ("againstElectronLooseMVA6")) {
      if (tau.tauID ("decayModeFinding") > 0.5 && 
          tau.tauID ("againstElectronLooseMVA6") > 0.5 && 
          tau.tauID ("againstMuonLoose3") > 0.5) {
        n++;
      }
      else tauPasses[i] = false;
      i++;
    }
  }
  if(n > 0) cutResults_->at (4).accumulativePassCount++;
  if((decision = decision && count(tauPasses.begin(), tauPasses.end(), true) > 0)) cutResults_->at (4).cumulativePassCount++;

  // tight iso
  n = i = 0;
  for (const auto &tau : taus) {
    if (tau.isTauIDAvailable ("byTightCombinedIsolationDeltaBetaCorr3Hits")) {
      if (tau.tauID ("byTightCombinedIsolationDeltaBetaCorr3Hits") > 0.5) {
        n++;
      }
      else tauPasses[i] = false;
      i++;
    }
    else if (tau.isTauIDAvailable ("byTightIsolationMVArun2v1DBoldDMwLT")) {
      if (tau.tauID ("byTightIsolationMVArun2v1DBoldDMwLT") > 0.5) {
        n++;
      }
      else tauPasses[i] = false;
      i++;
    }
  }
  if(n > 0) cutResults_->at (5).accumulativePassCount++;
  if((decision = decision && count(tauPasses.begin(), tauPasses.end(), true) > 0)) cutResults_->at (5).cumulativePassCount++;

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
