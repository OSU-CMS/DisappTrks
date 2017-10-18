from DisappTrks.BackgroundEstimation.config_cfg import *
from DisappTrks.StandardAnalysis.customize import *

if not os.environ["CMSSW_VERSION"].startswith ("CMSSW_7_6_"):
    print "Please use a CMSSW_7_6_X release..."
    sys.exit (0)

process = customize (process, "2015", applyPUReweighting = True, applyTriggerReweighting = True, applyMissingHitsCorrections = True, runMETFilters = False)
