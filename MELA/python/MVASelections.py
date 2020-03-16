import FWCore.ParameterSet.Config as cms
import copy
from DisappTrks.StandardAnalysis.Cuts import * # Put all the individual cuts in this file
from DisappTrks.StandardAnalysis.EventSelections import basicSelection
from DisappTrks.BackgroundEstimation.ElectronTagProbeSelections import ElectronTagSkim
from DisappTrks.BackgroundEstimation.MuonTagProbeSelections import MuonTagSkim

def createHitsVariations (ch, chName):
    globals ().update (createChannelVariations (ch, chName, None, cutTrkNLayersVariations))
    globals ().update (createChannelVariations (ch, chName, cutTrkNValidHitsSignal, cutTrkNValidHitsVariations))
    if os.environ["CMSSW_VERSION"].startswith ("CMSSW_9_4_") or os.environ["CMSSW_VERSION"].startswith ("CMSSW_10_2_"):
        replaceSingleCut (globals ()[chName + 'NHits3'].cuts, cutTrkNValidPixelHits[3], cutTrkNValidPixelHitsSignal)
        replaceSingleCut (globals ()[chName + 'NLayers3'].cuts, cutTrkNValidPixelHits[3], cutTrkNValidPixelHitsSignal)

###########################################################

mvaPreselectionCuts = [
    cutTrkPt55,
    cutTrkEta,
    cutTrkEcalGapVeto,
    cutTrkEtaMuonIneff1,
    cutTrkEtaMuonIneff2,
    cutTrkTOBCrack,
    cutTrkNValidPixelHitsSignal,
    cutTrkNValidHitsSignal,
]

if os.environ["CMSSW_VERSION"].startswith ("CMSSW_9_4_"):
    mvaPreselectionCuts.append(cutTrk2017LowEfficiencyRegion)
if os.environ["CMSSW_VERSION"].startswith ("CMSSW_10_2_"):
    # IMPORTANT FIXME: looks like this region started dying later in 2018 B
    # probably this is only relevant for C+D, but we've only checked C for now
    mvaPreselectionCuts.append(cutTrk2018LowEfficiencyRegion)

###########################################################
# MET preselection: basicSelection + track, no fiducial map
###########################################################

mvaMETPreselection = copy.deepcopy(basicSelection)
mvaMETPreselection.name = cms.string("mvaMETPreselection")
addCuts(mvaMETPreselection.cuts, mvaPreselectionCuts)

mvaMETPreselectionSmearedJets = copy.deepcopy(mvaMETPreselection)
replaceSingleCut(mvaMETPreselectionSmearedJets.cuts, cutJetJERSmearedPt, cutJetPt)

createHitsVariations(mvaMETPreselection, "mvaMETPreselection")
createHitsVariations(mvaMETPreselectionSmearedJets, "mvaMETPreselectionSmearedJets")

###########################################################
# electron preselection: ZtoEleProbeTrk, no fiducial map
###########################################################

mvaElePreselection = copy.deepcopy(ElectronTagSkim)
mvaElePreselection.name = cms.string("mvaElePreselection")
addSingleCut(mvaElePreselection.cuts, cutElectronMatchToTrigObj, cutElectronPt)

cutsToAdd = [
    cutElectronArbitration,
    cutTrkPt30,
]
cutsToAdd += mvaPreselectionCuts
cutsToAdd += [
    cutEleTrkInvMass10,
    cutTrkMuonVeto,
    cutTrkTauHadVeto,
    cutTrkArbitration,
    cutEleTrkInvMass80To100,
    cutEleTrkOS,
]

addCuts(mvaElePreselection.cuts, cutsToAdd)

createHitsVariations(mvaElePreselection, "mvaElePreselection")

###########################################################
# muon preselection: ZtoEleProbeTrk, no fiducial map, no ecalo cut
###########################################################

mvaMuonPreselection = copy.deepcopy(MuonTagSkim)
mvaMuonPreselection.name = cms.string("mvaMuonPreselection")
addSingleCut(mvaMuonPreselection.cuts, cutElectronMatchToTrigObj, cutMuonPt)

cutsToAdd = [
    cutMuonArbitration,
    cutTrkPt30,
]
cutsToAdd += mvaPreselectionCuts
cutsToAdd += [
    cutMuTrkInvMass10,
    cutTrkElecVeto,
    cutTrkTauHadVeto,
    cutTrkArbitration,
    cutMuTrkInvMass80To100,
    cutMuTrkOS,
]

addCuts(mvaMuonPreselection.cuts, cutsToAdd)

createHitsVariations(mvaMuonPreselection, "mvaMuonPreselection")
