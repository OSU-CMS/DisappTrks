from DisappTrks.StandardAnalysis.config_cfg import *
from DisappTrks.StandardAnalysis.customize import *

if not os.environ["CMSSW_VERSION"].startswith ("CMSSW_9_4_"):
    print "Please use a CMSSW_9_4_X release..."
    sys.exit (0)

process = customize (process, "2017", applyPUReweighting = True, applyTriggerReweighting = True, applyMissingHitsCorrections = True, runMETFilters = False)
