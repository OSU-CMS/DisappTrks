from DisappTrks.StandardAnalysis.config_cfg import *
#from DisappTrks.BackgroundEstimation.config_cfg import *
from DisappTrks.StandardAnalysis.customize import *

#if not os.environ["CMSSW_VERSION"].startswith ("CMSSW_10_2_"):
#    print "Please use a CMSSW_10_2_X release..."
#    sys.exit (0)

process = customize (process, "2023", "D", realData=True, applyPUReweighting = False, applyISRReweighting = False, applyTriggerReweighting = False, applyMissingHitsCorrections = False, runMETFilters = False)

#process.maxEvents = cms.untracked.PSet (
#    input = cms.untracked.int32 (100)
#)
