import FWCore.ParameterSet.Config as cms

#######################################################
##### Set up the branches to be added to the tree #####
#######################################################

EventVariableBranches = cms.PSet(
    inputCollection = cms.vstring("eventvariables"),
    branches = cms.VPSet (
        cms.PSet (
            name = cms.string("isrPt"),
            inputVariables = cms.vstring("isrPt"),
        ),
        cms.PSet (
            name = cms.string("lifetimeWeight"),
            inputVariables = cms.vstring("lifetimeWeight"),
        ),
        cms.PSet (
            name = cms.string("ctau0"),
            inputVariables = cms.vstring("cTau_1000024_0"),
        ),
        cms.PSet (
            name = cms.string("ctau1"),
            inputVariables = cms.vstring("cTau_1000024_1"),
        ),
        cms.PSet (
            name = cms.string("isrWeight"),
            inputVariables = cms.vstring("isrWeight"),
        ),
        cms.PSet (
            name = cms.string("isrWeightUp"),
            inputVariables = cms.vstring("isrWeightUp"),
        ),
        cms.PSet (
            name = cms.string("isrWeightDown"),
            inputVariables = cms.vstring("isrWeightDown"),
        ),
        cms.PSet (
            name = cms.string("puWeight"),
            inputVariables = cms.vstring("puScalingFactor"),
        ),
        cms.PSet (
            name = cms.string("puWeightUp"),
            inputVariables = cms.vstring("puScalingFactorUp"),
        ),
        cms.PSet (
            name = cms.string("puWeightDown"),
            inputVariables = cms.vstring("puScalingFactorDown"),
        ),
        cms.PSet (
            name = cms.string("missingOuterHitsWeight"),
            inputVariables = cms.vstring("trackScalingFactor"),
        ),
        cms.PSet (
            name = cms.string("metLegTriggerWeight"),
            inputVariables = cms.vstring("metLegWeight"),
        ),
        cms.PSet (
            name = cms.string("trackLegTriggerWeight"),
            inputVariables = cms.vstring("trackLegWeight"),
        ),
        cms.PSet (
            name = cms.string("grandOrTriggerWeight"),
            inputVariables = cms.vstring("grandOrWeight"),
        ),
        cms.PSet (
            name = cms.string("grandOrTriggerWeightMCUp"),
            inputVariables = cms.vstring("grandOrWeightMCUp"),
        ),
        cms.PSet (
            name = cms.string("grandOrTriggerWeightMCDown"),
            inputVariables = cms.vstring("grandOrWeightMCDown"),
        ),
        cms.PSet (
            name = cms.string("grandOrTriggerWeightDataUp"),
            inputVariables = cms.vstring("grandOrWeightDataUp"),
        ),
        cms.PSet (
            name = cms.string("grandOrTriggerWeightDataDown"),
            inputVariables = cms.vstring("grandOrWeightDataDown"),
        ),
    )
)

for srcCTau in [1, 10, 100, 1000, 10000]:
    for i in range(2, 10):
        dst = float(0.1 * i * srcCTau)
        dstCTau = str(int(dst)) if dst > 1 else '0p' + str(int(10 * dst))
        EventVariableBranches.branches.append(
            cms.PSet(
                name = cms.string("lifetimeWeight_1000024_" + str(srcCTau) + "cmTo" + dstCTau + "cm"),
                inputVariables = cms.vstring("lifetimeWeight_1000024_" + str(srcCTau) + "cmTo" + dstCTau + "cm"),
            )
        )

MetShiftBranches = cms.PSet(
    inputCollection = cms.vstring("mets"),
    histograms = cms.VPSet (
        cms.PSet(
            name = cms.string("metNoMu"),
            inputVariables = cms.vstring("noMuPt"),
        ),
        # shift up +1sigma
        cms.PSet(
            name = cms.string("metNoMu_JetResUp"),
            inputVariables = cms.vstring("noMuPt_JetResUp"),
        ),
        cms.PSet(
            name = cms.string("metNoMu_JetEnUp"),
            inputVariables = cms.vstring("noMuPt_JetEnUp"),
        ),
        cms.PSet(
            name = cms.string("metNoMu_ElectronEnUp"),
            inputVariables = cms.vstring("noMuPt_ElectronEnUp"),
        ),
        cms.PSet(
            name = cms.string("metNoMu_TauEnUp"),
            inputVariables = cms.vstring("noMuPt_TauEnUp"),
        ),
        cms.PSet(
            name = cms.string("metNoMu_UnclusteredEnUp"),
            inputVariables = cms.vstring("noMuPt_UnclusteredEnUp"),
        ),
        cms.PSet(
            name = cms.string("metNoMu_PhotonEnUp"),
            inputVariables = cms.vstring("noMuPt_PhotonEnUp"),
        ),
        # shift down -1sigma
        cms.PSet(
            name = cms.string("metNoMu_JetResDown"),
            inputVariables = cms.vstring("noMuPt_JetResDown"),
        ),
        cms.PSet(
            name = cms.string("metNoMu_JetEnDown"),
            inputVariables = cms.vstring("noMuPt_JetEnDown"),
        ),
        cms.PSet(
            name = cms.string("metNoMu_ElectronEnDown"),
            inputVariables = cms.vstring("noMuPt_ElectronEnDown"),
        ),
        cms.PSet(
            name = cms.string("metNoMu_TauEnDown"),
            inputVariables = cms.vstring("noMuPt_TauEnDown"),
        ),
        cms.PSet(
            name = cms.string("metNoMu_UnclusteredEnDown"),
            inputVariables = cms.vstring("noMuPt_UnclusteredEnDown"),
        ),
        cms.PSet(
            name = cms.string("metNoMu_PhotonEnDown"),
            inputVariables = cms.vstring("noMuPt_PhotonEnDown"),
        ),
    )
)
