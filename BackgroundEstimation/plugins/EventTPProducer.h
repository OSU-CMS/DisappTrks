#ifndef EVENT_TAG_AND_PROBE_PRODUCER
#define EVENT_TAG_AND_PROBE_PRODUCER

#include <sstream>

#include "TLorentzVector.h"

#include "DataFormats/Math/interface/deltaPhi.h"
#include "DataFormats/Math/interface/deltaR.h"

#include "OSUT3Analysis/AnaTools/interface/EventVariableProducer.h"
#include "OSUT3Analysis/AnaTools/interface/DataFormat.h"
#include "OSUT3Analysis/AnaTools/interface/CommonUtils.h"
#include "OSUT3Analysis/Collections/interface/Electron.h"
#include "OSUT3Analysis/Collections/interface/Muon.h"
#include "OSUT3Analysis/Collections/interface/Tau.h"
#include "OSUT3Analysis/Collections/interface/DisappearingTrack.h"

template<class T, class... Args> class EventTPProducer : public EventVariableProducer
{
  public:
    EventTPProducer (const edm::ParameterSet &);
    ~EventTPProducer ();

  private:
    void AddVariables(const edm::Event &, const edm::EventSetup &);

    edm::EDGetTokenT<vector<T> > tokenTags_;
    edm::EDGetTokenT<vector<osu::Track> > tokenProbes_;
    edm::EDGetTokenT<vector<pat::Jet> > tokenJets_;
    edm::EDGetTokenT<vector<pat::PackedCandidate> > tokenPFCands_;
    edm::EDGetTokenT<edm::TriggerResults> tokenTriggerBits_;
    edm::EDGetTokenT<vector<pat::TriggerObjectStandAlone> > tokenTriggerObjs_;

    bool doFilter_;
    bool doLooseFilter_;
    bool doSSFilter_;
    bool doLooseSSFilter_;
    bool doJetFilter_;
    
    string triggerCollectionName_;
    string triggerFilterName_;
    double triggerMatchingDR_;

    double probeTagMatchingDR_;

    const string tagCollectionParameter () const;
    bool goodInvMass (const T &, const osu::Track &, double &) const;
    bool goodInvMass (const T &, const pat::Jet &, double &) const;
    bool goodInvMass (const T &, const pat::PackedCandidate &, double &) const;
    bool passesVeto (const osu::Track &) const;
    bool passesLooseVeto (const osu::Track &) const;
    bool firesTrigger (const edm::Event &, const vector<pat::TriggerObjectStandAlone> &, const edm::TriggerResults &, const osu::Track &) const;
    template<class T0> bool matchedToTag (const osu::Track &, const vector<T0> &) const;
    template<class T0> const double getTrackIsolation (const T0 &, const vector<T0> &, const double, const double = 1.0e-12) const;
    bool jetMatchedToMuon (const pat::Jet &, const vector<pat::PackedCandidate> &) const;
};

typedef EventTPProducer<osu::Electron> EventElectronTPProducer;
typedef EventTPProducer<osu::Muon> EventMuonTPProducer;
typedef EventTPProducer<osu::Electron, osu::Tau> EventTauToElectronTPProducer;
typedef EventTPProducer<osu::Muon, osu::Tau> EventTauToMuonTPProducer;

#endif
