import FWCore.ParameterSet.Config as cms

from OSUT3Analysis.Configuration.cutUtilities import *

#######################################################
##### Set up the branches to be added to the tree #####
#######################################################

###########################
##### Event variables #####
###########################

EventVariableBranches_names = [
    "isrPt",
    "lifetimeWeight",
    "cTau_1000024_0",
    "cTau_1000024_1",
    "decayLength_1000024_0",
    "decayLength_1000024_1",
    "beta_1000024_0",
    "beta_1000024_1",
    "gamma_1000024_0",
    "gamma_1000024_1",
    "isrWeight",
    "isrWeightUp",
    "isrWeightDown",
    "puScalingFactor",
    "puScalingFactorUp",
    "puScalingFactorDown",
    "trackScalingFactor",
    "metLegWeight",
    "trackLegWeight",
    "grandOrWeight",
    "grandOrWeightMCUp",
    "grandOrWeightMCDown",
    "grandOrWeightDataUp",
    "grandOrWeightDataDown",
    "L1ECALPrefiringWeight",
    "L1ECALPrefiringWeightUp",
    "L1ECALPrefiringWeightDown",
    "hasPrefiredJets",
    "numPVReco",
    "nJets",
    "nTracks",
    "nTracksInsideJets",
    "nTracksOutsideJets",
    "trackRho",

    "nGoodTPPairs",
    "nProbesPassingVeto",
    "nProbesPassingLooseVeto",
    "nProbesFiringTrigger",
    "nProbesMatchingTag",
    "nProbesFiringTriggerMatchingTag",

    "nGoodSSTPPairs",
    "nSSProbesPassingVeto",
    "nSSProbesPassingLooseVeto",
    "nSSProbesFiringTrigger",
    "nSSProbesMatchingTag",
    "nSSProbesFiringTriggerMatchingTag",

    "nGoodTagJetPairs",
    "nGoodTagPFCHPairs",

    "jetInHEM1516",
    "jetOppositeHEM1516",
    "metJetHEM1516",
    "hem1516weight",
    "hem1516weightUp",
    "hem1516weightDown",

    "genCharginoMass",
    "genNeutralinoMass",
    "genGluinoMass",
]

# hitCharge_<track number>_<hit number>
for itrk in range(3):
    for ihit in range(20):
        EventVariableBranches_names.append('hitCharge_' + str(itrk) + '_' + str(ihit))
        EventVariableBranches_names.append('hitIsPixel_' + str(itrk) + '_' + str(ihit))
        EventVariableBranches_names.append('pixelSize_' + str(itrk) + '_' + str(ihit))
        EventVariableBranches_names.append('pixelSizeX_' + str(itrk) + '_' + str(ihit))
        EventVariableBranches_names.append('pixelSizeY_' + str(itrk) + '_' + str(ihit))

EventVariableBranches = cms.PSet(
    inputCollection = cms.vstring("eventvariables"),
    branches = cms.VPSet ([cms.PSet(name = cms.string(x), inputVariables = cms.vstring(x)) for x in EventVariableBranches_names]),
)

for srcCTau in [1, 10, 100, 1000, 10000]:
    destinationCTaus = [float(0.1 * i * srcCTau) for i in range(2, 11)]
    if srcCTau == 10:
        destinationCTaus.extend([float(0.01 * i * srcCTau) for i in range(1, 11)])
    for dst in destinationCTaus:
        dstCTau = str(int(dst)) if dst >= 1 else '0p' + str(int(10 * dst))
        thisName = "lifetimeWeight_1000024_" + str(srcCTau) + "cmTo" + dstCTau + "cm"
        EventVariableBranches.branches.append(
            cms.PSet(
                name = cms.string(thisName),
                inputVariables = cms.vstring(thisName),
            )
        )

###########################
#####       MET       #####
###########################

MetShiftBranches_names = [
    "noMuPt",
    "noMuPt_JetResUp",
    "noMuPt_JetEnUp",
    "noMuPt_ElectronEnUp",
    "noMuPt_TauEnUp",
    "noMuPt_UnclusteredEnUp",
    "noMuPt_PhotonEnUp",
    "noMuPt_JetResDown",
    "noMuPt_JetEnDown",
    "noMuPt_ElectronEnDown",
    "noMuPt_TauEnDown",
    "noMuPt_UnclusteredEnDown",
    "noMuPt_PhotonEnDown",

    "pt",
    "phi",
    "noMuPhi",
]
MetShiftBranches = cms.PSet(
    inputCollection = cms.vstring("mets"),
    branches = cms.VPSet ([cms.PSet(name = cms.string(x), inputVariables = cms.vstring(x)) for x in MetShiftBranches_names]),
)

###########################
#####     Tracks      #####
###########################

