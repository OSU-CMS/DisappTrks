import FWCore.ParameterSet.Config as cms

from OSUT3Analysis.Configuration.cutUtilities import *

####################################################################

MELAeventvariableNames = ['hitCharge_' + str(itrk) + '_' + str(ihit) for itrk in range(2) for ihit in range(20)]
MELAeventvariableNames.extend(['hitIsPixel_' + str(itrk) + '_' + str(ihit) for itrk in range(2) for ihit in range(20)])
MELAeventvariableNames.extend([
	'lifetimeWeight',
	'puScalingFactor',
	'isrWeight',
	'grandOrWeight',
	'L1ECALPrefiringWeight',
])

for srcCTau in [1, 10, 100, 1000, 10000]:
    destinationCTaus = [float(0.1 * i * srcCTau) for i in range(2, 11)]
    if srcCTau == 10:
        destinationCTaus.extend([float(0.01 * i * srcCTau) for i in range(1, 11)])
    for dst in destinationCTaus:
        dstCTau = str(int(dst)) if dst > 1 else '0p' + str(int(10 * dst))
        thisName = "lifetimeWeight_1000024_" + str(srcCTau) + "cmTo" + dstCTau + "cm"
        MELAeventvariableNames.append(thisName)

MELAeventvariableBranches = cms.PSet(
	inputCollections = cms.vstring('eventvariables'),
	branches = cms.VPSet([cms.PSet(name = cms.string(x), inputVariables = cms.vstring(x)) for x in MELAdEdxMeasurementNames]),
)

####################################################################

MELAtrackMetBranches = cms.PSet(
	inputCollections = cms.vstring('tracks', 'mets'),
	branches = cms.VPSet(
		cms.PSet(
			name = cms.string('trackMetPhi'),
			inputVariables = cms.vstring('dPhi(met.noMuPhi, track.phi)'),
		),
	),
)

####################################################################

MELAtrackJetBranches = cms.PSet(
	inputCollections = cms.vstring('tracks', 'jets'),
	branches = cms.VPSet(
		cms.PSet(
			name = cms.string('trackMetPhi'),
			inputVariables = cms.vstring('dPhi(jet.noMuPhi, track.phi)'),
		),
	),
)

####################################################################

MELAtrackBranches = cms.PSet(
	inputCollections = cms.vstring('tracks'),
	branches = cms.VPSet(
		cms.PSet(
			name = cms.string('matchedIsolatedTrack_dEdxStrip'),
			inputVariables = cms.vstring('matchedIsolatedTrack_dEdxStrip'),
		),
		cms.PSet(
			name = cms.string('matchedIsolatedTrack_dEdxPixel'),
			inputVariables = cms.vstring('matchedIsolatedTrack_dEdxPixel'),
		),
	),
)
