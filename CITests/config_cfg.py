import FWCore.ParameterSet.Config as cms
import OSUT3Analysis.DBTools.osusub_cfg as osusub
osusub.randomNumberSuffix = 1710338174
import re
import os
import userConfig_EGamma_2022F_cfg as pset
import FWCore.PythonUtilities.LumiList as LumiList
myLumis = LumiList.LumiList(filename = 'Cert_Collisions2022_355100_362760_Golden.json').getCMSSWString().split(',')

fileName = 'hist_' + str (osusub.jobNumber) + '.root'
pset.process.TFileService.fileName = fileName
pset.process.VertexCutOnlyPlotter.weights = cms.VPSet()
pset.process.PUScalingFactorProducer.dataset = cms.string("MuonEG_2015D")

pset.process.source.fileNames = cms.untracked.vstring (osusub.runList)
pset.process.source.secondaryFileNames = cms.untracked.vstring (osusub.secondaryRunList)
pset.process.source.lumisToProcess = cms.untracked.VLuminosityBlockRange()
pset.process.source.lumisToProcess.extend(myLumis)
pset.process.source.skipBadFiles = cms.untracked.bool (True)
pset.process.maxEvents.input = cms.untracked.int32 (1000)

siblings = []
if osusub.batchMode:
  try:
    if os.path.exists('default.json'):
      siblings.extend(osusub.getSiblingList("default.json",  osusub.runList, "/EGamma/Run2022F-EXODisappTrk-PromptReco-v1/AOD"))
    else:
      for fileName in osusub.runList:
        siblings.extend (osusub.getRun3SkimSiblings (fileName, "/EGamma/Run2022F-EXODisappTrk-PromptReco-v1/AOD"))
  except:
    print( "No valid grid proxy. Not adding sibling files.")
pset.process.source.secondaryFileNames.extend(siblings)


if hasattr(osusub, "eventMask"):
  try:
    eventRange = cms.untracked.VEventRange(osusub.eventMask)
    pset.process.source.eventsToProcess = eventRange
  except Exception as e:
    print("Error", e)
process = pset.process
