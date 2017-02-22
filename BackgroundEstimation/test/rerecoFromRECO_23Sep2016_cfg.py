# Auto generated configuration file
# using: 
# Revision: 1.19 
# Source: /local/reps/CMSSW/CMSSW/Configuration/Applications/python/ConfigBuilder.py,v 
# with command line options: RECO -s RECO,EI,PAT --runUnscheduled --nThreads 4 --data --era Run2_2016 --scenario pp --conditions 80X_dataRun2_Prompt_v15 --inputEventContent RECO --eventcontent MINIAOD --datatier MINIAOD --customise DisappTrks/BackgroundEstimation/customize.addMoreCaloTowers,DisappTrks/BackgroundEstimation/customize.addMoreElectronSeeds,Configuration/DataProcessing/RecoTLR.customisePostEra_Run2_2016 --filein file:pippo.root -n 100 --python_filename=rerecoFromRECO_23Sep2016_cfg.py --no_exec
import FWCore.ParameterSet.Config as cms

from Configuration.StandardSequences.Eras import eras

process = cms.Process('RERECO',eras.Run2_2016)

# import of standard configurations
process.load('Configuration.StandardSequences.Services_cff')
process.load('SimGeneral.HepPDTESSource.pythiapdt_cfi')
process.load('FWCore.MessageService.MessageLogger_cfi')
process.load('Configuration.EventContent.EventContent_cff')
process.load('Configuration.StandardSequences.GeometryRecoDB_cff')
process.load('Configuration.StandardSequences.MagneticField_AutoFromDBCurrent_cff')
process.load('Configuration.StandardSequences.Reconstruction_Data_cff')
process.load('CommonTools.ParticleFlow.EITopPAG_cff')
process.load('PhysicsTools.PatAlgos.slimming.metFilterPaths_cff')
process.load('Configuration.StandardSequences.EndOfProcess_cff')
process.load('Configuration.StandardSequences.FrontierConditions_GlobalTag_cff')

process.maxEvents = cms.untracked.PSet(
    input = cms.untracked.int32(100)
)

