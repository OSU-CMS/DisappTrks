from DisappTrks.BackgroundEstimation.config_cfg import *
from DisappTrks.StandardAnalysis.customize import *

if not os.environ["CMSSW_VERSION"].startswith ("CMSSW_12_4_"):
    print("Please use a CMSSW_12_4_X release...")
    sys.exit (0)

process = customize (process, "2022", applyPUReweighting = False, applyTriggerReweighting = False, applyMissingHitsCorrections = False, runMETFilters = False)
