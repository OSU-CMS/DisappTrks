//////////////////////////////////////////////////////////
// This class has been automatically generated on
// Wed Jun 12 13:48:05 2013 by ROOT version 5.32/00
// from TTree BNTree_WToMuSimple/BNTree_WToMuSimple
// found on file: condor/condor_2013_06_06_BNTreeTest/ZZ/hist_0.root
//////////////////////////////////////////////////////////

#ifndef BNTree_h
#define BNTree_h

#include <TROOT.h>
#include <TChain.h>
#include <TFile.h>

// Header file for the classes stored in the TTree if any.

// Fixed size dimensions of array or collections stored in the TTree if any.

class BNTree {
public :
   TTree          *fChain;   //!pointer to the analyzed TTree or TChain
   Int_t           fCurrent; //!current Tree number in a TChain

   // Declaration of leaf types
   vector<float>   *events_weight;
   vector<float>   *events_pthat;
   vector<float>   *events_qScale;
   vector<float>   *events_alphaQCD;
   vector<float>   *events_alphaQED;
   vector<float>   *events_scalePDF;
   vector<float>   *events_x1;
   vector<float>   *events_x2;
   vector<float>   *events_xPDF1;
   vector<float>   *events_xPDF2;
   vector<float>   *events_BSx;
   vector<float>   *events_BSy;
   vector<float>   *events_BSz;
   vector<float>   *events_PVx;
   vector<float>   *events_PVy;
   vector<float>   *events_PVz;
   vector<float>   *events_bField;
   vector<float>   *events_instLumi;
   vector<float>   *events_bxLumi;
   vector<float>   *events_FilterOutScrapingFraction;
   vector<float>   *events_sumNVtx;
   vector<float>   *events_sumTrueNVtx;
   vector<float>   *events_nm1_true;
   vector<float>   *events_n0_true;
   vector<float>   *events_np1_true;
   vector<float>   *events_numTruePV;
   vector<float>   *events_Q2ScaleUpWgt;
   vector<float>   *events_Q2ScaleDownWgt;
   vector<float>   *events_rho_kt6PFJets;
   vector<float>   *events_rho_kt6PFJetsCentralChargedPileUp;
   vector<float>   *events_rho_kt6PFJetsCentralNeutral;
   vector<float>   *events_rho_kt6PFJetsCentralNeutralTight;
   vector<float>   *events_run;
   vector<float>   *events_lumi;
   vector<float>   *events_sample;
   vector<float>   *events_numPV;
   vector<float>   *events_W0decay;
   vector<float>   *events_W1decay;
   vector<float>   *events_Z0decay;
   vector<float>   *events_Z1decay;
   vector<float>   *events_H0decay;
   vector<float>   *events_H1decay;
   vector<float>   *events_hcalnoiseLoose;
   vector<float>   *events_hcalnoiseTight;
   vector<float>   *events_GoodVertex;
   vector<float>   *events_FilterOutScraping;
   vector<float>   *events_HBHENoiseFilter;
   vector<float>   *events_CSCLooseHaloId;
   vector<float>   *events_CSCTightHaloId;
   vector<float>   *events_EcalLooseHaloId;
   vector<float>   *events_EcalTightHaloId;
   vector<float>   *events_HcalLooseHaloId;
   vector<float>   *events_HcalTightHaloId;
   vector<float>   *events_GlobalLooseHaloId;
   vector<float>   *events_GlobalTightHaloId;
   vector<float>   *events_LooseId;
   vector<float>   *events_TightId;
   vector<float>   *events_numGenPV;
   vector<float>   *events_nm1;
   vector<float>   *events_n0;
   vector<float>   *events_np1;
   vector<float>   *events_id1;
   vector<float>   *events_id2;
   vector<float>   *events_evt;
   vector<float>   *events_puScaleFactor;
   vector<float>   *events_muonScaleFactor;
   vector<float>   *events_electronScaleFactor;
   vector<float>   *events_stopCTauScaleFactor;
   vector<float>   *muons_energy;
   vector<float>   *muons_et;
   vector<float>   *muons_pt;
   vector<float>   *muons_px;
   vector<float>   *muons_py;
   vector<float>   *muons_pz;
   vector<float>   *muons_phi;
   vector<float>   *muons_eta;
   vector<float>   *muons_theta;
   vector<float>   *muons_trackIso;
   vector<float>   *muons_ecalIso;
   vector<float>   *muons_hcalIso;
   vector<float>   *muons_caloIso;
   vector<float>   *muons_trackIsDR03;
   vector<float>   *muons_ecalIsoDR03;
   vector<float>   *muons_hcalIsoDR03;
   vector<float>   *muons_caloIsoDR03;
   vector<float>   *muons_trackVetoIsoDR03;
   vector<float>   *muons_ecalVetoIsoDR03;
   vector<float>   *muons_hcalVetoIsoDR03;
   vector<float>   *muons_caloVetoIsoDR03;
   vector<float>   *muons_trackIsoDR05;
   vector<float>   *muons_ecalIsoDR05;
   vector<float>   *muons_hcalIsoDR05;
   vector<float>   *muons_caloIsoDR05;
   vector<float>   *muons_trackVetoIsoDR05;
   vector<float>   *muons_ecalVetoIsoDR05;
   vector<float>   *muons_hcalVetoIsoDR05;
   vector<float>   *muons_caloVetoIsoDR05;
   vector<float>   *muons_hcalE;
   vector<float>   *muons_ecalE;
   vector<float>   *muons_genET;
   vector<float>   *muons_genPT;
   vector<float>   *muons_genPhi;
   vector<float>   *muons_genEta;
   vector<float>   *muons_genMotherET;
   vector<float>   *muons_genMotherPT;
   vector<float>   *muons_genMotherPhi;
   vector<float>   *muons_genMotherEta;
   vector<float>   *muons_vx;
   vector<float>   *muons_vy;
   vector<float>   *muons_vz;
   vector<float>   *muons_tkNormChi2;
   vector<float>   *muons_tkPT;
   vector<float>   *muons_tkEta;
   vector<float>   *muons_tkPhi;
   vector<float>   *muons_tkDZ;
   vector<float>   *muons_tkD0;
   vector<float>   *muons_tkD0bs;
   vector<float>   *muons_tkD0err;
   vector<float>   *muons_samNormChi2;
   vector<float>   *muons_samPT;
   vector<float>   *muons_samEta;
   vector<float>   *muons_samPhi;
   vector<float>   *muons_samDZ;
   vector<float>   *muons_samD0;
   vector<float>   *muons_samD0bs;
   vector<float>   *muons_samD0err;
   vector<float>   *muons_comNormChi2;
   vector<float>   *muons_comPT;
   vector<float>   *muons_comEta;
   vector<float>   *muons_comPhi;
   vector<float>   *muons_comDZ;
   vector<float>   *muons_comD0;
   vector<float>   *muons_comD0bs;
   vector<float>   *muons_comD0err;
   vector<float>   *muons_isolationR03emVetoEt;
   vector<float>   *muons_isolationR03hadVetoEt;
   vector<float>   *muons_normalizedChi2;
   vector<float>   *muons_dVzPVz;
   vector<float>   *muons_dB;
   vector<float>   *muons_ptErr;
   vector<float>   *muons_innerTrackNormChi2;
   vector<float>   *muons_correctedD0;
   vector<float>   *muons_correctedD0Vertex;
   vector<float>   *muons_correctedDZ;
   vector<float>   *muons_particleIso;
   vector<float>   *muons_chargedHadronIso;
   vector<float>   *muons_neutralHadronIso;
   vector<float>   *muons_photonIso;
   vector<float>   *muons_puChargedHadronIso;
   vector<float>   *muons_chargedHadronIsoDR03;
   vector<float>   *muons_neutralHadronIsoDR03;
   vector<float>   *muons_photonIsoDR03;
   vector<float>   *muons_puChargedHadronIsoDR03;
   vector<float>   *muons_chargedHadronIsoDR04;
   vector<float>   *muons_neutralHadronIsoDR04;
   vector<float>   *muons_photonIsoDR04;
   vector<float>   *muons_puChargedHadronIsoDR04;
   vector<float>   *muons_rhoPrime;
   vector<float>   *muons_AEffDr03;
   vector<float>   *muons_AEffDr04;
   vector<float>   *muons_pfIsoR03SumChargedHadronPt;
   vector<float>   *muons_pfIsoR03SumNeutralHadronEt;
   vector<float>   *muons_pfIsoR03SumPhotonEt;
   vector<float>   *muons_pfIsoR03SumPUPt;
   vector<float>   *muons_pfIsoR04SumChargedHadronPt;
   vector<float>   *muons_pfIsoR04SumNeutralHadronEt;
   vector<float>   *muons_pfIsoR04SumPhotonEt;
   vector<float>   *muons_pfIsoR04SumPUPt;
   vector<float>   *muons_IP;
   vector<float>   *muons_IPError;
   vector<float>   *muons_timeAtIpInOut;
   vector<float>   *muons_timeAtIpInOutErr;
   vector<float>   *muons_timeAtIpOutIn;
   vector<float>   *muons_timeAtIpOutInErr;
   vector<float>   *muons_ecal_time;
   vector<float>   *muons_hcal_time;
   vector<float>   *muons_ecal_timeError;
   vector<float>   *muons_hcal_timeError;
   vector<float>   *muons_energy_ecal;
   vector<float>   *muons_energy_hcal;
   vector<float>   *muons_e3x3_ecal;
   vector<float>   *muons_e3x3_hcal;
   vector<float>   *muons_energyMax_ecal;
   vector<float>   *muons_energyMax_hcal;
   vector<float>   *muons_charge;
   vector<float>   *muons_IDGMPTight;
   vector<float>   *muons_tkNumValidHits;
   vector<float>   *muons_tkCharge;
   vector<float>   *muons_samNumValidHits;
   vector<float>   *muons_samCharge;
   vector<float>   *muons_comNumValidHits;
   vector<float>   *muons_comCharge;
   vector<float>   *muons_genId;
   vector<float>   *muons_genCharge;
   vector<float>   *muons_genNumberOfMothers;
   vector<float>   *muons_genMotherId;
   vector<float>   *muons_genMotherCharge;
   vector<float>   *muons_genMother0Id;
   vector<float>   *muons_genMother1Id;
   vector<float>   *muons_genGrandMother00Id;
   vector<float>   *muons_genGrandMother01Id;
   vector<float>   *muons_genGrandMother10Id;
   vector<float>   *muons_genGrandMother11Id;
   vector<float>   *muons_isPFMuon;
   vector<float>   *muons_isGoodMuon_1StationTight;
   vector<float>   *muons_isGlobalMuon;
   vector<float>   *muons_isTrackerMuon;
   vector<float>   *muons_isStandAloneMuon;
   vector<float>   *muons_isGlobalMuonPromptTight;
   vector<float>   *muons_numberOfValidMuonHits;
   vector<float>   *muons_numberOfValidTrackerHits;
   vector<float>   *muons_numberOfLayersWithMeasurement;
   vector<float>   *muons_pixelLayersWithMeasurement;
   vector<float>   *muons_numberOfMatches;
   vector<float>   *muons_numberOfValidTrackerHitsInnerTrack;
   vector<float>   *muons_numberOfValidPixelHits;
   vector<float>   *muons_numberOfMatchedStations;
   vector<float>   *muons_time_ndof;
   vector<float>   *muons_correctedD0VertexErr;
   vector<float>   *muons_correctedD0VertexSig;
   vector<float>   *muons_detIso;
   vector<float>   *muons_relPFdBetaIso;
   vector<float>   *muons_relPFrhoIso;
   vector<float>   *muons_metMT;
   vector<float>   *muons_correctedD0VertexInEBPlus;
   vector<float>   *muons_correctedD0VertexOutEBPlus;
   vector<float>   *muons_correctedD0VertexEEPlus;
   vector<float>   *muons_correctedD0BeamspotInEBPlus;
   vector<float>   *muons_correctedD0BeamspotOutEBPlus;
   vector<float>   *muons_correctedD0BeamspotEEPlus;
   vector<float>   *muons_correctedD0VertexInEBMinus;
   vector<float>   *muons_correctedD0VertexOutEBMinus;
   vector<float>   *muons_correctedD0VertexEEMinus;
   vector<float>   *muons_correctedD0BeamspotInEBMinus;
   vector<float>   *muons_correctedD0BeamspotOutEBMinus;
   vector<float>   *muons_correctedD0BeamspotEEMinus;
   vector<float>   *muons_correctedD0VertexInEBPositiveCharge;
   vector<float>   *muons_correctedD0VertexOutEBPositiveCharge;
   vector<float>   *muons_correctedD0VertexEEPositiveCharge;
   vector<float>   *muons_correctedD0BeamspotInEBPositiveCharge;
   vector<float>   *muons_correctedD0BeamspotOutEBPositiveCharge;
   vector<float>   *muons_correctedD0BeamspotEEPositiveCharge;
   vector<float>   *muons_correctedD0VertexInEBNegativeCharge;
   vector<float>   *muons_correctedD0VertexOutEBNegativeCharge;
   vector<float>   *muons_correctedD0VertexEENegativeCharge;
   vector<float>   *muons_correctedD0BeamspotInEBNegativeCharge;
   vector<float>   *muons_correctedD0BeamspotOutEBNegativeCharge;
   vector<float>   *muons_correctedD0BeamspotEENegativeCharge;
   vector<float>   *muons_tightID;
   vector<float>   *muons_tightIDdisplaced;
   vector<float>   *muons_genDeltaRLowest;
   vector<float>   *muons_genMatchedPdgId;
   vector<float>   *muons_genMatchedId;
   vector<float>   *muons_genMatchedMotherId;
   vector<float>   *muons_genMatchedMotherIdReverse;
   vector<float>   *muons_genMatchedGrandmotherId;
   vector<float>   *muons_genMatchedGrandmotherIdReverse;
   vector<float>   *muons_pfMuonsFromVertex;
   vector<float>   *electrons_energy;
   vector<float>   *electrons_et;
   vector<float>   *electrons_gsfEt;
   vector<float>   *electrons_pt;
   vector<float>   *electrons_px;
   vector<float>   *electrons_py;
   vector<float>   *electrons_pz;
   vector<float>   *electrons_phi;
   vector<float>   *electrons_eta;
   vector<float>   *electrons_theta;
   vector<float>   *electrons_pIn;
   vector<float>   *electrons_pOut;
   vector<float>   *electrons_EscOverPin;
   vector<float>   *electrons_EseedOverPout;
   vector<float>   *electrons_hadOverEm;
   vector<float>   *electrons_trackIso;
   vector<float>   *electrons_ecalIso;
   vector<float>   *electrons_hcalIso;
   vector<float>   *electrons_caloIso;
   vector<float>   *electrons_trackIsoDR03;
   vector<float>   *electrons_ecalIsoDR03;
   vector<float>   *electrons_hcalIsoDR03;
   vector<float>   *electrons_hcalIsoDR03depth1;
   vector<float>   *electrons_hcalIsoDR03depth2;
   vector<float>   *electrons_caloIsoDR03;
   vector<float>   *electrons_trackIsoDR04;
   vector<float>   *electrons_ecalIsoDR04;
   vector<float>   *electrons_hcalIsoDR04;
   vector<float>   *electrons_hcalIsoDR04depth1;
   vector<float>   *electrons_hcalIsoDR04depth2;
   vector<float>   *electrons_caloIsoDR04;
   vector<float>   *electrons_fbrem;
   vector<float>   *electrons_absInvEMinusInvPin;
   vector<float>   *electrons_delPhiIn;
   vector<float>   *electrons_delEtaIn;
   vector<float>   *electrons_genET;
   vector<float>   *electrons_genPT;
   vector<float>   *electrons_genPhi;
   vector<float>   *electrons_genEta;
   vector<float>   *electrons_genMotherET;
   vector<float>   *electrons_genMotherPT;
   vector<float>   *electrons_genMotherPhi;
   vector<float>   *electrons_genMotherEta;
   vector<float>   *electrons_vx;
   vector<float>   *electrons_vy;
   vector<float>   *electrons_vz;
   vector<float>   *electrons_scEnergy;
   vector<float>   *electrons_scRawEnergy;
   vector<float>   *electrons_scSigmaEtaEta;
   vector<float>   *electrons_scSigmaIEtaIEta;
   vector<float>   *electrons_scE1x5;
   vector<float>   *electrons_scE2x5Max;
   vector<float>   *electrons_scE5x5;
   vector<float>   *electrons_scEt;
   vector<float>   *electrons_scEta;
   vector<float>   *electrons_scPhi;
   vector<float>   *electrons_scZ;
   vector<float>   *electrons_tkNormChi2;
   vector<float>   *electrons_tkPT;
   vector<float>   *electrons_tkEta;
   vector<float>   *electrons_tkPhi;
   vector<float>   *electrons_tkDZ;
   vector<float>   *electrons_tkD0;
   vector<float>   *electrons_tkD0bs;
   vector<float>   *electrons_tkD0err;
   vector<float>   *electrons_mva;
   vector<float>   *electrons_mvaTrigV0;
   vector<float>   *electrons_mvaNonTrigV0;
   vector<float>   *electrons_dist;
   vector<float>   *electrons_dcot;
   vector<float>   *electrons_convradius;
   vector<float>   *electrons_convPointX;
   vector<float>   *electrons_convPointY;
   vector<float>   *electrons_convPointZ;
   vector<float>   *electrons_eMax;
   vector<float>   *electrons_eLeft;
   vector<float>   *electrons_eRight;
   vector<float>   *electrons_eTop;
   vector<float>   *electrons_eBottom;
   vector<float>   *electrons_e3x3;
   vector<float>   *electrons_swissCross;
   vector<float>   *electrons_seedEnergy;
   vector<float>   *electrons_seedTime;
   vector<float>   *electrons_swissCrossNoI85;
   vector<float>   *electrons_swissCrossI85;
   vector<float>   *electrons_E2overE9NoI85;
   vector<float>   *electrons_E2overE9I85;
   vector<float>   *electrons_correctedD0;
   vector<float>   *electrons_correctedD0Vertex;
   vector<float>   *electrons_correctedDZ;
   vector<float>   *electrons_particleIso;
   vector<float>   *electrons_chargedHadronIso;
   vector<float>   *electrons_neutralHadronIso;
   vector<float>   *electrons_photonIso;
   vector<float>   *electrons_puChargedHadronIso;
   vector<float>   *electrons_chargedHadronIsoDR03;
   vector<float>   *electrons_neutralHadronIsoDR03;
   vector<float>   *electrons_photonIsoDR03;
   vector<float>   *electrons_puChargedHadronIsoDR03;
   vector<float>   *electrons_chargedHadronIsoDR04;
   vector<float>   *electrons_neutralHadronIsoDR04;
   vector<float>   *electrons_photonIsoDR04;
   vector<float>   *electrons_puChargedHadronIsoDR04;
   vector<float>   *electrons_rhoPrime;
   vector<float>   *electrons_AEffDr03;
   vector<float>   *electrons_AEffDr04;
   vector<float>   *electrons_IP;
   vector<float>   *electrons_IPError;
   vector<float>   *electrons_charge;
   vector<float>   *electrons_classification;
   vector<float>   *electrons_genId;
   vector<float>   *electrons_genCharge;
   vector<float>   *electrons_genNumberOfMothers;
   vector<float>   *electrons_genMotherId;
   vector<float>   *electrons_genMotherCharge;
   vector<float>   *electrons_genMother0Id;
   vector<float>   *electrons_genMother1Id;
   vector<float>   *electrons_genGrandMother00Id;
   vector<float>   *electrons_genGrandMother01Id;
   vector<float>   *electrons_genGrandMother10Id;
   vector<float>   *electrons_genGrandMother11Id;
   vector<float>   *electrons_numClusters;
   vector<float>   *electrons_tkNumValidHits;
   vector<float>   *electrons_tkCharge;
   vector<float>   *electrons_gsfCharge;
   vector<float>   *electrons_isEB;
   vector<float>   *electrons_isEE;
   vector<float>   *electrons_isGap;
   vector<float>   *electrons_isEBEEGap;
   vector<float>   *electrons_isEBGap;
   vector<float>   *electrons_isEEGap;
   vector<float>   *electrons_isEcalDriven;
   vector<float>   *electrons_isTrackerDriven;
   vector<float>   *electrons_numberOfLostHits;
   vector<float>   *electrons_numberOfExpectedInnerHits;
   vector<float>   *electrons_numberOfValidPixelHits;
   vector<float>   *electrons_numberOfValidPixelBarrelHits;
   vector<float>   *electrons_numberOfValidPixelEndcapHits;
   vector<float>   *electrons_isHEEP;
   vector<float>   *electrons_isHEEPnoEt;
   vector<float>   *electrons_seedRecoFlag;
   vector<float>   *electrons_eidRobustHighEnergy;
   vector<float>   *electrons_eidRobustLoose;
   vector<float>   *electrons_eidRobustTight;
   vector<float>   *electrons_eidLoose;
   vector<float>   *electrons_eidTight;
   vector<float>   *electrons_eidVeryLooseMC;
   vector<float>   *electrons_eidLooseMC;
   vector<float>   *electrons_eidMediumMC;
   vector<float>   *electrons_eidTightMC;
   vector<float>   *electrons_eidSuperTightMC;
   vector<float>   *electrons_eidHyperTight1MC;
   vector<float>   *electrons_eidHyperTight2MC;
   vector<float>   *electrons_eidHyperTight3MC;
   vector<float>   *electrons_eidHyperTight4MC;
   vector<float>   *electrons_passConvVeto;
   vector<float>   *electrons_correctedD0VertexErr;
   vector<float>   *electrons_correctedD0VertexSig;
   vector<float>   *electrons_detIso;
   vector<float>   *electrons_relPFrhoIso;
   vector<float>   *electrons_metMT;
   vector<float>   *electrons_correctedD0VertexEEPositiveChargeLowPt;
   vector<float>   *electrons_correctedD0VertexEEPositiveChargeHighPt;
   vector<float>   *electrons_correctedD0VertexInEBPlus;
   vector<float>   *electrons_correctedD0VertexOutEBPlus;
   vector<float>   *electrons_correctedD0VertexEEPlus;
   vector<float>   *electrons_correctedD0BeamspotInEBPlus;
   vector<float>   *electrons_correctedD0BeamspotOutEBPlus;
   vector<float>   *electrons_correctedD0BeamspotEEPlus;
   vector<float>   *electrons_correctedD0VertexInEBMinus;
   vector<float>   *electrons_correctedD0VertexOutEBMinus;
   vector<float>   *electrons_correctedD0VertexEEMinus;
   vector<float>   *electrons_correctedD0BeamspotInEBMinus;
   vector<float>   *electrons_correctedD0BeamspotOutEBMinus;
   vector<float>   *electrons_correctedD0BeamspotEEMinus;
   vector<float>   *electrons_tightID;
   vector<float>   *electrons_correctedD0VertexInEBPositiveCharge;
   vector<float>   *electrons_correctedD0VertexOutEBPositiveCharge;
   vector<float>   *electrons_correctedD0VertexEEPositiveCharge;
   vector<float>   *electrons_correctedD0BeamspotInEBPositiveCharge;
   vector<float>   *electrons_correctedD0BeamspotOutEBPositiveCharge;
   vector<float>   *electrons_correctedD0BeamspotEEPositiveCharge;
   vector<float>   *electrons_correctedD0VertexInEBNegativeCharge;
   vector<float>   *electrons_correctedD0VertexOutEBNegativeCharge;
   vector<float>   *electrons_correctedD0VertexEENegativeCharge;
   vector<float>   *electrons_correctedD0BeamspotInEBNegativeCharge;
   vector<float>   *electrons_correctedD0BeamspotOutEBNegativeCharge;
   vector<float>   *electrons_correctedD0BeamspotEENegativeCharge;
   vector<float>   *electrons_tightIDdisplaced;
   vector<float>   *electrons_genDeltaRLowest;
   vector<float>   *electrons_genMatchedPdgId;
   vector<float>   *electrons_genMatchedId;
   vector<float>   *electrons_genMatchedMotherId;
   vector<float>   *electrons_genMatchedMotherIdReverse;
   vector<float>   *electrons_genMatchedGrandmotherId;
   vector<float>   *electrons_genMatchedGrandmotherIdReverse;
   vector<float>   *electrons_pfElectronsFromVertex;
   vector<float>   *taus_px;
   vector<float>   *taus_py;
   vector<float>   *taus_pz;
   vector<float>   *taus_energy;
   vector<float>   *taus_et;
   vector<float>   *taus_pt;
   vector<float>   *taus_eta;
   vector<float>   *taus_phi;
   vector<float>   *taus_emFraction;
   vector<float>   *taus_leadingTrackPt;
   vector<float>   *taus_leadingTrackIpVtdxy;
   vector<float>   *taus_leadingTrackIpVtdz;
   vector<float>   *taus_leadingTrackIpVtdxyError;
   vector<float>   *taus_leadingTrackIpVtdzError;
   vector<float>   *taus_leadingTrackVx;
   vector<float>   *taus_leadingTrackVy;
   vector<float>   *taus_leadingTrackVz;
   vector<float>   *taus_leadingTrackValidHits;
   vector<float>   *taus_leadingTrackNormChiSqrd;
   vector<float>   *taus_numProngs;
   vector<float>   *taus_numSignalGammas;
   vector<float>   *taus_numSignalNeutrals;
   vector<float>   *taus_numSignalPiZeros;
   vector<float>   *taus_decayMode;
   vector<float>   *taus_charge;
   vector<float>   *taus_inTheCracks;
   vector<float>   *taus_HPSagainstElectronLoose;
   vector<float>   *taus_HPSagainstElectronMVA;
   vector<float>   *taus_HPSagainstElectronMedium;
   vector<float>   *taus_HPSagainstElectronTight;
   vector<float>   *taus_HPSagainstMuonLoose;
   vector<float>   *taus_HPSagainstMuonMedium;
   vector<float>   *taus_HPSagainstMuonTight;
   vector<float>   *taus_HPSbyLooseCombinedIsolationDeltaBetaCorr;
   vector<float>   *taus_HPSbyMediumCombinedIsolationDeltaBetaCorr;
   vector<float>   *taus_HPSbyTightCombinedIsolationDeltaBetaCorr;
   vector<float>   *taus_HPSbyVLooseCombinedIsolationDeltaBetaCorr;
   vector<float>   *taus_HPSdecayModeFinding;
   vector<float>   *taus_leadingTrackValid;
   vector<float>   *taus_genDeltaRLowest;
   vector<float>   *taus_genMatchedPdgId;
   vector<float>   *taus_genMatchedId;
   vector<float>   *taus_genMatchedMotherId;
   vector<float>   *taus_genMatchedMotherIdReverse;
   vector<float>   *taus_genMatchedGrandmotherId;
   vector<float>   *taus_genMatchedGrandmotherIdReverse;
   vector<float>   *tracks_pt;
   vector<float>   *tracks_px;
   vector<float>   *tracks_py;
   vector<float>   *tracks_pz;
   vector<float>   *tracks_phi;
   vector<float>   *tracks_eta;
   vector<float>   *tracks_theta;
   vector<float>   *tracks_normChi2;
   vector<float>   *tracks_dZ;
   vector<float>   *tracks_d0;
   vector<float>   *tracks_d0err;
   vector<float>   *tracks_vx;
   vector<float>   *tracks_vy;
   vector<float>   *tracks_vz;
   vector<float>   *tracks_charge;
   vector<float>   *tracks_numValidHits;
   vector<float>   *tracks_isHighPurity;
   vector<float>   *tracks_caloEMDeltaRp3;
   vector<float>   *tracks_caloHadDeltaRp3;
   vector<float>   *tracks_caloEMDeltaRp4;
   vector<float>   *tracks_caloHadDeltaRp4;
   vector<float>   *tracks_caloEMDeltaRp5;
   vector<float>   *tracks_caloHadDeltaRp5;
   vector<float>   *tracks_nTracksRp5;
   vector<float>   *tracks_nHitsMissingOuter;
   vector<float>   *tracks_nHitsMissingInner;
   vector<float>   *tracks_nHitsMissingMiddle;
   vector<float>   *tracks_depTrkRp5;
   vector<float>   *tracks_d0wrtBS;
   vector<float>   *tracks_dZwrtBS;
   vector<float>   *tracks_depTrkRp5MinusPt;
   vector<float>   *tracks_caloTotDeltaRp5;
   vector<float>   *tracks_caloTotDeltaRp5ByP;
   vector<float>   *tracks_caloTotDeltaRp5RhoCorr;
   vector<float>   *tracks_caloTotDeltaRp5ByPRhoCorr;
   vector<float>   *tracks_isIso;
   vector<float>   *tracks_isMatchedDeadEcal;
   vector<float>   *tracks_ptErrorByPt;
   vector<float>   *tracks_ptError;
   vector<float>   *tracks_ptRes;
   vector<float>   *tracks_d0wrtPV;
   vector<float>   *tracks_dZwrtPV;
   vector<float>   *tracks_genDeltaRLowest;
   vector<float>   *tracks_genMatchedPdgId;
   vector<float>   *tracks_genMatchedId;
   vector<float>   *tracks_genMatchedMotherId;
   vector<float>   *tracks_genMatchedMotherIdReverse;
   vector<float>   *tracks_genMatchedGrandmotherId;
   vector<float>   *tracks_genMatchedGrandmotherIdReverse;
   vector<float>   *mets_et;
   vector<float>   *mets_pt;
   vector<float>   *mets_px;
   vector<float>   *mets_py;
   vector<float>   *mets_phi;
   vector<float>   *mets_Upt;
   vector<float>   *mets_Uphi;
   vector<float>   *mets_NeutralEMFraction;
   vector<float>   *mets_NeutralHadEtFraction;
   vector<float>   *mets_ChargedEMEtFraction;
   vector<float>   *mets_ChargedHadEtFraction;
   vector<float>   *mets_MuonEtFraction;
   vector<float>   *mets_Type6EtFraction;
   vector<float>   *mets_Type7EtFraction;
   vector<float>   *mets_genPT;
   vector<float>   *mets_genPhi;
   vector<float>   *mets_muonCorEx;
   vector<float>   *mets_muonCorEy;
   vector<float>   *mets_jet20CorEx;
   vector<float>   *mets_jet20CorEy;
   vector<float>   *mets_jet1CorEx;
   vector<float>   *mets_jet1CorEy;
   vector<float>   *mets_sumET;
   vector<float>   *mets_corSumET;
   vector<float>   *mets_mEtSig;
   vector<float>   *mets_metSignificance;
   vector<float>   *mets_significance;
   vector<float>   *mets_sigmaX2;
   vector<float>   *mets_sigmaY2;
   vector<float>   *mets_sigmaXY;
   vector<float>   *mets_sigmaYX;
   vector<float>   *mets_maxEtInEmTowers;
   vector<float>   *mets_emEtFraction;
   vector<float>   *mets_emEtInEB;
   vector<float>   *mets_emEtInEE;
   vector<float>   *mets_emEtInHF;
   vector<float>   *mets_maxEtInHadTowers;
   vector<float>   *mets_hadEtFraction;
   vector<float>   *mets_hadEtInHB;
   vector<float>   *mets_hadEtInHE;
   vector<float>   *mets_hadEtInHF;
   vector<float>   *mets_hadEtInHO;
   vector<float>   *mets_UDeltaPx;
   vector<float>   *mets_UDeltaPy;
   vector<float>   *mets_UDeltaP;
   vector<float>   *mets_Uscale;
   vector<float>   *mets_type2corPx;
   vector<float>   *mets_type2corPy;
   vector<float>   *mets_T2pt;
   vector<float>   *mets_T2px;
   vector<float>   *mets_T2py;
   vector<float>   *mets_T2phi;
   vector<float>   *mets_T2sumET;
   vector<float>   *mets_pfT1jet1pt;
   vector<float>   *mets_pfT1jet1phi;
   vector<float>   *mets_pfT1jet6pt;
   vector<float>   *mets_pfT1jet6phi;
   vector<float>   *mets_pfT1jet10pt;
   vector<float>   *mets_pfT1jet10phi;
   vector<float>   *jets_energy;
   vector<float>   *jets_et;
   vector<float>   *jets_pt;
   vector<float>   *jets_px;
   vector<float>   *jets_py;
   vector<float>   *jets_pz;
   vector<float>   *jets_phi;
   vector<float>   *jets_eta;
   vector<float>   *jets_theta;
   vector<float>   *jets_Upt;
   vector<float>   *jets_Uenergy;
   vector<float>   *jets_L2pt;
   vector<float>   *jets_L2L3pt;
   vector<float>   *jets_L2L3respt;
   vector<float>   *jets_respt;
   vector<float>   *jets_EMfrac;
   vector<float>   *jets_Hadfrac;
   vector<float>   *jets_charge;
   vector<float>   *jets_mass;
   vector<float>   *jets_area;
   vector<float>   *jets_fHPD;
   vector<float>   *jets_approximatefHPD;
   vector<float>   *jets_genPartonET;
   vector<float>   *jets_genPartonPT;
   vector<float>   *jets_genPartonEta;
   vector<float>   *jets_genPartonPhi;
   vector<float>   *jets_genJetET;
   vector<float>   *jets_genJetPT;
   vector<float>   *jets_genJetEta;
   vector<float>   *jets_genJetPhi;
   vector<float>   *jets_btagTChighPur;
   vector<float>   *jets_btagTChighEff;
   vector<float>   *jets_btagJetProb;
   vector<float>   *jets_btagJetBProb;
   vector<float>   *jets_btagSoftEle;
   vector<float>   *jets_btagSoftMuon;
   vector<float>   *jets_btagSoftMuonNoIP;
   vector<float>   *jets_btagSecVertex;
   vector<float>   *jets_btagSecVertexHighEff;
   vector<float>   *jets_btagSecVertexHighPur;
   vector<float>   *jets_btagCombinedSecVertex;
   vector<float>   *jets_btagCombinedSecVertexMVA;
   vector<float>   *jets_btagSoftMuonByPt;
   vector<float>   *jets_btagSoftMuonByIP3;
   vector<float>   *jets_btagSoftElectronByPt;
   vector<float>   *jets_btagSoftElectronByIP3;
   vector<float>   *jets_n90Hits;
   vector<float>   *jets_hitsInN90;
   vector<float>   *jets_chargedHadronEnergyFraction;
   vector<float>   *jets_neutralHadronEnergyFraction;
   vector<float>   *jets_chargedEmEnergyFraction;
   vector<float>   *jets_neutralEmEnergyFraction;
   vector<float>   *jets_fLong;
   vector<float>   *jets_fShort;
   vector<float>   *jets_etaetaMoment;
   vector<float>   *jets_phiphiMoment;
   vector<float>   *jets_JESunc;
   vector<float>   *jets_JECuncUp;
   vector<float>   *jets_JECuncDown;
   vector<float>   *jets_puJetMVA_full;
   vector<float>   *jets_puJetMVA_simple;
   vector<float>   *jets_puJetMVA_cutbased;
   vector<float>   *jets_dZ;
   vector<float>   *jets_dR2Mean;
   vector<float>   *jets_dRMean;
   vector<float>   *jets_frac01;
   vector<float>   *jets_frac02;
   vector<float>   *jets_frac03;
   vector<float>   *jets_frac04;
   vector<float>   *jets_frac05;
   vector<float>   *jets_frac06;
   vector<float>   *jets_frac07;
   vector<float>   *jets_beta;
   vector<float>   *jets_betaStar;
   vector<float>   *jets_betaClassic;
   vector<float>   *jets_betaStarClassic;
   vector<float>   *jets_ptD;
   vector<float>   *jets_nvtx;
   vector<float>   *jets_d0;
   vector<float>   *jets_leadCandPt;
   vector<float>   *jets_leadCandVx;
   vector<float>   *jets_leadCandVy;
   vector<float>   *jets_leadCandVz;
   vector<float>   *jets_leadCandDistFromPV;
   vector<float>   *jets_flavour;
   vector<float>   *jets_Nconst;
   vector<float>   *jets_jetIDMinimal;
   vector<float>   *jets_jetIDLooseAOD;
   vector<float>   *jets_jetIDLoose;
   vector<float>   *jets_jetIDTight;
   vector<float>   *jets_genPartonId;
   vector<float>   *jets_genPartonMotherId;
   vector<float>   *jets_genPartonMother0Id;
   vector<float>   *jets_genPartonMother1Id;
   vector<float>   *jets_genPartonGrandMotherId;
   vector<float>   *jets_genPartonGrandMother00Id;
   vector<float>   *jets_genPartonGrandMother01Id;
   vector<float>   *jets_genPartonGrandMother10Id;
   vector<float>   *jets_genPartonGrandMother11Id;
   vector<float>   *jets_chargedMultiplicity;
   vector<float>   *jets_neutralMultiplicity;
   vector<float>   *jets_nconstituents;
   vector<float>   *jets_nHit;
   vector<float>   *jets_puJetId_full;
   vector<float>   *jets_puJetId_simple;
   vector<float>   *jets_puJetId_cutbased;
   vector<float>   *jets_puJetId_tight_full;
   vector<float>   *jets_puJetId_tight_simple;
   vector<float>   *jets_puJetId_tight_cutbased;
   vector<float>   *jets_puJetId_medium_full;
   vector<float>   *jets_puJetId_medium_simple;
   vector<float>   *jets_puJetId_medium_cutbased;
   vector<float>   *jets_puJetId_loose_full;
   vector<float>   *jets_puJetId_loose_simple;
   vector<float>   *jets_puJetId_loose_cutbased;
   vector<float>   *genjets_pt;
   vector<float>   *genjets_eta;
   vector<float>   *genjets_phi;
   vector<float>   *genjets_px;
   vector<float>   *genjets_py;
   vector<float>   *genjets_pz;
   vector<float>   *genjets_et;
   vector<float>   *genjets_energy;
   vector<float>   *genjets_mass;
   vector<float>   *genjets_emEnergy;
   vector<float>   *genjets_hadEnergy;
   vector<float>   *genjets_invisibleEnergy;
   vector<float>   *genjets_auxiliaryEnergy;
   vector<float>   *genjets_charge;
   vector<float>   *superclusters_energy;
   vector<float>   *superclusters_et;
   vector<float>   *superclusters_ex;
   vector<float>   *superclusters_ey;
   vector<float>   *superclusters_ez;
   vector<float>   *superclusters_phi;
   vector<float>   *superclusters_eta;
   vector<float>   *superclusters_theta;

