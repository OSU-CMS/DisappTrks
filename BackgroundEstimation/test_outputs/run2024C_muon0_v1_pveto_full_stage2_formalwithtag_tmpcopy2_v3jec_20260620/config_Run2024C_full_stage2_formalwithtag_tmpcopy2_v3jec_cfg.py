import FWCore.ParameterSet.Config as cms

import DisappTrks.StandardAnalysis.protoConfig_cfg as protoConfig_module
INPUT_FILE = "file:/tmp/czheng_v1_pveto_20260620/skim_MuonTagSkim_Run2024C_full.root"
protoConfig_module.process.source.fileNames = cms.untracked.vstring([INPUT_FILE])

from DisappTrks.BackgroundEstimation.config_cfg import *
from DisappTrks.StandardAnalysis.customize import *
from DisappTrks.StandardAnalysis.utilities import changeJecConfigFile

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
changeJecConfigFile(process, "DisappTrks/BackgroundEstimation/test_outputs/run2024C_muon0_v1_pveto_full_stage2_formalwithtag_tmpcopy2_v3jec_20260620/JecConfigAK4_Run2024C_V3_validation.json")
process.MessageLogger.cerr.FwkReport.reportEvery = 1000

def _drop_eventvariable_from(module, dropped_label):
    kept = [tag for tag in module.collections.eventvariables if tag.getModuleLabel() != dropped_label]
    module.collections.eventvariables = cms.VInputTag(*kept)

for _channel, _dropped in (
    ("ZtoMuProbeTrk", "objectProducer51"),
    ("ZtoMuProbeTrkWithFilter", "objectProducer66"),
    ("ZtoMuProbeTrkWithSSFilter", "objectProducer81"),
):
    _drop_eventvariable_from(getattr(process, _channel + "CutCalculator"), _dropped)
    _drop_eventvariable_from(getattr(process, _channel + "CutFlowPlotter"), _dropped)

process.schedule = cms.Schedule(
    process.passecalBadCalibFilterUpdatePath,
    process.egmGsfElectronIDSequence_step,
    process.variableProducerPath,
    process.MuonTagSkim,
    process.ZtoMuProbeTrk,
    process.ZtoMuProbeTrkWithFilter,
    process.ZtoMuProbeTrkWithSSFilter,
)