# Input source
process.source = cms.Source("PoolSource",
    dropDescendantsOfDroppedBranches = cms.untracked.bool(False),
    fileNames = cms.untracked.vstring('file:pippo.root'),
    inputCommands = cms.untracked.vstring( ('drop *', 
        'keep DetIdedmEDCollection_siStripDigis_*_*', 
        'keep DetIdedmEDCollection_siPixelDigis_*_*', 
        'keep *_siPixelClusters_*_*', 
        'keep *_siStripClusters_*_*', 
        'keep ClusterSummary_clusterSummaryProducer_*_*', 
        'keep *_dt1DRecHits_*_*', 
        'keep *_dt4DSegments_*_*', 
        'keep *_dt1DCosmicRecHits_*_*', 
        'keep *_dt4DCosmicSegments_*_*', 
        'keep *_csc2DRecHits_*_*', 
        'keep *_cscSegments_*_*', 
        'keep *_rpcRecHits_*_*', 
        'keep *_hbhereco_*_*', 
        'keep *_hbheprereco_*_*', 
        'keep *_hfreco_*_*', 
        'keep *_horeco_*_*', 
        'keep HBHERecHitsSorted_hbherecoMB_*_*', 
        'keep HORecHitsSorted_horecoMB_*_*', 
        'keep HFRecHitsSorted_hfrecoMB_*_*', 
        'keep ZDCDataFramesSorted_hcalDigis_*_*', 
        'keep ZDCRecHitsSorted_*_*_*', 
        'keep *_reducedHcalRecHits_*_*', 
        'keep *_castorreco_*_*', 
        'keep HcalUnpackerReport_castorDigis_*_*', 
        'keep HcalUnpackerReport_hcalDigiAlCaMB_*_*', 
        'keep HcalUnpackerReport_hcalDigis_*_*', 
        'keep *_ecalPreshowerRecHit_*_*', 
        'keep *_ecalRecHit_*_*', 
        'keep *_ecalCompactTrigPrim_*_*', 
        'keep *_ecalTPSkim_*_*', 
        'keep *_selectDigi_*_*', 
        'keep EcalRecHitsSorted_reducedEcalRecHitsEE_*_*', 
        'keep EcalRecHitsSorted_reducedEcalRecHitsEB_*_*', 
        'keep EcalRecHitsSorted_reducedEcalRecHitsES_*_*', 
        'keep *_hybridSuperClusters_*_*', 
        'keep recoSuperClusters_correctedHybridSuperClusters_*_*', 
        'keep *_multi5x5SuperClusters_*_*', 
        'keep recoSuperClusters_multi5x5SuperClusters_*_*', 
        'keep recoSuperClusters_multi5x5SuperClustersWithPreshower_*_*', 
        'keep recoSuperClusters_correctedMulti5x5SuperClustersWithPreshower_*_*', 
        'keep recoPreshowerClusters_multi5x5SuperClustersWithPreshower_*_*', 
        'keep recoPreshowerClusterShapes_multi5x5PreshowerClusterShape_*_*', 
        'keep *_particleFlowSuperClusterECAL_*_*', 
        'drop recoClusterShapes_*_*_*', 
        'drop recoBasicClustersToOnerecoClusterShapesAssociation_*_*_*', 
        'drop recoBasicClusters_multi5x5BasicClusters_multi5x5BarrelBasicClusters_*', 
        'drop recoSuperClusters_multi5x5SuperClusters_multi5x5BarrelSuperClusters_*', 
        'keep *_CkfElectronCandidates_*_*', 
        'keep *_GsfGlobalElectronTest_*_*', 
        'keep *_electronMergedSeeds_*_*', 
        'keep recoGsfTracks_electronGsfTracks_*_*', 
        'keep recoGsfTrackExtras_electronGsfTracks_*_*', 
        'keep recoTrackExtras_electronGsfTracks_*_*', 
        'keep TrackingRecHitsOwned_electronGsfTracks_*_*', 
        'keep recoTracks_generalTracks_*_*', 
        'keep recoTrackExtras_generalTracks_*_*', 
        'keep TrackingRecHitsOwned_generalTracks_*_*', 
        'keep *_generalTracks_MVAValues_*', 
        'keep *_generalTracks_MVAVals_*', 
        'keep TrackingRecHitsOwned_extraFromSeeds_*_*', 
        'keep uints_extraFromSeeds_*_*', 
        'keep recoTracks_beamhaloTracks_*_*', 
        'keep recoTrackExtras_beamhaloTracks_*_*', 
        'keep TrackingRecHitsOwned_beamhaloTracks_*_*', 
        'keep recoTracks_conversionStepTracks_*_*', 
        'keep recoTrackExtras_conversionStepTracks_*_*', 
        'keep TrackingRecHitsOwned_conversionStepTracks_*_*', 
        'keep *_ctfPixelLess_*_*', 
        'keep *_dedxTruncated40_*_*', 
        'keep *_dedxHitInfo_*_*', 
        'keep *_dedxHarmonic2_*_*', 
        'keep *_trackExtrapolator_*_*', 
        'keep recoTracks_cosmicDCTracks_*_*', 
        'keep recoTrackExtras_cosmicDCTracks_*_*', 
        'keep TrackingRecHitsOwned_cosmicDCTracks_*_*', 
        'keep *_ak4CaloJets_*_*', 
        'keep *_ak4PFJets_*_*', 
        'keep *_ak4PFJetsCHS_*_*', 
        'keep *_ak8PFJetsCHS_*_*', 
        'keep *_ak8PFJetsCHSSoftDrop_*_*', 
        'keep *_cmsTopTagPFJetsCHS_*_*', 
        'keep *_JetPlusTrackZSPCorJetAntiKt4_*_*', 
        'keep *_ak4TrackJets_*_*', 
        'keep recoRecoChargedRefCandidates_trackRefsForJets_*_*', 
        'keep *_caloTowers_*_*', 
        'keep *_towerMaker_*_*', 
        'keep *_CastorTowerReco_*_*', 
        'keep *_ak4JetTracksAssociatorAtVertex_*_*', 
        'keep *_ak4JetTracksAssociatorAtVertexPF_*_*', 
        'keep *_ak4JetTracksAssociatorAtCaloFace_*_*', 
        'keep *_ak4JetTracksAssociatorExplicit_*_*', 
        'keep *_ak4JetExtender_*_*', 
        'keep *_ak4JetID_*_*', 
        'keep *_ak5CastorJets_*_*', 
        'keep *_ak5CastorJetID_*_*', 
        'keep *_ak7CastorJets_*_*', 
        'keep *_ak7CastorJetID_*_*', 
        'keep *_fixedGridRhoAll_*_*', 
        'keep *_fixedGridRhoFastjetAll_*_*', 
        'keep *_fixedGridRhoFastjetAllTmp_*_*', 
        'keep *_fixedGridRhoFastjetAllCalo_*_*', 
        'keep *_fixedGridRhoFastjetCentral_*_*', 
        'keep *_fixedGridRhoFastjetCentralCalo_*_*', 
        'keep *_fixedGridRhoFastjetCentralChargedPileUp_*_*', 
        'keep *_fixedGridRhoFastjetCentralNeutral_*_*', 
        'keep *_ak8PFJetsCHSSoftDropMass_*_*', 
        'keep recoCaloMETs_caloMet_*_*', 
        'keep recoCaloMETs_caloMetBE_*_*', 
        'keep recoCaloMETs_caloMetBEFO_*_*', 
        'keep recoCaloMETs_caloMetM_*_*', 
        'keep recoPFMETs_pfMet_*_*', 
        'keep recoPFMETs_pfChMet_*_*', 
        'keep recoPFMETs_pfMetEI_*_*', 
        'keep recoMuonMETCorrectionDataedmValueMap_muonMETValueMapProducer_*_*', 
        'keep recoHcalNoiseRBXs_hcalnoise_*_*', 
        'keep HcalNoiseSummary_hcalnoise_*_*', 
        'keep recoCSCHaloData_CSCHaloData_*_*', 
        'keep recoEcalHaloData_EcalHaloData_*_*', 
        'keep recoGlobalHaloData_GlobalHaloData_*_*', 
        'keep recoHcalHaloData_HcalHaloData_*_*', 
        'keep recoBeamHaloSummary_BeamHaloSummary_*_*', 
        'keep *_MuonSeed_*_*', 
        'keep *_ancientMuonSeed_*_*', 
        'keep *_displacedMuonSeeds_*_*', 
        'keep TrackingRecHitsOwned_globalMuons_*_*', 
        'keep TrackingRecHitsOwned_tevMuons_*_*', 
        'keep recoCaloMuons_calomuons_*_*', 
        'keep *_CosmicMuonSeed_*_*', 
        'keep recoTrackExtras_cosmicMuons_*_*', 
        'keep TrackingRecHitsOwned_cosmicMuons_*_*', 
        'keep recoTrackExtras_cosmicMuons1Leg_*_*', 
        'keep TrackingRecHitsOwned_cosmicMuons1Leg_*_*', 
        'keep recoTracks_cosmicsVetoTracks_*_*', 
        'keep *_SETMuonSeed_*_*', 
        'keep recoTracks_standAloneSETMuons_*_*', 
        'keep recoTrackExtras_standAloneSETMuons_*_*', 
        'keep TrackingRecHitsOwned_standAloneSETMuons_*_*', 
        'keep recoTracks_globalSETMuons_*_*', 
        'keep recoTrackExtras_globalSETMuons_*_*', 
        'keep TrackingRecHitsOwned_globalSETMuons_*_*', 
        'keep recoMuons_muonsWithSET_*_*', 
        'keep *_muons_*_*', 
        'keep *_particleFlow_muons_*', 
        'drop *_muons_muons1stStep2muonsMap_*', 
        'drop recoIsoDepositedmValueMap_muons_*_*', 
        'drop doubleedmValueMap_muons_muPFIso*_*', 
        'keep recoTracks_standAloneMuons_*_*', 
        'keep recoTrackExtras_standAloneMuons_*_*', 
        'keep TrackingRecHitsOwned_standAloneMuons_*_*', 
        'keep recoTracks_globalMuons_*_*', 
        'keep recoTrackExtras_globalMuons_*_*', 
        'keep recoTracks_tevMuons_*_*', 
        'keep recoTrackExtras_tevMuons_*_*', 
        'keep recoTracks_generalTracks_*_*', 
        'keep recoTracks_displacedTracks_*_*', 
        'keep recoTracksToOnerecoTracksAssociation_tevMuons_*_*', 
        'keep recoTracks_displacedGlobalMuons_*_*', 
        'keep recoTrackExtras_displacedGlobalMuons_*_*', 
        'keep TrackingRecHitsOwned_displacedGlobalMuons_*_*', 
        'keep recoTracks_cosmicMuons_*_*', 
        'keep recoMuons_muonsFromCosmics_*_*', 
        'keep recoTracks_cosmicMuons1Leg_*_*', 
        'keep recoMuons_muonsFromCosmics1Leg_*_*', 
        'keep recoTracks_refittedStandAloneMuons_*_*', 
        'keep recoTrackExtras_refittedStandAloneMuons_*_*', 
        'keep TrackingRecHitsOwned_refittedStandAloneMuons_*_*', 
        'keep recoTracks_displacedStandAloneMuons__*', 
        'keep recoTrackExtras_displacedStandAloneMuons_*_*', 
        'keep TrackingRecHitsOwned_displacedStandAloneMuons_*_*', 
        'keep *_muIsoDepositTk_*_*', 
        'keep *_muIsoDepositCalByAssociatorTowers_*_*', 
        'keep *_muIsoDepositCalByAssociatorHits_*_*', 
        'keep *_muIsoDepositJets_*_*', 
        'keep *_muGlobalIsoDepositCtfTk_*_*', 
        'keep *_muGlobalIsoDepositCalByAssociatorTowers_*_*', 
        'keep *_muGlobalIsoDepositCalByAssociatorHits_*_*', 
        'keep *_muGlobalIsoDepositJets_*_*', 
        'keep *_softPFMuonsTagInfos_*_*', 
        'keep *_softPFElectronsTagInfos_*_*', 
        'keep *_softPFElectronBJetTags_*_*', 
        'keep *_softPFMuonBJetTags_*_*', 
        'keep *_pfImpactParameterTagInfos_*_*', 
        'keep *_pfTrackCountingHighEffBJetTags_*_*', 
        'keep *_pfJetProbabilityBJetTags_*_*', 
        'keep *_pfJetBProbabilityBJetTags_*_*', 
        'keep *_pfSecondaryVertexTagInfos_*_*', 
        'keep *_pfInclusiveSecondaryVertexFinderTagInfos_*_*', 
        'keep *_pfSimpleSecondaryVertexHighEffBJetTags_*_*', 
        'keep *_pfSimpleInclusiveSecondaryVertexHighEffBJetTags_*_*', 
        'keep *_pfCombinedSecondaryVertexV2BJetTags_*_*', 
        'keep *_pfCombinedInclusiveSecondaryVertexV2BJetTags_*_*', 
        'keep *_pfCombinedMVAV2BJetTags_*_*', 
        'keep *_inclusiveCandidateSecondaryVertices_*_*', 
        'keep *_inclusiveCandidateSecondaryVerticesCvsL_*_*', 
        'keep *_pfInclusiveSecondaryVertexFinderCvsLTagInfos_*_*', 
        'keep *_pfCombinedCvsLJetTags_*_*', 
        'keep *_pfCombinedCvsBJetTags_*_*', 
        'keep recoRecoTauPiZeros_hpsPFTauProducer_pizeros_*', 
        'keep recoPFTaus_hpsPFTauProducer_*_*', 
        'keep *_hpsPFTauDiscriminationByDeadECALElectronRejection_*_*', 
        'keep *_hpsPFTauDiscriminationByDecayModeFinding_*_*', 
        'keep *_hpsPFTauDiscriminationByDecayModeFindingNewDMs_*_*', 
        'keep *_hpsPFTauDiscriminationByDecayModeFindingOldDMs_*_*', 
        'keep *_hpsPFTauDiscriminationByLooseIsolation_*_*', 
        'keep *_hpsPFTauDiscriminationByLooseChargedIsolation_*_*', 
        'keep *_hpsPFTauDiscriminationByLooseCombinedIsolationDBSumPtCorr3Hits_*_*', 
        'keep *_hpsPFTauDiscriminationByLooseCombinedIsolationDBSumPtCorr3HitsdR03_*_*', 
        'keep *_hpsPFTauDiscriminationByLooseElectronRejection_*_*', 
        'keep *_hpsPFTauDiscriminationByLooseMuonRejection3_*_*', 
        'keep *_hpsPFTauDiscriminationByMediumCombinedIsolationDBSumPtCorr3Hits_*_*', 
        'keep *_hpsPFTauDiscriminationByMediumCombinedIsolationDBSumPtCorr3HitsdR03_*_*', 
        'keep *_hpsPFTauDiscriminationByRawCombinedIsolationDBSumPtCorr3Hits_*_*', 
        'keep *_hpsPFTauDiscriminationByTightCombinedIsolationDBSumPtCorr3Hits_*_*', 
        'keep *_hpsPFTauDiscriminationByTightCombinedIsolationDBSumPtCorr3HitsdR03_*_*', 
        'keep *_hpsPFTauDiscriminationByTightMuonRejection3_*_*', 
        'keep *_hpsPFTauDiscriminationByPhotonPtSumOutsideSignalCone_*_*', 
        'keep *_hpsPFTauNeutralIsoPtSum_*_*', 
        'keep *_hpsPFTauPUcorrPtSum_*_*', 
        'keep *_hpsPFTauChargedIsoPtSum_*_*', 
        'keep *_hpsPFTauTransverseImpactParameters_*_*', 
        'keep *_hpsPFTauFootprintCorrection_*_*', 
        'keep *_hpsPFTauNeutralIsoPtSumWeight_*_*', 
        'keep *_hpsPFTauPhotonPtSumOutsideSignalCone_*_*', 
        'keep *_hpsPFTauDiscriminationByMVA6rawElectronRejection_*_*', 
        'keep *_hpsPFTauDiscriminationByMVA6VLooseElectronRejection_*_*', 
        'keep *_hpsPFTauDiscriminationByMVA6LooseElectronRejection_*_*', 
        'keep *_hpsPFTauDiscriminationByMVA6MediumElectronRejection_*_*', 
        'keep *_hpsPFTauDiscriminationByMVA6TightElectronRejection_*_*', 
        'keep *_hpsPFTauDiscriminationByMVA6VTightElectronRejection_*_*', 
        'keep *_hpsPFTauDiscriminationByIsolationMVArun2v1DBoldDMwLTraw_*_*', 
        'keep *_hpsPFTauDiscriminationByVLooseIsolationMVArun2v1DBoldDMwLT_*_*', 
        'keep *_hpsPFTauDiscriminationByLooseIsolationMVArun2v1DBoldDMwLT_*_*', 
        'keep *_hpsPFTauDiscriminationByMediumIsolationMVArun2v1DBoldDMwLT_*_*', 
        'keep *_hpsPFTauDiscriminationByTightIsolationMVArun2v1DBoldDMwLT_*_*', 
        'keep *_hpsPFTauDiscriminationByVTightIsolationMVArun2v1DBoldDMwLT_*_*', 
        'keep *_hpsPFTauDiscriminationByVVTightIsolationMVArun2v1DBoldDMwLT_*_*', 
        'keep *_hpsPFTauDiscriminationByIsolationMVArun2v1DBnewDMwLTraw_*_*', 
        'keep *_hpsPFTauDiscriminationByVLooseIsolationMVArun2v1DBnewDMwLT_*_*', 
        'keep *_hpsPFTauDiscriminationByLooseIsolationMVArun2v1DBnewDMwLT_*_*', 
        'keep *_hpsPFTauDiscriminationByMediumIsolationMVArun2v1DBnewDMwLT_*_*', 
        'keep *_hpsPFTauDiscriminationByTightIsolationMVArun2v1DBnewDMwLT_*_*', 
        'keep *_hpsPFTauDiscriminationByVTightIsolationMVArun2v1DBnewDMwLT_*_*', 
        'keep *_hpsPFTauDiscriminationByVVTightIsolationMVArun2v1DBnewDMwLT_*_*', 
        'keep *_hpsPFTauDiscriminationByIsolationMVArun2v1PWoldDMwLTraw_*_*', 
        'keep *_hpsPFTauDiscriminationByVLooseIsolationMVArun2v1PWoldDMwLT_*_*', 
        'keep *_hpsPFTauDiscriminationByLooseIsolationMVArun2v1PWoldDMwLT_*_*', 
        'keep *_hpsPFTauDiscriminationByMediumIsolationMVArun2v1PWoldDMwLT_*_*', 
        'keep *_hpsPFTauDiscriminationByTightIsolationMVArun2v1PWoldDMwLT_*_*', 
        'keep *_hpsPFTauDiscriminationByVTightIsolationMVArun2v1PWoldDMwLT_*_*', 
        'keep *_hpsPFTauDiscriminationByVVTightIsolationMVArun2v1PWoldDMwLT_*_*', 
        'keep *_hpsPFTauDiscriminationByIsolationMVArun2v1PWnewDMwLTraw_*_*', 
        'keep *_hpsPFTauDiscriminationByVLooseIsolationMVArun2v1PWnewDMwLT_*_*', 
        'keep *_hpsPFTauDiscriminationByLooseIsolationMVArun2v1PWnewDMwLT_*_*', 
        'keep *_hpsPFTauDiscriminationByMediumIsolationMVArun2v1PWnewDMwLT_*_*', 
        'keep *_hpsPFTauDiscriminationByTightIsolationMVArun2v1PWnewDMwLT_*_*', 
        'keep *_hpsPFTauDiscriminationByVTightIsolationMVArun2v1PWnewDMwLT_*_*', 
        'keep *_hpsPFTauDiscriminationByVVTightIsolationMVArun2v1PWnewDMwLT_*_*', 
        'keep *_hpsPFTauChargedIsoPtSumdR03_*_*', 
        'keep *_hpsPFTauNeutralIsoPtSumdR03_*_*', 
        'keep *_hpsPFTauNeutralIsoPtSumWeightdR03_*_*', 
        'keep *_hpsPFTauFootprintCorrectiondR03_*_*', 
        'keep *_hpsPFTauPhotonPtSumOutsideSignalConedR03_*_*', 
        'keep *_hpsPFTauDiscriminationByIsolationMVArun2v1DBdR03oldDMwLTraw_*_*', 
        'keep *_hpsPFTauDiscriminationByVLooseIsolationMVArun2v1DBdR03oldDMwLT_*_*', 
        'keep *_hpsPFTauDiscriminationByLooseIsolationMVArun2v1DBdR03oldDMwLT_*_*', 
        'keep *_hpsPFTauDiscriminationByMediumIsolationMVArun2v1DBdR03oldDMwLT_*_*', 
        'keep *_hpsPFTauDiscriminationByTightIsolationMVArun2v1DBdR03oldDMwLT_*_*', 
        'keep *_hpsPFTauDiscriminationByVTightIsolationMVArun2v1DBdR03oldDMwLT_*_*', 
        'keep *_hpsPFTauDiscriminationByVVTightIsolationMVArun2v1DBdR03oldDMwLT_*_*', 
        'keep *_hpsPFTauDiscriminationByIsolationMVArun2v1PWdR03oldDMwLTraw_*_*', 
        'keep *_hpsPFTauDiscriminationByVLooseIsolationMVArun2v1PWdR03oldDMwLT_*_*', 
        'keep *_hpsPFTauDiscriminationByLooseIsolationMVArun2v1PWdR03oldDMwLT_*_*', 
        'keep *_hpsPFTauDiscriminationByMediumIsolationMVArun2v1PWdR03oldDMwLT_*_*', 
        'keep *_hpsPFTauDiscriminationByTightIsolationMVArun2v1PWdR03oldDMwLT_*_*', 
        'keep *_hpsPFTauDiscriminationByVTightIsolationMVArun2v1PWdR03oldDMwLT_*_*', 
        'keep *_hpsPFTauDiscriminationByVVTightIsolationMVArun2v1PWdR03oldDMwLT_*_*', 
        'keep  *_offlinePrimaryVertices__*', 
        'keep *_offlinePrimaryVerticesWithBS_*_*', 
        'keep *_offlinePrimaryVerticesFromCosmicTracks_*_*', 
        'keep *_nuclearInteractionMaker_*_*', 
        'keep *_generalV0Candidates_*_*', 
        'keep *_inclusiveSecondaryVertices_*_*', 
        'keep recoGsfElectronCores_gsfElectronCores_*_*', 
        'keep recoGsfElectronCores_gedGsfElectronCores_*_*', 
        'keep recoGsfElectrons_gsfElectrons_*_*', 
        'keep recoGsfElectrons_gedGsfElectrons_*_*', 
        'keep recoGsfElectronCores_uncleanedOnlyGsfElectronCores_*_*', 
        'keep recoGsfElectrons_uncleanedOnlyGsfElectrons_*_*', 
        'keep floatedmValueMap_eidRobustLoose_*_*', 
        'keep floatedmValueMap_eidRobustTight_*_*', 
        'keep floatedmValueMap_eidRobustHighEnergy_*_*', 
        'keep floatedmValueMap_eidLoose_*_*', 
        'keep floatedmValueMap_eidTight_*_*', 
        'keep *_egmGedGsfElectronPFIsolation_*_*', 
        'keep *_photonEcalPFClusterIsolationProducer_*_*', 
        'keep *_electronEcalPFClusterIsolationProducer_*_*', 
        'keep *_photonHcalPFClusterIsolationProducer_*_*', 
        'keep *_electronHcalPFClusterIsolationProducer_*_*', 
        'drop *_egmGsfElectronIDs_*_*', 
        'drop *_egmPhotonIDs_*_*', 
        'keep *_gedPhotonCore_*_*', 
        'keep *_gedPhotons_*_*', 
        'keep *_particleBasedIsolation_*_*', 
        'keep recoPhotons_mustachePhotons_*_*', 
        'keep recoPhotonCores_mustachePhotonCore_*_*', 
        'keep recoPhotons_photons_*_*', 
        'keep recoPhotonCores_photonCore_*_*', 
        'keep recoConversions_conversions_*_*', 
        'keep recoConversions_mustacheConversions_*_*', 
        'drop *_conversions_uncleanedConversions_*', 
        'drop *_gedPhotonsTmp_valMapPFEgammaCandToPhoton_*', 
        'keep recoConversions_allConversions_*_*', 
        'keep recoConversions_allConversionsOldEG_*_*', 
        'keep recoTracks_ckfOutInTracksFromConversions_*_*', 
        'keep recoTracks_ckfInOutTracksFromConversions_*_*', 
        'keep recoTrackExtras_ckfOutInTracksFromConversions_*_*', 
        'keep recoTrackExtras_ckfInOutTracksFromConversions_*_*', 
        'keep TrackingRecHitsOwned_ckfOutInTracksFromConversions_*_*', 
        'keep TrackingRecHitsOwned_ckfInOutTracksFromConversions_*_*', 
        'keep recoConversions_uncleanedOnlyAllConversions_*_*', 
        'keep recoTracks_uncleanedOnlyCkfOutInTracksFromConversions_*_*', 
        'keep recoTracks_uncleanedOnlyCkfInOutTracksFromConversions_*_*', 
        'keep recoTrackExtras_uncleanedOnlyCkfOutInTracksFromConversions_*_*', 
        'keep recoTrackExtras_uncleanedOnlyCkfInOutTracksFromConversions_*_*', 
        'keep TrackingRecHitsOwned_uncleanedOnlyCkfOutInTracksFromConversions_*_*', 
        'keep TrackingRecHitsOwned_uncleanedOnlyCkfInOutTracksFromConversions_*_*', 
        'keep *_PhotonIDProd_*_*', 
        'keep *_PhotonIDProdGED_*_*', 
        'keep recoRecoEcalCandidates_hfRecoEcalCandidate_*_*', 
        'keep *_hfEMClusters_*_*', 
        'keep *_gedGsfElectronCores_*_*', 
        'keep *_gedGsfElectrons_*_*', 
        'keep *_pixelTracks_*_*', 
        'keep *_pixelVertices_*_*', 
        'drop CaloTowersSorted_towerMakerPF_*_*', 
        'keep recoPFRecHits_particleFlowClusterECAL_Cleaned_*', 
        'keep recoPFRecHits_particleFlowClusterHCAL_Cleaned_*', 
        'keep recoPFRecHits_particleFlowClusterHO_Cleaned_*', 
        'keep recoPFRecHits_particleFlowClusterHF_Cleaned_*', 
        'keep recoPFRecHits_particleFlowClusterPS_Cleaned_*', 
        'keep recoPFRecHits_particleFlowRecHitECAL_Cleaned_*', 
        'keep recoPFRecHits_particleFlowRecHitHBHE_Cleaned_*', 
        'keep recoPFRecHits_particleFlowRecHitHF_Cleaned_*', 
        'keep recoPFRecHits_particleFlowRecHitHO_Cleaned_*', 
        'keep recoPFRecHits_particleFlowRecHitPS_Cleaned_*', 
        'keep recoPFClusters_particleFlowClusterECAL_*_*', 
        'keep recoPFClusters_particleFlowClusterHCAL_*_*', 
        'keep recoPFClusters_particleFlowClusterHO_*_*', 
        'keep recoPFClusters_particleFlowClusterHF_*_*', 
        'keep recoPFClusters_particleFlowClusterPS_*_*', 
        'keep recoPFBlocks_particleFlowBlock_*_*', 
        'keep recoPFCandidates_particleFlowEGamma_*_*', 
        'keep recoCaloClusters_particleFlowEGamma_*_*', 
        'keep recoSuperClusters_particleFlowEGamma_*_*', 
        'keep recoConversions_particleFlowEGamma_*_*', 
        'keep recoPFCandidates_particleFlow_*_*', 
        'keep recoPFCandidates_particleFlowTmp_electrons_*', 
        'keep recoPFCandidates_particleFlowTmp_*_*', 
        'drop recoPFCandidates_particleFlowTmp__*', 
        'keep recoPFDisplacedVertexs_particleFlowDisplacedVertex_*_*', 
        'keep *_pfElectronTranslator_*_*', 
        'keep *_pfPhotonTranslator_*_*', 
        'keep *_particleFlow_electrons_*', 
        'keep *_particleFlow_photons_*', 
        'keep *_particleFlow_muons_*', 
        'keep *_trackerDrivenElectronSeeds_preid_*', 
        'keep *_particleFlowPtrs_*_*', 
        'keep *_particleFlowTmpPtrs_*_*', 
        'keep *_offlineBeamSpot_*_*', 
        'keep L1GlobalTriggerReadoutRecord_gtDigis_*_*', 
        'keep *_l1GtRecord_*_*', 
        'keep *_l1GtTriggerMenuLite_*_*', 
        'keep *_conditionsInEdm_*_*', 
        'keep *_l1extraParticles_*_*', 
        'keep *_l1L1GtObjectMap_*_*', 
        'keep L1MuGMTReadoutCollection_gtDigis_*_*', 
        'keep L1GctEmCand*_gctDigis_*_*', 
        'keep L1GctJetCand*_gctDigis_*_*', 
        'keep L1GctEtHad*_gctDigis_*_*', 
        'keep L1GctEtMiss*_gctDigis_*_*', 
        'keep L1GctEtTotal*_gctDigis_*_*', 
        'keep L1GctHtMiss*_gctDigis_*_*', 
        'keep L1GctJetCounts*_gctDigis_*_*', 
        'keep L1GctHFRingEtSums*_gctDigis_*_*', 
        'keep L1GctHFBitCounts*_gctDigis_*_*', 
        'keep LumiDetails_lumiProducer_*_*', 
        'keep LumiSummary_lumiProducer_*_*', 
        'keep *_gtStage2Digis__*', 
        'keep *_gmtStage2Digis_Muon_*', 
        'keep *_caloStage2Digis_Jet_*', 
        'keep *_caloStage2Digis_Tau_*', 
        'keep *_caloStage2Digis_EGamma_*', 
        'keep *_caloStage2Digis_EtSum_*', 
        'drop *_hlt*_*_*', 
        'keep GlobalObjectMapRecord_hltGtStage2ObjectMap_*_*', 
        'keep edmTriggerResults_*_*_*', 
        'keep triggerTriggerEvent_*_*_*', 
        'keep L1AcceptBunchCrossings_scalersRawToDigi_*_*', 
        'keep L1TriggerScalerss_scalersRawToDigi_*_*', 
        'keep Level1TriggerScalerss_scalersRawToDigi_*_*', 
        'keep LumiScalerss_scalersRawToDigi_*_*', 
        'keep BeamSpotOnlines_scalersRawToDigi_*_*', 
        'keep DcsStatuss_scalersRawToDigi_*_*', 
        'keep DcsStatuss_hltScalersRawToDigi_*_*', 
        'keep *_tcdsDigis_*_*', 
        'keep *_logErrorHarvester_*_*', 
        'keep *_pfIsolatedElectronsEI_*_*', 
        'keep *_pfIsolatedMuonsEI_*_*', 
        'keep recoPFJets_pfJetsEI_*_*', 
        'keep *_pfCombinedInclusiveSecondaryVertexV2BJetTagsEI_*_*', 
        'keep recoPFTaus_pfTausEI_*_*', 
        'keep recoPFTauDiscriminator_pfTausDiscriminationByDecayModeFinding_*_*', 
        'keep recoPFTauDiscriminator_pfTausDiscriminationByIsolation_*_*', 
        'keep recoPFMETs_pfMetEI_*_*', 
        'keep TotemFEDInfos_totemRPRawToDigi_*_*', 
        'keep TotemTriggerCounters_totemTriggerRawToDigi_*_*', 
        'keep TotemRPDigiedmDetSetVector_totemRPRawToDigi_*_*', 
        'keep TotemVFATStatusedmDetSetVector_totemRPRawToDigi_*_*', 
        'keep TotemRPClusteredmDetSetVector_totemRPClusterProducer_*_*', 
        'keep TotemRPRecHitedmDetSetVector_totemRPRecHitProducer_*_*', 
        'keep TotemRPUVPatternedmDetSetVector_totemRPUVPatternFinder_*_*', 
        'keep TotemRPLocalTrackedmDetSetVector_totemRPLocalTrackFitter_*_*' ) ),
    secondaryFileNames = cms.untracked.vstring()
)

