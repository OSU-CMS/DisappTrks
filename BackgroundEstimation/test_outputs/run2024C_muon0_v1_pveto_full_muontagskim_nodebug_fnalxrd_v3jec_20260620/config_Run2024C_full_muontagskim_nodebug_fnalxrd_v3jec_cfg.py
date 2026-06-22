import FWCore.ParameterSet.Config as cms
import os
import sys

# Temporary Run2024C V1 no-debug FNAL-XRootD MuonTagSkim-only full-stat config created by Codex on 2026-06-20.
# This lives outside the DisappTrks source tree so existing V1 files are not edited.
import DisappTrks.StandardAnalysis.protoConfig_cfg as protoConfig_module

INPUT_FILE = (
    "root://cmsxrootd.fnal.gov//store/data/Run2024C/Muon0/MINIAOD/"
    "MINIv6NANOv15-v1/2530000/00802afa-7a55-40cd-9f5a-846ad9e21a45.root"
)

protoConfig_module.process.source.fileNames = cms.untracked.vstring([INPUT_FILE])

from DisappTrks.BackgroundEstimation.config_cfg import *
from DisappTrks.StandardAnalysis.customize import *

if not (
    os.environ["CMSSW_VERSION"].startswith("CMSSW_12_4_")
    or os.environ["CMSSW_VERSION"].startswith("CMSSW_13_0_")
    or os.environ["CMSSW_VERSION"].startswith("CMSSW_15_0_")
):
    print("Please use CMSSW_12_4_X, CMSSW_13_0_X, or CMSSW_15_0_X...")
    sys.exit(0)

process = customize(
    process,
    "2024",
    "C",
    realData=True,
    applyPUReweighting=False,
    applyISRReweighting=False,
    applyTriggerReweighting=False,
    applyMissingHitsCorrections=False,
    runMETFilters=False,
)

process.source.fileNames = cms.untracked.vstring([INPUT_FILE])
process.maxEvents = cms.untracked.PSet(input=cms.untracked.int32(-1))


# Validation-only override added by Codex on 2026-06-20.
# Keep the default V1 schedule intact; only point OSUJetProducer at a
# temporary 2024 JEC config whose tag names match the current CVMFS payload.
from DisappTrks.StandardAnalysis.utilities import changeJecConfigFile
changeJecConfigFile(process, "DisappTrks/BackgroundEstimation/test_outputs/run2024C_muon0_v1_pveto_full_muontagskim_nodebug_fnalxrd_v3jec_20260620/JecConfigAK4_Run2024C_V3_validation.json")


# Validation-only narrowing: make only the MuonTagSkim input for V1 Pveto stage 2.
process.endPath = cms.EndPath(process.MuonTagSkimPoolOutputModule)
process.schedule = cms.Schedule(
    process.passecalBadCalibFilterUpdatePath,
    process.egmGsfElectronIDSequence_step,
    process.variableProducerPath,
    process.MuonTagSkim,
    process.endPath,
)

# Reduce per-event FwkReport logging for the full 50k-event validation.
process.MessageLogger.cerr.FwkReport.reportEvery = 5000
