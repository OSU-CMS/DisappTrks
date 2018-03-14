#include "DisappTrks/BackgroundEstimation/plugins/EventTPProducer.h"

#define M_Z (91.1876)

template<class T, class... Args>
EventTPProducer<T, Args...>::EventTPProducer (const edm::ParameterSet &cfg) :
  EventVariableProducer(cfg),
  doFilter_ (cfg.getParameter<bool> ("doFilter")),
  doSSFilter_ (cfg.getParameter<bool> ("doSSFilter"))
{
  tokenTags_ = consumes<vector<T> > (collections_.getParameter<edm::InputTag> (tagCollectionParameter ()));
  tokenProbes_ = consumes<vector<osu::Track> > (collections_.getParameter<edm::InputTag> ("tracks"));
  tokenJets_ = consumes<vector<pat::Jet> > (collections_.getParameter<edm::InputTag> ("jets"));
  tokenPFCands_ = consumes<vector<pat::PackedCandidate> > (collections_.getParameter<edm::InputTag> ("pfCandidates"));
}

template<class T, class... Args>
EventTPProducer<T, Args...>::~EventTPProducer ()
{
}

template<class T, class... Args> void
EventTPProducer<T, Args...>::AddVariables (const edm::Event &event)
{
  edm::Handle<vector<T> > tags;
  event.getByToken (tokenTags_, tags);

  edm::Handle<vector<osu::Track> > probes;
  event.getByToken (tokenProbes_, probes);

  edm::Handle<vector<pat::Jet> > jets;
  event.getByToken (tokenJets_, jets);

  edm::Handle<vector<pat::PackedCandidate> > pfCands;
  event.getByToken (tokenPFCands_, pfCands);

  if (!tags.isValid () || !probes.isValid ())
    return;

  unsigned nGoodTPPairs = 0, nProbesPassingVeto = 0,
           nGoodTagJetPairs = 0, nGoodTagPFCHPairs = 0,
           nGoodSSTPPairs = 0, nSSProbesPassingVeto = 0;
  vector<double> masses,
                 tagJetMasses, jetChargedHadronEnergyFractions, jetNeutralHadronEnergyFractions,
                 tagPFCHMasses, pfchRelIsos;
  vector<int> chargeProducts;
  for (const auto &tag : *tags)
    {
      for (const auto &probe : *probes)
        {
          double mass = 0.0;
          bool isGoodInvMass = goodInvMass (tag, probe, mass),
               isGoodTPPair = isGoodInvMass && (tag.charge () * probe.charge () < 0.0),
               isGoodSSTPPair = isGoodInvMass && (tag.charge () * probe.charge () > 0.0),
               isProbePassingVeto = passesVeto (probe);

          isGoodTPPair && nGoodTPPairs++;
          (isGoodTPPair && isProbePassingVeto) && nProbesPassingVeto++;

          isGoodSSTPPair && nGoodSSTPPairs++;
          (isGoodSSTPPair && isProbePassingVeto) && nSSProbesPassingVeto++;

          if (isGoodTPPair || isGoodSSTPPair)
            {
              masses.push_back (mass);
              chargeProducts.push_back (tag.charge () * probe.charge ());
            }
        }

      if (jets.isValid ())
        {
          for (const auto &probe : *jets)
            {
              double mass = 0.0;
              bool isGoodInvMass = goodInvMass (tag, probe, mass);

              isGoodInvMass && nGoodTagJetPairs++;

              if (isGoodInvMass)
                {
                  tagJetMasses.push_back (mass);
                  jetChargedHadronEnergyFractions.push_back (probe.chargedHadronEnergyFraction ());
                  jetNeutralHadronEnergyFractions.push_back (probe.neutralHadronEnergyFraction ());
                }
            }
        }

      if (pfCands.isValid ())
        {
          for (const auto &probe : *pfCands)
            {
              if (probe.charge () == 0 || abs (probe.pdgId ()) < 100.0)
                continue;
              double mass = 0.0,
                     relIso = getTrackIsolation (probe, *pfCands, 0.3) / probe.pt ();
              bool isGoodInvMass = goodInvMass (tag, probe, mass),
                   isGoodRelIso = (relIso < 0.05);

              (isGoodInvMass && isGoodRelIso) && nGoodTagPFCHPairs++;

              if (isGoodInvMass && isGoodRelIso)
                {
                  tagPFCHMasses.push_back (mass);
                  pfchRelIsos.push_back (relIso);
                }
            }
        }
    }

  (*eventvariables)["nGoodTPPairs"] = nGoodTPPairs;
  (*eventvariables)["nProbesPassingVeto"] = nProbesPassingVeto;

  (*eventvariables)["nGoodSSTPPairs"] = nGoodSSTPPairs;
  (*eventvariables)["nSSProbesPassingVeto"] = nSSProbesPassingVeto;

  (*eventvariables)["nGoodTagJetPairs"] = nGoodTagJetPairs;
  (*eventvariables)["nGoodTagPFCHPairs"] = nGoodTagPFCHPairs;

  for (unsigned i = 0; i < 10; i++)
    {
      stringstream ss;

      ss.str ("");
      ss << i;
      (*eventvariables)["tagProbeMass_" + ss.str ()] = (masses.size () > i ? masses.at (i) : INVALID_VALUE);
      (*eventvariables)["tagProbeChargeProduct_" + ss.str ()] = (chargeProducts.size () > i ? chargeProducts.at (i) : INVALID_VALUE);
      (*eventvariables)["tagJetMass_" + ss.str ()] = (tagJetMasses.size () > i ? tagJetMasses.at (i) : INVALID_VALUE);
      (*eventvariables)["jetChargedHadronEnergyFraction_" + ss.str ()] = (jetChargedHadronEnergyFractions.size () > i ? jetChargedHadronEnergyFractions.at (i) : INVALID_VALUE);
      (*eventvariables)["jetNeutralHadronEnergyFraction_" + ss.str ()] = (jetNeutralHadronEnergyFractions.size () > i ? jetNeutralHadronEnergyFractions.at (i) : INVALID_VALUE);
      (*eventvariables)["tagPFCHMass_" + ss.str ()] = (tagPFCHMasses.size () > i ? tagPFCHMasses.at (i) : INVALID_VALUE);
      (*eventvariables)["pfchRelIso_" + ss.str ()] = (pfchRelIsos.size () > i ? pfchRelIsos.at (i) : INVALID_VALUE);
    }

  if (doFilter_)
    (*eventvariables)["EventVariableProducerFilterDecision"] = (nProbesPassingVeto > 0);
  if (doSSFilter_)
    (*eventvariables)["EventVariableProducerFilterDecision"] = (nSSProbesPassingVeto > 0);
}