process.options = cms.untracked.PSet(
    allowUnscheduled = cms.untracked.bool(True)
)

# Production Info
process.configurationMetadata = cms.untracked.PSet(
    annotation = cms.untracked.string('RECO nevts:100'),
    name = cms.untracked.string('Applications'),
    version = cms.untracked.string('$Revision: 1.19 $')
)

# Output definition

process.MINIAODoutput = cms.OutputModule("PoolOutputModule",
    compressionAlgorithm = cms.untracked.string('LZMA'),
    compressionLevel = cms.untracked.int32(4),
    dataset = cms.untracked.PSet(
        dataTier = cms.untracked.string('MINIAOD'),
        filterName = cms.untracked.string('')
    ),
    dropMetaData = cms.untracked.string('ALL'),
    eventAutoFlushCompressedSize = cms.untracked.int32(15728640),
    fastCloning = cms.untracked.bool(False),
    fileName = cms.untracked.string('RECO_RECO_EI_PAT.root'),
    outputCommands = process.MINIAODEventContent.outputCommands,
    overrideInputFileSplitLevels = cms.untracked.bool(True)
)

# Additional output definition

# Other statements
from Configuration.AlCa.GlobalTag import GlobalTag
process.GlobalTag = GlobalTag(process.GlobalTag, '80X_dataRun2_Prompt_v15', '')

