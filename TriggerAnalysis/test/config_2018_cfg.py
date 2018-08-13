from DisappTrks.TriggerAnalysis.config_cfg import *
from DisappTrks.StandardAnalysis.customize import *

if not os.environ["CMSSW_VERSION"].startswith ("CMSSW_10_1_"):
    print "Please use a CMSSW_10_1_X release..."
    sys.exit (0)

process = customize (process, "2018", applyPUReweighting = False, applyISRReweighting = False, applyTriggerReweighting = False, applyMissingHitsCorrections = True, runMETFilters = False)
