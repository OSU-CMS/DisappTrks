# Simply copy the contents of the input file to an output file.
# To use for transferring a dataset with crab.  
#
# Start from:
# https://raw.githubusercontent.com/cms-sw/cmssw/CMSSW_7_4_X/PhysicsTools/Utilities/configuration/copyPickMerge_cfg.py


import FWCore.ParameterSet.Config as cms

process = cms.Process("CopyEvent")
process.source = cms.Source ("PoolSource",
                             fileNames = cms.untracked.vstring ("file:miniAOD.root"),   
)

process.Out = cms.OutputModule("PoolOutputModule",
                               fileName = cms.untracked.string ("copy.root")  
)

process.end = cms.EndPath(process.Out)