process.load('DisappTrks.CandidateTrackProducer.CandidateTrackProducer_cfi')
process.candidateTracks = cms.Path(process.candidateTrackProducer)
from DisappTrks.CandidateTrackProducer.customize import disappTrksOutputCommands
process.MINIAODoutput.outputCommands.extend(disappTrksOutputCommands)

# Path and EndPath definitions
process.reconstruction_step = cms.Path(process.reconstruction_fromRECO)
process.eventinterpretaion_step = cms.Path(process.EIsequence)
process.Flag_trackingFailureFilter = cms.Path(process.goodVertices+process.trackingFailureFilter)
process.Flag_goodVertices = cms.Path(process.primaryVertexFilter)
process.Flag_CSCTightHaloFilter = cms.Path(process.CSCTightHaloFilter)
process.Flag_trkPOGFilters = cms.Path(process.trkPOGFilters)
process.Flag_trkPOG_logErrorTooManyClusters = cms.Path(~process.logErrorTooManyClusters)
process.Flag_EcalDeadCellTriggerPrimitiveFilter = cms.Path(process.EcalDeadCellTriggerPrimitiveFilter)
process.Flag_ecalLaserCorrFilter = cms.Path(process.ecalLaserCorrFilter)
process.Flag_globalSuperTightHalo2016Filter = cms.Path(process.globalSuperTightHalo2016Filter)
process.Flag_eeBadScFilter = cms.Path(process.eeBadScFilter)
process.Flag_METFilters = cms.Path(process.metFilters)
process.Flag_chargedHadronTrackResolutionFilter = cms.Path(process.chargedHadronTrackResolutionFilter)
process.Flag_globalTightHalo2016Filter = cms.Path(process.globalTightHalo2016Filter)
process.Flag_CSCTightHaloTrkMuUnvetoFilter = cms.Path(process.CSCTightHaloTrkMuUnvetoFilter)
process.Flag_HBHENoiseIsoFilter = cms.Path(process.HBHENoiseFilterResultProducer+process.HBHENoiseIsoFilter)
process.Flag_hcalLaserEventFilter = cms.Path(process.hcalLaserEventFilter)
process.Flag_HBHENoiseFilter = cms.Path(process.HBHENoiseFilterResultProducer+process.HBHENoiseFilter)
process.Flag_trkPOG_toomanystripclus53X = cms.Path(~process.toomanystripclus53X)
process.Flag_EcalDeadCellBoundaryEnergyFilter = cms.Path(process.EcalDeadCellBoundaryEnergyFilter)
process.Flag_trkPOG_manystripclus53X = cms.Path(~process.manystripclus53X)
process.Flag_HcalStripHaloFilter = cms.Path(process.HcalStripHaloFilter)
process.Flag_muonBadTrackFilter = cms.Path(process.muonBadTrackFilter)
process.Flag_CSCTightHalo2015Filter = cms.Path(process.CSCTightHalo2015Filter)
process.endjob_step = cms.EndPath(process.endOfProcess)
process.MINIAODoutput_step = cms.EndPath(process.MINIAODoutput)

