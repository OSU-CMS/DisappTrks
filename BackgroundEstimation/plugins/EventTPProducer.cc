#include "DisappTrks/BackgroundEstimation/plugins/EventTPProducer.h"

#define M_Z (91.1876)

template<class T, class... Args>
EventTPProducer<T, Args...>::EventTPProducer (const edm::ParameterSet &cfg) :
  EventVariableProducer(cfg)
{
  tokenTags_ = consumes<vector<T> > (collections_.getParameter<edm::InputTag> ("tags"));
  tokenProbes_ = consumes<vector<osu::Track> > (collections_.getParameter<edm::InputTag> ("probes"));
}

template<class T, class... Args>
EventTPProducer<T, Args...>::~EventTPProducer()
{}

template<class T, class... Args> void
EventTPProducer<T, Args...>::AddVariables (const edm::Event &event)
{
  edm::Handle<vector<T> > tags;
  event.getByToken (tokenTags_, tags);

  edm::Handle<vector<osu::Track> > probes;
  event.getByToken (tokenProbes_, probes);

  unsigned nGoodTPPairs = 0, nProbesPassingVeto = 0;
  for (const auto &tag : *tags)
    {
      for (const auto &probe : *probes)
        {
          bool isGoodTPPair = goodInvMass (tag, probe) && (tag.charge () * probe.charge () < 0.0),
               isProbePassingVeto = passesVeto (probe);

          isGoodTPPair && nGoodTPPairs++;
          (isGoodTPPair && isProbePassingVeto) && nProbesPassingVeto++;
        }
    }

  (*eventvariables)["nGoodTPPairs"] = nGoodTPPairs;
  (*eventvariables)["nProbesPassingVeto"] = nProbesPassingVeto;
}

template<class T, class... Args> bool
EventTPProducer<T, Args...>::goodInvMass (const T &tag, const osu::Track &probe) const
{
  return false;
}

template<> bool
EventTPProducer<osu::Electron>::goodInvMass (const osu::Electron &tag, const osu::Track &probe) const
{
  TLorentzVector t (tag.energy (), tag.px (), tag.py (), tag.pz ()),
                 p (probe.energyOfElectron (), probe.px (), probe.py (), probe.pz ());
  double m = (t + p).M ();
  return (fabs (m - M_Z) < 10.0);
}

template<> bool
EventTPProducer<osu::Muon>::goodInvMass (const osu::Muon &tag, const osu::Track &probe) const
{
  TLorentzVector t (tag.energy (), tag.px (), tag.py (), tag.pz ()),
                 p (probe.energyOfMuon (), probe.px (), probe.py (), probe.pz ());
  double m = (t + p).M ();
  return (fabs (m - M_Z) < 10.0);
}

template<> bool
EventTPProducer<osu::Electron, osu::Tau>::goodInvMass (const osu::Electron &tag, const osu::Track &probe) const
{
  TLorentzVector t (tag.energy (), tag.px (), tag.py (), tag.pz ()),
                 p (probe.energyOfPion (), probe.px (), probe.py (), probe.pz ());
  double m = (t + p).M ();
  return (15.0 < (m - M_Z) && (m - M_Z) < 50.0);
}

template<> bool
EventTPProducer<osu::Muon, osu::Tau>::goodInvMass (const osu::Muon &tag, const osu::Track &probe) const
{
  TLorentzVector t (tag.energy (), tag.px (), tag.py (), tag.pz ()),
                 p (probe.energyOfPion (), probe.px (), probe.py (), probe.pz ());
  double m = (t + p).M ();
  return (15.0 < (m - M_Z) && (m - M_Z) < 50.0);
}

template<class T, class... Args> bool
EventTPProducer<T, Args...>::passesVeto (const osu::Track &probe) const
{
  return false;
}

template<> bool
EventTPProducer<osu::Electron>::passesVeto (const osu::Track &probe) const
{
  bool passes = probe.deltaRToClosestElectron () > 0.15
             && probe.caloNewNoPUDRp5CentralCalo () < 10.0
             && probe.hitAndTOBDrop_bestTrackMissingOuterHits () >= 3.0;
  return passes;
}

template<> bool
EventTPProducer<osu::Muon>::passesVeto (const osu::Track &probe) const
{
  bool passes = probe.deltaRToClosestMuon () > 0.15
             && probe.hitAndTOBDrop_bestTrackMissingOuterHits () >= 3.0;
  return passes;
}

template<> bool
EventTPProducer<osu::Electron, osu::Tau>::passesVeto (const osu::Track &probe) const
{
  bool passes = probe.deltaRToClosestTauHad () > 0.15
             && probe.dRMinJet () > 0.5
             && probe.caloNewNoPUDRp5CentralCalo () < 10.0
             && probe.hitAndTOBDrop_bestTrackMissingOuterHits () >= 3.0;
  return passes;
}

template<> bool
EventTPProducer<osu::Muon, osu::Tau>::passesVeto (const osu::Track &probe) const
{
  bool passes = probe.deltaRToClosestTauHad () > 0.15
             && probe.dRMinJet () > 0.5
             && probe.caloNewNoPUDRp5CentralCalo () < 10.0
             && probe.hitAndTOBDrop_bestTrackMissingOuterHits () >= 3.0;
  return passes;
}

#include "FWCore/Framework/interface/MakerMacros.h"
DEFINE_FWK_MODULE(EventElectronTPProducer);
DEFINE_FWK_MODULE(EventMuonTPProducer);
DEFINE_FWK_MODULE(EventTauToElectronTPProducer);
DEFINE_FWK_MODULE(EventTauToMuonTPProducer);
