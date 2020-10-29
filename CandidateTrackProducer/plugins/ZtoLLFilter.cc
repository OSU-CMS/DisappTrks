#include "TLorentzVector.h"

#include "OSUT3Analysis/AnaTools/interface/CommonUtils.h"
#include "DisappTrks/CandidateTrackProducer/plugins/ZToLLFilter.h"

template<Flavor T>
ZToLLFilter<T>::ZToLLFilter (const edm::ParameterSet& iConfig) :
  triggers_   (iConfig.getParameter<edm::InputTag> ("triggers")),
  vertices_   (iConfig.getParameter<edm::InputTag> ("vertices")),
  electrons_  (iConfig.getParameter<edm::InputTag> ("electrons")),
  muons_      (iConfig.getParameter<edm::InputTag> ("muons")),
  triggerNames_     (iConfig.getParameter<vector<string> > ("triggerNames")),
  dataTakingPeriod_ (iConfig.getParameter<string> ("dataTakingPeriod"))
{
  assert(dataTakingPeriod_ == "2017" || dataTakingPeriod_ == "2018");

  is2017_ = (dataTakingPeriod_ == "2017");

  triggersToken_  = consumes<edm::TriggerResults> (triggers_);
  verticesToken_  = consumes<vector<reco::Vertex> > (vertices_);
  electronsToken_ = consumes<vector<pat::Electron> > (electrons_);
  muonsToken_     = consumes<vector<pat::Muon> > (muons_);
}

template<Flavor T>
ZToLLFilter<T>::~ZToLLFilter ()
{
}

template<Flavor T> bool
ZToLLFilter<T>::filter (edm::Event &event, const edm::EventSetup &setup)
{
  edm::Handle<edm::TriggerResults> triggers;
  event.getByToken(triggersToken_, triggers);

  edm::Handle<vector<reco::Vertex> > vertices;
  event.getByToken(verticesToken_, vertices);

  edm::Handle<vector<pat::Electron> > electrons;
  event.getByToken(electronsToken_, electrons);

  edm::Handle<vector<pat::Muon> > muons;
  event.getByToken(muonsToken_, muons);

  //////////////////////////////

  if(!passesTrigger(event, *triggers)) return false;

  vector<pat::Electron> selectedElectrons;
  vector<pat::Muon> selectedMuons;

  selectLeptons(event, vertices->at(0), *electrons, *muons, selectedElectrons, selectedMuons);

  return filterDecision(selectedElectrons, selectedMuons);
}

template<Flavor T> bool
ZToLLFilter<T>::passesTrigger (const edm::Event &event, const edm::TriggerResults &triggers) const
{
  bool triggerDecision = triggerNames_.empty() ? true : false;
  const edm::TriggerNames &triggerNames = event.triggerNames (triggers);

  for (unsigned i = 0; i < triggerNames.size (); i++)
    {
      string name = triggerNames.triggerName (i);
      bool pass = triggers.accept (i);
      for (const auto &trigger : triggerNames_)
        {
          if (name.find (trigger) == 0)
            triggerDecision = triggerDecision || pass;
        }
    }

  return triggerDecision;
}

template<Flavor T> void
ZToLLFilter<T>::selectLeptons(const edm::Event &event,
                              const reco::Vertex &vertex,
                              const vector<pat::Electron> &electrons,
                              const vector<pat::Muon> &muons,
                              vector<pat::Electron> &selectedElectrons,
                              vector<pat::Muon> &selectedMuons)
{
  return;
}