# Schedule definition
process.schedule = cms.Schedule(process.reconstruction_step,process.eventinterpretaion_step,process.Flag_HBHENoiseFilter,process.Flag_HBHENoiseIsoFilter,process.Flag_CSCTightHaloFilter,process.Flag_CSCTightHaloTrkMuUnvetoFilter,process.Flag_CSCTightHalo2015Filter,process.Flag_globalTightHalo2016Filter,process.Flag_globalSuperTightHalo2016Filter,process.Flag_HcalStripHaloFilter,process.Flag_hcalLaserEventFilter,process.Flag_EcalDeadCellTriggerPrimitiveFilter,process.Flag_EcalDeadCellBoundaryEnergyFilter,process.Flag_goodVertices,process.Flag_eeBadScFilter,process.Flag_ecalLaserCorrFilter,process.Flag_trkPOGFilters,process.Flag_chargedHadronTrackResolutionFilter,process.Flag_muonBadTrackFilter,process.Flag_trkPOG_manystripclus53X,process.Flag_trkPOG_toomanystripclus53X,process.Flag_trkPOG_logErrorTooManyClusters,process.Flag_METFilters,process.candidateTracks,process.endjob_step,process.MINIAODoutput_step)

#Setup FWK for multithreaded
process.options.numberOfThreads=cms.untracked.uint32(4)
process.options.numberOfStreams=cms.untracked.uint32(0)