   // List of branches
   TBranch        *b_events_weight;   //!
   TBranch        *b_events_pthat;   //!
   TBranch        *b_events_qScale;   //!
   TBranch        *b_events_alphaQCD;   //!
   TBranch        *b_events_alphaQED;   //!
   TBranch        *b_events_scalePDF;   //!
   TBranch        *b_events_x1;   //!
   TBranch        *b_events_x2;   //!
   TBranch        *b_events_xPDF1;   //!
   TBranch        *b_events_xPDF2;   //!
   TBranch        *b_events_BSx;   //!
   TBranch        *b_events_BSy;   //!
   TBranch        *b_events_BSz;   //!
   TBranch        *b_events_PVx;   //!
   TBranch        *b_events_PVy;   //!
   TBranch        *b_events_PVz;   //!
   TBranch        *b_events_bField;   //!
   TBranch        *b_events_instLumi;   //!
   TBranch        *b_events_bxLumi;   //!
   TBranch        *b_events_FilterOutScrapingFraction;   //!
   TBranch        *b_events_sumNVtx;   //!
   TBranch        *b_events_sumTrueNVtx;   //!
   TBranch        *b_events_nm1_true;   //!
   TBranch        *b_events_n0_true;   //!
   TBranch        *b_events_np1_true;   //!
   TBranch        *b_events_numTruePV;   //!
   TBranch        *b_events_Q2ScaleUpWgt;   //!
   TBranch        *b_events_Q2ScaleDownWgt;   //!
   TBranch        *b_events_rho_kt6PFJets;   //!
   TBranch        *b_events_rho_kt6PFJetsCentralChargedPileUp;   //!
   TBranch        *b_events_rho_kt6PFJetsCentralNeutral;   //!
   TBranch        *b_events_rho_kt6PFJetsCentralNeutralTight;   //!
   TBranch        *b_events_run;   //!
   TBranch        *b_events_lumi;   //!
   TBranch        *b_events_sample;   //!
   TBranch        *b_events_numPV;   //!
   TBranch        *b_events_W0decay;   //!
   TBranch        *b_events_W1decay;   //!
   TBranch        *b_events_Z0decay;   //!
   TBranch        *b_events_Z1decay;   //!
   TBranch        *b_events_H0decay;   //!
   TBranch        *b_events_H1decay;   //!
   TBranch        *b_events_hcalnoiseLoose;   //!
   TBranch        *b_events_hcalnoiseTight;   //!
   TBranch        *b_events_GoodVertex;   //!
   TBranch        *b_events_FilterOutScraping;   //!
   TBranch        *b_events_HBHENoiseFilter;   //!
   TBranch        *b_events_CSCLooseHaloId;   //!
   TBranch        *b_events_CSCTightHaloId;   //!
   TBranch        *b_events_EcalLooseHaloId;   //!
   TBranch        *b_events_EcalTightHaloId;   //!
   TBranch        *b_events_HcalLooseHaloId;   //!
   TBranch        *b_events_HcalTightHaloId;   //!
   TBranch        *b_events_GlobalLooseHaloId;   //!
   TBranch        *b_events_GlobalTightHaloId;   //!
   TBranch        *b_events_LooseId;   //!
   TBranch        *b_events_TightId;   //!
   TBranch        *b_events_numGenPV;   //!
   TBranch        *b_events_nm1;   //!
   TBranch        *b_events_n0;   //!
   TBranch        *b_events_np1;   //!
   TBranch        *b_events_id1;   //!
   TBranch        *b_events_id2;   //!
   TBranch        *b_events_evt;   //!
   TBranch        *b_events_puScaleFactor;   //!
   TBranch        *b_events_muonScaleFactor;   //!
   TBranch        *b_events_electronScaleFactor;   //!
   TBranch        *b_events_stopCTauScaleFactor;   //!
   TBranch        *b_muons_energy;   //!
   TBranch        *b_muons_et;   //!
   TBranch        *b_muons_pt;   //!
   TBranch        *b_muons_px;   //!
   TBranch        *b_muons_py;   //!
   TBranch        *b_muons_pz;   //!
   TBranch        *b_muons_phi;   //!
   TBranch        *b_muons_eta;   //!
   TBranch        *b_muons_theta;   //!
   TBranch        *b_muons_trackIso;   //!
   TBranch        *b_muons_ecalIso;   //!
   TBranch        *b_muons_hcalIso;   //!
   TBranch        *b_muons_caloIso;   //!
   TBranch        *b_muons_trackIsDR03;   //!
   TBranch        *b_muons_ecalIsoDR03;   //!
   TBranch        *b_muons_hcalIsoDR03;   //!
   TBranch        *b_muons_caloIsoDR03;   //!
   TBranch        *b_muons_trackVetoIsoDR03;   //!
   TBranch        *b_muons_ecalVetoIsoDR03;   //!
   TBranch        *b_muons_hcalVetoIsoDR03;   //!
   TBranch        *b_muons_caloVetoIsoDR03;   //!
   TBranch        *b_muons_trackIsoDR05;   //!
   TBranch        *b_muons_ecalIsoDR05;   //!
   TBranch        *b_muons_hcalIsoDR05;   //!
   TBranch        *b_muons_caloIsoDR05;   //!
   TBranch        *b_muons_trackVetoIsoDR05;   //!
   TBranch        *b_muons_ecalVetoIsoDR05;   //!
   TBranch        *b_muons_hcalVetoIsoDR05;   //!
   TBranch        *b_muons_caloVetoIsoDR05;   //!
   TBranch        *b_muons_hcalE;   //!
   TBranch        *b_muons_ecalE;   //!
   TBranch        *b_muons_genET;   //!
   TBranch        *b_muons_genPT;   //!
   TBranch        *b_muons_genPhi;   //!
   TBranch        *b_muons_genEta;   //!
   TBranch        *b_muons_genMotherET;   //!
   TBranch        *b_muons_genMotherPT;   //!
   TBranch        *b_muons_genMotherPhi;   //!
   TBranch        *b_muons_genMotherEta;   //!
   TBranch        *b_muons_vx;   //!
   TBranch        *b_muons_vy;   //!
   TBranch        *b_muons_vz;   //!
   TBranch        *b_muons_tkNormChi2;   //!
   TBranch        *b_muons_tkPT;   //!
   TBranch        *b_muons_tkEta;   //!
   TBranch        *b_muons_tkPhi;   //!
   TBranch        *b_muons_tkDZ;   //!
   TBranch        *b_muons_tkD0;   //!
   TBranch        *b_muons_tkD0bs;   //!
   TBranch        *b_muons_tkD0err;   //!
   TBranch        *b_muons_samNormChi2;   //!
   TBranch        *b_muons_samPT;   //!
   TBranch        *b_muons_samEta;   //!
   TBranch        *b_muons_samPhi;   //!
   TBranch        *b_muons_samDZ;   //!
   TBranch        *b_muons_samD0;   //!
   TBranch        *b_muons_samD0bs;   //!
   TBranch        *b_muons_samD0err;   //!
   TBranch        *b_muons_comNormChi2;   //!
   TBranch        *b_muons_comPT;   //!
   TBranch        *b_muons_comEta;   //!
   TBranch        *b_muons_comPhi;   //!
   TBranch        *b_muons_comDZ;   //!
   TBranch        *b_muons_comD0;   //!
   TBranch        *b_muons_comD0bs;   //!
   TBranch        *b_muons_comD0err;   //!
   TBranch        *b_muons_isolationR03emVetoEt;   //!
   TBranch        *b_muons_isolationR03hadVetoEt;   //!
   TBranch        *b_muons_normalizedChi2;   //!
   TBranch        *b_muons_dVzPVz;   //!
   TBranch        *b_muons_dB;   //!
   TBranch        *b_muons_ptErr;   //!
   TBranch        *b_muons_innerTrackNormChi2;   //!
   TBranch        *b_muons_correctedD0;   //!
   TBranch        *b_muons_correctedD0Vertex;   //!
   TBranch        *b_muons_correctedDZ;   //!
   TBranch        *b_muons_particleIso;   //!
   TBranch        *b_muons_chargedHadronIso;   //!
   TBranch        *b_muons_neutralHadronIso;   //!
   TBranch        *b_muons_photonIso;   //!
   TBranch        *b_muons_puChargedHadronIso;   //!
   TBranch        *b_muons_chargedHadronIsoDR03;   //!
   TBranch        *b_muons_neutralHadronIsoDR03;   //!
   TBranch        *b_muons_photonIsoDR03;   //!
   TBranch        *b_muons_puChargedHadronIsoDR03;   //!
   TBranch        *b_muons_chargedHadronIsoDR04;   //!
   TBranch        *b_muons_neutralHadronIsoDR04;   //!
   TBranch        *b_muons_photonIsoDR04;   //!
   TBranch        *b_muons_puChargedHadronIsoDR04;   //!
   TBranch        *b_muons_rhoPrime;   //!
   TBranch        *b_muons_AEffDr03;   //!
   TBranch        *b_muons_AEffDr04;   //!
   TBranch        *b_muons_pfIsoR03SumChargedHadronPt;   //!
   TBranch        *b_muons_pfIsoR03SumNeutralHadronEt;   //!
   TBranch        *b_muons_pfIsoR03SumPhotonEt;   //!
   TBranch        *b_muons_pfIsoR03SumPUPt;   //!
   TBranch        *b_muons_pfIsoR04SumChargedHadronPt;   //!
   TBranch        *b_muons_pfIsoR04SumNeutralHadronEt;   //!
   TBranch        *b_muons_pfIsoR04SumPhotonEt;   //!
   TBranch        *b_muons_pfIsoR04SumPUPt;   //!
   TBranch        *b_muons_IP;   //!
   TBranch        *b_muons_IPError;   //!
   TBranch        *b_muons_timeAtIpInOut;   //!
   TBranch        *b_muons_timeAtIpInOutErr;   //!
   TBranch        *b_muons_timeAtIpOutIn;   //!
   TBranch        *b_muons_timeAtIpOutInErr;   //!
   TBranch        *b_muons_ecal_time;   //!
   TBranch        *b_muons_hcal_time;   //!
   TBranch        *b_muons_ecal_timeError;   //!
   TBranch        *b_muons_hcal_timeError;   //!
   TBranch        *b_muons_energy_ecal;   //!
   TBranch        *b_muons_energy_hcal;   //!
   TBranch        *b_muons_e3x3_ecal;   //!
   TBranch        *b_muons_e3x3_hcal;   //!
   TBranch        *b_muons_energyMax_ecal;   //!
   TBranch        *b_muons_energyMax_hcal;   //!
   TBranch        *b_muons_charge;   //!
   TBranch        *b_muons_IDGMPTight;   //!
   TBranch        *b_muons_tkNumValidHits;   //!
   TBranch        *b_muons_tkCharge;   //!
   TBranch        *b_muons_samNumValidHits;   //!
   TBranch        *b_muons_samCharge;   //!
   TBranch        *b_muons_comNumValidHits;   //!
   TBranch        *b_muons_comCharge;   //!
   TBranch        *b_muons_genId;   //!
   TBranch        *b_muons_genCharge;   //!
   TBranch        *b_muons_genNumberOfMothers;   //!
   TBranch        *b_muons_genMotherId;   //!
   TBranch        *b_muons_genMotherCharge;   //!
   TBranch        *b_muons_genMother0Id;   //!
   TBranch        *b_muons_genMother1Id;   //!
   TBranch        *b_muons_genGrandMother00Id;   //!
   TBranch        *b_muons_genGrandMother01Id;   //!
   TBranch        *b_muons_genGrandMother10Id;   //!
   TBranch        *b_muons_genGrandMother11Id;   //!
   TBranch        *b_muons_isPFMuon;   //!
   TBranch        *b_muons_isGoodMuon_1StationTight;   //!
   TBranch        *b_muons_isGlobalMuon;   //!
   TBranch        *b_muons_isTrackerMuon;   //!
   TBranch        *b_muons_isStandAloneMuon;   //!
   TBranch        *b_muons_isGlobalMuonPromptTight;   //!
   TBranch        *b_muons_numberOfValidMuonHits;   //!
   TBranch        *b_muons_numberOfValidTrackerHits;   //!
   TBranch        *b_muons_numberOfLayersWithMeasurement;   //!
   TBranch        *b_muons_pixelLayersWithMeasurement;   //!
   TBranch        *b_muons_numberOfMatches;   //!
   TBranch        *b_muons_numberOfValidTrackerHitsInnerTrack;   //!
   TBranch        *b_muons_numberOfValidPixelHits;   //!
   TBranch        *b_muons_numberOfMatchedStations;   //!
   TBranch        *b_muons_time_ndof;   //!
   TBranch        *b_muons_correctedD0VertexErr;   //!
   TBranch        *b_muons_correctedD0VertexSig;   //!
   TBranch        *b_muons_detIso;   //!
   TBranch        *b_muons_relPFdBetaIso;   //!
   TBranch        *b_muons_relPFrhoIso;   //!
   TBranch        *b_muons_metMT;   //!
   TBranch        *b_muons_correctedD0VertexInEBPlus;   //!
   TBranch        *b_muons_correctedD0VertexOutEBPlus;   //!
   TBranch        *b_muons_correctedD0VertexEEPlus;   //!
   TBranch        *b_muons_correctedD0BeamspotInEBPlus;   //!
   TBranch        *b_muons_correctedD0BeamspotOutEBPlus;   //!
   TBranch        *b_muons_correctedD0BeamspotEEPlus;   //!
   TBranch        *b_muons_correctedD0VertexInEBMinus;   //!
   TBranch        *b_muons_correctedD0VertexOutEBMinus;   //!
   TBranch        *b_muons_correctedD0VertexEEMinus;   //!
   TBranch        *b_muons_correctedD0BeamspotInEBMinus;   //!
   TBranch        *b_muons_correctedD0BeamspotOutEBMinus;   //!
   TBranch        *b_muons_correctedD0BeamspotEEMinus;   //!
   TBranch        *b_muons_correctedD0VertexInEBPositiveCharge;   //!
   TBranch        *b_muons_correctedD0VertexOutEBPositiveCharge;   //!
   TBranch        *b_muons_correctedD0VertexEEPositiveCharge;   //!
   TBranch        *b_muons_correctedD0BeamspotInEBPositiveCharge;   //!
   TBranch        *b_muons_correctedD0BeamspotOutEBPositiveCharge;   //!
   TBranch        *b_muons_correctedD0BeamspotEEPositiveCharge;   //!
   TBranch        *b_muons_correctedD0VertexInEBNegativeCharge;   //!
   TBranch        *b_muons_correctedD0VertexOutEBNegativeCharge;   //!
   TBranch        *b_muons_correctedD0VertexEENegativeCharge;   //!
   TBranch        *b_muons_correctedD0BeamspotInEBNegativeCharge;   //!
   TBranch        *b_muons_correctedD0BeamspotOutEBNegativeCharge;   //!
   TBranch        *b_muons_correctedD0BeamspotEENegativeCharge;   //!
   TBranch        *b_muons_tightID;   //!
   TBranch        *b_muons_tightIDdisplaced;   //!
   TBranch        *b_muons_genDeltaRLowest;   //!
   TBranch        *b_muons_genMatchedPdgId;   //!
   TBranch        *b_muons_genMatchedId;   //!
   TBranch        *b_muons_genMatchedMotherId;   //!
   TBranch        *b_muons_genMatchedMotherIdReverse;   //!
   TBranch        *b_muons_genMatchedGrandmotherId;   //!
   TBranch        *b_muons_genMatchedGrandmotherIdReverse;   //!
   TBranch        *b_muons_pfMuonsFromVertex;   //!
   TBranch        *b_electrons_energy;   //!
   TBranch        *b_electrons_et;   //!
   TBranch        *b_electrons_gsfEt;   //!
   TBranch        *b_electrons_pt;   //!
   TBranch        *b_electrons_px;   //!
   TBranch        *b_electrons_py;   //!
   TBranch        *b_electrons_pz;   //!
   TBranch        *b_electrons_phi;   //!
   TBranch        *b_electrons_eta;   //!
   TBranch        *b_electrons_theta;   //!
   TBranch        *b_electrons_pIn;   //!
   TBranch        *b_electrons_pOut;   //!
   TBranch        *b_electrons_EscOverPin;   //!
   TBranch        *b_electrons_EseedOverPout;   //!
   TBranch        *b_electrons_hadOverEm;   //!
   TBranch        *b_electrons_trackIso;   //!
   TBranch        *b_electrons_ecalIso;   //!
   TBranch        *b_electrons_hcalIso;   //!
   TBranch        *b_electrons_caloIso;   //!
   TBranch        *b_electrons_trackIsoDR03;   //!
   TBranch        *b_electrons_ecalIsoDR03;   //!
   TBranch        *b_electrons_hcalIsoDR03;   //!
   TBranch        *b_electrons_hcalIsoDR03depth1;   //!
   TBranch        *b_electrons_hcalIsoDR03depth2;   //!
   TBranch        *b_electrons_caloIsoDR03;   //!
   TBranch        *b_electrons_trackIsoDR04;   //!
   TBranch        *b_electrons_ecalIsoDR04;   //!
   TBranch        *b_electrons_hcalIsoDR04;   //!
   TBranch        *b_electrons_hcalIsoDR04depth1;   //!
   TBranch        *b_electrons_hcalIsoDR04depth2;   //!
   TBranch        *b_electrons_caloIsoDR04;   //!
   TBranch        *b_electrons_fbrem;   //!
   TBranch        *b_electrons_absInvEMinusInvPin;   //!
   TBranch        *b_electrons_delPhiIn;   //!
   TBranch        *b_electrons_delEtaIn;   //!
   TBranch        *b_electrons_genET;   //!
   TBranch        *b_electrons_genPT;   //!
   TBranch        *b_electrons_genPhi;   //!
   TBranch        *b_electrons_genEta;   //!
   TBranch        *b_electrons_genMotherET;   //!
   TBranch        *b_electrons_genMotherPT;   //!
   TBranch        *b_electrons_genMotherPhi;   //!
   TBranch        *b_electrons_genMotherEta;   //!
   TBranch        *b_electrons_vx;   //!
   TBranch        *b_electrons_vy;   //!
   TBranch        *b_electrons_vz;   //!
   TBranch        *b_electrons_scEnergy;   //!
   TBranch        *b_electrons_scRawEnergy;   //!
   TBranch        *b_electrons_scSigmaEtaEta;   //!
   TBranch        *b_electrons_scSigmaIEtaIEta;   //!
   TBranch        *b_electrons_scE1x5;   //!
   TBranch        *b_electrons_scE2x5Max;   //!
   TBranch        *b_electrons_scE5x5;   //!
   TBranch        *b_electrons_scEt;   //!
   TBranch        *b_electrons_scEta;   //!
   TBranch        *b_electrons_scPhi;   //!
   TBranch        *b_electrons_scZ;   //!
   TBranch        *b_electrons_tkNormChi2;   //!
   TBranch        *b_electrons_tkPT;   //!
   TBranch        *b_electrons_tkEta;   //!
   TBranch        *b_electrons_tkPhi;   //!
   TBranch        *b_electrons_tkDZ;   //!
   TBranch        *b_electrons_tkD0;   //!
   TBranch        *b_electrons_tkD0bs;   //!
   TBranch        *b_electrons_tkD0err;   //!
   TBranch        *b_electrons_mva;   //!
   TBranch        *b_electrons_mvaTrigV0;   //!
   TBranch        *b_electrons_mvaNonTrigV0;   //!
   TBranch        *b_electrons_dist;   //!
   TBranch        *b_electrons_dcot;   //!
   TBranch        *b_electrons_convradius;   //!
   TBranch        *b_electrons_convPointX;   //!
   TBranch        *b_electrons_convPointY;   //!
   TBranch        *b_electrons_convPointZ;   //!
   TBranch        *b_electrons_eMax;   //!
   TBranch        *b_electrons_eLeft;   //!
   TBranch        *b_electrons_eRight;   //!
   TBranch        *b_electrons_eTop;   //!
   TBranch        *b_electrons_eBottom;   //!
   TBranch        *b_electrons_e3x3;   //!
   TBranch        *b_electrons_swissCross;   //!
   TBranch        *b_electrons_seedEnergy;   //!
   TBranch        *b_electrons_seedTime;   //!
   TBranch        *b_electrons_swissCrossNoI85;   //!
   TBranch        *b_electrons_swissCrossI85;   //!
   TBranch        *b_electrons_E2overE9NoI85;   //!
   TBranch        *b_electrons_E2overE9I85;   //!
   TBranch        *b_electrons_correctedD0;   //!
   TBranch        *b_electrons_correctedD0Vertex;   //!
   TBranch        *b_electrons_correctedDZ;   //!
   TBranch        *b_electrons_particleIso;   //!
   TBranch        *b_electrons_chargedHadronIso;   //!
   TBranch        *b_electrons_neutralHadronIso;   //!
   TBranch        *b_electrons_photonIso;   //!
   TBranch        *b_electrons_puChargedHadronIso;   //!
   TBranch        *b_electrons_chargedHadronIsoDR03;   //!
   TBranch        *b_electrons_neutralHadronIsoDR03;   //!
   TBranch        *b_electrons_photonIsoDR03;   //!
   TBranch        *b_electrons_puChargedHadronIsoDR03;   //!
   TBranch        *b_electrons_chargedHadronIsoDR04;   //!
   TBranch        *b_electrons_neutralHadronIsoDR04;   //!
   TBranch        *b_electrons_photonIsoDR04;   //!
   TBranch        *b_electrons_puChargedHadronIsoDR04;   //!
   TBranch        *b_electrons_rhoPrime;   //!
   TBranch        *b_electrons_AEffDr03;   //!
   TBranch        *b_electrons_AEffDr04;   //!
   TBranch        *b_electrons_IP;   //!
   TBranch        *b_electrons_IPError;   //!
   TBranch        *b_electrons_charge;   //!
   TBranch        *b_electrons_classification;   //!
   TBranch        *b_electrons_genId;   //!
   TBranch        *b_electrons_genCharge;   //!
   TBranch        *b_electrons_genNumberOfMothers;   //!
   TBranch        *b_electrons_genMotherId;   //!
   TBranch        *b_electrons_genMotherCharge;   //!
   TBranch        *b_electrons_genMother0Id;   //!
   TBranch        *b_electrons_genMother1Id;   //!
   TBranch        *b_electrons_genGrandMother00Id;   //!
   TBranch        *b_electrons_genGrandMother01Id;   //!
   TBranch        *b_electrons_genGrandMother10Id;   //!
   TBranch        *b_electrons_genGrandMother11Id;   //!
   TBranch        *b_electrons_numClusters;   //!
   TBranch        *b_electrons_tkNumValidHits;   //!
   TBranch        *b_electrons_tkCharge;   //!
   TBranch        *b_electrons_gsfCharge;   //!
   TBranch        *b_electrons_isEB;   //!
   TBranch        *b_electrons_isEE;   //!
   TBranch        *b_electrons_isGap;   //!
   TBranch        *b_electrons_isEBEEGap;   //!
   TBranch        *b_electrons_isEBGap;   //!
   TBranch        *b_electrons_isEEGap;   //!
   TBranch        *b_electrons_isEcalDriven;   //!
   TBranch        *b_electrons_isTrackerDriven;   //!
   TBranch        *b_electrons_numberOfLostHits;   //!
   TBranch        *b_electrons_numberOfExpectedInnerHits;   //!
   TBranch        *b_electrons_numberOfValidPixelHits;   //!
   TBranch        *b_electrons_numberOfValidPixelBarrelHits;   //!
   TBranch        *b_electrons_numberOfValidPixelEndcapHits;   //!
   TBranch        *b_electrons_isHEEP;   //!
   TBranch        *b_electrons_isHEEPnoEt;   //!
   TBranch        *b_electrons_seedRecoFlag;   //!
   TBranch        *b_electrons_eidRobustHighEnergy;   //!
   TBranch        *b_electrons_eidRobustLoose;   //!
   TBranch        *b_electrons_eidRobustTight;   //!
   TBranch        *b_electrons_eidLoose;   //!
   TBranch        *b_electrons_eidTight;   //!
   TBranch        *b_electrons_eidVeryLooseMC;   //!
   TBranch        *b_electrons_eidLooseMC;   //!
   TBranch        *b_electrons_eidMediumMC;   //!
   TBranch        *b_electrons_eidTightMC;   //!
   TBranch        *b_electrons_eidSuperTightMC;   //!
   TBranch        *b_electrons_eidHyperTight1MC;   //!
   TBranch        *b_electrons_eidHyperTight2MC;   //!
   TBranch        *b_electrons_eidHyperTight3MC;   //!
   TBranch        *b_electrons_eidHyperTight4MC;   //!
   TBranch        *b_electrons_passConvVeto;   //!
   TBranch        *b_electrons_correctedD0VertexErr;   //!
   TBranch        *b_electrons_correctedD0VertexSig;   //!
   TBranch        *b_electrons_detIso;   //!
   TBranch        *b_electrons_relPFrhoIso;   //!
   TBranch        *b_electrons_metMT;   //!
   TBranch        *b_electrons_correctedD0VertexEEPositiveChargeLowPt;   //!
   TBranch        *b_electrons_correctedD0VertexEEPositiveChargeHighPt;   //!
   TBranch        *b_electrons_correctedD0VertexInEBPlus;   //!
   TBranch        *b_electrons_correctedD0VertexOutEBPlus;   //!
   TBranch        *b_electrons_correctedD0VertexEEPlus;   //!
   TBranch        *b_electrons_correctedD0BeamspotInEBPlus;   //!
   TBranch        *b_electrons_correctedD0BeamspotOutEBPlus;   //!
   TBranch        *b_electrons_correctedD0BeamspotEEPlus;   //!
   TBranch        *b_electrons_correctedD0VertexInEBMinus;   //!
   TBranch        *b_electrons_correctedD0VertexOutEBMinus;   //!
   TBranch        *b_electrons_correctedD0VertexEEMinus;   //!
   TBranch        *b_electrons_correctedD0BeamspotInEBMinus;   //!
   TBranch        *b_electrons_correctedD0BeamspotOutEBMinus;   //!
   TBranch        *b_electrons_correctedD0BeamspotEEMinus;   //!
   TBranch        *b_electrons_tightID;   //!
   TBranch        *b_electrons_correctedD0VertexInEBPositiveCharge;   //!
   TBranch        *b_electrons_correctedD0VertexOutEBPositiveCharge;   //!
   TBranch        *b_electrons_correctedD0VertexEEPositiveCharge;   //!
   TBranch        *b_electrons_correctedD0BeamspotInEBPositiveCharge;   //!
   TBranch        *b_electrons_correctedD0BeamspotOutEBPositiveCharge;   //!
   TBranch        *b_electrons_correctedD0BeamspotEEPositiveCharge;   //!
   TBranch        *b_electrons_correctedD0VertexInEBNegativeCharge;   //!
   TBranch        *b_electrons_correctedD0VertexOutEBNegativeCharge;   //!
   TBranch        *b_electrons_correctedD0VertexEENegativeCharge;   //!
   TBranch        *b_electrons_correctedD0BeamspotInEBNegativeCharge;   //!
   TBranch        *b_electrons_correctedD0BeamspotOutEBNegativeCharge;   //!
   TBranch        *b_electrons_correctedD0BeamspotEENegativeCharge;   //!
   TBranch        *b_electrons_tightIDdisplaced;   //!
   TBranch        *b_electrons_genDeltaRLowest;   //!
   TBranch        *b_electrons_genMatchedPdgId;   //!
   TBranch        *b_electrons_genMatchedId;   //!
   TBranch        *b_electrons_genMatchedMotherId;   //!
   TBranch        *b_electrons_genMatchedMotherIdReverse;   //!
   TBranch        *b_electrons_genMatchedGrandmotherId;   //!
   TBranch        *b_electrons_genMatchedGrandmotherIdReverse;   //!
   TBranch        *b_electrons_pfElectronsFromVertex;   //!
   TBranch        *b_taus_px;   //!
   TBranch        *b_taus_py;   //!
   TBranch        *b_taus_pz;   //!
   TBranch        *b_taus_energy;   //!
   TBranch        *b_taus_et;   //!
   TBranch        *b_taus_pt;   //!
   TBranch        *b_taus_eta;   //!
   TBranch        *b_taus_phi;   //!
   TBranch        *b_taus_emFraction;   //!
   TBranch        *b_taus_leadingTrackPt;   //!
   TBranch        *b_taus_leadingTrackIpVtdxy;   //!
   TBranch        *b_taus_leadingTrackIpVtdz;   //!
   TBranch        *b_taus_leadingTrackIpVtdxyError;   //!
   TBranch        *b_taus_leadingTrackIpVtdzError;   //!
   TBranch        *b_taus_leadingTrackVx;   //!
   TBranch        *b_taus_leadingTrackVy;   //!
   TBranch        *b_taus_leadingTrackVz;   //!
   TBranch        *b_taus_leadingTrackValidHits;   //!
   TBranch        *b_taus_leadingTrackNormChiSqrd;   //!
   TBranch        *b_taus_numProngs;   //!
   TBranch        *b_taus_numSignalGammas;   //!
   TBranch        *b_taus_numSignalNeutrals;   //!
   TBranch        *b_taus_numSignalPiZeros;   //!
   TBranch        *b_taus_decayMode;   //!
   TBranch        *b_taus_charge;   //!
   TBranch        *b_taus_inTheCracks;   //!
   TBranch        *b_taus_HPSagainstElectronLoose;   //!
   TBranch        *b_taus_HPSagainstElectronMVA;   //!
   TBranch        *b_taus_HPSagainstElectronMedium;   //!
   TBranch        *b_taus_HPSagainstElectronTight;   //!
   TBranch        *b_taus_HPSagainstMuonLoose;   //!
   TBranch        *b_taus_HPSagainstMuonMedium;   //!
   TBranch        *b_taus_HPSagainstMuonTight;   //!
   TBranch        *b_taus_HPSbyLooseCombinedIsolationDeltaBetaCorr;   //!
   TBranch        *b_taus_HPSbyMediumCombinedIsolationDeltaBetaCorr;   //!
   TBranch        *b_taus_HPSbyTightCombinedIsolationDeltaBetaCorr;   //!
   TBranch        *b_taus_HPSbyVLooseCombinedIsolationDeltaBetaCorr;   //!
   TBranch        *b_taus_HPSdecayModeFinding;   //!
   TBranch        *b_taus_leadingTrackValid;   //!
   TBranch        *b_taus_genDeltaRLowest;   //!
   TBranch        *b_taus_genMatchedPdgId;   //!
   TBranch        *b_taus_genMatchedId;   //!
   TBranch        *b_taus_genMatchedMotherId;   //!
   TBranch        *b_taus_genMatchedMotherIdReverse;   //!
   TBranch        *b_taus_genMatchedGrandmotherId;   //!
   TBranch        *b_taus_genMatchedGrandmotherIdReverse;   //!
   TBranch        *b_tracks_pt;   //!
   TBranch        *b_tracks_px;   //!
   TBranch        *b_tracks_py;   //!
   TBranch        *b_tracks_pz;   //!
   TBranch        *b_tracks_phi;   //!
   TBranch        *b_tracks_eta;   //!
   TBranch        *b_tracks_theta;   //!
   TBranch        *b_tracks_normChi2;   //!
   TBranch        *b_tracks_dZ;   //!
   TBranch        *b_tracks_d0;   //!
   TBranch        *b_tracks_d0err;   //!
   TBranch        *b_tracks_vx;   //!
   TBranch        *b_tracks_vy;   //!
   TBranch        *b_tracks_vz;   //!
   TBranch        *b_tracks_charge;   //!
   TBranch        *b_tracks_numValidHits;   //!
   TBranch        *b_tracks_isHighPurity;   //!
   TBranch        *b_tracks_caloEMDeltaRp3;   //!
   TBranch        *b_tracks_caloHadDeltaRp3;   //!
   TBranch        *b_tracks_caloEMDeltaRp4;   //!
   TBranch        *b_tracks_caloHadDeltaRp4;   //!
   TBranch        *b_tracks_caloEMDeltaRp5;   //!
   TBranch        *b_tracks_caloHadDeltaRp5;   //!
   TBranch        *b_tracks_nTracksRp5;   //!
   TBranch        *b_tracks_nHitsMissingOuter;   //!
   TBranch        *b_tracks_nHitsMissingInner;   //!
   TBranch        *b_tracks_nHitsMissingMiddle;   //!
   TBranch        *b_tracks_depTrkRp5;   //!
   TBranch        *b_tracks_d0wrtBS;   //!
   TBranch        *b_tracks_dZwrtBS;   //!
   TBranch        *b_tracks_depTrkRp5MinusPt;   //!
   TBranch        *b_tracks_caloTotDeltaRp5;   //!
   TBranch        *b_tracks_caloTotDeltaRp5ByP;   //!
   TBranch        *b_tracks_caloTotDeltaRp5RhoCorr;   //!
   TBranch        *b_tracks_caloTotDeltaRp5ByPRhoCorr;   //!
   TBranch        *b_tracks_isIso;   //!
   TBranch        *b_tracks_isMatchedDeadEcal;   //!
   TBranch        *b_tracks_ptErrorByPt;   //!
   TBranch        *b_tracks_ptError;   //!
   TBranch        *b_tracks_ptRes;   //!
   TBranch        *b_tracks_d0wrtPV;   //!
   TBranch        *b_tracks_dZwrtPV;   //!
   TBranch        *b_tracks_genDeltaRLowest;   //!
   TBranch        *b_tracks_genMatchedPdgId;   //!
   TBranch        *b_tracks_genMatchedId;   //!
   TBranch        *b_tracks_genMatchedMotherId;   //!
   TBranch        *b_tracks_genMatchedMotherIdReverse;   //!
   TBranch        *b_tracks_genMatchedGrandmotherId;   //!
   TBranch        *b_tracks_genMatchedGrandmotherIdReverse;   //!
   TBranch        *b_mets_et;   //!
   TBranch        *b_mets_pt;   //!
   TBranch        *b_mets_px;   //!
   TBranch        *b_mets_py;   //!
   TBranch        *b_mets_phi;   //!
   TBranch        *b_mets_Upt;   //!
   TBranch        *b_mets_Uphi;   //!
   TBranch        *b_mets_NeutralEMFraction;   //!
   TBranch        *b_mets_NeutralHadEtFraction;   //!
   TBranch        *b_mets_ChargedEMEtFraction;   //!
   TBranch        *b_mets_ChargedHadEtFraction;   //!
   TBranch        *b_mets_MuonEtFraction;   //!
   TBranch        *b_mets_Type6EtFraction;   //!
   TBranch        *b_mets_Type7EtFraction;   //!
   TBranch        *b_mets_genPT;   //!
   TBranch        *b_mets_genPhi;   //!
   TBranch        *b_mets_muonCorEx;   //!
   TBranch        *b_mets_muonCorEy;   //!
   TBranch        *b_mets_jet20CorEx;   //!
   TBranch        *b_mets_jet20CorEy;   //!
   TBranch        *b_mets_jet1CorEx;   //!
   TBranch        *b_mets_jet1CorEy;   //!
   TBranch        *b_mets_sumET;   //!
   TBranch        *b_mets_corSumET;   //!
   TBranch        *b_mets_mEtSig;   //!
   TBranch        *b_mets_metSignificance;   //!
   TBranch        *b_mets_significance;   //!
   TBranch        *b_mets_sigmaX2;   //!
   TBranch        *b_mets_sigmaY2;   //!
   TBranch        *b_mets_sigmaXY;   //!
   TBranch        *b_mets_sigmaYX;   //!
   TBranch        *b_mets_maxEtInEmTowers;   //!
   TBranch        *b_mets_emEtFraction;   //!
   TBranch        *b_mets_emEtInEB;   //!
   TBranch        *b_mets_emEtInEE;   //!
   TBranch        *b_mets_emEtInHF;   //!
   TBranch        *b_mets_maxEtInHadTowers;   //!
   TBranch        *b_mets_hadEtFraction;   //!
   TBranch        *b_mets_hadEtInHB;   //!
   TBranch        *b_mets_hadEtInHE;   //!
   TBranch        *b_mets_hadEtInHF;   //!
   TBranch        *b_mets_hadEtInHO;   //!
   TBranch        *b_mets_UDeltaPx;   //!
   TBranch        *b_mets_UDeltaPy;   //!
   TBranch        *b_mets_UDeltaP;   //!
   TBranch        *b_mets_Uscale;   //!
   TBranch        *b_mets_type2corPx;   //!
   TBranch        *b_mets_type2corPy;   //!
   TBranch        *b_mets_T2pt;   //!
   TBranch        *b_mets_T2px;   //!
   TBranch        *b_mets_T2py;   //!
   TBranch        *b_mets_T2phi;   //!
   TBranch        *b_mets_T2sumET;   //!
   TBranch        *b_mets_pfT1jet1pt;   //!
   TBranch        *b_mets_pfT1jet1phi;   //!
   TBranch        *b_mets_pfT1jet6pt;   //!
   TBranch        *b_mets_pfT1jet6phi;   //!
   TBranch        *b_mets_pfT1jet10pt;   //!
   TBranch        *b_mets_pfT1jet10phi;   //!
   TBranch        *b_jets_energy;   //!
   TBranch        *b_jets_et;   //!
   TBranch        *b_jets_pt;   //!
   TBranch        *b_jets_px;   //!
   TBranch        *b_jets_py;   //!
   TBranch        *b_jets_pz;   //!
   TBranch        *b_jets_phi;   //!
   TBranch        *b_jets_eta;   //!
   TBranch        *b_jets_theta;   //!
   TBranch        *b_jets_Upt;   //!
   TBranch        *b_jets_Uenergy;   //!
   TBranch        *b_jets_L2pt;   //!
   TBranch        *b_jets_L2L3pt;   //!
   TBranch        *b_jets_L2L3respt;   //!
   TBranch        *b_jets_respt;   //!
   TBranch        *b_jets_EMfrac;   //!
   TBranch        *b_jets_Hadfrac;   //!
   TBranch        *b_jets_charge;   //!
   TBranch        *b_jets_mass;   //!
   TBranch        *b_jets_area;   //!
   TBranch        *b_jets_fHPD;   //!
   TBranch        *b_jets_approximatefHPD;   //!
   TBranch        *b_jets_genPartonET;   //!
   TBranch        *b_jets_genPartonPT;   //!
   TBranch        *b_jets_genPartonEta;   //!
   TBranch        *b_jets_genPartonPhi;   //!
   TBranch        *b_jets_genJetET;   //!
   TBranch        *b_jets_genJetPT;   //!
   TBranch        *b_jets_genJetEta;   //!
   TBranch        *b_jets_genJetPhi;   //!
   TBranch        *b_jets_btagTChighPur;   //!
   TBranch        *b_jets_btagTChighEff;   //!
   TBranch        *b_jets_btagJetProb;   //!
   TBranch        *b_jets_btagJetBProb;   //!
   TBranch        *b_jets_btagSoftEle;   //!
   TBranch        *b_jets_btagSoftMuon;   //!
   TBranch        *b_jets_btagSoftMuonNoIP;   //!
   TBranch        *b_jets_btagSecVertex;   //!
   TBranch        *b_jets_btagSecVertexHighEff;   //!
   TBranch        *b_jets_btagSecVertexHighPur;   //!
   TBranch        *b_jets_btagCombinedSecVertex;   //!
   TBranch        *b_jets_btagCombinedSecVertexMVA;   //!
   TBranch        *b_jets_btagSoftMuonByPt;   //!
   TBranch        *b_jets_btagSoftMuonByIP3;   //!
   TBranch        *b_jets_btagSoftElectronByPt;   //!
   TBranch        *b_jets_btagSoftElectronByIP3;   //!
   TBranch        *b_jets_n90Hits;   //!
   TBranch        *b_jets_hitsInN90;   //!
   TBranch        *b_jets_chargedHadronEnergyFraction;   //!
   TBranch        *b_jets_neutralHadronEnergyFraction;   //!
   TBranch        *b_jets_chargedEmEnergyFraction;   //!
   TBranch        *b_jets_neutralEmEnergyFraction;   //!
   TBranch        *b_jets_fLong;   //!
   TBranch        *b_jets_fShort;   //!
   TBranch        *b_jets_etaetaMoment;   //!
   TBranch        *b_jets_phiphiMoment;   //!
   TBranch        *b_jets_JESunc;   //!
   TBranch        *b_jets_JECuncUp;   //!
   TBranch        *b_jets_JECuncDown;   //!
   TBranch        *b_jets_puJetMVA_full;   //!
   TBranch        *b_jets_puJetMVA_simple;   //!
   TBranch        *b_jets_puJetMVA_cutbased;   //!
   TBranch        *b_jets_dZ;   //!
   TBranch        *b_jets_dR2Mean;   //!
   TBranch        *b_jets_dRMean;   //!
   TBranch        *b_jets_frac01;   //!
   TBranch        *b_jets_frac02;   //!
   TBranch        *b_jets_frac03;   //!
   TBranch        *b_jets_frac04;   //!
   TBranch        *b_jets_frac05;   //!
   TBranch        *b_jets_frac06;   //!
   TBranch        *b_jets_frac07;   //!
   TBranch        *b_jets_beta;   //!
   TBranch        *b_jets_betaStar;   //!
   TBranch        *b_jets_betaClassic;   //!
   TBranch        *b_jets_betaStarClassic;   //!
   TBranch        *b_jets_ptD;   //!
   TBranch        *b_jets_nvtx;   //!
   TBranch        *b_jets_d0;   //!
   TBranch        *b_jets_leadCandPt;   //!
   TBranch        *b_jets_leadCandVx;   //!
   TBranch        *b_jets_leadCandVy;   //!
   TBranch        *b_jets_leadCandVz;   //!
   TBranch        *b_jets_leadCandDistFromPV;   //!
   TBranch        *b_jets_flavour;   //!
   TBranch        *b_jets_Nconst;   //!
   TBranch        *b_jets_jetIDMinimal;   //!
   TBranch        *b_jets_jetIDLooseAOD;   //!
   TBranch        *b_jets_jetIDLoose;   //!
   TBranch        *b_jets_jetIDTight;   //!
   TBranch        *b_jets_genPartonId;   //!
   TBranch        *b_jets_genPartonMotherId;   //!
   TBranch        *b_jets_genPartonMother0Id;   //!
   TBranch        *b_jets_genPartonMother1Id;   //!
   TBranch        *b_jets_genPartonGrandMotherId;   //!
   TBranch        *b_jets_genPartonGrandMother00Id;   //!
   TBranch        *b_jets_genPartonGrandMother01Id;   //!
   TBranch        *b_jets_genPartonGrandMother10Id;   //!
   TBranch        *b_jets_genPartonGrandMother11Id;   //!
   TBranch        *b_jets_chargedMultiplicity;   //!
   TBranch        *b_jets_neutralMultiplicity;   //!
   TBranch        *b_jets_nconstituents;   //!
   TBranch        *b_jets_nHit;   //!
   TBranch        *b_jets_puJetId_full;   //!
   TBranch        *b_jets_puJetId_simple;   //!
   TBranch        *b_jets_puJetId_cutbased;   //!
   TBranch        *b_jets_puJetId_tight_full;   //!
   TBranch        *b_jets_puJetId_tight_simple;   //!
   TBranch        *b_jets_puJetId_tight_cutbased;   //!
   TBranch        *b_jets_puJetId_medium_full;   //!
   TBranch        *b_jets_puJetId_medium_simple;   //!
   TBranch        *b_jets_puJetId_medium_cutbased;   //!
   TBranch        *b_jets_puJetId_loose_full;   //!
   TBranch        *b_jets_puJetId_loose_simple;   //!
   TBranch        *b_jets_puJetId_loose_cutbased;   //!
   TBranch        *b_genjets_pt;   //!
   TBranch        *b_genjets_eta;   //!
   TBranch        *b_genjets_phi;   //!
   TBranch        *b_genjets_px;   //!
   TBranch        *b_genjets_py;   //!
   TBranch        *b_genjets_pz;   //!
   TBranch        *b_genjets_et;   //!
   TBranch        *b_genjets_energy;   //!
   TBranch        *b_genjets_mass;   //!
   TBranch        *b_genjets_emEnergy;   //!
   TBranch        *b_genjets_hadEnergy;   //!
   TBranch        *b_genjets_invisibleEnergy;   //!
   TBranch        *b_genjets_auxiliaryEnergy;   //!
   TBranch        *b_genjets_charge;   //!
   TBranch        *b_superclusters_energy;   //!
   TBranch        *b_superclusters_et;   //!
   TBranch        *b_superclusters_ex;   //!
   TBranch        *b_superclusters_ey;   //!
   TBranch        *b_superclusters_ez;   //!
   TBranch        *b_superclusters_phi;   //!
   TBranch        *b_superclusters_eta;   //!
   TBranch        *b_superclusters_theta;   //!

