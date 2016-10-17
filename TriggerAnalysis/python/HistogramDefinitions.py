import FWCore.ParameterSet.Config as cms
from DisappTrks.StandardAnalysis.invMass import *
from OSUT3Analysis.Configuration.pdgIdBins import *
from OSUT3Analysis.Configuration.cutUtilities import *

bins = []
nBins = 1000
xbinPowerHi = 3.0
xbinPowerLo = 0.0

binPowerWidth = (xbinPowerHi - xbinPowerLo) / nBins
for ibin in range(nBins+1):
    bins.append(pow(10, xbinPowerLo + ibin * binPowerWidth))

###############################################
##### Set up the histograms to be plotted #####
###############################################

METHistograms = cms.PSet(
    inputCollection = cms.vstring("mets"),
    histograms = cms.VPSet(
         cms.PSet(
            name = cms.string("metNoMu"),
            title = cms.string("MetNoMu;E_{T}^{miss} excluding muons [GeV]"),
            binsX = cms.untracked.vdouble(bins),
            inputVariables = cms.vstring("noMuPt"),
            ),
        )
    )

MuonHistograms = cms.PSet(
    inputCollection = cms.vstring("muons"),
    histograms = cms.VPSet(
        cms.PSet(
            name = cms.string("muonPt"),
            title = cms.string("Muon Transverse Momentum; muon p_{T} [GeV]"),
            binsX = cms.untracked.vdouble(bins),
            inputVariables = cms.vstring("pt"),
            ),
        )
    )

TrackHistograms = cms.PSet(
    inputCollection = cms.vstring("tracks"),
    histograms = cms.VPSet(
        cms.PSet(
            name = cms.string("trackPt"),
            title = cms.string("Track Transverse Momentum; track p_{T} [GeV]"),
            binsX = cms.untracked.vdouble(bins),
            inputVariables = cms.vstring("pt"),
            ),
        )
    )
)
