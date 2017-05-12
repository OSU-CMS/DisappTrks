from DisappTrks.SignalSystematics.config_cfg import *
from DisappTrks.StandardAnalysis.customize import *

if not os.environ["CMSSW_VERSION"].startswith ("CMSSW_8_0_"):
    print "Please use a CMSSW_8_0_X release..."
    sys.exit (0)

process = customize (process, "2016BC", applyPUReweighting = True, applyTriggerReweighting = True, runMETFilters = False)
