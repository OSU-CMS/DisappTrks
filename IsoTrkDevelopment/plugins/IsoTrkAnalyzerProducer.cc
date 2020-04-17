#include "DisappTrks/IsoTrkDevelopment/plugins/IsoTrkAnalyzerProducer.h"
#include "DataFormats/Math/interface/deltaR.h"
#include "DataFormats/Math/interface/LorentzVector.h"

#include "TLorentzVector.h"

#define M_Z (91.1876)
#define CHARGINO (1000024)
template<class T, class... Args>
IsoTrkAnalyzerProducer<T, Args...>::IsoTrkAnalyzerProducer (const edm::ParameterSet &cfg) :
  EventVariableProducer(cfg)
{
  tokenProbes_ = consumes<vector<T> > (collections_.getParameter<edm::InputTag> (tagCollectionParameter ()));
  genParticlesToken_ = consumes<vector<reco::GenParticle> > (collections_.getParameter<edm::InputTag> ("hardInteractionMcparticles"));
}

template<class T, class... Args>
IsoTrkAnalyzerProducer<T, Args...>::~IsoTrkAnalyzerProducer ()
{
}

template<class T, class... Args> void
IsoTrkAnalyzerProducer<T, Args...>::AddVariables (const edm::Event &event)
{
  edm::Handle<vector<T> > probes;
  event.getByToken (tokenProbes_, probes);

  edm::Handle<vector<reco::GenParticle> > genParticles;
  event.getByToken (genParticlesToken_, genParticles);

 //  std::cout << "Valid probes:"  << probes.isValid ()  << std::endl;
  if ( !probes.isValid () || !genParticles.isValid())
    return;

  int nCharginoMatchedIsoTrk = 0;
  int nGenChargino = 0;

  vector<math::XYZTLorentzVector> matchedProbeLorentzVectors;
  vector<math::XYZTLorentzVector> genLorentzVectors;


  // Find Chargino matched IsolatedTrack
  for (const auto &probe : *probes){
    for (const auto &genParticle : *genParticles){
      if(abs(genParticle.pdgId()) == CHARGINO && genProbeMatched(probe,genParticle)){
        matchedProbeLorentzVectors.push_back(probe.p4());
        nCharginoMatchedIsoTrk++;
        break;
      }
    }
  }

  for (const auto &genParticle : *genParticles)
    {
      if (abs(genParticle.pdgId()) == CHARGINO){
        genLorentzVectors.push_back(genParticle.p4());
        nGenChargino++;
      }
    }
  // End of truth particles

  if( genLorentzVectors.size() == 0 ) 
    return;

  
  // Store probe/genParticle associated variables
  (*eventvariables)["nCharginoMatchedIsoTrk"] = nCharginoMatchedIsoTrk;
  (*eventvariables)["nGenChargino"]           = nGenChargino; 
  (*eventvariables)["MatchedProbeLeadingPt"]         = matchedProbeLorentzVectors.size() > 0 ? matchedProbeLorentzVectors.at(0).Pt() : -1.0;
  (*eventvariables)["GenCharginoLeadingPt"]   = genLorentzVectors.size() > 0 ? genLorentzVectors.at(0).Pt() : -1.0;
}


template<> const string
IsoTrkAnalyzerProducer<osu::Track,reco::GenParticle>::tagCollectionParameter () const
{
  return "tracks";
}

template<class T, class... Args> bool
IsoTrkAnalyzerProducer< T, Args...>::genProbeMatched (const osu::Track &probe, const reco::GenParticle &genParticle) const
{
  double dR = deltaR(probe, genParticle);
  if (dR < 0.01) { return true; }
  return false;
}

/*
template<class T, class... Args> bool
IsoTrkAnalyzerProducer<T, Args...>::passesVeto (const osu::Track &probe) const
{
  return false;
}
*/

/*template<> bool
IsoTrkAnalyzerProducer<osu::Track, osu::Electron>::passesVeto (const osu::Track &probe) const
{
#if DATA_FORMAT == MINI_AOD_2017
  bool passes = probe.deltaRToClosestPFElectron () > 0.15
             && (probe.matchedCaloJetEmEnergy() + probe.matchedCaloJetHadEnergy()) < 10.0
             && probe.hitAndTOBDrop_bestTrackMissingOuterHits () >= 3.0;
#else
  bool passes = probe.deltaRToClosestElectron () > 0.15
             && probe.caloNewNoPUDRp5CentralCalo () < 10.0
             && probe.hitAndTOBDrop_bestTrackMissingOuterHits () >= 3.0;
#endif

  return passes;
}
*/


#include "FWCore/Framework/interface/MakerMacros.h"
DEFINE_FWK_MODULE(GenMatchedTrackProducer);
