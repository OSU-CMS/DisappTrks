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
#include "OSUT3Analysis/Collections/interface/Track.h"

template<class T, class... Args> class EventTPProducer : public EventVariableProducer
{
  public:
    EventTPProducer (const edm::ParameterSet &);
    ~EventTPProducer ();

  private:
    void AddVariables(const edm::Event &);
    edm::EDGetTokenT<vector<T> > tokenTags_;
    edm::EDGetTokenT<vector<osu::Track> > tokenProbes_;
    edm::EDGetTokenT<vector<osu::Jet> > tokenJets_;
    edm::EDGetTokenT<vector<pat::PackedCandidate> > tokenPFCands_;
    bool doFilter_;
    bool doSSFilter_;

    const string tagCollectionParameter () const;
    bool goodInvMass (const T &, const osu::Track &, double &) const;
    bool goodInvMass (const T &, const osu::Jet &, double &) const;
    bool goodInvMass (const T &, const pat::PackedCandidate &, double &) const;
    bool passesVeto (const osu::Track &) const;
    template<class T0> const double getTrackIsolation (const T0 &, const vector<T0> &, const double, const double = 1.0e-12) const;
};

typedef EventTPProducer<osu::Electron> EventElectronTPProducer;
typedef EventTPProducer<osu::Muon> EventMuonTPProducer;
typedef EventTPProducer<osu::Electron, osu::Tau> EventTauToElectronTPProducer;
typedef EventTPProducer<osu::Muon, osu::Tau> EventTauToMuonTPProducer;

#endif