TrackDebugBranches_names = [
    "packedPixelBarrelHitPattern",
    "packedPixelEndcapHitPattern",
    
    "firstLayerWithValidHit",
    "lastLayerWithValidHit",
    
    "hasValidHitInPixelBarrelLayer1",
    "hasValidHitInPixelBarrelLayer2",
    "hasValidHitInPixelBarrelLayer3",
    "hasValidHitInPixelBarrelLayer4",

    "hasValidHitInPixelEndcapLayer1",
    "hasValidHitInPixelEndcapLayer2",
    "hasValidHitInPixelEndcapLayer3",
    
    "hitPattern_.pixelBarrelLayersNull",
    "hitPattern_.pixelEndcapLayersNull",

    "hitPattern_.numberOfValidPixelHits", 
    "hitPattern_.trackerLayersWithMeasurement",

    "bestTrackNumberOfValidHits",
    "bestTrackNumberOfValidPixelHits",
    "bestTrackNumberOfValidPixelBarrelHits",
    "bestTrackNumberOfValidPixelEndcapHits",
    "bestTrackMissingInnerHits",
    "bestTrackMissingMiddleHits",
    "bestTrackMissingOuterHits",

    "hitAndTOBDrop_bestTrackMissingOuterHits",

    "numberOfTrackerHits",
    "numberOfPixelHits",
    "numberOfStripHits",
    "numberOfPixelBarrelHits",
    "numberOfPixelEndcapHits",
    "numberOfStripTIBHits",
    "numberOfStripTIDHits",
    "numberOfStripTOBHits",
    "numberOfStripTECHits",

    "missingInnerHits",
    "missingMiddleHits",
    "missingOuterHits",

    "missingTrackerHits",
    "missingPixelHits",
    "missingStripHits",
    "missingPixelBarrelHits",
    "missingPixelEndcapHits",
    "missingStripTIBHits",
    "missingStripTIDHits",
    "missingStripTOBHits",
    "missingStripTECHits",

    "expectedTrackerHits",
    "expectedPixelHits",
    "expectedStripHits",
    "expectedPixelBarrelHits",
    "expectedPixelEndcapHits",
    "expectedStripTIBHits",
    "expectedStripTIDHits",
    "expectedStripTOBHits",
    "expectedStripTECHits",

    "expectedIncludeInactiveTrackerHits",
    "expectedIncludeInactivePixelHits",
    "expectedIncludeInactiveStripHits",
    "expectedIncludeInactivePixelBarrelHits",
    "expectedIncludeInactivePixelEndcapHits",
    "expectedIncludeInactiveStripTIBHits",
    "expectedIncludeInactiveStripTIDHits",
    "expectedIncludeInactiveStripTOBHits",
    "expectedIncludeInactiveStripTECHits",

    "trackerLayersNull",
    "pixelLayersNull",
    "stripLayersNull",
    "pixelBarrelLayersNull",
    "pixelEndcapLayersNull",
    "stripTIBLayersNull",
    "stripTIDLayersNull",
    "stripTOBLayersNull",
    "stripTECLayersNull",

    "numberOfBadHits",

    "numberOfLostInnerHits",
    "numberOfLostMiddleHits",
    "numberOfLostOuterHits",
    "numberOfLostHits",

    "pt",
    "p",
    "eta",
    "phi",
    "normalizedChi2",
    "charge",
    "caloNewDRp5",
    "dRMinJet",

    "deltaRToClosestElectron",
    "deltaRToClosestVetoElectron",
    "deltaRToClosestLooseElectron",
    "deltaRToClosestMediumElectron",
    "deltaRToClosestTightElectron",
    "deltaRToClosestMuon",
    "deltaRToClosestLooseMuon",
    "deltaRToClosestMediumMuon",
    "deltaRToClosestTightMuon",
    "deltaRToClosestTau",
    "deltaRToClosestTauHad",

    "deltaRToClosestPFElectron",
    "deltaRToClosestPFMuon",
    "deltaRToClosestPFChHad",

    "pfElectronIsoDR03",
    "pfPUElectronIsoDR03",
    "pfMuonIsoDR03",
    "pfPUMuonIsoDR03",
    "pfHFIsoDR03",
    "pfPUHFIsoDR03",
    "pfLostTrackIsoDR03",
    "pfPULostTrackIsoDR03",
    "isoTrackIsoDR03",
    "pfChHadIsoDR03",
    "pfPUChHadIsoDR03",
    "pfNeutralHadIsoDR03",
    "pfPUNeutralHadIsoDR03",
    "pfPhotonIsoDR03",
    "pfPUPhotonIsoDR03",

    "caloNewNoPUDRp5",
    "caloNewNoPUDRp5Calo",
    "caloNewNoPUDRp5CentralCalo",
    "caloNewNoPUDRp3",
    "caloNewNoPUDRp3Calo",
    "caloNewNoPUDRp3CentralCalo",
    "caloNewNoPUDRp2",
    "caloNewNoPUDRp2Calo",
    "caloNewNoPUDRp2CentralCalo",
    "caloNewNoPUDRp1",
    "caloNewNoPUDRp1Calo",
    "caloNewNoPUDRp1CentralCalo",

    "trackIsoNoPUDRp5",
    "trackIsoNoPUDRp3",
    "trackIsoNoPUDRp2",
    "trackIsoNoPUDRp1",
]