   BNTree(TTree *tree=0);
   virtual ~BNTree();
   virtual Int_t    Cut(Long64_t entry);
   virtual Int_t    GetEntry(Long64_t entry);
   virtual Long64_t LoadTree(Long64_t entry);
   virtual void     Init(TTree *tree);
   virtual void     Loop(TString outFile="");
   virtual Bool_t   Notify();
   virtual void     Show(Long64_t entry = -1);
};

#endif

#ifdef BNTree_cxx
BNTree::BNTree(TTree *tree) : fChain(0) 
{
// if parameter tree is not specified (or zero), connect the file
// used to generate this class and read the Tree.
   if (tree == 0) {  
      TFile *f = (TFile*)gROOT->GetListOfFiles()->FindObject("condor/condor_2013_06_06_BNTreeTest/ZZ/hist_0.root");
      if (!f || !f->IsOpen()) {
         f = new TFile("condor/condor_2013_06_06_BNTreeTest/ZZ/hist_0.root");
      }
      TDirectory * dir = (TDirectory*)f->Get("condor/condor_2013_06_06_BNTreeTest/ZZ/hist_0.root:/OSUAnalysis/WToMuSimple");
      dir->GetObject("BNTree_WToMuSimple",tree);

   }
   Init(tree);
}

BNTree::~BNTree()
{
   if (!fChain) return;
   delete fChain->GetCurrentFile();
}