template<> void
ZToLLFilter<ELECTRON>::selectLeptons(const edm::Event &event,
                                     const reco::Vertex &vertex,
                                     const vector<pat::Electron> &electrons,
                                     const vector<pat::Muon> &muons,
                                     vector<pat::Electron> &selectedElectrons,
                                     vector<pat::Muon> &selectedMuons)
{
  for(const auto &electron : electrons) {
    if(electron.pt() <= 25) continue;
    if(fabs(electron.eta()) >= 2.1) continue;
    if(!electron.electronID(is2017_ ? "cutBasedElectronID-Fall17-94X-V1-tight" : "cutBasedElectronID-Fall17-94X-V2-tight")) continue;
    
    if(fabs(electron.superCluster()->eta()) <= 1.479) {
      if(fabs(electron.gsfTrack()->dxy(vertex.position())) >= 0.05) continue;
      if(fabs(electron.gsfTrack()->dz(vertex.position())) >= 0.10) continue;
    }
    else {
      if(fabs(electron.gsfTrack()->dxy(vertex.position())) >= 0.10) continue;
      if(fabs(electron.gsfTrack()->dz(vertex.position())) >= 0.20) continue;
    }

    selectedElectrons.push_back(electron);
  }
}

template<> void
ZToLLFilter<MUON>::selectLeptons(const edm::Event &event,
                                 const reco::Vertex &vertex,
                                 const vector<pat::Electron> &electrons,
                                 const vector<pat::Muon> &muons,
                                 vector<pat::Electron> &selectedElectrons,
                                 vector<pat::Muon> &selectedMuons)
{
  for(const auto &muon : muons) {
    if(muon.pt() <= (is2017_ ? 29 : 26)) continue;
    if(fabs(muon.eta()) >= 2.1) continue;
    if(!muon.isTightMuon(vertex)) continue;

    double muIso = muon.pfIsolationR04().sumChargedHadronPt;
    muIso += max(0.0, muon.pfIsolationR04().sumNeutralHadronEt + muon.pfIsolationR04().sumPhotonEt - 0.5 * muon.pfIsolationR04().sumPUPt);
    if(muIso / muon.pt() >= 0.15) continue;

    selectedMuons.push_back(muon);
  }
}

template<Flavor T> bool
ZToLLFilter<T>::filterDecision(const vector<pat::Electron> selectedElectrons,
                               const vector<pat::Muon> selectedMuons) const
{
  return true;
}

template<> bool
ZToLLFilter<ELECTRON>::filterDecision(const vector<pat::Electron> selectedElectrons,
                                      const vector<pat::Muon> selectedMuons) const
{
  if(selectedElectrons.size() != 2) return false;

  double energy = selectedElectrons[0].energy() + selectedElectrons[1].energy();
  double px = selectedElectrons[0].px() + selectedElectrons[1].px();
  double py = selectedElectrons[0].py() + selectedElectrons[1].py();
  double pz = selectedElectrons[0].pz() + selectedElectrons[1].pz();

  double invmass = sqrt(energy*energy - px*px - py*py - pz*pz);
  if(fabs(invmass - 91.1876) >= 10.0) return false;
  if(selectedElectrons[0].charge() * selectedElectrons[1].charge() >= 0) return false;

  return true;
}

template<> bool
ZToLLFilter<MUON>::filterDecision(const vector<pat::Electron> selectedElectrons,
                                  const vector<pat::Muon> selectedMuons) const
{
  if(selectedMuons.size() != 2) return false;

  double energy = selectedMuons[0].energy() + selectedMuons[1].energy();
  double px = selectedMuons[0].px() + selectedMuons[1].px();
  double py = selectedMuons[0].py() + selectedMuons[1].py();
  double pz = selectedMuons[0].pz() + selectedMuons[1].pz();

  double invmass = sqrt(energy*energy - px*px - py*py - pz*pz);
  if(fabs(invmass - 91.1876) >= 10.0) return false;
  if(selectedMuons[0].charge() * selectedMuons[1].charge() >= 0) return false;

  return true;
}

typedef ZToLLFilter<ELECTRON> ZToEEFilter;
typedef ZToLLFilter<MUON>     ZToMuMuFilter;

DEFINE_FWK_MODULE (ZToEEFilter);
DEFINE_FWK_MODULE (ZToMuMuFilter);
