import sys
import os
import FWCore.ParameterSet.Config as cms

# Run with:
#  /afs/cern.ch/work/w/wulsin/public/disappTrk/signalMCGenV2/testSimVertex/CMSSW_6_1_2/src/Demo/DemoAnalyzer > cmsRun vertexAnalyzer_cfg.py 2>&1 | tee vertexAnalyzer_cfg.log


process = cms.Process("Demo")

process.load("FWCore.MessageService.MessageLogger_cfi")

process.maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
process.MessageLogger.cerr.FwkReport.reportEvery = 1

process.source = cms.Source("PoolSource",
    # replace 'myfile.root' with the source file you want to use
    fileNames = cms.untracked.vstring(
#        'file:/afs/cern.ch/work/w/wulsin/public/disappTrk/signalMCGenV2/CMSSW_5_3_11/src/DisappTrks/SignalMC/chargino_amsb_GEN-bkup.root'
#'file:condor_2014_03_11_FullSelectionStopCtauZero_AMSB_mGrav100K_5ns_pickevents_merged.root'
#    'file:/afs/cern.ch/work/w/wulsin/public/disappTrk/signalMCGenV2/CMSSW_5_3_11/src/DisappTrks/SignalMC/chargino_amsb_GEN_SIM-testLongLife1.root'
    'file:/afs/cern.ch/work/w/wulsin/public/disappTrk/signalMCGenV2/CMSSW_5_3_11/src/DisappTrks/SignalMC/chargino_amsb_GEN_SIM.root'
        )
)

process.source.duplicateCheckMode = cms.untracked.string('noDuplicateCheck')

process.demo = cms.EDAnalyzer('VertexAnalyzer'
)


process.TFileService = cms.Service("TFileService",
                                   fileName = cms.string('histo.root')
)


# CtauZero:
## process.TFileService.fileName = cms.string('histo_CtauZero.root')
## process.source.fileNames = cms.untracked.vstring('file:condor_2014_03_11_FullSelectionStopCtauZero_AMSB_mGrav100K_5ns_pickevents_merged.root')

## # CtauNonZero:
## process.TFileService.fileName = cms.string('histo_CtauNonZero.root')
## process.source.fileNames = cms.untracked.vstring('file:condor_2014_03_11_FullSelectionStopCtauNonZero_AMSB_mGrav100K_5ns_pickevents_merged.root')


## Test long lifetime:
## process.TFileService.fileName = cms.string('histo_testLongLife1.root')
## process.source.fileNames = cms.untracked.vstring('file:/afs/cern.ch/work/w/wulsin/public/disappTrk/signalMCGenV2/CMSSW_5_3_11/src/DisappTrks/SignalMC/chargino_amsb_GEN_SIM-testLongLife1.root')

## Test 5ns:
## process.TFileService.fileName = cms.string('histo_test5ns.root')
## process.source.fileNames = cms.untracked.vstring('file:/afs/cern.ch/work/w/wulsin/public/disappTrk/signalMCGenV2/CMSSW_5_3_11/src/DisappTrks/SignalMC/chargino_amsb_GEN_SIM-5ns.root')


## Test 50ns:
## process.TFileService.fileName = cms.string('histo_test50ns.root')
## process.source.fileNames = cms.untracked.vstring('file:/afs/cern.ch/work/w/wulsin/public/disappTrk/signalMCGenV2/CMSSW_5_3_11/src/DisappTrks/SignalMC/chargino_amsb_GEN_SIM-50ns.root')

## ## Test 5ns-noDecays:
## process.TFileService.fileName = cms.string('histo_test5nsNoDecays.root')
## process.source.fileNames = cms.untracked.vstring('file:/afs/cern.ch/work/w/wulsin/public/disappTrk/signalMCGenV2/CMSSW_5_3_11/src/DisappTrks/SignalMC/charginoPartGun_GEN_SIM.root')

## Test 5ns-WithDecays:
## process.TFileService.fileName = cms.string('histo_test5nsWithDecays.root')
## process.source.fileNames = cms.untracked.vstring('file:/afs/cern.ch/work/w/wulsin/public/disappTrk/signalMCGenV2/CMSSW_5_3_11/src/DisappTrks/SignalMC/charginoPartGun_5nsWithDecays.root')


## Test 5ns-WithDecays:
## process.source.fileNames = cms.untracked.vstring('file:/afs/cern.ch/work/w/wulsin/public/disappTrk/signalMCGenV2/CMSSW_5_3_11/src/DisappTrks/SignalMC/charginoPartGun_GEN_SIM_5nsDefault.root')
## process.TFileService.fileName = cms.string('charginoPartGun_5nsDefault.root')

## Test new Beans:
process.source.fileNames = cms.untracked.vstring()
dir = 'condor/AMSB_chargino_200GeV_ctau1000cm/'
for file in os.listdir(dir):
    if file.find(".root") != -1 and file.find("RECO") != -1: # Skip over files that do not contain .root.
        process.source.fileNames.extend(cms.untracked.vstring('file:' + dir + file))
process.TFileService.fileName = cms.string('histoVertexDecayRECO.root')


process.p = cms.Path(process.demo)

