import FWCore.ParameterSet.Config as cms

###########################################################
##### Set up process #####
###########################################################

process = cms.Process ('OSUAnalysis')
process.load ('FWCore.MessageService.MessageLogger_cfi')
process.MessageLogger.cerr.FwkReport.reportEvery = 1
process.source = cms.Source ('PoolSource',
    fileNames = cms.untracked.vstring (
#        'file:charginoPartGun_GEN_SIM_5nsWithDecayFlagsOn.root', 
#        'file:AMSB_chargino_test_GEN.root', 
#    'root://xrootd.ba.infn.it//store/user/wulsin/AMSB_chargino_100GeV_ctau1000cm_FilterSumPt50_8TeV_pythia6_V1/AMSB_chargino_100GeV_ctau1000cm_FilterSumPt50_8TeV_pythia6_V1/d66ce63f45b0919f1bcc6fe69cbbc5b1/AMSB_chargino_RECO_9_1_ELT.root', 
#    'root://xrootd.ba.infn.it//store/user/wulsin/AMSB_chargino_100GeV_ctau10cm_FilterSumPt50_8TeV_pythia6_V1/AMSB_chargino_100GeV_ctau10cm_FilterSumPt50_8TeV_pythia6_V1/a5bf8a415c75e7e03ed81894f138fdd4/AMSB_chargino_RECO_100_1_eB0.root',  
#          'file:../HSCP_testPythia8_GEN.root',
#          'file:HSCPstopToBottom_M_1000_1000mm_Tune4C_8TeV_pythia8_cff_GEN_SIM.root', 
        'file:charginoPartGun_GEN_SIM.root', 
    )
)

process.maxEvents = cms.untracked.PSet (
    input = cms.untracked.int32 (-1)
)

###########################################################
##### Set up the analyzer #####
###########################################################

process.load("SimGeneral.HepPDTESSource.pythiapdt_cfi")
process.particleListDrawer = cms.EDAnalyzer ('ParticleListDrawer',
    maxEventsToPrint = cms.untracked.int32(-1),
    printVertex = cms.untracked.bool(True),
#    src = cms.InputTag("genParticles")
    src = cms.InputTag("genParticlePlusGeant")
)

process.myPath = cms.Path (process.particleListDrawer)
