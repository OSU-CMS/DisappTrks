from DisappTrks.StandardAnalysis.config_cfg import *
from DisappTrks.StandardAnalysis.customize import *

if not os.environ["CMSSW_VERSION"].startswith ("CMSSW_10_2_"):
    print "Please use a CMSSW_10_2_X release..."
    sys.exit (0)

process = customize (process, "2018", applyPUReweighting = True, applyISRReweighting = True, applyTriggerReweighting = True, applyMissingHitsCorrections = True, runMETFilters = True)
