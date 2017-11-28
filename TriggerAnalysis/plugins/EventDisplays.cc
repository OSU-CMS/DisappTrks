#include "DisappTrks/TriggerAnalysis/plugins/EventDisplays.h"

EventDisplays::EventDisplays (const edm::ParameterSet &cfg) :
  mets_          (cfg.getParameter<edm::InputTag>  ("mets")),
  caloMETs_      (cfg.getParameter<edm::InputTag>  ("caloMETs")),
  muons_         (cfg.getParameter<edm::InputTag>  ("muons")),
  genParticles_  (cfg.getParameter<edm::InputTag>  ("genParticles")),
  jets_          (cfg.getParameter<edm::InputTag>  ("jets"))
{
}

EventDisplays::~EventDisplays ()
{
}

bool
EventDisplays::filter (edm::Event &event, const edm::EventSetup &setup)
{
  edm::Handle<vector<reco::PFMET> > mets;
  event.getByLabel (mets_, mets);
  edm::Handle<vector<reco::CaloMET> > caloMETs;
  event.getByLabel (caloMETs_, caloMETs);
  edm::Handle<vector<reco::Muon> > muons;
  event.getByLabel (muons_, muons);
  /*edm::Handle<vector<reco::GenParticle> > genParticles;
  event.getByLabel (genParticles_, genParticles);
  edm::Handle<vector<reco::PFJet> > jets;
  event.getByLabel (jets_, jets);*/

  if (muons->empty ())
    return false;
  return true;
}

#include "FWCore/Framework/interface/MakerMacros.h"
DEFINE_FWK_MODULE(EventDisplays);
