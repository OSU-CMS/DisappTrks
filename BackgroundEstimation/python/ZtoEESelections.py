import FWCore.ParameterSet.Config as cms
import copy
from DisappTrks.StandardAnalysis.Cuts import * # Put all the individual cuts in this file
from DisappTrks.StandardAnalysis.EventSelections import *  # Get the composite cut definitions

##################################################
## Fake track control sample:  start with Z->mu mu events
##################################################
ZtoEE = cms.PSet(
    name = cms.string("ZtoEE"),
    triggers = triggersSingleEle,
    metFilters = metFilters,
    cuts = cms.VPSet (
        cutMetFilters,
        cutElectronPairPt, # this will be >22 for 76X and >26 for 80X
        cutElectronPairEta21,
        cutElectronPairTightID,
        cutElectronPairTightPFIso,
        cutEEChargeProduct,
        cutEEInvMassZLo,
        cutEEInvMassZHi,
    )
)
##################################################

# create copies of all above selections with the fiducial electron/muon cuts removed
for selection in list (locals ()):
    if not hasattr (locals ()[selection], "name") or not hasattr (locals ()[selection], "triggers") or not hasattr (locals ()[selection], "cuts"):
        continue
    locals ()[selection + "NoElectronMuonFiducialCuts"] = copy.deepcopy (locals ()[selection])
    locals ()[selection + "NoElectronMuonFiducialCuts"].name = cms.string (locals ()[selection].name.value () + "NoElectronMuonFiducialCuts")
    removeCuts (locals ()[selection + "NoElectronMuonFiducialCuts"].cuts, [cutTrkFiducialElectron, cutTrkFiducialMuon])