# customisation of the process.

# Automatic addition of the customisation function from DisappTrks.BackgroundEstimation.customize
from DisappTrks.BackgroundEstimation.customize import addMoreCaloTowers,addMoreElectronSeeds 

#call to customisation function addMoreCaloTowers imported from DisappTrks.BackgroundEstimation.customize
process = addMoreCaloTowers(process)

#call to customisation function addMoreElectronSeeds imported from DisappTrks.BackgroundEstimation.customize
process = addMoreElectronSeeds(process)

# Automatic addition of the customisation function from Configuration.DataProcessing.RecoTLR
from Configuration.DataProcessing.RecoTLR import customisePostEra_Run2_2016 

#call to customisation function customisePostEra_Run2_2016 imported from Configuration.DataProcessing.RecoTLR
process = customisePostEra_Run2_2016(process)

# End of customisation functions
#do not add changes to your config after this point (unless you know what you are doing)
from FWCore.ParameterSet.Utilities import convertToUnscheduled
process=convertToUnscheduled(process)
process.load('Configuration.StandardSequences.PAT_cff')
from FWCore.ParameterSet.Utilities import cleanUnscheduled
process=cleanUnscheduled(process)

# customisation of the process.

# Automatic addition of the customisation function from PhysicsTools.PatAlgos.slimming.miniAOD_tools
from PhysicsTools.PatAlgos.slimming.miniAOD_tools import miniAOD_customizeAllData 

#call to customisation function miniAOD_customizeAllData imported from PhysicsTools.PatAlgos.slimming.miniAOD_tools
process = miniAOD_customizeAllData(process)

# End of customisation functions
