import FWCore.ParameterSet.Config as cms
from DisappTrks.StandardAnalysis.IntegratedLuminosity_cff import *
import os

# parameters:
# input file for each lepton type
# for each SF:
# inputCollection {electron, muon, track}
# sfType {Trigger, Reco, ID, Iso}
# version: 2015, 2016
# optional: wp {Veto, Loose, Medium, Tight}
# optional list: eras (e.g. [BCDEF, GH])
# optional list: lumis (e.g. [19717, 16146])
# optional double: additionalSystematic (in percent of central value, e.g. 0.01) -- "optional" to framework operation but mandated by POGs
# optional double: additionalSystematicBelow20GeV (in percent of central value, e.g. 0.01) -- "optional" to framework operation but mandated by POGs
# optional double: additionalSystematicAbove80GeV (in percent of central value, e.g. 0.01) -- "optional" to framework operation but mandated by POGs
# input distribution is in a histogram called $inputCollection$sfType$version$wp$eras
#    e.g. muonID2016TightBCDEF
# output weight called $inputCollection$sfType$version$wp
#    e.g. muonID2016Tight

# inputs are generally TH2Fs of pt vs eta
# sometimes they're |eta| or 1D plots

# N.B.: respective SFs are only produced by ObjectScalingFactorProducer if "electrons" or "muons" are in the list of object collections to get
#       so we can put e/mu together and choose the weights to apply

# https://twiki.cern.ch/twiki/bin/view/CMS/EgammaIDRecipesRun2#Electron_efficiencies_and_scale
# https://twiki.cern.ch/twiki/bin/view/CMS/MuonReferenceEffsRun2#Muon_reconstruction_identificati

leptonScaleFactors2015 = cms.VPSet (
    cms.PSet (
        inputCollection = cms.string("muons"),
        sfType = cms.string("Trigger"),
        version = cms.string("2015"),
        wp = cms.string("IsoMu20_OR_IsoTkMu20"),
        additionalSystematic = cms.double(0.005),
    ),
    cms.PSet (
        inputCollection = cms.string("muons"),
        sfType = cms.string("ID"),
        version = cms.string("2015"),
        wp = cms.string("Tight"),
        additionalSystematic = cms.double(0.01),
    ),
    cms.PSet (
        inputCollection = cms.string("muons"),
        sfType = cms.string("Iso"),
        version = cms.string("2015"),
        wp = cms.string("Tight"),
        additionalSystematic = cms.double(0.005),

    ),
    cms.PSet (
        inputCollection = cms.string("electrons"),
        sfType = cms.string("Reco"),
        version = cms.string("2015"),
    ),
    cms.PSet (
        inputCollection = cms.string("electrons"),
        sfType = cms.string("ID"),
        version = cms.string("2015"),
        wp = cms.string("Tight"),
    ),
)

leptonScaleFactors2016 = cms.VPSet (
    cms.PSet (
        inputCollection = cms.string("muons"),
        sfType = cms.string("Trigger"),
        version = cms.string("2016"),
        wp = cms.string("IsoMu24_OR_IsoTkMu24"),
        eras = cms.vstring("BCDEF", "GH"),
        lumis = cms.vdouble(lumi["SingleMuon_2016BCDEF"], lumi["SingleMuon_2016GH"]),
        additionalSystematic = cms.double(0.005),
    ),
    cms.PSet (
        inputCollection = cms.string("muons"),
        sfType = cms.string("ID"),
        version = cms.string("2016"),
        wp = cms.string("Tight"),
        eras = cms.vstring("BCDEF", "GH"),
        lumis = cms.vdouble(lumi["SingleMuon_2016BCDEF"], lumi["SingleMuon_2016GH"]),
        additionalSystematic = cms.double(0.01),
    ),
    cms.PSet (
        inputCollection = cms.string("muons"),
        sfType = cms.string("Iso"),
        version = cms.string("2016"),
        wp = cms.string("Tight"),
        eras = cms.vstring("BCDEF", "GH"),
        lumis = cms.vdouble(lumi["SingleMuon_2016BCDEF"], lumi["SingleMuon_2016GH"]),
        additionalSystematic = cms.double(0.005),

    ),
    cms.PSet (
        inputCollection = cms.string("muons"),
        sfType = cms.string("Tracking"),
        version = cms.string("2016"),
        eras = cms.vstring("BCDEF", "GH"),
        lumis = cms.vdouble(lumi["SingleMuon_2016BCDEF"], lumi["SingleMuon_2016GH"]),
    ),
    cms.PSet (
        inputCollection = cms.string("electrons"),
        sfType = cms.string("Reco"),
        version = cms.string("2016"),
    ),
    cms.PSet (
        inputCollection = cms.string("electrons"),
        sfType = cms.string("ID"),
        version = cms.string("2016"),
        wp = cms.string("Tight"),
    ),
)

LeptonScaleFactorProducer = {
    'name'         : 'ObjectScalingFactorProducer',
    'electronFile' : cms.string(os.environ['CMSSW_BASE'] + '/src/OSUT3Analysis/AnaTools/data/electronSFs.root'),
    'muonFile'     : cms.string(os.environ['CMSSW_BASE'] + '/src/OSUT3Analysis/AnaTools/data/muonSFs.root'),
    #'trackFile'    : cms.string(os.environ['CMSSW_BASE'] + '/src/OSUT3Analysis/AnaTools/data/trackSFs.root'),
    'scaleFactors' : leptonScaleFactors2015,
}

if os.environ["CMSSW_VERSION"].startswith ("CMSSW_8_0_"):
    LeptonScaleFactorProducer['scaleFactors'] = leptonScaleFactors2016
