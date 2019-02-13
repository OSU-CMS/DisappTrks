from DisappTrks.SignalSystematics.config_cfg import *
from DisappTrks.StandardAnalysis.customize import *

if not os.environ["CMSSW_VERSION"].startswith ("CMSSW_7_6_"):
    print "Please use a CMSSW_7_6_X release..."
    sys.exit (0)

process = customize (process, "2015", applyPUReweighting = True, applyISRReweighting = True, applyTriggerReweighting = True, applyMissingHitsCorrections = True, runMETFilters = False)

# When using these channels for calculating a new weight in MC, use the following customization instead:
# ZtoMuMuISRStudy, ZtoMuMuISRStudyJet30
# hitsSystematicsCtrlSelection, muonCtrlSelection
# process = customize (process, "2015", applyPUReweighting = True, applyISRReweighting = False, applyTriggerReweighting = False, applyMissingHitsCorrections = False, runMETFilters = False)
