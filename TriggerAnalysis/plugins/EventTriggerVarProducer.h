#ifndef EVENT_TRIGGER_VAR_PRODUCER
#define EVENT_TRIGGER_VAR_PRODUCER

#include "OSUT3Analysis/AnaTools/interface/EventVariableProducer.h"

#include "DataFormats/Math/interface/deltaR.h"

#include "OSUT3Analysis/AnaTools/interface/DataFormat.h"
#include "OSUT3Analysis/AnaTools/interface/CommonUtils.h"

class EventTriggerVarProducer : public EventVariableProducer {
public:
  EventTriggerVarProducer(const edm::ParameterSet &);
  ~EventTriggerVarProducer() {};

private:
  bool getHLTObj(const edm::TriggerNames &triggerNames,
                 const vector<pat::TriggerObjectStandAlone> &triggerObjs,
                 const string &collection,
                 pat::TriggerObjectStandAlone &obj) const;

  bool genMatched(const TYPE(tracks) &, const vector<reco::GenParticle> &, const int, const int, const double) const;
  bool genMatched(const pat::Muon &, const vector<reco::GenParticle> &, const int, const int, const double) const;

  bool isGoodTrack(const TYPE(tracks) &, const reco::Vertex &, const vector<TYPE(tracks)> &) const;
  bool isGoodTrack(const TYPE(tracks) &, const reco::Vertex &, const vector<TYPE(tracks)> &, const vector<reco::GenParticle> &) const;

  bool isGoodMuon(const pat::Muon &, const reco::Vertex &, const vector<pat::Muon> &) const;

  void AddVariables(const edm::Event &);

  edm::EDGetTokenT<vector<TYPE(jets)> > tokenJets_;
  edm::EDGetTokenT<vector<TYPE(tracks)> > tokenTracks_;
  edm::EDGetTokenT<vector<pat::Muon> > tokenMuons_;
  edm::EDGetTokenT<vector<reco::Vertex> > tokenVertices_;
  edm::EDGetTokenT<edm::TriggerResults> tokenTriggerBits_;
  edm::EDGetTokenT<vector<pat::TriggerObjectStandAlone> > tokenTriggerObjs_;
  edm::EDGetTokenT<vector<reco::GenParticle> > tokenGenParticles_;

  std::vector<string> triggerNames;
  std::map<string, bool> triggerFires;

  std::vector<string> filterNames;
  std::map<string, bool> filterFires;

  std::vector<string> signalTriggerNames;
  bool signalGrandOrFires;
};

#endif