template<class T, class... Args> const string
EventTPProducer<T, Args...>::tagCollectionParameter () const
{
  return "";
}

template<> const string
EventTPProducer<osu::Electron>::tagCollectionParameter () const
{
  return "electrons";
}

template<> const string
EventTPProducer<osu::Muon>::tagCollectionParameter () const
{
  return "muons";
}

template<> const string
EventTPProducer<osu::Electron, osu::Tau>::tagCollectionParameter () const
{
  return "electrons";
}

template<> const string
EventTPProducer<osu::Muon, osu::Tau>::tagCollectionParameter () const
{
  return "muons";
}

template<class T, class... Args> bool
EventTPProducer<T, Args...>::goodInvMass (const T &tag, const osu::Track &probe, double &m) const
{
  return false;
}

template<> bool
EventTPProducer<osu::Electron>::goodInvMass (const osu::Electron &tag, const osu::Track &probe, double &m) const
{
  TLorentzVector t (tag.px (), tag.py (), tag.pz (), tag.energy ()),
                 p (probe.px (), probe.py (), probe.pz (), probe.energyOfElectron ());
  m = (t + p).M ();
  return (fabs (m - M_Z) < 10.0);
}

template<> bool
EventTPProducer<osu::Muon>::goodInvMass (const osu::Muon &tag, const osu::Track &probe, double &m) const
{
  TLorentzVector t (tag.px (), tag.py (), tag.pz (), tag.energy ()),
                 p (probe.px (), probe.py (), probe.pz (), probe.energyOfMuon ());
  m = (t + p).M ();
  return (fabs (m - M_Z) < 10.0);
}

template<> bool
EventTPProducer<osu::Electron, osu::Tau>::goodInvMass (const osu::Electron &tag, const osu::Track &probe, double &m) const
{
  TLorentzVector t (tag.px (), tag.py (), tag.pz (), tag.energy ()),
                 p (probe.px (), probe.py (), probe.pz (), probe.energyOfPion ());
  m = (t + p).M ();
  return (15.0 < (M_Z - m) && (M_Z - m) < 50.0);
}

template<> bool
EventTPProducer<osu::Muon, osu::Tau>::goodInvMass (const osu::Muon &tag, const osu::Track &probe, double &m) const
{
  TLorentzVector t (tag.px (), tag.py (), tag.pz (), tag.energy ()),
                 p (probe.px (), probe.py (), probe.pz (), probe.energyOfPion ());
  m = (t + p).M ();
  return (15.0 < (M_Z - m) && (M_Z - m) < 50.0);
}

