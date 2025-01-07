#include "DisappTrks/ToyModels/plugins/ParticleGunVarProducer.h"

#define M_Z (91.1876)

template<class T, class... Args>
ParticleGunVarProducer<T, Args...>::ParticleGunVarProducer (const edm::ParameterSet &cfg) :
  EventVariableProducer(cfg)
{
  tokenProbes_ = consumes<vector<T> > (collections_.getParameter<edm::InputTag> (tagCollectionParameter ()));
  tokenMuons_ = consumes<vector<TYPE(muons)> > (collections_.getParameter<edm::InputTag> ("muons"));
  genParticlesToken_ = consumes<vector<reco::GenParticle> > (collections_.getParameter<edm::InputTag> ("hardInteractionMcparticles"));
}

template<class T, class... Args>
ParticleGunVarProducer<T, Args...>::~ParticleGunVarProducer ()
{
}

template<class T, class... Args> void
ParticleGunVarProducer<T, Args...>::AddVariables (const edm::Event &event, const edm::EventSetup &setup)
{
  edm::Handle<vector<T> > probes;
  event.getByToken (tokenProbes_, probes);

  edm::Handle<vector<TYPE(muons)> > muons;
  event.getByToken (tokenMuons_, muons);


  edm::Handle<vector<reco::GenParticle> > genParticles;
  event.getByToken (genParticlesToken_, genParticles);

//  std::cout << "Valid probes:"  << probes.isValid ()  << std::endl;
  if ( !probes.isValid () || !genParticles.isValid())
    return;

 // TYPE(tracks) CharginoTrack;

  reco::GenParticle  chargino_truth;
  reco::GenParticle  muon_truth;
  double  dR = 999;
  double  dEta = 999;
  double  dPhi = 999;
  double  dP = 999;
  double  rP = 999;
  double  NLnrP = 999;
  double  dPt = 999;
  double  rPt = 999;
  double  NLnrPt = 999;
  double  dAngle = 999;
  bool    isLeptonVeto = false;
  bool    isOuterHitsVeto = false;
  bool    charginoflag = false;
  bool    GenCharginoFlag = false;
  bool    GenMuonFlag = false;
  // Get truth particles 
  TVector3 v_chargino,v_muon,displacement,pos_chargino,pos_muon;
  for (const auto &genParticle : *genParticles)
    {
      if (abs(genParticle.pdgId()) == 1000024){
        chargino_truth = genParticle;
	GenCharginoFlag = true;
      }
      if (abs(genParticle.pdgId()) == 13     ){
	muon_truth = genParticle;
	GenMuonFlag = true;
      }
    }
  // End of truth particles

  if( GenCharginoFlag == false ||  GenMuonFlag == false ) 
    return;

  // Calcualting deflecting angle
  v_chargino.SetPtEtaPhi(chargino_truth.pt(), chargino_truth.eta(), chargino_truth.phi());
  v_muon.SetPtEtaPhi(muon_truth.pt(), muon_truth.eta(), muon_truth.phi());

  pos_chargino.SetXYZ( chargino_truth.vx(),chargino_truth.vy(),chargino_truth.vz() );
  pos_muon.SetXYZ( muon_truth.vx(),muon_truth.vy(),muon_truth.vz() );
  displacement = pos_chargino-pos_muon;
  
  //// Correction of incoming momentum to vertex
  double rho = chargino_truth.pt()/(0.3*3.8)*100;
  double rotation_angle = 2*TMath::ASin( (displacement.Mag()/2.0)/rho);
  v_chargino.RotateZ(-chargino_truth.charge()*rotation_angle);

  dR = v_chargino.DeltaR(v_muon);
  dEta = v_chargino.Eta()-v_muon.Eta();
  dPhi = v_chargino.DeltaPhi(v_muon);
  dP = v_chargino.Mag()-v_muon.Mag();
  rP = v_muon.Mag()/v_chargino.Mag();
  NLnrP = -log(v_muon.Mag()/v_chargino.Mag());
  dPt = v_chargino.Pt()-v_muon.Pt();
  rPt = v_muon.Pt()/v_chargino.Pt();
  NLnrPt = -log(v_muon.Pt()/v_chargino.Pt());
  dAngle = v_chargino.Angle(v_muon);
  //std::cout << "dP "  << dP  <<  ";" << " dAngle " << dAngle << ";" << "dR "  << dR << std::endl;
  // End of calculation deflection  

  for (const auto &probe : *probes)
    {
//      cout <<"promptOrTauDecay PdgId:" <<probe.genMatchedParticle().promptOrTauDecayPdgId <<endl;
//     if( probe.genMatchedParticle().promptOrTauDecayPdgId == 1000024 ){
#if DATA_FORMAT_IS_CUSTOM && DATA_FORMAT_IS_2022
     if( probe.dxy() < 10.0 ){
#elif DATA_FORMAT_IS_CUSTOM
     if( probe.d0() < 10.0 ){
#else
      if( probe.dxy() < 10.0 ){
#endif
        isLeptonVeto = passesVeto(probe);
        isOuterHitsVeto = passesOuterHits(probe);
	if( isLeptonVeto == false ){
	  //std::cout << "Pt "  << chargino_truth.pt()  <<  ";" << " eta:  " << chargino_truth.eta() << ";" << "phi: "  <<  chargino_truth.phi() << std::endl;	  
	}
        charginoflag = true;
    //    std::cout <<  "Passing lepton veto: "  << isLeptonVeto << std::endl;
      } 
    }
  
  // Store global Vertex variables
  (*eventvariables)["DeltaR"]     = dR;
  (*eventvariables)["DeltaEta"]   = dEta;
  (*eventvariables)["DeltaPhi"]   = dPhi;
  (*eventvariables)["DeltaP"]     = dP;
  (*eventvariables)["RatioP"]     = rP;
  (*eventvariables)["NLnRatioP"]  = NLnrP;
  (*eventvariables)["DeltaPt"]     = dPt;
  (*eventvariables)["RatioPt"]     = rPt;
  (*eventvariables)["NLnRatioPt"]  = NLnrPt;
  (*eventvariables)["DeltaAngle"] = dAngle;
  (*eventvariables)["passesVeto"] = isLeptonVeto;
  (*eventvariables)["passesOuterHits"] = isOuterHitsVeto;
  (*eventvariables)["MissOuterDeltaR"]     = (isOuterHitsVeto && charginoflag)?dR:-999;
  (*eventvariables)["MissOuterDeltaEta"]   = (isOuterHitsVeto && charginoflag)?dEta:-999;
  (*eventvariables)["MissOuterDeltaPhi"]   = (isOuterHitsVeto && charginoflag)?dPhi:-999;
  (*eventvariables)["MissOuterDeltaP"]     = (isOuterHitsVeto && charginoflag)?dP:-999;
  (*eventvariables)["MissOuterRatioP"]     = (isOuterHitsVeto && charginoflag)?rP:-999;
  (*eventvariables)["MissOuterNLnRatioP"]  = (isOuterHitsVeto && charginoflag)?NLnrP:-999;
  (*eventvariables)["MissOuterDeltaPt"]    = (isOuterHitsVeto && charginoflag)?dPt:-999;
  (*eventvariables)["MissOuterRatioPt"]     = (isOuterHitsVeto && charginoflag)?rPt:-999;
  (*eventvariables)["MissOuterNLnRatioPt"]  = (isOuterHitsVeto && charginoflag)?NLnrPt:-999;
  (*eventvariables)["MissOuterDeltaAngle"] = (isOuterHitsVeto && charginoflag)?dAngle:-999;
  (*eventvariables)["DisTrkDeltaR"]     = (isLeptonVeto && charginoflag)?dR:-999;
  (*eventvariables)["DisTrkDeltaEta"]   = (isLeptonVeto && charginoflag)?dEta:-999;
  (*eventvariables)["DisTrkDeltaPhi"]   = (isLeptonVeto && charginoflag)?dPhi:-999;
  (*eventvariables)["DisTrkDeltaP"]     = (isLeptonVeto && charginoflag)?dP:-999;
  (*eventvariables)["DisTrkRatioP"]     = (isLeptonVeto && charginoflag)?rP:-999;
  (*eventvariables)["DisTrkNLnRatioP"]  = (isLeptonVeto && charginoflag)?NLnrP:-999;
  (*eventvariables)["DisTrkDeltaPt"]    = (isLeptonVeto && charginoflag)?dPt:-999;
  (*eventvariables)["DisTrkRatioPt"]    = (isLeptonVeto && charginoflag)?rPt:-999;
  (*eventvariables)["DisTrkNLnRatioPt"] = (isLeptonVeto && charginoflag)?NLnrPt:-999;
  (*eventvariables)["DisTrkDeltaAngle"] = (isLeptonVeto && charginoflag)?dAngle:-999;
  
  (*eventvariables)["DecayVtxRho"] = TMath::Sqrt( muon_truth.vx()*muon_truth.vx()+muon_truth.vy()*muon_truth.vy() );
  (*eventvariables)["DecayVtxZ"]   = muon_truth.vz();
  (*eventvariables)["GenTrkEta"]   = chargino_truth.eta();
  (*eventvariables)["GenTrkPt"]    = chargino_truth.pt();
  (*eventvariables)["GenTrkP"]     = v_chargino.Mag();
  (*eventvariables)["GenTrkMu"]     = v_muon.Mag();
  (*eventvariables)["MissOuterGenTrkMu"]   = (isOuterHitsVeto && charginoflag)?v_muon.Mag():-999;
  (*eventvariables)["DisTrkGenTrkMu"]     = (isLeptonVeto && charginoflag)?v_muon.Mag():-999;
  
}


template<> const string
ParticleGunVarProducer<osu::Track,TYPE(muons)>::tagCollectionParameter () const
{
  return "tracks";
}


template<class T, class... Args> bool
ParticleGunVarProducer<T, Args...>::passesVeto (const osu::Track &probe) const
{
  return false;
}

/*template<> bool
ParticleGunVarProducer<osu::Track, osu::Electron>::passesVeto (const osu::Track &probe) const
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
template<> bool
ParticleGunVarProducer<osu::Track,TYPE(muons)>::passesVeto (const osu::Track &probe) const
{
#if DATA_FORMAT == MINI_AOD_2017
  bool passes = probe.deltaRToClosestPFMuon () > 0.15
             && probe.hitAndTOBDrop_bestTrackMissingOuterHits () >= 3.0;
#elif DATA_FORMAT == MINI_AOD_2022_CUSTOM || DATA_FORMAT == MINI_AOD_ONLY_2022_CUSTOM
  bool passes = probe.deltaRToClosestMuon () > 0.15
             && probe.hitAndTOBDrop_bestTrackMissingOuterHits () >= 3.0;
#else
  bool passes = probe.deltaRToClosestMuon () > 0.15
             && probe.hitAndTOBDrop_bestTrackMissingOuterHits () >= 3.0;          
#endif

  return passes;
//    return true;
}

template<> bool
ParticleGunVarProducer<osu::Track,TYPE(muons)>::passesOuterHits (const osu::Track &probe) const
{
#if DATA_FORMAT == MINI_AOD_2017
  bool passes = probe.hitAndTOBDrop_bestTrackMissingOuterHits () >= 3.0;
#else
  bool passes = probe.hitAndTOBDrop_bestTrackMissingOuterHits () >= 3.0;          
#endif

  return passes;
//    return true;
}

template<class T, class... Args> template<class T0> const double
ParticleGunVarProducer<T, Args...>::getTrackIsolation (const T0 &track, const vector<T0> &tracks, const double outerDeltaR, const double innerDeltaR) const
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

template<class T, class... Args> bool
ParticleGunVarProducer<T, Args...>::jetMatchedToMuon (const pat::Jet &jet, const vector<pat::PackedCandidate> &pfCands) const
{
  for (const auto &pfCand : pfCands)
    {
      if (abs (pfCand.pdgId ()) != 13)
        continue;
      if (deltaR (jet, pfCand) < 0.4)
        return true;
    }
  return false;
}

#include "FWCore/Framework/interface/MakerMacros.h"
DEFINE_FWK_MODULE(ParticleGunMuonVarProducer);
