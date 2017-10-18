from DisappTrks.TriggerAnalysis.config_cfg import *
from DisappTrks.StandardAnalysis.customize import *

if not os.environ["CMSSW_VERSION"].startswith ("CMSSW_9_2_"):
    print "Please use a CMSSW_9_2_X release..."
    sys.exit (0)

process = customize (process, "2017", applyPUReweighting = False, applyTriggerReweighting = False, applyMissingHitsCorrections = True, runMETFilters = False)