template<class T, class... Args> bool
EventTPProducer<T, Args...>::goodInvMass (const T &tag, const pat::Jet &probe, double &m) const
{
  return false;
}

template<> bool
EventTPProducer<osu::Electron>::goodInvMass (const osu::Electron &tag, const pat::Jet &probe, double &m) const
{
  TLorentzVector t (tag.px (), tag.py (), tag.pz (), tag.energy ()),
                 p (probe.px (), probe.py (), probe.pz (), probe.energy ());
  m = (t + p).M ();
  return (fabs (m - M_Z) < 10.0);
}

template<> bool
EventTPProducer<osu::Muon>::goodInvMass (const osu::Muon &tag, const pat::Jet &probe, double &m) const
{
  TLorentzVector t (tag.px (), tag.py (), tag.pz (), tag.energy ()),
                 p (probe.px (), probe.py (), probe.pz (), probe.energy ());
  m = (t + p).M ();
  return (fabs (m - M_Z) < 10.0);
}

template<> bool
EventTPProducer<osu::Electron, osu::Tau>::goodInvMass (const osu::Electron &tag, const pat::Jet &probe, double &m) const
{
  TLorentzVector t (tag.px (), tag.py (), tag.pz (), tag.energy ()),
                 p (probe.px (), probe.py (), probe.pz (), probe.energy ());
  m = (t + p).M ();
  return (15.0 < (M_Z - m) && (M_Z - m) < 50.0);
}

template<> bool
EventTPProducer<osu::Muon, osu::Tau>::goodInvMass (const osu::Muon &tag, const pat::Jet &probe, double &m) const
{
  TLorentzVector t (tag.px (), tag.py (), tag.pz (), tag.energy ()),
                 p (probe.px (), probe.py (), probe.pz (), probe.energy ());
  m = (t + p).M ();
  return (15.0 < (M_Z - m) && (M_Z - m) < 50.0);
}

template<class T, class... Args> bool
EventTPProducer<T, Args...>::goodInvMass (const T &tag, const pat::PackedCandidate &probe, double &m) const
{
  return false;
}

template<> bool
EventTPProducer<osu::Electron>::goodInvMass (const osu::Electron &tag, const pat::PackedCandidate &probe, double &m) const
{
  TLorentzVector t (tag.px (), tag.py (), tag.pz (), tag.energy ()),
                 p (probe.px (), probe.py (), probe.pz (), probe.energy ());
  m = (t + p).M ();
  return (fabs (m - M_Z) < 10.0);
}

template<> bool
EventTPProducer<osu::Muon>::goodInvMass (const osu::Muon &tag, const pat::PackedCandidate &probe, double &m) const
{
  TLorentzVector t (tag.px (), tag.py (), tag.pz (), tag.energy ()),
                 p (probe.px (), probe.py (), probe.pz (), probe.energy ());
  m = (t + p).M ();
  return (fabs (m - M_Z) < 10.0);
}

template<> bool
EventTPProducer<osu::Electron, osu::Tau>::goodInvMass (const osu::Electron &tag, const pat::PackedCandidate &probe, double &m) const
{
  TLorentzVector t (tag.px (), tag.py (), tag.pz (), tag.energy ()),
                 p (probe.px (), probe.py (), probe.pz (), probe.energy ());
  m = (t + p).M ();
  return (15.0 < (M_Z - m) && (M_Z - m) < 50.0);
}

template<> bool
EventTPProducer<osu::Muon, osu::Tau>::goodInvMass (const osu::Muon &tag, const pat::PackedCandidate &probe, double &m) const
{
  TLorentzVector t (tag.px (), tag.py (), tag.pz (), tag.energy ()),
                 p (probe.px (), probe.py (), probe.pz (), probe.energy ());
  m = (t + p).M ();
  return (15.0 < (M_Z - m) && (M_Z - m) < 50.0);
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

template<class T, class... Args> template<class T0> const double
EventTPProducer<T, Args...>::getTrackIsolation (const T0 &track, const vector<T0> &tracks, const double outerDeltaR, const double innerDeltaR) const
{
  double sumPt = 0.0;

  for (const auto &t : tracks)
    {
      if (!t.charge ())
        continue;

      double dR = deltaR (track, t);
      if (dR < outerDeltaR && dR > innerDeltaR)
        sumPt += t.pt ();
    }

  return sumPt;
}

#include "FWCore/Framework/interface/MakerMacros.h"
DEFINE_FWK_MODULE(EventElectronTPProducer);
DEFINE_FWK_MODULE(EventMuonTPProducer);
DEFINE_FWK_MODULE(EventTauToElectronTPProducer);
DEFINE_FWK_MODULE(EventTauToMuonTPProducer);
