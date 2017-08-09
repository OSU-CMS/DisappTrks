from DisappTrks.TriggerAnalysis.config_cfg import *
from DisappTrks.StandardAnalysis.customize import *

if not os.environ["CMSSW_VERSION"].startswith ("CMSSW_9_2_"):
    print "Please use a CMSSW_9_2_X release..."
    sys.exit (0)

print "# FIXME: using 2016DEFGH customization"
process = customize (process, "2016DEFGH", applyPUReweighting = False, applyTriggerReweighting = False, runMETFilters = False)