Int_t BNTree::GetEntry(Long64_t entry)
{
// Read contents of entry.
   if (!fChain) return 0;
   return fChain->GetEntry(entry);
}
Long64_t BNTree::LoadTree(Long64_t entry)
{
// Set the environment to read one entry
   if (!fChain) return -5;
   Long64_t centry = fChain->LoadTree(entry);
   if (centry < 0) return centry;
   if (fChain->GetTreeNumber() != fCurrent) {
      fCurrent = fChain->GetTreeNumber();
      Notify();
   }
   return centry;
}

void BNTree::Init(TTree *tree)
{
   // The Init() function is called when the selector needs to initialize
   // a new tree or chain. Typically here the branch addresses and branch
   // pointers of the tree will be set.
   // It is normally not necessary to make changes to the generated
   // code, but the routine can be extended by the user if needed.
   // Init() will be called many times when running on PROOF
   // (once per file to be processed).

   // Set object pointer
   events_weight = 0;
   events_pthat = 0;
   events_qScale = 0;
   events_alphaQCD = 0;
   events_alphaQED = 0;
   events_scalePDF = 0;
   events_x1 = 0;
   events_x2 = 0;
   events_xPDF1 = 0;
   events_xPDF2 = 0;
   events_BSx = 0;
   events_BSy = 0;
   events_BSz = 0;
   events_PVx = 0;
   events_PVy = 0;
   events_PVz = 0;
   events_bField = 0;
   events_instLumi = 0;
   events_bxLumi = 0;
   events_FilterOutScrapingFraction = 0;
   events_sumNVtx = 0;
   events_sumTrueNVtx = 0;
   events_nm1_true = 0;
   events_n0_true = 0;
   events_np1_true = 0;
   events_numTruePV = 0;
   events_Q2ScaleUpWgt = 0;
   events_Q2ScaleDownWgt = 0;
   events_rho_kt6PFJets = 0;
   events_rho_kt6PFJetsCentralChargedPileUp = 0;
   events_rho_kt6PFJetsCentralNeutral = 0;
   events_rho_kt6PFJetsCentralNeutralTight = 0;
   events_run = 0;
   events_lumi = 0;
   events_sample = 0;
   events_numPV = 0;
   events_W0decay = 0;
   events_W1decay = 0;
   events_Z0decay = 0;
   events_Z1decay = 0;
   events_H0decay = 0;
   events_H1decay = 0;
   events_hcalnoiseLoose = 0;
   events_hcalnoiseTight = 0;
   events_GoodVertex = 0;
   events_FilterOutScraping = 0;
   events_HBHENoiseFilter = 0;
   events_CSCLooseHaloId = 0;
   events_CSCTightHaloId = 0;
   events_EcalLooseHaloId = 0;
   events_EcalTightHaloId = 0;
   events_HcalLooseHaloId = 0;
   events_HcalTightHaloId = 0;
   events_GlobalLooseHaloId = 0;
   events_GlobalTightHaloId = 0;
   events_LooseId = 0;
   events_TightId = 0;
   events_numGenPV = 0;
   events_nm1 = 0;
   events_n0 = 0;
   events_np1 = 0;
   events_id1 = 0;
   events_id2 = 0;
   events_evt = 0;
   events_puScaleFactor = 0;
   events_muonScaleFactor = 0;
   events_electronScaleFactor = 0;
   events_stopCTauScaleFactor = 0;
   muons_energy = 0;
   muons_et = 0;
   muons_pt = 0;
   muons_px = 0;
   muons_py = 0;
   muons_pz = 0;
   muons_phi = 0;
   muons_eta = 0;
   muons_theta = 0;
   muons_trackIso = 0;
   muons_ecalIso = 0;
   muons_hcalIso = 0;
   muons_caloIso = 0;
   muons_trackIsDR03 = 0;
   muons_ecalIsoDR03 = 0;
   muons_hcalIsoDR03 = 0;
   muons_caloIsoDR03 = 0;
   muons_trackVetoIsoDR03 = 0;
   muons_ecalVetoIsoDR03 = 0;
   muons_hcalVetoIsoDR03 = 0;
   muons_caloVetoIsoDR03 = 0;
   muons_trackIsoDR05 = 0;
   muons_ecalIsoDR05 = 0;
   muons_hcalIsoDR05 = 0;
   muons_caloIsoDR05 = 0;
   muons_trackVetoIsoDR05 = 0;
   muons_ecalVetoIsoDR05 = 0;
   muons_hcalVetoIsoDR05 = 0;
   muons_caloVetoIsoDR05 = 0;
   muons_hcalE = 0;
   muons_ecalE = 0;
   muons_genET = 0;
   muons_genPT = 0;
   muons_genPhi = 0;
   muons_genEta = 0;
   muons_genMotherET = 0;
   muons_genMotherPT = 0;
   muons_genMotherPhi = 0;
   muons_genMotherEta = 0;
   muons_vx = 0;
   muons_vy = 0;
   muons_vz = 0;
   muons_tkNormChi2 = 0;
   muons_tkPT = 0;
   muons_tkEta = 0;
   muons_tkPhi = 0;
   muons_tkDZ = 0;
   muons_tkD0 = 0;
   muons_tkD0bs = 0;
   muons_tkD0err = 0;
   muons_samNormChi2 = 0;
   muons_samPT = 0;
   muons_samEta = 0;
   muons_samPhi = 0;
   muons_samDZ = 0;
   muons_samD0 = 0;
   muons_samD0bs = 0;
   muons_samD0err = 0;
   muons_comNormChi2 = 0;
   muons_comPT = 0;
   muons_comEta = 0;
   muons_comPhi = 0;
   muons_comDZ = 0;
   muons_comD0 = 0;
   muons_comD0bs = 0;
   muons_comD0err = 0;
   muons_isolationR03emVetoEt = 0;
   muons_isolationR03hadVetoEt = 0;
   muons_normalizedChi2 = 0;
   muons_dVzPVz = 0;
   muons_dB = 0;
   muons_ptErr = 0;
   muons_innerTrackNormChi2 = 0;
   muons_correctedD0 = 0;
   muons_correctedD0Vertex = 0;
   muons_correctedDZ = 0;
   muons_particleIso = 0;
   muons_chargedHadronIso = 0;
   muons_neutralHadronIso = 0;
   muons_photonIso = 0;
   muons_puChargedHadronIso = 0;
   muons_chargedHadronIsoDR03 = 0;
   muons_neutralHadronIsoDR03 = 0;
   muons_photonIsoDR03 = 0;
   muons_puChargedHadronIsoDR03 = 0;
   muons_chargedHadronIsoDR04 = 0;
   muons_neutralHadronIsoDR04 = 0;
   muons_photonIsoDR04 = 0;
   muons_puChargedHadronIsoDR04 = 0;
   muons_rhoPrime = 0;
   muons_AEffDr03 = 0;
   muons_AEffDr04 = 0;
   muons_pfIsoR03SumChargedHadronPt = 0;
   muons_pfIsoR03SumNeutralHadronEt = 0;
   muons_pfIsoR03SumPhotonEt = 0;
   muons_pfIsoR03SumPUPt = 0;
   muons_pfIsoR04SumChargedHadronPt = 0;
   muons_pfIsoR04SumNeutralHadronEt = 0;
   muons_pfIsoR04SumPhotonEt = 0;
   muons_pfIsoR04SumPUPt = 0;
   muons_IP = 0;
   muons_IPError = 0;
   muons_timeAtIpInOut = 0;
   muons_timeAtIpInOutErr = 0;
   muons_timeAtIpOutIn = 0;
   muons_timeAtIpOutInErr = 0;
   muons_ecal_time = 0;
   muons_hcal_time = 0;
   muons_ecal_timeError = 0;
   muons_hcal_timeError = 0;
   muons_energy_ecal = 0;
   muons_energy_hcal = 0;
   muons_e3x3_ecal = 0;
   muons_e3x3_hcal = 0;
   muons_energyMax_ecal = 0;
   muons_energyMax_hcal = 0;
   muons_charge = 0;
   muons_IDGMPTight = 0;
   muons_tkNumValidHits = 0;
   muons_tkCharge = 0;
   muons_samNumValidHits = 0;
   muons_samCharge = 0;
   muons_comNumValidHits = 0;
   muons_comCharge = 0;
   muons_genId = 0;
   muons_genCharge = 0;
   muons_genNumberOfMothers = 0;
   muons_genMotherId = 0;
   muons_genMotherCharge = 0;
   muons_genMother0Id = 0;
   muons_genMother1Id = 0;
   muons_genGrandMother00Id = 0;
   muons_genGrandMother01Id = 0;
   muons_genGrandMother10Id = 0;
   muons_genGrandMother11Id = 0;
   muons_isPFMuon = 0;
   muons_isGoodMuon_1StationTight = 0;
   muons_isGlobalMuon = 0;
   muons_isTrackerMuon = 0;
   muons_isStandAloneMuon = 0;
   muons_isGlobalMuonPromptTight = 0;
   muons_numberOfValidMuonHits = 0;
   muons_numberOfValidTrackerHits = 0;
   muons_numberOfLayersWithMeasurement = 0;
   muons_pixelLayersWithMeasurement = 0;
   muons_numberOfMatches = 0;
   muons_numberOfValidTrackerHitsInnerTrack = 0;
   muons_numberOfValidPixelHits = 0;
   muons_numberOfMatchedStations = 0;
   muons_time_ndof = 0;
   muons_correctedD0VertexErr = 0;
   muons_correctedD0VertexSig = 0;
   muons_detIso = 0;
   muons_relPFdBetaIso = 0;
   muons_relPFrhoIso = 0;
   muons_metMT = 0;
   muons_correctedD0VertexInEBPlus = 0;
   muons_correctedD0VertexOutEBPlus = 0;
   muons_correctedD0VertexEEPlus = 0;
   muons_correctedD0BeamspotInEBPlus = 0;
   muons_correctedD0BeamspotOutEBPlus = 0;
   muons_correctedD0BeamspotEEPlus = 0;
   muons_correctedD0VertexInEBMinus = 0;
   muons_correctedD0VertexOutEBMinus = 0;
   muons_correctedD0VertexEEMinus = 0;
   muons_correctedD0BeamspotInEBMinus = 0;
   muons_correctedD0BeamspotOutEBMinus = 0;
   muons_correctedD0BeamspotEEMinus = 0;
   muons_correctedD0VertexInEBPositiveCharge = 0;
   muons_correctedD0VertexOutEBPositiveCharge = 0;
   muons_correctedD0VertexEEPositiveCharge = 0;
   muons_correctedD0BeamspotInEBPositiveCharge = 0;
   muons_correctedD0BeamspotOutEBPositiveCharge = 0;
   muons_correctedD0BeamspotEEPositiveCharge = 0;
   muons_correctedD0VertexInEBNegativeCharge = 0;
   muons_correctedD0VertexOutEBNegativeCharge = 0;
   muons_correctedD0VertexEENegativeCharge = 0;
   muons_correctedD0BeamspotInEBNegativeCharge = 0;
   muons_correctedD0BeamspotOutEBNegativeCharge = 0;
   muons_correctedD0BeamspotEENegativeCharge = 0;
   muons_tightID = 0;
   muons_tightIDdisplaced = 0;
   muons_genDeltaRLowest = 0;
   muons_genMatchedPdgId = 0;
   muons_genMatchedId = 0;
   muons_genMatchedMotherId = 0;
   muons_genMatchedMotherIdReverse = 0;
   muons_genMatchedGrandmotherId = 0;
   muons_genMatchedGrandmotherIdReverse = 0;
   muons_pfMuonsFromVertex = 0;
   electrons_energy = 0;
   electrons_et = 0;
   electrons_gsfEt = 0;
   electrons_pt = 0;
   electrons_px = 0;
   electrons_py = 0;
   electrons_pz = 0;
   electrons_phi = 0;
   electrons_eta = 0;
   electrons_theta = 0;
   electrons_pIn = 0;
   electrons_pOut = 0;
   electrons_EscOverPin = 0;
   electrons_EseedOverPout = 0;
   electrons_hadOverEm = 0;
   electrons_trackIso = 0;
   electrons_ecalIso = 0;
   electrons_hcalIso = 0;
   electrons_caloIso = 0;
   electrons_trackIsoDR03 = 0;
   electrons_ecalIsoDR03 = 0;
   electrons_hcalIsoDR03 = 0;
   electrons_hcalIsoDR03depth1 = 0;
   electrons_hcalIsoDR03depth2 = 0;
   electrons_caloIsoDR03 = 0;
   electrons_trackIsoDR04 = 0;
   electrons_ecalIsoDR04 = 0;
   electrons_hcalIsoDR04 = 0;
   electrons_hcalIsoDR04depth1 = 0;
   electrons_hcalIsoDR04depth2 = 0;
   electrons_caloIsoDR04 = 0;
   electrons_fbrem = 0;
   electrons_absInvEMinusInvPin = 0;
   electrons_delPhiIn = 0;
   electrons_delEtaIn = 0;
   electrons_genET = 0;
   electrons_genPT = 0;
   electrons_genPhi = 0;
   electrons_genEta = 0;
   electrons_genMotherET = 0;
   electrons_genMotherPT = 0;
   electrons_genMotherPhi = 0;
   electrons_genMotherEta = 0;
   electrons_vx = 0;
   electrons_vy = 0;
   electrons_vz = 0;
   electrons_scEnergy = 0;
   electrons_scRawEnergy = 0;
   electrons_scSigmaEtaEta = 0;
   electrons_scSigmaIEtaIEta = 0;
   electrons_scE1x5 = 0;
   electrons_scE2x5Max = 0;
   electrons_scE5x5 = 0;
   electrons_scEt = 0;
   electrons_scEta = 0;
   electrons_scPhi = 0;
   electrons_scZ = 0;
   electrons_tkNormChi2 = 0;
   electrons_tkPT = 0;
   electrons_tkEta = 0;
   electrons_tkPhi = 0;
   electrons_tkDZ = 0;
   electrons_tkD0 = 0;
   electrons_tkD0bs = 0;
   electrons_tkD0err = 0;
   electrons_mva = 0;
   electrons_mvaTrigV0 = 0;
   electrons_mvaNonTrigV0 = 0;
   electrons_dist = 0;
   electrons_dcot = 0;
   electrons_convradius = 0;
   electrons_convPointX = 0;
   electrons_convPointY = 0;
   electrons_convPointZ = 0;
   electrons_eMax = 0;
   electrons_eLeft = 0;
   electrons_eRight = 0;
   electrons_eTop = 0;
   electrons_eBottom = 0;
   electrons_e3x3 = 0;
   electrons_swissCross = 0;
   electrons_seedEnergy = 0;
   electrons_seedTime = 0;
   electrons_swissCrossNoI85 = 0;
   electrons_swissCrossI85 = 0;
   electrons_E2overE9NoI85 = 0;
   electrons_E2overE9I85 = 0;
   electrons_correctedD0 = 0;
   electrons_correctedD0Vertex = 0;
   electrons_correctedDZ = 0;
   electrons_particleIso = 0;
   electrons_chargedHadronIso = 0;
   electrons_neutralHadronIso = 0;
   electrons_photonIso = 0;
   electrons_puChargedHadronIso = 0;
   electrons_chargedHadronIsoDR03 = 0;
   electrons_neutralHadronIsoDR03 = 0;
   electrons_photonIsoDR03 = 0;
   electrons_puChargedHadronIsoDR03 = 0;
   electrons_chargedHadronIsoDR04 = 0;
   electrons_neutralHadronIsoDR04 = 0;
   electrons_photonIsoDR04 = 0;
   electrons_puChargedHadronIsoDR04 = 0;
   electrons_rhoPrime = 0;
   electrons_AEffDr03 = 0;
   electrons_AEffDr04 = 0;
   electrons_IP = 0;
   electrons_IPError = 0;
   electrons_charge = 0;
   electrons_classification = 0;
   electrons_genId = 0;
   electrons_genCharge = 0;
   electrons_genNumberOfMothers = 0;
   electrons_genMotherId = 0;
   electrons_genMotherCharge = 0;
   electrons_genMother0Id = 0;
   electrons_genMother1Id = 0;
   electrons_genGrandMother00Id = 0;
   electrons_genGrandMother01Id = 0;
   electrons_genGrandMother10Id = 0;
   electrons_genGrandMother11Id = 0;
   electrons_numClusters = 0;
   electrons_tkNumValidHits = 0;
   electrons_tkCharge = 0;
   electrons_gsfCharge = 0;
   electrons_isEB = 0;
   electrons_isEE = 0;
   electrons_isGap = 0;
   electrons_isEBEEGap = 0;
   electrons_isEBGap = 0;
   electrons_isEEGap = 0;
   electrons_isEcalDriven = 0;
   electrons_isTrackerDriven = 0;
   electrons_numberOfLostHits = 0;
   electrons_numberOfExpectedInnerHits = 0;
   electrons_numberOfValidPixelHits = 0;
   electrons_numberOfValidPixelBarrelHits = 0;
   electrons_numberOfValidPixelEndcapHits = 0;
   electrons_isHEEP = 0;
   electrons_isHEEPnoEt = 0;
   electrons_seedRecoFlag = 0;
   electrons_eidRobustHighEnergy = 0;
   electrons_eidRobustLoose = 0;
   electrons_eidRobustTight = 0;
   electrons_eidLoose = 0;
   electrons_eidTight = 0;
   electrons_eidVeryLooseMC = 0;
   electrons_eidLooseMC = 0;
   electrons_eidMediumMC = 0;
   electrons_eidTightMC = 0;
   electrons_eidSuperTightMC = 0;
   electrons_eidHyperTight1MC = 0;
   electrons_eidHyperTight2MC = 0;
   electrons_eidHyperTight3MC = 0;
   electrons_eidHyperTight4MC = 0;
   electrons_passConvVeto = 0;
   electrons_correctedD0VertexErr = 0;
   electrons_correctedD0VertexSig = 0;
   electrons_detIso = 0;
   electrons_relPFrhoIso = 0;
   electrons_metMT = 0;
   electrons_correctedD0VertexEEPositiveChargeLowPt = 0;
   electrons_correctedD0VertexEEPositiveChargeHighPt = 0;
   electrons_correctedD0VertexInEBPlus = 0;
   electrons_correctedD0VertexOutEBPlus = 0;
   electrons_correctedD0VertexEEPlus = 0;
   electrons_correctedD0BeamspotInEBPlus = 0;
   electrons_correctedD0BeamspotOutEBPlus = 0;
   electrons_correctedD0BeamspotEEPlus = 0;
   electrons_correctedD0VertexInEBMinus = 0;
   electrons_correctedD0VertexOutEBMinus = 0;
   electrons_correctedD0VertexEEMinus = 0;
   electrons_correctedD0BeamspotInEBMinus = 0;
   electrons_correctedD0BeamspotOutEBMinus = 0;
   electrons_correctedD0BeamspotEEMinus = 0;
   electrons_tightID = 0;
   electrons_correctedD0VertexInEBPositiveCharge = 0;
   electrons_correctedD0VertexOutEBPositiveCharge = 0;
   electrons_correctedD0VertexEEPositiveCharge = 0;
   electrons_correctedD0BeamspotInEBPositiveCharge = 0;
   electrons_correctedD0BeamspotOutEBPositiveCharge = 0;
   electrons_correctedD0BeamspotEEPositiveCharge = 0;
   electrons_correctedD0VertexInEBNegativeCharge = 0;
   electrons_correctedD0VertexOutEBNegativeCharge = 0;
   electrons_correctedD0VertexEENegativeCharge = 0;
   electrons_correctedD0BeamspotInEBNegativeCharge = 0;
   electrons_correctedD0BeamspotOutEBNegativeCharge = 0;
   electrons_correctedD0BeamspotEENegativeCharge = 0;
   electrons_tightIDdisplaced = 0;
   electrons_genDeltaRLowest = 0;
   electrons_genMatchedPdgId = 0;
   electrons_genMatchedId = 0;
   electrons_genMatchedMotherId = 0;
   electrons_genMatchedMotherIdReverse = 0;
   electrons_genMatchedGrandmotherId = 0;
   electrons_genMatchedGrandmotherIdReverse = 0;
   electrons_pfElectronsFromVertex = 0;
   taus_px = 0;
   taus_py = 0;
   taus_pz = 0;
   taus_energy = 0;
   taus_et = 0;
   taus_pt = 0;
   taus_eta = 0;
   taus_phi = 0;
   taus_emFraction = 0;
   taus_leadingTrackPt = 0;
   taus_leadingTrackIpVtdxy = 0;
   taus_leadingTrackIpVtdz = 0;
   taus_leadingTrackIpVtdxyError = 0;
   taus_leadingTrackIpVtdzError = 0;
   taus_leadingTrackVx = 0;
   taus_leadingTrackVy = 0;
   taus_leadingTrackVz = 0;
   taus_leadingTrackValidHits = 0;
   taus_leadingTrackNormChiSqrd = 0;
   taus_numProngs = 0;
   taus_numSignalGammas = 0;
   taus_numSignalNeutrals = 0;
   taus_numSignalPiZeros = 0;
   taus_decayMode = 0;
   taus_charge = 0;
   taus_inTheCracks = 0;
   taus_HPSagainstElectronLoose = 0;
   taus_HPSagainstElectronMVA = 0;
   taus_HPSagainstElectronMedium = 0;
   taus_HPSagainstElectronTight = 0;
   taus_HPSagainstMuonLoose = 0;
   taus_HPSagainstMuonMedium = 0;
   taus_HPSagainstMuonTight = 0;
   taus_HPSbyLooseCombinedIsolationDeltaBetaCorr = 0;
   taus_HPSbyMediumCombinedIsolationDeltaBetaCorr = 0;
   taus_HPSbyTightCombinedIsolationDeltaBetaCorr = 0;
   taus_HPSbyVLooseCombinedIsolationDeltaBetaCorr = 0;
   taus_HPSdecayModeFinding = 0;
   taus_leadingTrackValid = 0;
   taus_genDeltaRLowest = 0;
   taus_genMatchedPdgId = 0;
   taus_genMatchedId = 0;
   taus_genMatchedMotherId = 0;
   taus_genMatchedMotherIdReverse = 0;
   taus_genMatchedGrandmotherId = 0;
   taus_genMatchedGrandmotherIdReverse = 0;
   tracks_pt = 0;
   tracks_px = 0;
   tracks_py = 0;
   tracks_pz = 0;
   tracks_phi = 0;
   tracks_eta = 0;
   tracks_theta = 0;
   tracks_normChi2 = 0;
   tracks_dZ = 0;
   tracks_d0 = 0;
   tracks_d0err = 0;
   tracks_vx = 0;
   tracks_vy = 0;
   tracks_vz = 0;
   tracks_charge = 0;
   tracks_numValidHits = 0;
   tracks_isHighPurity = 0;
   tracks_caloEMDeltaRp3 = 0;
   tracks_caloHadDeltaRp3 = 0;
   tracks_caloEMDeltaRp4 = 0;
   tracks_caloHadDeltaRp4 = 0;
   tracks_caloEMDeltaRp5 = 0;
   tracks_caloHadDeltaRp5 = 0;
   tracks_nTracksRp5 = 0;
   tracks_nHitsMissingOuter = 0;
   tracks_nHitsMissingInner = 0;
   tracks_nHitsMissingMiddle = 0;
   tracks_depTrkRp5 = 0;
   tracks_d0wrtBS = 0;
   tracks_dZwrtBS = 0;
   tracks_depTrkRp5MinusPt = 0;
   tracks_caloTotDeltaRp5 = 0;
   tracks_caloTotDeltaRp5ByP = 0;
   tracks_caloTotDeltaRp5RhoCorr = 0;
   tracks_caloTotDeltaRp5ByPRhoCorr = 0;
   tracks_isIso = 0;
   tracks_isMatchedDeadEcal = 0;
   tracks_ptErrorByPt = 0;
   tracks_ptError = 0;
   tracks_ptRes = 0;
   tracks_d0wrtPV = 0;
   tracks_dZwrtPV = 0;
   tracks_genDeltaRLowest = 0;
   tracks_genMatchedPdgId = 0;
   tracks_genMatchedId = 0;
   tracks_genMatchedMotherId = 0;
   tracks_genMatchedMotherIdReverse = 0;
   tracks_genMatchedGrandmotherId = 0;
   tracks_genMatchedGrandmotherIdReverse = 0;
   mets_et = 0;
   mets_pt = 0;
   mets_px = 0;
   mets_py = 0;
   mets_phi = 0;
   mets_Upt = 0;
   mets_Uphi = 0;
   mets_NeutralEMFraction = 0;
   mets_NeutralHadEtFraction = 0;
   mets_ChargedEMEtFraction = 0;
   mets_ChargedHadEtFraction = 0;
   mets_MuonEtFraction = 0;
   mets_Type6EtFraction = 0;
   mets_Type7EtFraction = 0;
   mets_genPT = 0;
   mets_genPhi = 0;
   mets_muonCorEx = 0;
   mets_muonCorEy = 0;
   mets_jet20CorEx = 0;
   mets_jet20CorEy = 0;
   mets_jet1CorEx = 0;
   mets_jet1CorEy = 0;
   mets_sumET = 0;
   mets_corSumET = 0;
   mets_mEtSig = 0;
   mets_metSignificance = 0;
   mets_significance = 0;
   mets_sigmaX2 = 0;
   mets_sigmaY2 = 0;
   mets_sigmaXY = 0;
   mets_sigmaYX = 0;
   mets_maxEtInEmTowers = 0;
   mets_emEtFraction = 0;
   mets_emEtInEB = 0;
   mets_emEtInEE = 0;
   mets_emEtInHF = 0;
   mets_maxEtInHadTowers = 0;
   mets_hadEtFraction = 0;
   mets_hadEtInHB = 0;
   mets_hadEtInHE = 0;
   mets_hadEtInHF = 0;
   mets_hadEtInHO = 0;
   mets_UDeltaPx = 0;
   mets_UDeltaPy = 0;
   mets_UDeltaP = 0;
   mets_Uscale = 0;
   mets_type2corPx = 0;
   mets_type2corPy = 0;
   mets_T2pt = 0;
   mets_T2px = 0;
   mets_T2py = 0;
   mets_T2phi = 0;
   mets_T2sumET = 0;
   mets_pfT1jet1pt = 0;
   mets_pfT1jet1phi = 0;
   mets_pfT1jet6pt = 0;
   mets_pfT1jet6phi = 0;
   mets_pfT1jet10pt = 0;
   mets_pfT1jet10phi = 0;
   jets_energy = 0;
   jets_et = 0;
   jets_pt = 0;
   jets_px = 0;
   jets_py = 0;
   jets_pz = 0;
   jets_phi = 0;
   jets_eta = 0;
   jets_theta = 0;
   jets_Upt = 0;
   jets_Uenergy = 0;
   jets_L2pt = 0;
   jets_L2L3pt = 0;
   jets_L2L3respt = 0;
   jets_respt = 0;
   jets_EMfrac = 0;
   jets_Hadfrac = 0;
   jets_charge = 0;
   jets_mass = 0;
   jets_area = 0;
   jets_fHPD = 0;
   jets_approximatefHPD = 0;
   jets_genPartonET = 0;
   jets_genPartonPT = 0;
   jets_genPartonEta = 0;
   jets_genPartonPhi = 0;
   jets_genJetET = 0;
   jets_genJetPT = 0;
   jets_genJetEta = 0;
   jets_genJetPhi = 0;
   jets_btagTChighPur = 0;
   jets_btagTChighEff = 0;
   jets_btagJetProb = 0;
   jets_btagJetBProb = 0;
   jets_btagSoftEle = 0;
   jets_btagSoftMuon = 0;
   jets_btagSoftMuonNoIP = 0;
   jets_btagSecVertex = 0;
   jets_btagSecVertexHighEff = 0;
   jets_btagSecVertexHighPur = 0;
   jets_btagCombinedSecVertex = 0;
   jets_btagCombinedSecVertexMVA = 0;
   jets_btagSoftMuonByPt = 0;
   jets_btagSoftMuonByIP3 = 0;
   jets_btagSoftElectronByPt = 0;
   jets_btagSoftElectronByIP3 = 0;
   jets_n90Hits = 0;
   jets_hitsInN90 = 0;
   jets_chargedHadronEnergyFraction = 0;
   jets_neutralHadronEnergyFraction = 0;
   jets_chargedEmEnergyFraction = 0;
   jets_neutralEmEnergyFraction = 0;
   jets_fLong = 0;
   jets_fShort = 0;
   jets_etaetaMoment = 0;
   jets_phiphiMoment = 0;
   jets_JESunc = 0;
   jets_JECuncUp = 0;
   jets_JECuncDown = 0;
   jets_puJetMVA_full = 0;
   jets_puJetMVA_simple = 0;
   jets_puJetMVA_cutbased = 0;
   jets_dZ = 0;
   jets_dR2Mean = 0;
   jets_dRMean = 0;
   jets_frac01 = 0;
   jets_frac02 = 0;
   jets_frac03 = 0;
   jets_frac04 = 0;
   jets_frac05 = 0;
   jets_frac06 = 0;
   jets_frac07 = 0;
   jets_beta = 0;
   jets_betaStar = 0;
   jets_betaClassic = 0;
   jets_betaStarClassic = 0;
   jets_ptD = 0;
   jets_nvtx = 0;
   jets_d0 = 0;
   jets_leadCandPt = 0;
   jets_leadCandVx = 0;
   jets_leadCandVy = 0;
   jets_leadCandVz = 0;
   jets_leadCandDistFromPV = 0;
   jets_flavour = 0;
   jets_Nconst = 0;
   jets_jetIDMinimal = 0;
   jets_jetIDLooseAOD = 0;
   jets_jetIDLoose = 0;
   jets_jetIDTight = 0;
   jets_genPartonId = 0;
   jets_genPartonMotherId = 0;
   jets_genPartonMother0Id = 0;
   jets_genPartonMother1Id = 0;
   jets_genPartonGrandMotherId = 0;
   jets_genPartonGrandMother00Id = 0;
   jets_genPartonGrandMother01Id = 0;
   jets_genPartonGrandMother10Id = 0;
   jets_genPartonGrandMother11Id = 0;
   jets_chargedMultiplicity = 0;
   jets_neutralMultiplicity = 0;
   jets_nconstituents = 0;
   jets_nHit = 0;
   jets_puJetId_full = 0;
   jets_puJetId_simple = 0;
   jets_puJetId_cutbased = 0;
   jets_puJetId_tight_full = 0;
   jets_puJetId_tight_simple = 0;
   jets_puJetId_tight_cutbased = 0;
   jets_puJetId_medium_full = 0;
   jets_puJetId_medium_simple = 0;
   jets_puJetId_medium_cutbased = 0;
   jets_puJetId_loose_full = 0;
   jets_puJetId_loose_simple = 0;
   jets_puJetId_loose_cutbased = 0;
   genjets_pt = 0;
   genjets_eta = 0;
   genjets_phi = 0;
   genjets_px = 0;
   genjets_py = 0;
   genjets_pz = 0;
   genjets_et = 0;
   genjets_energy = 0;
   genjets_mass = 0;
   genjets_emEnergy = 0;
   genjets_hadEnergy = 0;
   genjets_invisibleEnergy = 0;
   genjets_auxiliaryEnergy = 0;
   genjets_charge = 0;
   superclusters_energy = 0;
   superclusters_et = 0;
   superclusters_ex = 0;
   superclusters_ey = 0;
   superclusters_ez = 0;
   superclusters_phi = 0;
   superclusters_eta = 0;
   superclusters_theta = 0;
   // Set branch addresses and branch pointers
   if (!tree) return;
   fChain = tree;
   fCurrent = -1;
   fChain->SetMakeClass(1);

   fChain->SetBranchAddress("events_weight", &events_weight, &b_events_weight);
   fChain->SetBranchAddress("events_pthat", &events_pthat, &b_events_pthat);
   fChain->SetBranchAddress("events_qScale", &events_qScale, &b_events_qScale);
   fChain->SetBranchAddress("events_alphaQCD", &events_alphaQCD, &b_events_alphaQCD);
   fChain->SetBranchAddress("events_alphaQED", &events_alphaQED, &b_events_alphaQED);
   fChain->SetBranchAddress("events_scalePDF", &events_scalePDF, &b_events_scalePDF);
   fChain->SetBranchAddress("events_x1", &events_x1, &b_events_x1);
   fChain->SetBranchAddress("events_x2", &events_x2, &b_events_x2);
   fChain->SetBranchAddress("events_xPDF1", &events_xPDF1, &b_events_xPDF1);
   fChain->SetBranchAddress("events_xPDF2", &events_xPDF2, &b_events_xPDF2);
   fChain->SetBranchAddress("events_BSx", &events_BSx, &b_events_BSx);
   fChain->SetBranchAddress("events_BSy", &events_BSy, &b_events_BSy);
   fChain->SetBranchAddress("events_BSz", &events_BSz, &b_events_BSz);
   fChain->SetBranchAddress("events_PVx", &events_PVx, &b_events_PVx);
   fChain->SetBranchAddress("events_PVy", &events_PVy, &b_events_PVy);
   fChain->SetBranchAddress("events_PVz", &events_PVz, &b_events_PVz);
   fChain->SetBranchAddress("events_bField", &events_bField, &b_events_bField);
   fChain->SetBranchAddress("events_instLumi", &events_instLumi, &b_events_instLumi);
   fChain->SetBranchAddress("events_bxLumi", &events_bxLumi, &b_events_bxLumi);
   fChain->SetBranchAddress("events_FilterOutScrapingFraction", &events_FilterOutScrapingFraction, &b_events_FilterOutScrapingFraction);
   fChain->SetBranchAddress("events_sumNVtx", &events_sumNVtx, &b_events_sumNVtx);
   fChain->SetBranchAddress("events_sumTrueNVtx", &events_sumTrueNVtx, &b_events_sumTrueNVtx);
   fChain->SetBranchAddress("events_nm1_true", &events_nm1_true, &b_events_nm1_true);
   fChain->SetBranchAddress("events_n0_true", &events_n0_true, &b_events_n0_true);
   fChain->SetBranchAddress("events_np1_true", &events_np1_true, &b_events_np1_true);
   fChain->SetBranchAddress("events_numTruePV", &events_numTruePV, &b_events_numTruePV);
   fChain->SetBranchAddress("events_Q2ScaleUpWgt", &events_Q2ScaleUpWgt, &b_events_Q2ScaleUpWgt);
   fChain->SetBranchAddress("events_Q2ScaleDownWgt", &events_Q2ScaleDownWgt, &b_events_Q2ScaleDownWgt);
   fChain->SetBranchAddress("events_rho_kt6PFJets", &events_rho_kt6PFJets, &b_events_rho_kt6PFJets);
   fChain->SetBranchAddress("events_rho_kt6PFJetsCentralChargedPileUp", &events_rho_kt6PFJetsCentralChargedPileUp, &b_events_rho_kt6PFJetsCentralChargedPileUp);
   fChain->SetBranchAddress("events_rho_kt6PFJetsCentralNeutral", &events_rho_kt6PFJetsCentralNeutral, &b_events_rho_kt6PFJetsCentralNeutral);
   fChain->SetBranchAddress("events_rho_kt6PFJetsCentralNeutralTight", &events_rho_kt6PFJetsCentralNeutralTight, &b_events_rho_kt6PFJetsCentralNeutralTight);
   fChain->SetBranchAddress("events_run", &events_run, &b_events_run);
   fChain->SetBranchAddress("events_lumi", &events_lumi, &b_events_lumi);
   fChain->SetBranchAddress("events_sample", &events_sample, &b_events_sample);
   fChain->SetBranchAddress("events_numPV", &events_numPV, &b_events_numPV);
   fChain->SetBranchAddress("events_W0decay", &events_W0decay, &b_events_W0decay);
   fChain->SetBranchAddress("events_W1decay", &events_W1decay, &b_events_W1decay);
   fChain->SetBranchAddress("events_Z0decay", &events_Z0decay, &b_events_Z0decay);
   fChain->SetBranchAddress("events_Z1decay", &events_Z1decay, &b_events_Z1decay);
   fChain->SetBranchAddress("events_H0decay", &events_H0decay, &b_events_H0decay);
   fChain->SetBranchAddress("events_H1decay", &events_H1decay, &b_events_H1decay);
   fChain->SetBranchAddress("events_hcalnoiseLoose", &events_hcalnoiseLoose, &b_events_hcalnoiseLoose);
   fChain->SetBranchAddress("events_hcalnoiseTight", &events_hcalnoiseTight, &b_events_hcalnoiseTight);
   fChain->SetBranchAddress("events_GoodVertex", &events_GoodVertex, &b_events_GoodVertex);
   fChain->SetBranchAddress("events_FilterOutScraping", &events_FilterOutScraping, &b_events_FilterOutScraping);
   fChain->SetBranchAddress("events_HBHENoiseFilter", &events_HBHENoiseFilter, &b_events_HBHENoiseFilter);
   fChain->SetBranchAddress("events_CSCLooseHaloId", &events_CSCLooseHaloId, &b_events_CSCLooseHaloId);
   fChain->SetBranchAddress("events_CSCTightHaloId", &events_CSCTightHaloId, &b_events_CSCTightHaloId);
   fChain->SetBranchAddress("events_EcalLooseHaloId", &events_EcalLooseHaloId, &b_events_EcalLooseHaloId);
   fChain->SetBranchAddress("events_EcalTightHaloId", &events_EcalTightHaloId, &b_events_EcalTightHaloId);
   fChain->SetBranchAddress("events_HcalLooseHaloId", &events_HcalLooseHaloId, &b_events_HcalLooseHaloId);
   fChain->SetBranchAddress("events_HcalTightHaloId", &events_HcalTightHaloId, &b_events_HcalTightHaloId);
   fChain->SetBranchAddress("events_GlobalLooseHaloId", &events_GlobalLooseHaloId, &b_events_GlobalLooseHaloId);
   fChain->SetBranchAddress("events_GlobalTightHaloId", &events_GlobalTightHaloId, &b_events_GlobalTightHaloId);
   fChain->SetBranchAddress("events_LooseId", &events_LooseId, &b_events_LooseId);
   fChain->SetBranchAddress("events_TightId", &events_TightId, &b_events_TightId);
   fChain->SetBranchAddress("events_numGenPV", &events_numGenPV, &b_events_numGenPV);
   fChain->SetBranchAddress("events_nm1", &events_nm1, &b_events_nm1);
   fChain->SetBranchAddress("events_n0", &events_n0, &b_events_n0);
   fChain->SetBranchAddress("events_np1", &events_np1, &b_events_np1);
   fChain->SetBranchAddress("events_id1", &events_id1, &b_events_id1);
   fChain->SetBranchAddress("events_id2", &events_id2, &b_events_id2);
   fChain->SetBranchAddress("events_evt", &events_evt, &b_events_evt);
   fChain->SetBranchAddress("events_puScaleFactor", &events_puScaleFactor, &b_events_puScaleFactor);
   fChain->SetBranchAddress("events_muonScaleFactor", &events_muonScaleFactor, &b_events_muonScaleFactor);
   fChain->SetBranchAddress("events_electronScaleFactor", &events_electronScaleFactor, &b_events_electronScaleFactor);
   fChain->SetBranchAddress("events_stopCTauScaleFactor", &events_stopCTauScaleFactor, &b_events_stopCTauScaleFactor);
   fChain->SetBranchAddress("muons_energy", &muons_energy, &b_muons_energy);
   fChain->SetBranchAddress("muons_et", &muons_et, &b_muons_et);
   fChain->SetBranchAddress("muons_pt", &muons_pt, &b_muons_pt);
   fChain->SetBranchAddress("muons_px", &muons_px, &b_muons_px);
   fChain->SetBranchAddress("muons_py", &muons_py, &b_muons_py);
   fChain->SetBranchAddress("muons_pz", &muons_pz, &b_muons_pz);
   fChain->SetBranchAddress("muons_phi", &muons_phi, &b_muons_phi);
   fChain->SetBranchAddress("muons_eta", &muons_eta, &b_muons_eta);
   fChain->SetBranchAddress("muons_theta", &muons_theta, &b_muons_theta);
   fChain->SetBranchAddress("muons_trackIso", &muons_trackIso, &b_muons_trackIso);
   fChain->SetBranchAddress("muons_ecalIso", &muons_ecalIso, &b_muons_ecalIso);
   fChain->SetBranchAddress("muons_hcalIso", &muons_hcalIso, &b_muons_hcalIso);
   fChain->SetBranchAddress("muons_caloIso", &muons_caloIso, &b_muons_caloIso);
   fChain->SetBranchAddress("muons_trackIsDR03", &muons_trackIsDR03, &b_muons_trackIsDR03);
   fChain->SetBranchAddress("muons_ecalIsoDR03", &muons_ecalIsoDR03, &b_muons_ecalIsoDR03);
   fChain->SetBranchAddress("muons_hcalIsoDR03", &muons_hcalIsoDR03, &b_muons_hcalIsoDR03);
   fChain->SetBranchAddress("muons_caloIsoDR03", &muons_caloIsoDR03, &b_muons_caloIsoDR03);
   fChain->SetBranchAddress("muons_trackVetoIsoDR03", &muons_trackVetoIsoDR03, &b_muons_trackVetoIsoDR03);
   fChain->SetBranchAddress("muons_ecalVetoIsoDR03", &muons_ecalVetoIsoDR03, &b_muons_ecalVetoIsoDR03);
   fChain->SetBranchAddress("muons_hcalVetoIsoDR03", &muons_hcalVetoIsoDR03, &b_muons_hcalVetoIsoDR03);
   fChain->SetBranchAddress("muons_caloVetoIsoDR03", &muons_caloVetoIsoDR03, &b_muons_caloVetoIsoDR03);
   fChain->SetBranchAddress("muons_trackIsoDR05", &muons_trackIsoDR05, &b_muons_trackIsoDR05);
   fChain->SetBranchAddress("muons_ecalIsoDR05", &muons_ecalIsoDR05, &b_muons_ecalIsoDR05);
   fChain->SetBranchAddress("muons_hcalIsoDR05", &muons_hcalIsoDR05, &b_muons_hcalIsoDR05);
   fChain->SetBranchAddress("muons_caloIsoDR05", &muons_caloIsoDR05, &b_muons_caloIsoDR05);
   fChain->SetBranchAddress("muons_trackVetoIsoDR05", &muons_trackVetoIsoDR05, &b_muons_trackVetoIsoDR05);
   fChain->SetBranchAddress("muons_ecalVetoIsoDR05", &muons_ecalVetoIsoDR05, &b_muons_ecalVetoIsoDR05);
   fChain->SetBranchAddress("muons_hcalVetoIsoDR05", &muons_hcalVetoIsoDR05, &b_muons_hcalVetoIsoDR05);
   fChain->SetBranchAddress("muons_caloVetoIsoDR05", &muons_caloVetoIsoDR05, &b_muons_caloVetoIsoDR05);
   fChain->SetBranchAddress("muons_hcalE", &muons_hcalE, &b_muons_hcalE);
   fChain->SetBranchAddress("muons_ecalE", &muons_ecalE, &b_muons_ecalE);
   fChain->SetBranchAddress("muons_genET", &muons_genET, &b_muons_genET);
   fChain->SetBranchAddress("muons_genPT", &muons_genPT, &b_muons_genPT);
   fChain->SetBranchAddress("muons_genPhi", &muons_genPhi, &b_muons_genPhi);
   fChain->SetBranchAddress("muons_genEta", &muons_genEta, &b_muons_genEta);
   fChain->SetBranchAddress("muons_genMotherET", &muons_genMotherET, &b_muons_genMotherET);
   fChain->SetBranchAddress("muons_genMotherPT", &muons_genMotherPT, &b_muons_genMotherPT);
   fChain->SetBranchAddress("muons_genMotherPhi", &muons_genMotherPhi, &b_muons_genMotherPhi);
   fChain->SetBranchAddress("muons_genMotherEta", &muons_genMotherEta, &b_muons_genMotherEta);
   fChain->SetBranchAddress("muons_vx", &muons_vx, &b_muons_vx);
   fChain->SetBranchAddress("muons_vy", &muons_vy, &b_muons_vy);
   fChain->SetBranchAddress("muons_vz", &muons_vz, &b_muons_vz);
   fChain->SetBranchAddress("muons_tkNormChi2", &muons_tkNormChi2, &b_muons_tkNormChi2);
   fChain->SetBranchAddress("muons_tkPT", &muons_tkPT, &b_muons_tkPT);
   fChain->SetBranchAddress("muons_tkEta", &muons_tkEta, &b_muons_tkEta);
   fChain->SetBranchAddress("muons_tkPhi", &muons_tkPhi, &b_muons_tkPhi);
   fChain->SetBranchAddress("muons_tkDZ", &muons_tkDZ, &b_muons_tkDZ);
   fChain->SetBranchAddress("muons_tkD0", &muons_tkD0, &b_muons_tkD0);
   fChain->SetBranchAddress("muons_tkD0bs", &muons_tkD0bs, &b_muons_tkD0bs);
   fChain->SetBranchAddress("muons_tkD0err", &muons_tkD0err, &b_muons_tkD0err);
   fChain->SetBranchAddress("muons_samNormChi2", &muons_samNormChi2, &b_muons_samNormChi2);
   fChain->SetBranchAddress("muons_samPT", &muons_samPT, &b_muons_samPT);
   fChain->SetBranchAddress("muons_samEta", &muons_samEta, &b_muons_samEta);
   fChain->SetBranchAddress("muons_samPhi", &muons_samPhi, &b_muons_samPhi);
   fChain->SetBranchAddress("muons_samDZ", &muons_samDZ, &b_muons_samDZ);
   fChain->SetBranchAddress("muons_samD0", &muons_samD0, &b_muons_samD0);
   fChain->SetBranchAddress("muons_samD0bs", &muons_samD0bs, &b_muons_samD0bs);
   fChain->SetBranchAddress("muons_samD0err", &muons_samD0err, &b_muons_samD0err);
   fChain->SetBranchAddress("muons_comNormChi2", &muons_comNormChi2, &b_muons_comNormChi2);
   fChain->SetBranchAddress("muons_comPT", &muons_comPT, &b_muons_comPT);
   fChain->SetBranchAddress("muons_comEta", &muons_comEta, &b_muons_comEta);
   fChain->SetBranchAddress("muons_comPhi", &muons_comPhi, &b_muons_comPhi);
   fChain->SetBranchAddress("muons_comDZ", &muons_comDZ, &b_muons_comDZ);
   fChain->SetBranchAddress("muons_comD0", &muons_comD0, &b_muons_comD0);
   fChain->SetBranchAddress("muons_comD0bs", &muons_comD0bs, &b_muons_comD0bs);
   fChain->SetBranchAddress("muons_comD0err", &muons_comD0err, &b_muons_comD0err);
   fChain->SetBranchAddress("muons_isolationR03emVetoEt", &muons_isolationR03emVetoEt, &b_muons_isolationR03emVetoEt);
   fChain->SetBranchAddress("muons_isolationR03hadVetoEt", &muons_isolationR03hadVetoEt, &b_muons_isolationR03hadVetoEt);
   fChain->SetBranchAddress("muons_normalizedChi2", &muons_normalizedChi2, &b_muons_normalizedChi2);
   fChain->SetBranchAddress("muons_dVzPVz", &muons_dVzPVz, &b_muons_dVzPVz);
   fChain->SetBranchAddress("muons_dB", &muons_dB, &b_muons_dB);
   fChain->SetBranchAddress("muons_ptErr", &muons_ptErr, &b_muons_ptErr);
   fChain->SetBranchAddress("muons_innerTrackNormChi2", &muons_innerTrackNormChi2, &b_muons_innerTrackNormChi2);
   fChain->SetBranchAddress("muons_correctedD0", &muons_correctedD0, &b_muons_correctedD0);
   fChain->SetBranchAddress("muons_correctedD0Vertex", &muons_correctedD0Vertex, &b_muons_correctedD0Vertex);
   fChain->SetBranchAddress("muons_correctedDZ", &muons_correctedDZ, &b_muons_correctedDZ);
   fChain->SetBranchAddress("muons_particleIso", &muons_particleIso, &b_muons_particleIso);
   fChain->SetBranchAddress("muons_chargedHadronIso", &muons_chargedHadronIso, &b_muons_chargedHadronIso);
   fChain->SetBranchAddress("muons_neutralHadronIso", &muons_neutralHadronIso, &b_muons_neutralHadronIso);
   fChain->SetBranchAddress("muons_photonIso", &muons_photonIso, &b_muons_photonIso);
   fChain->SetBranchAddress("muons_puChargedHadronIso", &muons_puChargedHadronIso, &b_muons_puChargedHadronIso);
   fChain->SetBranchAddress("muons_chargedHadronIsoDR03", &muons_chargedHadronIsoDR03, &b_muons_chargedHadronIsoDR03);
   fChain->SetBranchAddress("muons_neutralHadronIsoDR03", &muons_neutralHadronIsoDR03, &b_muons_neutralHadronIsoDR03);
   fChain->SetBranchAddress("muons_photonIsoDR03", &muons_photonIsoDR03, &b_muons_photonIsoDR03);
   fChain->SetBranchAddress("muons_puChargedHadronIsoDR03", &muons_puChargedHadronIsoDR03, &b_muons_puChargedHadronIsoDR03);
   fChain->SetBranchAddress("muons_chargedHadronIsoDR04", &muons_chargedHadronIsoDR04, &b_muons_chargedHadronIsoDR04);
   fChain->SetBranchAddress("muons_neutralHadronIsoDR04", &muons_neutralHadronIsoDR04, &b_muons_neutralHadronIsoDR04);
   fChain->SetBranchAddress("muons_photonIsoDR04", &muons_photonIsoDR04, &b_muons_photonIsoDR04);
   fChain->SetBranchAddress("muons_puChargedHadronIsoDR04", &muons_puChargedHadronIsoDR04, &b_muons_puChargedHadronIsoDR04);
   fChain->SetBranchAddress("muons_rhoPrime", &muons_rhoPrime, &b_muons_rhoPrime);
   fChain->SetBranchAddress("muons_AEffDr03", &muons_AEffDr03, &b_muons_AEffDr03);
   fChain->SetBranchAddress("muons_AEffDr04", &muons_AEffDr04, &b_muons_AEffDr04);
   fChain->SetBranchAddress("muons_pfIsoR03SumChargedHadronPt", &muons_pfIsoR03SumChargedHadronPt, &b_muons_pfIsoR03SumChargedHadronPt);
   fChain->SetBranchAddress("muons_pfIsoR03SumNeutralHadronEt", &muons_pfIsoR03SumNeutralHadronEt, &b_muons_pfIsoR03SumNeutralHadronEt);
   fChain->SetBranchAddress("muons_pfIsoR03SumPhotonEt", &muons_pfIsoR03SumPhotonEt, &b_muons_pfIsoR03SumPhotonEt);
   fChain->SetBranchAddress("muons_pfIsoR03SumPUPt", &muons_pfIsoR03SumPUPt, &b_muons_pfIsoR03SumPUPt);
   fChain->SetBranchAddress("muons_pfIsoR04SumChargedHadronPt", &muons_pfIsoR04SumChargedHadronPt, &b_muons_pfIsoR04SumChargedHadronPt);
   fChain->SetBranchAddress("muons_pfIsoR04SumNeutralHadronEt", &muons_pfIsoR04SumNeutralHadronEt, &b_muons_pfIsoR04SumNeutralHadronEt);
   fChain->SetBranchAddress("muons_pfIsoR04SumPhotonEt", &muons_pfIsoR04SumPhotonEt, &b_muons_pfIsoR04SumPhotonEt);
   fChain->SetBranchAddress("muons_pfIsoR04SumPUPt", &muons_pfIsoR04SumPUPt, &b_muons_pfIsoR04SumPUPt);
   fChain->SetBranchAddress("muons_IP", &muons_IP, &b_muons_IP);
   fChain->SetBranchAddress("muons_IPError", &muons_IPError, &b_muons_IPError);
   fChain->SetBranchAddress("muons_timeAtIpInOut", &muons_timeAtIpInOut, &b_muons_timeAtIpInOut);
   fChain->SetBranchAddress("muons_timeAtIpInOutErr", &muons_timeAtIpInOutErr, &b_muons_timeAtIpInOutErr);
   fChain->SetBranchAddress("muons_timeAtIpOutIn", &muons_timeAtIpOutIn, &b_muons_timeAtIpOutIn);
   fChain->SetBranchAddress("muons_timeAtIpOutInErr", &muons_timeAtIpOutInErr, &b_muons_timeAtIpOutInErr);
   fChain->SetBranchAddress("muons_ecal_time", &muons_ecal_time, &b_muons_ecal_time);
   fChain->SetBranchAddress("muons_hcal_time", &muons_hcal_time, &b_muons_hcal_time);
   fChain->SetBranchAddress("muons_ecal_timeError", &muons_ecal_timeError, &b_muons_ecal_timeError);
   fChain->SetBranchAddress("muons_hcal_timeError", &muons_hcal_timeError, &b_muons_hcal_timeError);
   fChain->SetBranchAddress("muons_energy_ecal", &muons_energy_ecal, &b_muons_energy_ecal);
   fChain->SetBranchAddress("muons_energy_hcal", &muons_energy_hcal, &b_muons_energy_hcal);
   fChain->SetBranchAddress("muons_e3x3_ecal", &muons_e3x3_ecal, &b_muons_e3x3_ecal);
   fChain->SetBranchAddress("muons_e3x3_hcal", &muons_e3x3_hcal, &b_muons_e3x3_hcal);
   fChain->SetBranchAddress("muons_energyMax_ecal", &muons_energyMax_ecal, &b_muons_energyMax_ecal);
   fChain->SetBranchAddress("muons_energyMax_hcal", &muons_energyMax_hcal, &b_muons_energyMax_hcal);
   fChain->SetBranchAddress("muons_charge", &muons_charge, &b_muons_charge);
   fChain->SetBranchAddress("muons_IDGMPTight", &muons_IDGMPTight, &b_muons_IDGMPTight);
   fChain->SetBranchAddress("muons_tkNumValidHits", &muons_tkNumValidHits, &b_muons_tkNumValidHits);
   fChain->SetBranchAddress("muons_tkCharge", &muons_tkCharge, &b_muons_tkCharge);
   fChain->SetBranchAddress("muons_samNumValidHits", &muons_samNumValidHits, &b_muons_samNumValidHits);
   fChain->SetBranchAddress("muons_samCharge", &muons_samCharge, &b_muons_samCharge);
   fChain->SetBranchAddress("muons_comNumValidHits", &muons_comNumValidHits, &b_muons_comNumValidHits);
   fChain->SetBranchAddress("muons_comCharge", &muons_comCharge, &b_muons_comCharge);
   fChain->SetBranchAddress("muons_genId", &muons_genId, &b_muons_genId);
   fChain->SetBranchAddress("muons_genCharge", &muons_genCharge, &b_muons_genCharge);
   fChain->SetBranchAddress("muons_genNumberOfMothers", &muons_genNumberOfMothers, &b_muons_genNumberOfMothers);
   fChain->SetBranchAddress("muons_genMotherId", &muons_genMotherId, &b_muons_genMotherId);
   fChain->SetBranchAddress("muons_genMotherCharge", &muons_genMotherCharge, &b_muons_genMotherCharge);
   fChain->SetBranchAddress("muons_genMother0Id", &muons_genMother0Id, &b_muons_genMother0Id);
   fChain->SetBranchAddress("muons_genMother1Id", &muons_genMother1Id, &b_muons_genMother1Id);
   fChain->SetBranchAddress("muons_genGrandMother00Id", &muons_genGrandMother00Id, &b_muons_genGrandMother00Id);
   fChain->SetBranchAddress("muons_genGrandMother01Id", &muons_genGrandMother01Id, &b_muons_genGrandMother01Id);
   fChain->SetBranchAddress("muons_genGrandMother10Id", &muons_genGrandMother10Id, &b_muons_genGrandMother10Id);
   fChain->SetBranchAddress("muons_genGrandMother11Id", &muons_genGrandMother11Id, &b_muons_genGrandMother11Id);
   fChain->SetBranchAddress("muons_isPFMuon", &muons_isPFMuon, &b_muons_isPFMuon);
   fChain->SetBranchAddress("muons_isGoodMuon_1StationTight", &muons_isGoodMuon_1StationTight, &b_muons_isGoodMuon_1StationTight);
   fChain->SetBranchAddress("muons_isGlobalMuon", &muons_isGlobalMuon, &b_muons_isGlobalMuon);
   fChain->SetBranchAddress("muons_isTrackerMuon", &muons_isTrackerMuon, &b_muons_isTrackerMuon);
   fChain->SetBranchAddress("muons_isStandAloneMuon", &muons_isStandAloneMuon, &b_muons_isStandAloneMuon);
   fChain->SetBranchAddress("muons_isGlobalMuonPromptTight", &muons_isGlobalMuonPromptTight, &b_muons_isGlobalMuonPromptTight);
   fChain->SetBranchAddress("muons_numberOfValidMuonHits", &muons_numberOfValidMuonHits, &b_muons_numberOfValidMuonHits);
   fChain->SetBranchAddress("muons_numberOfValidTrackerHits", &muons_numberOfValidTrackerHits, &b_muons_numberOfValidTrackerHits);
   fChain->SetBranchAddress("muons_numberOfLayersWithMeasurement", &muons_numberOfLayersWithMeasurement, &b_muons_numberOfLayersWithMeasurement);
   fChain->SetBranchAddress("muons_pixelLayersWithMeasurement", &muons_pixelLayersWithMeasurement, &b_muons_pixelLayersWithMeasurement);
   fChain->SetBranchAddress("muons_numberOfMatches", &muons_numberOfMatches, &b_muons_numberOfMatches);
   fChain->SetBranchAddress("muons_numberOfValidTrackerHitsInnerTrack", &muons_numberOfValidTrackerHitsInnerTrack, &b_muons_numberOfValidTrackerHitsInnerTrack);
   fChain->SetBranchAddress("muons_numberOfValidPixelHits", &muons_numberOfValidPixelHits, &b_muons_numberOfValidPixelHits);
   fChain->SetBranchAddress("muons_numberOfMatchedStations", &muons_numberOfMatchedStations, &b_muons_numberOfMatchedStations);
   fChain->SetBranchAddress("muons_time_ndof", &muons_time_ndof, &b_muons_time_ndof);
   fChain->SetBranchAddress("muons_correctedD0VertexErr", &muons_correctedD0VertexErr, &b_muons_correctedD0VertexErr);
   fChain->SetBranchAddress("muons_correctedD0VertexSig", &muons_correctedD0VertexSig, &b_muons_correctedD0VertexSig);
   fChain->SetBranchAddress("muons_detIso", &muons_detIso, &b_muons_detIso);
   fChain->SetBranchAddress("muons_relPFdBetaIso", &muons_relPFdBetaIso, &b_muons_relPFdBetaIso);
   fChain->SetBranchAddress("muons_relPFrhoIso", &muons_relPFrhoIso, &b_muons_relPFrhoIso);
   fChain->SetBranchAddress("muons_metMT", &muons_metMT, &b_muons_metMT);
   fChain->SetBranchAddress("muons_correctedD0VertexInEBPlus", &muons_correctedD0VertexInEBPlus, &b_muons_correctedD0VertexInEBPlus);
   fChain->SetBranchAddress("muons_correctedD0VertexOutEBPlus", &muons_correctedD0VertexOutEBPlus, &b_muons_correctedD0VertexOutEBPlus);
   fChain->SetBranchAddress("muons_correctedD0VertexEEPlus", &muons_correctedD0VertexEEPlus, &b_muons_correctedD0VertexEEPlus);
   fChain->SetBranchAddress("muons_correctedD0BeamspotInEBPlus", &muons_correctedD0BeamspotInEBPlus, &b_muons_correctedD0BeamspotInEBPlus);
   fChain->SetBranchAddress("muons_correctedD0BeamspotOutEBPlus", &muons_correctedD0BeamspotOutEBPlus, &b_muons_correctedD0BeamspotOutEBPlus);
   fChain->SetBranchAddress("muons_correctedD0BeamspotEEPlus", &muons_correctedD0BeamspotEEPlus, &b_muons_correctedD0BeamspotEEPlus);
   fChain->SetBranchAddress("muons_correctedD0VertexInEBMinus", &muons_correctedD0VertexInEBMinus, &b_muons_correctedD0VertexInEBMinus);
   fChain->SetBranchAddress("muons_correctedD0VertexOutEBMinus", &muons_correctedD0VertexOutEBMinus, &b_muons_correctedD0VertexOutEBMinus);
   fChain->SetBranchAddress("muons_correctedD0VertexEEMinus", &muons_correctedD0VertexEEMinus, &b_muons_correctedD0VertexEEMinus);
   fChain->SetBranchAddress("muons_correctedD0BeamspotInEBMinus", &muons_correctedD0BeamspotInEBMinus, &b_muons_correctedD0BeamspotInEBMinus);
   fChain->SetBranchAddress("muons_correctedD0BeamspotOutEBMinus", &muons_correctedD0BeamspotOutEBMinus, &b_muons_correctedD0BeamspotOutEBMinus);
   fChain->SetBranchAddress("muons_correctedD0BeamspotEEMinus", &muons_correctedD0BeamspotEEMinus, &b_muons_correctedD0BeamspotEEMinus);
   fChain->SetBranchAddress("muons_correctedD0VertexInEBPositiveCharge", &muons_correctedD0VertexInEBPositiveCharge, &b_muons_correctedD0VertexInEBPositiveCharge);
   fChain->SetBranchAddress("muons_correctedD0VertexOutEBPositiveCharge", &muons_correctedD0VertexOutEBPositiveCharge, &b_muons_correctedD0VertexOutEBPositiveCharge);
   fChain->SetBranchAddress("muons_correctedD0VertexEEPositiveCharge", &muons_correctedD0VertexEEPositiveCharge, &b_muons_correctedD0VertexEEPositiveCharge);
   fChain->SetBranchAddress("muons_correctedD0BeamspotInEBPositiveCharge", &muons_correctedD0BeamspotInEBPositiveCharge, &b_muons_correctedD0BeamspotInEBPositiveCharge);
   fChain->SetBranchAddress("muons_correctedD0BeamspotOutEBPositiveCharge", &muons_correctedD0BeamspotOutEBPositiveCharge, &b_muons_correctedD0BeamspotOutEBPositiveCharge);
   fChain->SetBranchAddress("muons_correctedD0BeamspotEEPositiveCharge", &muons_correctedD0BeamspotEEPositiveCharge, &b_muons_correctedD0BeamspotEEPositiveCharge);
   fChain->SetBranchAddress("muons_correctedD0VertexInEBNegativeCharge", &muons_correctedD0VertexInEBNegativeCharge, &b_muons_correctedD0VertexInEBNegativeCharge);
   fChain->SetBranchAddress("muons_correctedD0VertexOutEBNegativeCharge", &muons_correctedD0VertexOutEBNegativeCharge, &b_muons_correctedD0VertexOutEBNegativeCharge);
   fChain->SetBranchAddress("muons_correctedD0VertexEENegativeCharge", &muons_correctedD0VertexEENegativeCharge, &b_muons_correctedD0VertexEENegativeCharge);
   fChain->SetBranchAddress("muons_correctedD0BeamspotInEBNegativeCharge", &muons_correctedD0BeamspotInEBNegativeCharge, &b_muons_correctedD0BeamspotInEBNegativeCharge);
   fChain->SetBranchAddress("muons_correctedD0BeamspotOutEBNegativeCharge", &muons_correctedD0BeamspotOutEBNegativeCharge, &b_muons_correctedD0BeamspotOutEBNegativeCharge);
   fChain->SetBranchAddress("muons_correctedD0BeamspotEENegativeCharge", &muons_correctedD0BeamspotEENegativeCharge, &b_muons_correctedD0BeamspotEENegativeCharge);
   fChain->SetBranchAddress("muons_tightID", &muons_tightID, &b_muons_tightID);
   fChain->SetBranchAddress("muons_tightIDdisplaced", &muons_tightIDdisplaced, &b_muons_tightIDdisplaced);
   fChain->SetBranchAddress("muons_genDeltaRLowest", &muons_genDeltaRLowest, &b_muons_genDeltaRLowest);
   fChain->SetBranchAddress("muons_genMatchedPdgId", &muons_genMatchedPdgId, &b_muons_genMatchedPdgId);
   fChain->SetBranchAddress("muons_genMatchedId", &muons_genMatchedId, &b_muons_genMatchedId);
   fChain->SetBranchAddress("muons_genMatchedMotherId", &muons_genMatchedMotherId, &b_muons_genMatchedMotherId);
   fChain->SetBranchAddress("muons_genMatchedMotherIdReverse", &muons_genMatchedMotherIdReverse, &b_muons_genMatchedMotherIdReverse);
   fChain->SetBranchAddress("muons_genMatchedGrandmotherId", &muons_genMatchedGrandmotherId, &b_muons_genMatchedGrandmotherId);
   fChain->SetBranchAddress("muons_genMatchedGrandmotherIdReverse", &muons_genMatchedGrandmotherIdReverse, &b_muons_genMatchedGrandmotherIdReverse);
   fChain->SetBranchAddress("muons_pfMuonsFromVertex", &muons_pfMuonsFromVertex, &b_muons_pfMuonsFromVertex);
   fChain->SetBranchAddress("electrons_energy", &electrons_energy, &b_electrons_energy);
   fChain->SetBranchAddress("electrons_et", &electrons_et, &b_electrons_et);
   fChain->SetBranchAddress("electrons_gsfEt", &electrons_gsfEt, &b_electrons_gsfEt);
   fChain->SetBranchAddress("electrons_pt", &electrons_pt, &b_electrons_pt);
   fChain->SetBranchAddress("electrons_px", &electrons_px, &b_electrons_px);
   fChain->SetBranchAddress("electrons_py", &electrons_py, &b_electrons_py);
   fChain->SetBranchAddress("electrons_pz", &electrons_pz, &b_electrons_pz);
   fChain->SetBranchAddress("electrons_phi", &electrons_phi, &b_electrons_phi);
   fChain->SetBranchAddress("electrons_eta", &electrons_eta, &b_electrons_eta);
   fChain->SetBranchAddress("electrons_theta", &electrons_theta, &b_electrons_theta);
   fChain->SetBranchAddress("electrons_pIn", &electrons_pIn, &b_electrons_pIn);
   fChain->SetBranchAddress("electrons_pOut", &electrons_pOut, &b_electrons_pOut);
   fChain->SetBranchAddress("electrons_EscOverPin", &electrons_EscOverPin, &b_electrons_EscOverPin);
   fChain->SetBranchAddress("electrons_EseedOverPout", &electrons_EseedOverPout, &b_electrons_EseedOverPout);
   fChain->SetBranchAddress("electrons_hadOverEm", &electrons_hadOverEm, &b_electrons_hadOverEm);
   fChain->SetBranchAddress("electrons_trackIso", &electrons_trackIso, &b_electrons_trackIso);
   fChain->SetBranchAddress("electrons_ecalIso", &electrons_ecalIso, &b_electrons_ecalIso);
   fChain->SetBranchAddress("electrons_hcalIso", &electrons_hcalIso, &b_electrons_hcalIso);
   fChain->SetBranchAddress("electrons_caloIso", &electrons_caloIso, &b_electrons_caloIso);
   fChain->SetBranchAddress("electrons_trackIsoDR03", &electrons_trackIsoDR03, &b_electrons_trackIsoDR03);
   fChain->SetBranchAddress("electrons_ecalIsoDR03", &electrons_ecalIsoDR03, &b_electrons_ecalIsoDR03);
   fChain->SetBranchAddress("electrons_hcalIsoDR03", &electrons_hcalIsoDR03, &b_electrons_hcalIsoDR03);
   fChain->SetBranchAddress("electrons_hcalIsoDR03depth1", &electrons_hcalIsoDR03depth1, &b_electrons_hcalIsoDR03depth1);
   fChain->SetBranchAddress("electrons_hcalIsoDR03depth2", &electrons_hcalIsoDR03depth2, &b_electrons_hcalIsoDR03depth2);
   fChain->SetBranchAddress("electrons_caloIsoDR03", &electrons_caloIsoDR03, &b_electrons_caloIsoDR03);
   fChain->SetBranchAddress("electrons_trackIsoDR04", &electrons_trackIsoDR04, &b_electrons_trackIsoDR04);
   fChain->SetBranchAddress("electrons_ecalIsoDR04", &electrons_ecalIsoDR04, &b_electrons_ecalIsoDR04);
   fChain->SetBranchAddress("electrons_hcalIsoDR04", &electrons_hcalIsoDR04, &b_electrons_hcalIsoDR04);
   fChain->SetBranchAddress("electrons_hcalIsoDR04depth1", &electrons_hcalIsoDR04depth1, &b_electrons_hcalIsoDR04depth1);
   fChain->SetBranchAddress("electrons_hcalIsoDR04depth2", &electrons_hcalIsoDR04depth2, &b_electrons_hcalIsoDR04depth2);
   fChain->SetBranchAddress("electrons_caloIsoDR04", &electrons_caloIsoDR04, &b_electrons_caloIsoDR04);
   fChain->SetBranchAddress("electrons_fbrem", &electrons_fbrem, &b_electrons_fbrem);
   fChain->SetBranchAddress("electrons_absInvEMinusInvPin", &electrons_absInvEMinusInvPin, &b_electrons_absInvEMinusInvPin);
   fChain->SetBranchAddress("electrons_delPhiIn", &electrons_delPhiIn, &b_electrons_delPhiIn);
   fChain->SetBranchAddress("electrons_delEtaIn", &electrons_delEtaIn, &b_electrons_delEtaIn);
   fChain->SetBranchAddress("electrons_genET", &electrons_genET, &b_electrons_genET);
   fChain->SetBranchAddress("electrons_genPT", &electrons_genPT, &b_electrons_genPT);
   fChain->SetBranchAddress("electrons_genPhi", &electrons_genPhi, &b_electrons_genPhi);
   fChain->SetBranchAddress("electrons_genEta", &electrons_genEta, &b_electrons_genEta);
   fChain->SetBranchAddress("electrons_genMotherET", &electrons_genMotherET, &b_electrons_genMotherET);
   fChain->SetBranchAddress("electrons_genMotherPT", &electrons_genMotherPT, &b_electrons_genMotherPT);
   fChain->SetBranchAddress("electrons_genMotherPhi", &electrons_genMotherPhi, &b_electrons_genMotherPhi);
   fChain->SetBranchAddress("electrons_genMotherEta", &electrons_genMotherEta, &b_electrons_genMotherEta);
   fChain->SetBranchAddress("electrons_vx", &electrons_vx, &b_electrons_vx);
   fChain->SetBranchAddress("electrons_vy", &electrons_vy, &b_electrons_vy);
   fChain->SetBranchAddress("electrons_vz", &electrons_vz, &b_electrons_vz);
   fChain->SetBranchAddress("electrons_scEnergy", &electrons_scEnergy, &b_electrons_scEnergy);
   fChain->SetBranchAddress("electrons_scRawEnergy", &electrons_scRawEnergy, &b_electrons_scRawEnergy);
   fChain->SetBranchAddress("electrons_scSigmaEtaEta", &electrons_scSigmaEtaEta, &b_electrons_scSigmaEtaEta);
   fChain->SetBranchAddress("electrons_scSigmaIEtaIEta", &electrons_scSigmaIEtaIEta, &b_electrons_scSigmaIEtaIEta);
   fChain->SetBranchAddress("electrons_scE1x5", &electrons_scE1x5, &b_electrons_scE1x5);
   fChain->SetBranchAddress("electrons_scE2x5Max", &electrons_scE2x5Max, &b_electrons_scE2x5Max);
   fChain->SetBranchAddress("electrons_scE5x5", &electrons_scE5x5, &b_electrons_scE5x5);
   fChain->SetBranchAddress("electrons_scEt", &electrons_scEt, &b_electrons_scEt);
   fChain->SetBranchAddress("electrons_scEta", &electrons_scEta, &b_electrons_scEta);
   fChain->SetBranchAddress("electrons_scPhi", &electrons_scPhi, &b_electrons_scPhi);
   fChain->SetBranchAddress("electrons_scZ", &electrons_scZ, &b_electrons_scZ);
   fChain->SetBranchAddress("electrons_tkNormChi2", &electrons_tkNormChi2, &b_electrons_tkNormChi2);
   fChain->SetBranchAddress("electrons_tkPT", &electrons_tkPT, &b_electrons_tkPT);
   fChain->SetBranchAddress("electrons_tkEta", &electrons_tkEta, &b_electrons_tkEta);
   fChain->SetBranchAddress("electrons_tkPhi", &electrons_tkPhi, &b_electrons_tkPhi);
   fChain->SetBranchAddress("electrons_tkDZ", &electrons_tkDZ, &b_electrons_tkDZ);
   fChain->SetBranchAddress("electrons_tkD0", &electrons_tkD0, &b_electrons_tkD0);
   fChain->SetBranchAddress("electrons_tkD0bs", &electrons_tkD0bs, &b_electrons_tkD0bs);
   fChain->SetBranchAddress("electrons_tkD0err", &electrons_tkD0err, &b_electrons_tkD0err);
   fChain->SetBranchAddress("electrons_mva", &electrons_mva, &b_electrons_mva);
   fChain->SetBranchAddress("electrons_mvaTrigV0", &electrons_mvaTrigV0, &b_electrons_mvaTrigV0);
   fChain->SetBranchAddress("electrons_mvaNonTrigV0", &electrons_mvaNonTrigV0, &b_electrons_mvaNonTrigV0);
   fChain->SetBranchAddress("electrons_dist", &electrons_dist, &b_electrons_dist);
   fChain->SetBranchAddress("electrons_dcot", &electrons_dcot, &b_electrons_dcot);
   fChain->SetBranchAddress("electrons_convradius", &electrons_convradius, &b_electrons_convradius);
   fChain->SetBranchAddress("electrons_convPointX", &electrons_convPointX, &b_electrons_convPointX);
   fChain->SetBranchAddress("electrons_convPointY", &electrons_convPointY, &b_electrons_convPointY);
   fChain->SetBranchAddress("electrons_convPointZ", &electrons_convPointZ, &b_electrons_convPointZ);
   fChain->SetBranchAddress("electrons_eMax", &electrons_eMax, &b_electrons_eMax);
   fChain->SetBranchAddress("electrons_eLeft", &electrons_eLeft, &b_electrons_eLeft);
   fChain->SetBranchAddress("electrons_eRight", &electrons_eRight, &b_electrons_eRight);
   fChain->SetBranchAddress("electrons_eTop", &electrons_eTop, &b_electrons_eTop);
   fChain->SetBranchAddress("electrons_eBottom", &electrons_eBottom, &b_electrons_eBottom);
   fChain->SetBranchAddress("electrons_e3x3", &electrons_e3x3, &b_electrons_e3x3);
   fChain->SetBranchAddress("electrons_swissCross", &electrons_swissCross, &b_electrons_swissCross);
   fChain->SetBranchAddress("electrons_seedEnergy", &electrons_seedEnergy, &b_electrons_seedEnergy);
   fChain->SetBranchAddress("electrons_seedTime", &electrons_seedTime, &b_electrons_seedTime);
   fChain->SetBranchAddress("electrons_swissCrossNoI85", &electrons_swissCrossNoI85, &b_electrons_swissCrossNoI85);
   fChain->SetBranchAddress("electrons_swissCrossI85", &electrons_swissCrossI85, &b_electrons_swissCrossI85);
   fChain->SetBranchAddress("electrons_E2overE9NoI85", &electrons_E2overE9NoI85, &b_electrons_E2overE9NoI85);
   fChain->SetBranchAddress("electrons_E2overE9I85", &electrons_E2overE9I85, &b_electrons_E2overE9I85);
   fChain->SetBranchAddress("electrons_correctedD0", &electrons_correctedD0, &b_electrons_correctedD0);
   fChain->SetBranchAddress("electrons_correctedD0Vertex", &electrons_correctedD0Vertex, &b_electrons_correctedD0Vertex);
   fChain->SetBranchAddress("electrons_correctedDZ", &electrons_correctedDZ, &b_electrons_correctedDZ);
   fChain->SetBranchAddress("electrons_particleIso", &electrons_particleIso, &b_electrons_particleIso);
   fChain->SetBranchAddress("electrons_chargedHadronIso", &electrons_chargedHadronIso, &b_electrons_chargedHadronIso);
   fChain->SetBranchAddress("electrons_neutralHadronIso", &electrons_neutralHadronIso, &b_electrons_neutralHadronIso);
   fChain->SetBranchAddress("electrons_photonIso", &electrons_photonIso, &b_electrons_photonIso);
   fChain->SetBranchAddress("electrons_puChargedHadronIso", &electrons_puChargedHadronIso, &b_electrons_puChargedHadronIso);
   fChain->SetBranchAddress("electrons_chargedHadronIsoDR03", &electrons_chargedHadronIsoDR03, &b_electrons_chargedHadronIsoDR03);
   fChain->SetBranchAddress("electrons_neutralHadronIsoDR03", &electrons_neutralHadronIsoDR03, &b_electrons_neutralHadronIsoDR03);
   fChain->SetBranchAddress("electrons_photonIsoDR03", &electrons_photonIsoDR03, &b_electrons_photonIsoDR03);
   fChain->SetBranchAddress("electrons_puChargedHadronIsoDR03", &electrons_puChargedHadronIsoDR03, &b_electrons_puChargedHadronIsoDR03);
   fChain->SetBranchAddress("electrons_chargedHadronIsoDR04", &electrons_chargedHadronIsoDR04, &b_electrons_chargedHadronIsoDR04);
   fChain->SetBranchAddress("electrons_neutralHadronIsoDR04", &electrons_neutralHadronIsoDR04, &b_electrons_neutralHadronIsoDR04);
   fChain->SetBranchAddress("electrons_photonIsoDR04", &electrons_photonIsoDR04, &b_electrons_photonIsoDR04);
   fChain->SetBranchAddress("electrons_puChargedHadronIsoDR04", &electrons_puChargedHadronIsoDR04, &b_electrons_puChargedHadronIsoDR04);
   fChain->SetBranchAddress("electrons_rhoPrime", &electrons_rhoPrime, &b_electrons_rhoPrime);
   fChain->SetBranchAddress("electrons_AEffDr03", &electrons_AEffDr03, &b_electrons_AEffDr03);
   fChain->SetBranchAddress("electrons_AEffDr04", &electrons_AEffDr04, &b_electrons_AEffDr04);
   fChain->SetBranchAddress("electrons_IP", &electrons_IP, &b_electrons_IP);
   fChain->SetBranchAddress("electrons_IPError", &electrons_IPError, &b_electrons_IPError);
   fChain->SetBranchAddress("electrons_charge", &electrons_charge, &b_electrons_charge);
   fChain->SetBranchAddress("electrons_classification", &electrons_classification, &b_electrons_classification);
   fChain->SetBranchAddress("electrons_genId", &electrons_genId, &b_electrons_genId);
   fChain->SetBranchAddress("electrons_genCharge", &electrons_genCharge, &b_electrons_genCharge);
   fChain->SetBranchAddress("electrons_genNumberOfMothers", &electrons_genNumberOfMothers, &b_electrons_genNumberOfMothers);
   fChain->SetBranchAddress("electrons_genMotherId", &electrons_genMotherId, &b_electrons_genMotherId);
   fChain->SetBranchAddress("electrons_genMotherCharge", &electrons_genMotherCharge, &b_electrons_genMotherCharge);
   fChain->SetBranchAddress("electrons_genMother0Id", &electrons_genMother0Id, &b_electrons_genMother0Id);
   fChain->SetBranchAddress("electrons_genMother1Id", &electrons_genMother1Id, &b_electrons_genMother1Id);
   fChain->SetBranchAddress("electrons_genGrandMother00Id", &electrons_genGrandMother00Id, &b_electrons_genGrandMother00Id);
   fChain->SetBranchAddress("electrons_genGrandMother01Id", &electrons_genGrandMother01Id, &b_electrons_genGrandMother01Id);
   fChain->SetBranchAddress("electrons_genGrandMother10Id", &electrons_genGrandMother10Id, &b_electrons_genGrandMother10Id);
   fChain->SetBranchAddress("electrons_genGrandMother11Id", &electrons_genGrandMother11Id, &b_electrons_genGrandMother11Id);
   fChain->SetBranchAddress("electrons_numClusters", &electrons_numClusters, &b_electrons_numClusters);
   fChain->SetBranchAddress("electrons_tkNumValidHits", &electrons_tkNumValidHits, &b_electrons_tkNumValidHits);
   fChain->SetBranchAddress("electrons_tkCharge", &electrons_tkCharge, &b_electrons_tkCharge);
   fChain->SetBranchAddress("electrons_gsfCharge", &electrons_gsfCharge, &b_electrons_gsfCharge);
   fChain->SetBranchAddress("electrons_isEB", &electrons_isEB, &b_electrons_isEB);
   fChain->SetBranchAddress("electrons_isEE", &electrons_isEE, &b_electrons_isEE);
   fChain->SetBranchAddress("electrons_isGap", &electrons_isGap, &b_electrons_isGap);
   fChain->SetBranchAddress("electrons_isEBEEGap", &electrons_isEBEEGap, &b_electrons_isEBEEGap);
   fChain->SetBranchAddress("electrons_isEBGap", &electrons_isEBGap, &b_electrons_isEBGap);
   fChain->SetBranchAddress("electrons_isEEGap", &electrons_isEEGap, &b_electrons_isEEGap);
   fChain->SetBranchAddress("electrons_isEcalDriven", &electrons_isEcalDriven, &b_electrons_isEcalDriven);
   fChain->SetBranchAddress("electrons_isTrackerDriven", &electrons_isTrackerDriven, &b_electrons_isTrackerDriven);
   fChain->SetBranchAddress("electrons_numberOfLostHits", &electrons_numberOfLostHits, &b_electrons_numberOfLostHits);
   fChain->SetBranchAddress("electrons_numberOfExpectedInnerHits", &electrons_numberOfExpectedInnerHits, &b_electrons_numberOfExpectedInnerHits);
   fChain->SetBranchAddress("electrons_numberOfValidPixelHits", &electrons_numberOfValidPixelHits, &b_electrons_numberOfValidPixelHits);
   fChain->SetBranchAddress("electrons_numberOfValidPixelBarrelHits", &electrons_numberOfValidPixelBarrelHits, &b_electrons_numberOfValidPixelBarrelHits);
   fChain->SetBranchAddress("electrons_numberOfValidPixelEndcapHits", &electrons_numberOfValidPixelEndcapHits, &b_electrons_numberOfValidPixelEndcapHits);
   fChain->SetBranchAddress("electrons_isHEEP", &electrons_isHEEP, &b_electrons_isHEEP);
   fChain->SetBranchAddress("electrons_isHEEPnoEt", &electrons_isHEEPnoEt, &b_electrons_isHEEPnoEt);
   fChain->SetBranchAddress("electrons_seedRecoFlag", &electrons_seedRecoFlag, &b_electrons_seedRecoFlag);
   fChain->SetBranchAddress("electrons_eidRobustHighEnergy", &electrons_eidRobustHighEnergy, &b_electrons_eidRobustHighEnergy);
   fChain->SetBranchAddress("electrons_eidRobustLoose", &electrons_eidRobustLoose, &b_electrons_eidRobustLoose);
   fChain->SetBranchAddress("electrons_eidRobustTight", &electrons_eidRobustTight, &b_electrons_eidRobustTight);
   fChain->SetBranchAddress("electrons_eidLoose", &electrons_eidLoose, &b_electrons_eidLoose);
   fChain->SetBranchAddress("electrons_eidTight", &electrons_eidTight, &b_electrons_eidTight);
   fChain->SetBranchAddress("electrons_eidVeryLooseMC", &electrons_eidVeryLooseMC, &b_electrons_eidVeryLooseMC);
   fChain->SetBranchAddress("electrons_eidLooseMC", &electrons_eidLooseMC, &b_electrons_eidLooseMC);
   fChain->SetBranchAddress("electrons_eidMediumMC", &electrons_eidMediumMC, &b_electrons_eidMediumMC);
   fChain->SetBranchAddress("electrons_eidTightMC", &electrons_eidTightMC, &b_electrons_eidTightMC);
   fChain->SetBranchAddress("electrons_eidSuperTightMC", &electrons_eidSuperTightMC, &b_electrons_eidSuperTightMC);
   fChain->SetBranchAddress("electrons_eidHyperTight1MC", &electrons_eidHyperTight1MC, &b_electrons_eidHyperTight1MC);
   fChain->SetBranchAddress("electrons_eidHyperTight2MC", &electrons_eidHyperTight2MC, &b_electrons_eidHyperTight2MC);
   fChain->SetBranchAddress("electrons_eidHyperTight3MC", &electrons_eidHyperTight3MC, &b_electrons_eidHyperTight3MC);
   fChain->SetBranchAddress("electrons_eidHyperTight4MC", &electrons_eidHyperTight4MC, &b_electrons_eidHyperTight4MC);
   fChain->SetBranchAddress("electrons_passConvVeto", &electrons_passConvVeto, &b_electrons_passConvVeto);
   fChain->SetBranchAddress("electrons_correctedD0VertexErr", &electrons_correctedD0VertexErr, &b_electrons_correctedD0VertexErr);
   fChain->SetBranchAddress("electrons_correctedD0VertexSig", &electrons_correctedD0VertexSig, &b_electrons_correctedD0VertexSig);
   fChain->SetBranchAddress("electrons_detIso", &electrons_detIso, &b_electrons_detIso);
   fChain->SetBranchAddress("electrons_relPFrhoIso", &electrons_relPFrhoIso, &b_electrons_relPFrhoIso);
   fChain->SetBranchAddress("electrons_metMT", &electrons_metMT, &b_electrons_metMT);
   fChain->SetBranchAddress("electrons_correctedD0VertexEEPositiveChargeLowPt", &electrons_correctedD0VertexEEPositiveChargeLowPt, &b_electrons_correctedD0VertexEEPositiveChargeLowPt);
   fChain->SetBranchAddress("electrons_correctedD0VertexEEPositiveChargeHighPt", &electrons_correctedD0VertexEEPositiveChargeHighPt, &b_electrons_correctedD0VertexEEPositiveChargeHighPt);
   fChain->SetBranchAddress("electrons_correctedD0VertexInEBPlus", &electrons_correctedD0VertexInEBPlus, &b_electrons_correctedD0VertexInEBPlus);
   fChain->SetBranchAddress("electrons_correctedD0VertexOutEBPlus", &electrons_correctedD0VertexOutEBPlus, &b_electrons_correctedD0VertexOutEBPlus);
   fChain->SetBranchAddress("electrons_correctedD0VertexEEPlus", &electrons_correctedD0VertexEEPlus, &b_electrons_correctedD0VertexEEPlus);
   fChain->SetBranchAddress("electrons_correctedD0BeamspotInEBPlus", &electrons_correctedD0BeamspotInEBPlus, &b_electrons_correctedD0BeamspotInEBPlus);
   fChain->SetBranchAddress("electrons_correctedD0BeamspotOutEBPlus", &electrons_correctedD0BeamspotOutEBPlus, &b_electrons_correctedD0BeamspotOutEBPlus);
   fChain->SetBranchAddress("electrons_correctedD0BeamspotEEPlus", &electrons_correctedD0BeamspotEEPlus, &b_electrons_correctedD0BeamspotEEPlus);
   fChain->SetBranchAddress("electrons_correctedD0VertexInEBMinus", &electrons_correctedD0VertexInEBMinus, &b_electrons_correctedD0VertexInEBMinus);
   fChain->SetBranchAddress("electrons_correctedD0VertexOutEBMinus", &electrons_correctedD0VertexOutEBMinus, &b_electrons_correctedD0VertexOutEBMinus);
   fChain->SetBranchAddress("electrons_correctedD0VertexEEMinus", &electrons_correctedD0VertexEEMinus, &b_electrons_correctedD0VertexEEMinus);
   fChain->SetBranchAddress("electrons_correctedD0BeamspotInEBMinus", &electrons_correctedD0BeamspotInEBMinus, &b_electrons_correctedD0BeamspotInEBMinus);
   fChain->SetBranchAddress("electrons_correctedD0BeamspotOutEBMinus", &electrons_correctedD0BeamspotOutEBMinus, &b_electrons_correctedD0BeamspotOutEBMinus);
   fChain->SetBranchAddress("electrons_correctedD0BeamspotEEMinus", &electrons_correctedD0BeamspotEEMinus, &b_electrons_correctedD0BeamspotEEMinus);
   fChain->SetBranchAddress("electrons_tightID", &electrons_tightID, &b_electrons_tightID);
   fChain->SetBranchAddress("electrons_correctedD0VertexInEBPositiveCharge", &electrons_correctedD0VertexInEBPositiveCharge, &b_electrons_correctedD0VertexInEBPositiveCharge);
   fChain->SetBranchAddress("electrons_correctedD0VertexOutEBPositiveCharge", &electrons_correctedD0VertexOutEBPositiveCharge, &b_electrons_correctedD0VertexOutEBPositiveCharge);
   fChain->SetBranchAddress("electrons_correctedD0VertexEEPositiveCharge", &electrons_correctedD0VertexEEPositiveCharge, &b_electrons_correctedD0VertexEEPositiveCharge);
   fChain->SetBranchAddress("electrons_correctedD0BeamspotInEBPositiveCharge", &electrons_correctedD0BeamspotInEBPositiveCharge, &b_electrons_correctedD0BeamspotInEBPositiveCharge);
   fChain->SetBranchAddress("electrons_correctedD0BeamspotOutEBPositiveCharge", &electrons_correctedD0BeamspotOutEBPositiveCharge, &b_electrons_correctedD0BeamspotOutEBPositiveCharge);
   fChain->SetBranchAddress("electrons_correctedD0BeamspotEEPositiveCharge", &electrons_correctedD0BeamspotEEPositiveCharge, &b_electrons_correctedD0BeamspotEEPositiveCharge);
   fChain->SetBranchAddress("electrons_correctedD0VertexInEBNegativeCharge", &electrons_correctedD0VertexInEBNegativeCharge, &b_electrons_correctedD0VertexInEBNegativeCharge);
   fChain->SetBranchAddress("electrons_correctedD0VertexOutEBNegativeCharge", &electrons_correctedD0VertexOutEBNegativeCharge, &b_electrons_correctedD0VertexOutEBNegativeCharge);
   fChain->SetBranchAddress("electrons_correctedD0VertexEENegativeCharge", &electrons_correctedD0VertexEENegativeCharge, &b_electrons_correctedD0VertexEENegativeCharge);
   fChain->SetBranchAddress("electrons_correctedD0BeamspotInEBNegativeCharge", &electrons_correctedD0BeamspotInEBNegativeCharge, &b_electrons_correctedD0BeamspotInEBNegativeCharge);
   fChain->SetBranchAddress("electrons_correctedD0BeamspotOutEBNegativeCharge", &electrons_correctedD0BeamspotOutEBNegativeCharge, &b_electrons_correctedD0BeamspotOutEBNegativeCharge);
   fChain->SetBranchAddress("electrons_correctedD0BeamspotEENegativeCharge", &electrons_correctedD0BeamspotEENegativeCharge, &b_electrons_correctedD0BeamspotEENegativeCharge);
   fChain->SetBranchAddress("electrons_tightIDdisplaced", &electrons_tightIDdisplaced, &b_electrons_tightIDdisplaced);
   fChain->SetBranchAddress("electrons_genDeltaRLowest", &electrons_genDeltaRLowest, &b_electrons_genDeltaRLowest);
   fChain->SetBranchAddress("electrons_genMatchedPdgId", &electrons_genMatchedPdgId, &b_electrons_genMatchedPdgId);
   fChain->SetBranchAddress("electrons_genMatchedId", &electrons_genMatchedId, &b_electrons_genMatchedId);
   fChain->SetBranchAddress("electrons_genMatchedMotherId", &electrons_genMatchedMotherId, &b_electrons_genMatchedMotherId);
   fChain->SetBranchAddress("electrons_genMatchedMotherIdReverse", &electrons_genMatchedMotherIdReverse, &b_electrons_genMatchedMotherIdReverse);
   fChain->SetBranchAddress("electrons_genMatchedGrandmotherId", &electrons_genMatchedGrandmotherId, &b_electrons_genMatchedGrandmotherId);
   fChain->SetBranchAddress("electrons_genMatchedGrandmotherIdReverse", &electrons_genMatchedGrandmotherIdReverse, &b_electrons_genMatchedGrandmotherIdReverse);
   fChain->SetBranchAddress("electrons_pfElectronsFromVertex", &electrons_pfElectronsFromVertex, &b_electrons_pfElectronsFromVertex);
   fChain->SetBranchAddress("taus_px", &taus_px, &b_taus_px);
   fChain->SetBranchAddress("taus_py", &taus_py, &b_taus_py);
   fChain->SetBranchAddress("taus_pz", &taus_pz, &b_taus_pz);
   fChain->SetBranchAddress("taus_energy", &taus_energy, &b_taus_energy);
   fChain->SetBranchAddress("taus_et", &taus_et, &b_taus_et);
   fChain->SetBranchAddress("taus_pt", &taus_pt, &b_taus_pt);
   fChain->SetBranchAddress("taus_eta", &taus_eta, &b_taus_eta);
   fChain->SetBranchAddress("taus_phi", &taus_phi, &b_taus_phi);
   fChain->SetBranchAddress("taus_emFraction", &taus_emFraction, &b_taus_emFraction);
   fChain->SetBranchAddress("taus_leadingTrackPt", &taus_leadingTrackPt, &b_taus_leadingTrackPt);
   fChain->SetBranchAddress("taus_leadingTrackIpVtdxy", &taus_leadingTrackIpVtdxy, &b_taus_leadingTrackIpVtdxy);
   fChain->SetBranchAddress("taus_leadingTrackIpVtdz", &taus_leadingTrackIpVtdz, &b_taus_leadingTrackIpVtdz);
   fChain->SetBranchAddress("taus_leadingTrackIpVtdxyError", &taus_leadingTrackIpVtdxyError, &b_taus_leadingTrackIpVtdxyError);
   fChain->SetBranchAddress("taus_leadingTrackIpVtdzError", &taus_leadingTrackIpVtdzError, &b_taus_leadingTrackIpVtdzError);
   fChain->SetBranchAddress("taus_leadingTrackVx", &taus_leadingTrackVx, &b_taus_leadingTrackVx);
   fChain->SetBranchAddress("taus_leadingTrackVy", &taus_leadingTrackVy, &b_taus_leadingTrackVy);
   fChain->SetBranchAddress("taus_leadingTrackVz", &taus_leadingTrackVz, &b_taus_leadingTrackVz);
   fChain->SetBranchAddress("taus_leadingTrackValidHits", &taus_leadingTrackValidHits, &b_taus_leadingTrackValidHits);
   fChain->SetBranchAddress("taus_leadingTrackNormChiSqrd", &taus_leadingTrackNormChiSqrd, &b_taus_leadingTrackNormChiSqrd);
   fChain->SetBranchAddress("taus_numProngs", &taus_numProngs, &b_taus_numProngs);
   fChain->SetBranchAddress("taus_numSignalGammas", &taus_numSignalGammas, &b_taus_numSignalGammas);
   fChain->SetBranchAddress("taus_numSignalNeutrals", &taus_numSignalNeutrals, &b_taus_numSignalNeutrals);
   fChain->SetBranchAddress("taus_numSignalPiZeros", &taus_numSignalPiZeros, &b_taus_numSignalPiZeros);
   fChain->SetBranchAddress("taus_decayMode", &taus_decayMode, &b_taus_decayMode);
   fChain->SetBranchAddress("taus_charge", &taus_charge, &b_taus_charge);
   fChain->SetBranchAddress("taus_inTheCracks", &taus_inTheCracks, &b_taus_inTheCracks);
   fChain->SetBranchAddress("taus_HPSagainstElectronLoose", &taus_HPSagainstElectronLoose, &b_taus_HPSagainstElectronLoose);
   fChain->SetBranchAddress("taus_HPSagainstElectronMVA", &taus_HPSagainstElectronMVA, &b_taus_HPSagainstElectronMVA);
   fChain->SetBranchAddress("taus_HPSagainstElectronMedium", &taus_HPSagainstElectronMedium, &b_taus_HPSagainstElectronMedium);
   fChain->SetBranchAddress("taus_HPSagainstElectronTight", &taus_HPSagainstElectronTight, &b_taus_HPSagainstElectronTight);
   fChain->SetBranchAddress("taus_HPSagainstMuonLoose", &taus_HPSagainstMuonLoose, &b_taus_HPSagainstMuonLoose);
   fChain->SetBranchAddress("taus_HPSagainstMuonMedium", &taus_HPSagainstMuonMedium, &b_taus_HPSagainstMuonMedium);
   fChain->SetBranchAddress("taus_HPSagainstMuonTight", &taus_HPSagainstMuonTight, &b_taus_HPSagainstMuonTight);
   fChain->SetBranchAddress("taus_HPSbyLooseCombinedIsolationDeltaBetaCorr", &taus_HPSbyLooseCombinedIsolationDeltaBetaCorr, &b_taus_HPSbyLooseCombinedIsolationDeltaBetaCorr);
   fChain->SetBranchAddress("taus_HPSbyMediumCombinedIsolationDeltaBetaCorr", &taus_HPSbyMediumCombinedIsolationDeltaBetaCorr, &b_taus_HPSbyMediumCombinedIsolationDeltaBetaCorr);
   fChain->SetBranchAddress("taus_HPSbyTightCombinedIsolationDeltaBetaCorr", &taus_HPSbyTightCombinedIsolationDeltaBetaCorr, &b_taus_HPSbyTightCombinedIsolationDeltaBetaCorr);
   fChain->SetBranchAddress("taus_HPSbyVLooseCombinedIsolationDeltaBetaCorr", &taus_HPSbyVLooseCombinedIsolationDeltaBetaCorr, &b_taus_HPSbyVLooseCombinedIsolationDeltaBetaCorr);
   fChain->SetBranchAddress("taus_HPSdecayModeFinding", &taus_HPSdecayModeFinding, &b_taus_HPSdecayModeFinding);
   fChain->SetBranchAddress("taus_leadingTrackValid", &taus_leadingTrackValid, &b_taus_leadingTrackValid);
   fChain->SetBranchAddress("taus_genDeltaRLowest", &taus_genDeltaRLowest, &b_taus_genDeltaRLowest);
   fChain->SetBranchAddress("taus_genMatchedPdgId", &taus_genMatchedPdgId, &b_taus_genMatchedPdgId);
   fChain->SetBranchAddress("taus_genMatchedId", &taus_genMatchedId, &b_taus_genMatchedId);
   fChain->SetBranchAddress("taus_genMatchedMotherId", &taus_genMatchedMotherId, &b_taus_genMatchedMotherId);
   fChain->SetBranchAddress("taus_genMatchedMotherIdReverse", &taus_genMatchedMotherIdReverse, &b_taus_genMatchedMotherIdReverse);
   fChain->SetBranchAddress("taus_genMatchedGrandmotherId", &taus_genMatchedGrandmotherId, &b_taus_genMatchedGrandmotherId);
   fChain->SetBranchAddress("taus_genMatchedGrandmotherIdReverse", &taus_genMatchedGrandmotherIdReverse, &b_taus_genMatchedGrandmotherIdReverse);
   fChain->SetBranchAddress("tracks_pt", &tracks_pt, &b_tracks_pt);
   fChain->SetBranchAddress("tracks_px", &tracks_px, &b_tracks_px);
   fChain->SetBranchAddress("tracks_py", &tracks_py, &b_tracks_py);
   fChain->SetBranchAddress("tracks_pz", &tracks_pz, &b_tracks_pz);
   fChain->SetBranchAddress("tracks_phi", &tracks_phi, &b_tracks_phi);
   fChain->SetBranchAddress("tracks_eta", &tracks_eta, &b_tracks_eta);
   fChain->SetBranchAddress("tracks_theta", &tracks_theta, &b_tracks_theta);
   fChain->SetBranchAddress("tracks_normChi2", &tracks_normChi2, &b_tracks_normChi2);
   fChain->SetBranchAddress("tracks_dZ", &tracks_dZ, &b_tracks_dZ);
   fChain->SetBranchAddress("tracks_d0", &tracks_d0, &b_tracks_d0);
   fChain->SetBranchAddress("tracks_d0err", &tracks_d0err, &b_tracks_d0err);
   fChain->SetBranchAddress("tracks_vx", &tracks_vx, &b_tracks_vx);
   fChain->SetBranchAddress("tracks_vy", &tracks_vy, &b_tracks_vy);
   fChain->SetBranchAddress("tracks_vz", &tracks_vz, &b_tracks_vz);
   fChain->SetBranchAddress("tracks_charge", &tracks_charge, &b_tracks_charge);
   fChain->SetBranchAddress("tracks_numValidHits", &tracks_numValidHits, &b_tracks_numValidHits);
   fChain->SetBranchAddress("tracks_isHighPurity", &tracks_isHighPurity, &b_tracks_isHighPurity);
   fChain->SetBranchAddress("tracks_caloEMDeltaRp3", &tracks_caloEMDeltaRp3, &b_tracks_caloEMDeltaRp3);
   fChain->SetBranchAddress("tracks_caloHadDeltaRp3", &tracks_caloHadDeltaRp3, &b_tracks_caloHadDeltaRp3);
   fChain->SetBranchAddress("tracks_caloEMDeltaRp4", &tracks_caloEMDeltaRp4, &b_tracks_caloEMDeltaRp4);
   fChain->SetBranchAddress("tracks_caloHadDeltaRp4", &tracks_caloHadDeltaRp4, &b_tracks_caloHadDeltaRp4);
   fChain->SetBranchAddress("tracks_caloEMDeltaRp5", &tracks_caloEMDeltaRp5, &b_tracks_caloEMDeltaRp5);
   fChain->SetBranchAddress("tracks_caloHadDeltaRp5", &tracks_caloHadDeltaRp5, &b_tracks_caloHadDeltaRp5);
   fChain->SetBranchAddress("tracks_nTracksRp5", &tracks_nTracksRp5, &b_tracks_nTracksRp5);
   fChain->SetBranchAddress("tracks_nHitsMissingOuter", &tracks_nHitsMissingOuter, &b_tracks_nHitsMissingOuter);
   fChain->SetBranchAddress("tracks_nHitsMissingInner", &tracks_nHitsMissingInner, &b_tracks_nHitsMissingInner);
   fChain->SetBranchAddress("tracks_nHitsMissingMiddle", &tracks_nHitsMissingMiddle, &b_tracks_nHitsMissingMiddle);
   fChain->SetBranchAddress("tracks_depTrkRp5", &tracks_depTrkRp5, &b_tracks_depTrkRp5);
   fChain->SetBranchAddress("tracks_d0wrtBS", &tracks_d0wrtBS, &b_tracks_d0wrtBS);
   fChain->SetBranchAddress("tracks_dZwrtBS", &tracks_dZwrtBS, &b_tracks_dZwrtBS);
   fChain->SetBranchAddress("tracks_depTrkRp5MinusPt", &tracks_depTrkRp5MinusPt, &b_tracks_depTrkRp5MinusPt);
   fChain->SetBranchAddress("tracks_caloTotDeltaRp5", &tracks_caloTotDeltaRp5, &b_tracks_caloTotDeltaRp5);
   fChain->SetBranchAddress("tracks_caloTotDeltaRp5ByP", &tracks_caloTotDeltaRp5ByP, &b_tracks_caloTotDeltaRp5ByP);
   fChain->SetBranchAddress("tracks_caloTotDeltaRp5RhoCorr", &tracks_caloTotDeltaRp5RhoCorr, &b_tracks_caloTotDeltaRp5RhoCorr);
   fChain->SetBranchAddress("tracks_caloTotDeltaRp5ByPRhoCorr", &tracks_caloTotDeltaRp5ByPRhoCorr, &b_tracks_caloTotDeltaRp5ByPRhoCorr);
   fChain->SetBranchAddress("tracks_isIso", &tracks_isIso, &b_tracks_isIso);
   fChain->SetBranchAddress("tracks_isMatchedDeadEcal", &tracks_isMatchedDeadEcal, &b_tracks_isMatchedDeadEcal);
   fChain->SetBranchAddress("tracks_ptErrorByPt", &tracks_ptErrorByPt, &b_tracks_ptErrorByPt);
   fChain->SetBranchAddress("tracks_ptError", &tracks_ptError, &b_tracks_ptError);
   fChain->SetBranchAddress("tracks_ptRes", &tracks_ptRes, &b_tracks_ptRes);
   fChain->SetBranchAddress("tracks_d0wrtPV", &tracks_d0wrtPV, &b_tracks_d0wrtPV);
   fChain->SetBranchAddress("tracks_dZwrtPV", &tracks_dZwrtPV, &b_tracks_dZwrtPV);
   fChain->SetBranchAddress("tracks_genDeltaRLowest", &tracks_genDeltaRLowest, &b_tracks_genDeltaRLowest);
   fChain->SetBranchAddress("tracks_genMatchedPdgId", &tracks_genMatchedPdgId, &b_tracks_genMatchedPdgId);
   fChain->SetBranchAddress("tracks_genMatchedId", &tracks_genMatchedId, &b_tracks_genMatchedId);
   fChain->SetBranchAddress("tracks_genMatchedMotherId", &tracks_genMatchedMotherId, &b_tracks_genMatchedMotherId);
   fChain->SetBranchAddress("tracks_genMatchedMotherIdReverse", &tracks_genMatchedMotherIdReverse, &b_tracks_genMatchedMotherIdReverse);
   fChain->SetBranchAddress("tracks_genMatchedGrandmotherId", &tracks_genMatchedGrandmotherId, &b_tracks_genMatchedGrandmotherId);
   fChain->SetBranchAddress("tracks_genMatchedGrandmotherIdReverse", &tracks_genMatchedGrandmotherIdReverse, &b_tracks_genMatchedGrandmotherIdReverse);
   fChain->SetBranchAddress("mets_et", &mets_et, &b_mets_et);
   fChain->SetBranchAddress("mets_pt", &mets_pt, &b_mets_pt);
   fChain->SetBranchAddress("mets_px", &mets_px, &b_mets_px);
   fChain->SetBranchAddress("mets_py", &mets_py, &b_mets_py);
   fChain->SetBranchAddress("mets_phi", &mets_phi, &b_mets_phi);
   fChain->SetBranchAddress("mets_Upt", &mets_Upt, &b_mets_Upt);
   fChain->SetBranchAddress("mets_Uphi", &mets_Uphi, &b_mets_Uphi);
   fChain->SetBranchAddress("mets_NeutralEMFraction", &mets_NeutralEMFraction, &b_mets_NeutralEMFraction);
   fChain->SetBranchAddress("mets_NeutralHadEtFraction", &mets_NeutralHadEtFraction, &b_mets_NeutralHadEtFraction);
   fChain->SetBranchAddress("mets_ChargedEMEtFraction", &mets_ChargedEMEtFraction, &b_mets_ChargedEMEtFraction);
   fChain->SetBranchAddress("mets_ChargedHadEtFraction", &mets_ChargedHadEtFraction, &b_mets_ChargedHadEtFraction);
   fChain->SetBranchAddress("mets_MuonEtFraction", &mets_MuonEtFraction, &b_mets_MuonEtFraction);
   fChain->SetBranchAddress("mets_Type6EtFraction", &mets_Type6EtFraction, &b_mets_Type6EtFraction);
   fChain->SetBranchAddress("mets_Type7EtFraction", &mets_Type7EtFraction, &b_mets_Type7EtFraction);
   fChain->SetBranchAddress("mets_genPT", &mets_genPT, &b_mets_genPT);
   fChain->SetBranchAddress("mets_genPhi", &mets_genPhi, &b_mets_genPhi);
   fChain->SetBranchAddress("mets_muonCorEx", &mets_muonCorEx, &b_mets_muonCorEx);
   fChain->SetBranchAddress("mets_muonCorEy", &mets_muonCorEy, &b_mets_muonCorEy);
   fChain->SetBranchAddress("mets_jet20CorEx", &mets_jet20CorEx, &b_mets_jet20CorEx);
   fChain->SetBranchAddress("mets_jet20CorEy", &mets_jet20CorEy, &b_mets_jet20CorEy);
   fChain->SetBranchAddress("mets_jet1CorEx", &mets_jet1CorEx, &b_mets_jet1CorEx);
   fChain->SetBranchAddress("mets_jet1CorEy", &mets_jet1CorEy, &b_mets_jet1CorEy);
   fChain->SetBranchAddress("mets_sumET", &mets_sumET, &b_mets_sumET);
   fChain->SetBranchAddress("mets_corSumET", &mets_corSumET, &b_mets_corSumET);
   fChain->SetBranchAddress("mets_mEtSig", &mets_mEtSig, &b_mets_mEtSig);
   fChain->SetBranchAddress("mets_metSignificance", &mets_metSignificance, &b_mets_metSignificance);
   fChain->SetBranchAddress("mets_significance", &mets_significance, &b_mets_significance);
   fChain->SetBranchAddress("mets_sigmaX2", &mets_sigmaX2, &b_mets_sigmaX2);
   fChain->SetBranchAddress("mets_sigmaY2", &mets_sigmaY2, &b_mets_sigmaY2);
   fChain->SetBranchAddress("mets_sigmaXY", &mets_sigmaXY, &b_mets_sigmaXY);
   fChain->SetBranchAddress("mets_sigmaYX", &mets_sigmaYX, &b_mets_sigmaYX);
   fChain->SetBranchAddress("mets_maxEtInEmTowers", &mets_maxEtInEmTowers, &b_mets_maxEtInEmTowers);
   fChain->SetBranchAddress("mets_emEtFraction", &mets_emEtFraction, &b_mets_emEtFraction);
   fChain->SetBranchAddress("mets_emEtInEB", &mets_emEtInEB, &b_mets_emEtInEB);
   fChain->SetBranchAddress("mets_emEtInEE", &mets_emEtInEE, &b_mets_emEtInEE);
   fChain->SetBranchAddress("mets_emEtInHF", &mets_emEtInHF, &b_mets_emEtInHF);
   fChain->SetBranchAddress("mets_maxEtInHadTowers", &mets_maxEtInHadTowers, &b_mets_maxEtInHadTowers);
   fChain->SetBranchAddress("mets_hadEtFraction", &mets_hadEtFraction, &b_mets_hadEtFraction);
   fChain->SetBranchAddress("mets_hadEtInHB", &mets_hadEtInHB, &b_mets_hadEtInHB);
   fChain->SetBranchAddress("mets_hadEtInHE", &mets_hadEtInHE, &b_mets_hadEtInHE);
   fChain->SetBranchAddress("mets_hadEtInHF", &mets_hadEtInHF, &b_mets_hadEtInHF);
   fChain->SetBranchAddress("mets_hadEtInHO", &mets_hadEtInHO, &b_mets_hadEtInHO);
   fChain->SetBranchAddress("mets_UDeltaPx", &mets_UDeltaPx, &b_mets_UDeltaPx);
   fChain->SetBranchAddress("mets_UDeltaPy", &mets_UDeltaPy, &b_mets_UDeltaPy);
   fChain->SetBranchAddress("mets_UDeltaP", &mets_UDeltaP, &b_mets_UDeltaP);
   fChain->SetBranchAddress("mets_Uscale", &mets_Uscale, &b_mets_Uscale);
   fChain->SetBranchAddress("mets_type2corPx", &mets_type2corPx, &b_mets_type2corPx);
   fChain->SetBranchAddress("mets_type2corPy", &mets_type2corPy, &b_mets_type2corPy);
   fChain->SetBranchAddress("mets_T2pt", &mets_T2pt, &b_mets_T2pt);
   fChain->SetBranchAddress("mets_T2px", &mets_T2px, &b_mets_T2px);
   fChain->SetBranchAddress("mets_T2py", &mets_T2py, &b_mets_T2py);
   fChain->SetBranchAddress("mets_T2phi", &mets_T2phi, &b_mets_T2phi);
   fChain->SetBranchAddress("mets_T2sumET", &mets_T2sumET, &b_mets_T2sumET);
   fChain->SetBranchAddress("mets_pfT1jet1pt", &mets_pfT1jet1pt, &b_mets_pfT1jet1pt);
   fChain->SetBranchAddress("mets_pfT1jet1phi", &mets_pfT1jet1phi, &b_mets_pfT1jet1phi);
   fChain->SetBranchAddress("mets_pfT1jet6pt", &mets_pfT1jet6pt, &b_mets_pfT1jet6pt);
   fChain->SetBranchAddress("mets_pfT1jet6phi", &mets_pfT1jet6phi, &b_mets_pfT1jet6phi);
   fChain->SetBranchAddress("mets_pfT1jet10pt", &mets_pfT1jet10pt, &b_mets_pfT1jet10pt);
   fChain->SetBranchAddress("mets_pfT1jet10phi", &mets_pfT1jet10phi, &b_mets_pfT1jet10phi);
   fChain->SetBranchAddress("jets_energy", &jets_energy, &b_jets_energy);
   fChain->SetBranchAddress("jets_et", &jets_et, &b_jets_et);
   fChain->SetBranchAddress("jets_pt", &jets_pt, &b_jets_pt);
   fChain->SetBranchAddress("jets_px", &jets_px, &b_jets_px);
   fChain->SetBranchAddress("jets_py", &jets_py, &b_jets_py);
   fChain->SetBranchAddress("jets_pz", &jets_pz, &b_jets_pz);
   fChain->SetBranchAddress("jets_phi", &jets_phi, &b_jets_phi);
   fChain->SetBranchAddress("jets_eta", &jets_eta, &b_jets_eta);
   fChain->SetBranchAddress("jets_theta", &jets_theta, &b_jets_theta);
   fChain->SetBranchAddress("jets_Upt", &jets_Upt, &b_jets_Upt);
   fChain->SetBranchAddress("jets_Uenergy", &jets_Uenergy, &b_jets_Uenergy);
   fChain->SetBranchAddress("jets_L2pt", &jets_L2pt, &b_jets_L2pt);
   fChain->SetBranchAddress("jets_L2L3pt", &jets_L2L3pt, &b_jets_L2L3pt);
   fChain->SetBranchAddress("jets_L2L3respt", &jets_L2L3respt, &b_jets_L2L3respt);
   fChain->SetBranchAddress("jets_respt", &jets_respt, &b_jets_respt);
   fChain->SetBranchAddress("jets_EMfrac", &jets_EMfrac, &b_jets_EMfrac);
   fChain->SetBranchAddress("jets_Hadfrac", &jets_Hadfrac, &b_jets_Hadfrac);
   fChain->SetBranchAddress("jets_charge", &jets_charge, &b_jets_charge);
   fChain->SetBranchAddress("jets_mass", &jets_mass, &b_jets_mass);
   fChain->SetBranchAddress("jets_area", &jets_area, &b_jets_area);
   fChain->SetBranchAddress("jets_fHPD", &jets_fHPD, &b_jets_fHPD);
   fChain->SetBranchAddress("jets_approximatefHPD", &jets_approximatefHPD, &b_jets_approximatefHPD);
   fChain->SetBranchAddress("jets_genPartonET", &jets_genPartonET, &b_jets_genPartonET);
   fChain->SetBranchAddress("jets_genPartonPT", &jets_genPartonPT, &b_jets_genPartonPT);
   fChain->SetBranchAddress("jets_genPartonEta", &jets_genPartonEta, &b_jets_genPartonEta);
   fChain->SetBranchAddress("jets_genPartonPhi", &jets_genPartonPhi, &b_jets_genPartonPhi);
   fChain->SetBranchAddress("jets_genJetET", &jets_genJetET, &b_jets_genJetET);
   fChain->SetBranchAddress("jets_genJetPT", &jets_genJetPT, &b_jets_genJetPT);
   fChain->SetBranchAddress("jets_genJetEta", &jets_genJetEta, &b_jets_genJetEta);
   fChain->SetBranchAddress("jets_genJetPhi", &jets_genJetPhi, &b_jets_genJetPhi);
   fChain->SetBranchAddress("jets_btagTChighPur", &jets_btagTChighPur, &b_jets_btagTChighPur);
   fChain->SetBranchAddress("jets_btagTChighEff", &jets_btagTChighEff, &b_jets_btagTChighEff);
   fChain->SetBranchAddress("jets_btagJetProb", &jets_btagJetProb, &b_jets_btagJetProb);
   fChain->SetBranchAddress("jets_btagJetBProb", &jets_btagJetBProb, &b_jets_btagJetBProb);
   fChain->SetBranchAddress("jets_btagSoftEle", &jets_btagSoftEle, &b_jets_btagSoftEle);
   fChain->SetBranchAddress("jets_btagSoftMuon", &jets_btagSoftMuon, &b_jets_btagSoftMuon);
   fChain->SetBranchAddress("jets_btagSoftMuonNoIP", &jets_btagSoftMuonNoIP, &b_jets_btagSoftMuonNoIP);
   fChain->SetBranchAddress("jets_btagSecVertex", &jets_btagSecVertex, &b_jets_btagSecVertex);
   fChain->SetBranchAddress("jets_btagSecVertexHighEff", &jets_btagSecVertexHighEff, &b_jets_btagSecVertexHighEff);
   fChain->SetBranchAddress("jets_btagSecVertexHighPur", &jets_btagSecVertexHighPur, &b_jets_btagSecVertexHighPur);
   fChain->SetBranchAddress("jets_btagCombinedSecVertex", &jets_btagCombinedSecVertex, &b_jets_btagCombinedSecVertex);
   fChain->SetBranchAddress("jets_btagCombinedSecVertexMVA", &jets_btagCombinedSecVertexMVA, &b_jets_btagCombinedSecVertexMVA);
   fChain->SetBranchAddress("jets_btagSoftMuonByPt", &jets_btagSoftMuonByPt, &b_jets_btagSoftMuonByPt);
   fChain->SetBranchAddress("jets_btagSoftMuonByIP3", &jets_btagSoftMuonByIP3, &b_jets_btagSoftMuonByIP3);
   fChain->SetBranchAddress("jets_btagSoftElectronByPt", &jets_btagSoftElectronByPt, &b_jets_btagSoftElectronByPt);
   fChain->SetBranchAddress("jets_btagSoftElectronByIP3", &jets_btagSoftElectronByIP3, &b_jets_btagSoftElectronByIP3);
   fChain->SetBranchAddress("jets_n90Hits", &jets_n90Hits, &b_jets_n90Hits);
   fChain->SetBranchAddress("jets_hitsInN90", &jets_hitsInN90, &b_jets_hitsInN90);
   fChain->SetBranchAddress("jets_chargedHadronEnergyFraction", &jets_chargedHadronEnergyFraction, &b_jets_chargedHadronEnergyFraction);
   fChain->SetBranchAddress("jets_neutralHadronEnergyFraction", &jets_neutralHadronEnergyFraction, &b_jets_neutralHadronEnergyFraction);
   fChain->SetBranchAddress("jets_chargedEmEnergyFraction", &jets_chargedEmEnergyFraction, &b_jets_chargedEmEnergyFraction);
   fChain->SetBranchAddress("jets_neutralEmEnergyFraction", &jets_neutralEmEnergyFraction, &b_jets_neutralEmEnergyFraction);
   fChain->SetBranchAddress("jets_fLong", &jets_fLong, &b_jets_fLong);
   fChain->SetBranchAddress("jets_fShort", &jets_fShort, &b_jets_fShort);
   fChain->SetBranchAddress("jets_etaetaMoment", &jets_etaetaMoment, &b_jets_etaetaMoment);
   fChain->SetBranchAddress("jets_phiphiMoment", &jets_phiphiMoment, &b_jets_phiphiMoment);
   fChain->SetBranchAddress("jets_JESunc", &jets_JESunc, &b_jets_JESunc);
   fChain->SetBranchAddress("jets_JECuncUp", &jets_JECuncUp, &b_jets_JECuncUp);
   fChain->SetBranchAddress("jets_JECuncDown", &jets_JECuncDown, &b_jets_JECuncDown);
   fChain->SetBranchAddress("jets_puJetMVA_full", &jets_puJetMVA_full, &b_jets_puJetMVA_full);
   fChain->SetBranchAddress("jets_puJetMVA_simple", &jets_puJetMVA_simple, &b_jets_puJetMVA_simple);
   fChain->SetBranchAddress("jets_puJetMVA_cutbased", &jets_puJetMVA_cutbased, &b_jets_puJetMVA_cutbased);
   fChain->SetBranchAddress("jets_dZ", &jets_dZ, &b_jets_dZ);
   fChain->SetBranchAddress("jets_dR2Mean", &jets_dR2Mean, &b_jets_dR2Mean);
   fChain->SetBranchAddress("jets_dRMean", &jets_dRMean, &b_jets_dRMean);
   fChain->SetBranchAddress("jets_frac01", &jets_frac01, &b_jets_frac01);
   fChain->SetBranchAddress("jets_frac02", &jets_frac02, &b_jets_frac02);
   fChain->SetBranchAddress("jets_frac03", &jets_frac03, &b_jets_frac03);
   fChain->SetBranchAddress("jets_frac04", &jets_frac04, &b_jets_frac04);
   fChain->SetBranchAddress("jets_frac05", &jets_frac05, &b_jets_frac05);
   fChain->SetBranchAddress("jets_frac06", &jets_frac06, &b_jets_frac06);
   fChain->SetBranchAddress("jets_frac07", &jets_frac07, &b_jets_frac07);
   fChain->SetBranchAddress("jets_beta", &jets_beta, &b_jets_beta);
   fChain->SetBranchAddress("jets_betaStar", &jets_betaStar, &b_jets_betaStar);
   fChain->SetBranchAddress("jets_betaClassic", &jets_betaClassic, &b_jets_betaClassic);
   fChain->SetBranchAddress("jets_betaStarClassic", &jets_betaStarClassic, &b_jets_betaStarClassic);
   fChain->SetBranchAddress("jets_ptD", &jets_ptD, &b_jets_ptD);
   fChain->SetBranchAddress("jets_nvtx", &jets_nvtx, &b_jets_nvtx);
   fChain->SetBranchAddress("jets_d0", &jets_d0, &b_jets_d0);
   fChain->SetBranchAddress("jets_leadCandPt", &jets_leadCandPt, &b_jets_leadCandPt);
   fChain->SetBranchAddress("jets_leadCandVx", &jets_leadCandVx, &b_jets_leadCandVx);
   fChain->SetBranchAddress("jets_leadCandVy", &jets_leadCandVy, &b_jets_leadCandVy);
   fChain->SetBranchAddress("jets_leadCandVz", &jets_leadCandVz, &b_jets_leadCandVz);
   fChain->SetBranchAddress("jets_leadCandDistFromPV", &jets_leadCandDistFromPV, &b_jets_leadCandDistFromPV);
   fChain->SetBranchAddress("jets_flavour", &jets_flavour, &b_jets_flavour);
   fChain->SetBranchAddress("jets_Nconst", &jets_Nconst, &b_jets_Nconst);
   fChain->SetBranchAddress("jets_jetIDMinimal", &jets_jetIDMinimal, &b_jets_jetIDMinimal);
   fChain->SetBranchAddress("jets_jetIDLooseAOD", &jets_jetIDLooseAOD, &b_jets_jetIDLooseAOD);
   fChain->SetBranchAddress("jets_jetIDLoose", &jets_jetIDLoose, &b_jets_jetIDLoose);
   fChain->SetBranchAddress("jets_jetIDTight", &jets_jetIDTight, &b_jets_jetIDTight);
   fChain->SetBranchAddress("jets_genPartonId", &jets_genPartonId, &b_jets_genPartonId);
   fChain->SetBranchAddress("jets_genPartonMotherId", &jets_genPartonMotherId, &b_jets_genPartonMotherId);
   fChain->SetBranchAddress("jets_genPartonMother0Id", &jets_genPartonMother0Id, &b_jets_genPartonMother0Id);
   fChain->SetBranchAddress("jets_genPartonMother1Id", &jets_genPartonMother1Id, &b_jets_genPartonMother1Id);
   fChain->SetBranchAddress("jets_genPartonGrandMotherId", &jets_genPartonGrandMotherId, &b_jets_genPartonGrandMotherId);
   fChain->SetBranchAddress("jets_genPartonGrandMother00Id", &jets_genPartonGrandMother00Id, &b_jets_genPartonGrandMother00Id);
   fChain->SetBranchAddress("jets_genPartonGrandMother01Id", &jets_genPartonGrandMother01Id, &b_jets_genPartonGrandMother01Id);
   fChain->SetBranchAddress("jets_genPartonGrandMother10Id", &jets_genPartonGrandMother10Id, &b_jets_genPartonGrandMother10Id);
   fChain->SetBranchAddress("jets_genPartonGrandMother11Id", &jets_genPartonGrandMother11Id, &b_jets_genPartonGrandMother11Id);
   fChain->SetBranchAddress("jets_chargedMultiplicity", &jets_chargedMultiplicity, &b_jets_chargedMultiplicity);
   fChain->SetBranchAddress("jets_neutralMultiplicity", &jets_neutralMultiplicity, &b_jets_neutralMultiplicity);
   fChain->SetBranchAddress("jets_nconstituents", &jets_nconstituents, &b_jets_nconstituents);
   fChain->SetBranchAddress("jets_nHit", &jets_nHit, &b_jets_nHit);
   fChain->SetBranchAddress("jets_puJetId_full", &jets_puJetId_full, &b_jets_puJetId_full);
   fChain->SetBranchAddress("jets_puJetId_simple", &jets_puJetId_simple, &b_jets_puJetId_simple);
   fChain->SetBranchAddress("jets_puJetId_cutbased", &jets_puJetId_cutbased, &b_jets_puJetId_cutbased);
   fChain->SetBranchAddress("jets_puJetId_tight_full", &jets_puJetId_tight_full, &b_jets_puJetId_tight_full);
   fChain->SetBranchAddress("jets_puJetId_tight_simple", &jets_puJetId_tight_simple, &b_jets_puJetId_tight_simple);
   fChain->SetBranchAddress("jets_puJetId_tight_cutbased", &jets_puJetId_tight_cutbased, &b_jets_puJetId_tight_cutbased);
   fChain->SetBranchAddress("jets_puJetId_medium_full", &jets_puJetId_medium_full, &b_jets_puJetId_medium_full);
   fChain->SetBranchAddress("jets_puJetId_medium_simple", &jets_puJetId_medium_simple, &b_jets_puJetId_medium_simple);
   fChain->SetBranchAddress("jets_puJetId_medium_cutbased", &jets_puJetId_medium_cutbased, &b_jets_puJetId_medium_cutbased);
   fChain->SetBranchAddress("jets_puJetId_loose_full", &jets_puJetId_loose_full, &b_jets_puJetId_loose_full);
   fChain->SetBranchAddress("jets_puJetId_loose_simple", &jets_puJetId_loose_simple, &b_jets_puJetId_loose_simple);
   fChain->SetBranchAddress("jets_puJetId_loose_cutbased", &jets_puJetId_loose_cutbased, &b_jets_puJetId_loose_cutbased);
   fChain->SetBranchAddress("genjets_pt", &genjets_pt, &b_genjets_pt);
   fChain->SetBranchAddress("genjets_eta", &genjets_eta, &b_genjets_eta);
   fChain->SetBranchAddress("genjets_phi", &genjets_phi, &b_genjets_phi);
   fChain->SetBranchAddress("genjets_px", &genjets_px, &b_genjets_px);
   fChain->SetBranchAddress("genjets_py", &genjets_py, &b_genjets_py);
   fChain->SetBranchAddress("genjets_pz", &genjets_pz, &b_genjets_pz);
   fChain->SetBranchAddress("genjets_et", &genjets_et, &b_genjets_et);
   fChain->SetBranchAddress("genjets_energy", &genjets_energy, &b_genjets_energy);
   fChain->SetBranchAddress("genjets_mass", &genjets_mass, &b_genjets_mass);
   fChain->SetBranchAddress("genjets_emEnergy", &genjets_emEnergy, &b_genjets_emEnergy);
   fChain->SetBranchAddress("genjets_hadEnergy", &genjets_hadEnergy, &b_genjets_hadEnergy);
   fChain->SetBranchAddress("genjets_invisibleEnergy", &genjets_invisibleEnergy, &b_genjets_invisibleEnergy);
   fChain->SetBranchAddress("genjets_auxiliaryEnergy", &genjets_auxiliaryEnergy, &b_genjets_auxiliaryEnergy);
   fChain->SetBranchAddress("genjets_charge", &genjets_charge, &b_genjets_charge);
   fChain->SetBranchAddress("superclusters_energy", &superclusters_energy, &b_superclusters_energy);
   fChain->SetBranchAddress("superclusters_et", &superclusters_et, &b_superclusters_et);
   fChain->SetBranchAddress("superclusters_ex", &superclusters_ex, &b_superclusters_ex);
   fChain->SetBranchAddress("superclusters_ey", &superclusters_ey, &b_superclusters_ey);
   fChain->SetBranchAddress("superclusters_ez", &superclusters_ez, &b_superclusters_ez);
   fChain->SetBranchAddress("superclusters_phi", &superclusters_phi, &b_superclusters_phi);
   fChain->SetBranchAddress("superclusters_eta", &superclusters_eta, &b_superclusters_eta);
   fChain->SetBranchAddress("superclusters_theta", &superclusters_theta, &b_superclusters_theta);
   Notify();
}

Bool_t BNTree::Notify()
{
   // The Notify() function is called when a new file is opened. This
   // can be either for a new TTree in a TChain or when when a new TTree
   // is started when using PROOF. It is normally not necessary to make changes
   // to the generated code, but the routine can be extended by the
   // user if needed. The return value is currently not used.

   return kTRUE;
}

void BNTree::Show(Long64_t entry)
{
// Print contents of entry.
// If entry is not specified, print current entry
   if (!fChain) return;
   fChain->Show(entry);
}
Int_t BNTree::Cut(Long64_t entry)
{
// This function may be called from Loop.
// returns  1 if entry is accepted.
// returns -1 otherwise.
   return 1;
}
#endif // #ifdef BNTree_cxx