from DisappTrks.StandardAnalysis.protoConfig_cfg import UseCandidateTracks
if not UseCandidateTracks:
    TrackDebugBranches_names.extend([
        "dRToMatchedCandidateTrack",
        "matchedCaloJetEmEnergy",
        "matchedCaloJetHadEnergy",
        "pfLepOverlap",
        "pfNeutralSum",
        "dz",
        "dxy",
        "dzError",
        "dxyError",
        "fromPV",
        "isHighPurityTrack",
        "isTightTrack",
        "isLooseTrack",
        "dEdxStrip",
        "dEdxPixel",
    ])
else:
    TrackDebugBranches_names.extend([
        "dRToMatchedIsolatedTrack",
        "matchedIsolatedTrack_pfIsolationDR03.chargedHadronIso",
        "matchedIsolatedTrack_pfIsolationDR03.neutralHadronIso",
        "matchedIsolatedTrack_pfIsolationDR03.photonIso",
        "matchedIsolatedTrack_pfIsolationDR03.puChargedHadronIso",
        "matchedIsolatedTrack_matchedCaloJetEmEnergy",
        "matchedIsolatedTrack_matchedCaloJetHadEnergy",
        "matchedIsolatedTrack_pfLepOverlap",
        "matchedIsolatedTrack_pfNeutralSum",
        "matchedIsolatedTrack_dz",
        "matchedIsolatedTrack_dxy",
        "matchedIsolatedTrack_dzError",
        "matchedIsolatedTrack_dxyError",
        "matchedIsolatedTrack_fromPV",
        "matchedIsolatedTrack_isHighPurityTrack",
        "matchedIsolatedTrack_isTightTrack",
        "matchedIsolatedTrack_isLooseTrack",
        "matchedIsolatedTrack_dEdxStrip",
        "matchedIsolatedTrack_dEdxPixel",
        "matchedIsolatedTrack_crossedEcalStatus",
        "matchedIsolatedTrack_crossHcalStatus",
        "matchedIsolatedTrack_deltaEta",
        "matchedIsolatedTrack_deltaPhi",
    ])

TrackDebugBranches = cms.PSet(
    inputCollection = cms.vstring("tracks"),
    branches = cms.VPSet ([cms.PSet(name = cms.string(x), inputVariables = cms.vstring(x)) for x in TrackDebugBranches_names]),
)

####################################
#####     Isolated Tracks      #####
####################################

IsolatedTrackDebugBranches = cms.PSet(
    inputCollection = cms.vstring("tracks"),
    branches = cms.VPSet ([cms.PSet(name = cms.string("matchedCandidateTrack_" + x), inputVariables = cms.vstring("matchedCandidateTrack." + x)) for x in TrackDebugBranches_names]),
)

####################################
#####   Track-eventvariables   #####
####################################

TrackEventvariablesDebugBranches = cms.PSet(
    inputCollection = cms.vstring("tracks", "eventvariables"),
    branches = cms.VPSet (
        cms.PSet(
            name = cms.string("trackD0WRTPV"),
            inputVariables = cms.vstring(trackD0WRTPV),
        ),
        cms.PSet(
            name = cms.string("trackDZWRTPV"),
            inputVariables = cms.vstring(trackDZWRTPV),
        ),
    )   
)

####################################
#####    Toy Model variables   #####
####################################

# Toy model for tracker-as-target
FakeDecayBranches = cms.PSet (
    inputCollection = cms.vstring("eventvariables"),
    branches = cms.VPSet (
        cms.PSet (
            name = cms.string("DeltaAngle_overall"),
            inputVariables = cms.vstring("DeltaAngle"),
        ),
        cms.PSet (
            name = cms.string("Pprime_overall"),
            inputVariables = cms.vstring("GenTrkMu"),
        ),
        cms.PSet (
            name = cms.string("DeltaAngle_missouter"),
            inputVariables = cms.vstring("MissOuterDeltaAngle"),
        ),
        cms.PSet (
            name = cms.string("Pprime_missouter"),
            inputVariables = cms.vstring("MissOuterGenTrkMu"),
        ),
        cms.PSet (
            name = cms.string("DeltaAngle_distrk"),
            inputVariables = cms.vstring("DisTrkDeltaAngle"),
        ),
        cms.PSet (
            name = cms.string("Pprime_distrk"),
            inputVariables = cms.vstring("DisTrkGenTrkMu"),
        ),
    )
)