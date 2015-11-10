import FWCore.ParameterSet.Config as cms
import copy
from DisappTrks.StandardAnalysis.Cuts import * # Put all the individual cuts in this file 
from DisappTrks.StandardAnalysis.EventSelections import *  # Get the composite cut definitions  


# FIXME:  These channels do not yet work - need to be updated for Run 2.  

##################################################
## Electron tag and probe sample 
##################################################
ZtoElecDisTrk = cms.PSet(
    name = cms.string("ZtoElecDisTrk"),
    triggers = triggersSingleElec,
    cuts = cms.VPSet (), 
)

tagElecCuts = [
    cutElecPt20,
    cutElecEta21,
    cutElecTightID,  # FIXME:  Must fix this selection
    #  cutElecPFIso,  # Ask Bing what he uses for this 
]
elecTrkCuts = [
    cutElecTrkDeltaR,
    cutElecTrkInvMass80To100,
]
addCuts(ZtoElecDisTrk.cuts, tagElecCuts) 
addCuts(ZtoElecDisTrk.cuts, disTrkCuts) 
addCuts(ZtoElecDisTrk.cuts, tauTrkCuts) 

ZtoElecProbeTrk = copy.deepcopy(ZtoElecDisTrk)
ZtoElecProbeTrk.name = cms.string("ZtoElecProbeTrk")  
cutsToRemove = [
    cutTrkElecVeto,
    cutTrkEcalo, 
]
removeCuts(ZtoElecProbeTrk.cuts, cutsToRemove)  



