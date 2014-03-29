import sys
import FWCore.ParameterSet.Config as cms

# Run with:
#  /afs/cern.ch/work/w/wulsin/public/disappTrk/signalMCGenV2/testSimVertex/CMSSW_6_1_2/src/Demo/DemoAnalyzer > cmsRun decayAnalyzer_cfg.py 2>&1 | tee decayAnalyzer_cfg.log 


process = cms.Process("Demo")

process.load("FWCore.MessageService.MessageLogger_cfi")

process.maxEvents = cms.untracked.PSet( input = cms.untracked.int32(10) )
process.MessageLogger.cerr.FwkReport.reportEvery = 1

process.source = cms.Source("PoolSource",
    # replace 'myfile.root' with the source file you want to use
    fileNames = cms.untracked.vstring(
#        'file:/afs/cern.ch/work/w/wulsin/public/disappTrk/signalMCGenV2/CMSSW_5_3_11/src/DisappTrks/SignalMC/chargino_amsb_GEN-bkup.root'
#'file:condor_2014_03_11_FullSelectionStopCtauZero_AMSB_mGrav100K_5ns_pickevents_merged.root'
#    'file:/afs/cern.ch/work/w/wulsin/public/disappTrk/signalMCGenV2/CMSSW_5_3_11/src/DisappTrks/SignalMC/chargino_amsb_GEN_SIM-testLongLife1.root' 
# 'file:/afs/cern.ch/work/w/wulsin/public/disappTrk/signalMCGenV2/CMSSW_5_3_11/src/DisappTrks/SignalMC/chargino_amsb_GEN_SIM.root'
    ##    'file:../chargino_amsb_RECO.root'  
#    'file:/home/wulsin/disappTrks/signalMCGenV2/CMSSW_5_3_11/src/DisappTrks/SignalMC/condor/signalGenV1/amsbChargino_mGrav50K_5ns/chargino_amsb_RECO_0.root', 
##     'file:../condor/signalGenV1/amsbChargino_mGrav50K_5ns/chargino_amsb_RECO_1.root', 
##     'file:../condor/signalGenV1/amsbChargino_mGrav50K_5ns/chargino_amsb_RECO_2.root', 
##     'file:../condor/signalGenV1/amsbChargino_mGrav50K_5ns/chargino_amsb_RECO_3.root', 
##     'file:../condor/signalGenV1/amsbChargino_mGrav50K_5ns/chargino_amsb_RECO_4.root',
#    'file:/home/wulsin/disappTrks/BeanStopTesting/AMSB_chargino_GEN_numEvent20.root', 
    'file:/home/wulsin/disappTrks/BeanStopTesting/AMSB_chargino_GEN.root', 
    )
                          )

process.source.duplicateCheckMode = cms.untracked.string('noDuplicateCheck') 

process.demo = cms.EDAnalyzer('DecayAnalyzer',
                              genParticleTag = cms.InputTag("genParticles"),
)


process.TFileService = cms.Service("TFileService",
                                   fileName = cms.string('histoDecay.root')
)

process.p = cms.Path(process.demo)


## ## Test GEN-only file:  
## process.source.fileNames = cms.untracked.vstring('file:/home/wulsin/disappTrks/BeanStopTesting/AMSB_chargino_GEN.root')
## process.TFileService.fileName = cms.string('histoDecayFromGENOnly.root')

# ## Test Geant simulation:  
# process.genParticlePlusGEANT = cms.EDProducer("GenPlusSimParticleProducer",
#                                                  src           = cms.InputTag("g4SimHits"),   # use "famosSimHits" for FAMOS
#                                                  setStatus     = cms.int32(8),                # set status = 8 for GEANT GPs
#                                                  filter        = cms.vstring("pt > 0.0"),     # just for testing (optional)
#                                                  genParticles  = cms.InputTag("genParticles") # original genParticle list
#                                                  )
# process.demo.genParticleTag = cms.InputTag("genParticlePlusGEANT")  
# import os
# process.source.fileNames = cms.untracked.vstring()  
# #process.source.fileNames = cms.untracked.vstring('file:/home/wulsin/disappTrks/signalMCGenV2/CMSSW_5_3_11/src/DisappTrks/SignalMC/condor/signalGenV1/amsbChargino_mGrav50K_5ns/chargino_amsb_RECO_0.root')  
# dir = '/home/wulsin/disappTrks/signalMCGenV2/CMSSW_5_3_11/src/DisappTrks/SignalMC/condor/signalGenV1/amsbChargino_mGrav50K_5ns/'  
# for file in os.listdir(dir):
#     if file.find(".root") != -1 and file.find("RECO") != -1: # Skip over files that do not contain .root.
#         process.source.fileNames.extend(cms.untracked.vstring('file:' + dir + file))
# process.TFileService.fileName = cms.string('histoDecayWithGeant.root')
# process.p = cms.Path(process.genParticlePlusGEANT + process.demo)

## process.source.fileNames = cms.untracked.vstring('file:chargino_amsb_RECO_0_CharginoNoDecay.root')  
## process.TFileService.fileName = cms.string('histoDecayWithGeant_CharginoNoDecay.root')

## process.source.fileNames = cms.untracked.vstring('file:charginoPartGun_GEN_SIM_5nsWithDecayFlagsOn.root') 
## process.TFileService.fileName = cms.string('histoDecayWithGeant_CharginoPartGun.root')

process.source.fileNames = cms.untracked.vstring('file:AMSB_chargino_test_GEN.root')  
process.TFileService.fileName = cms.string('histoDecayTest.root')





