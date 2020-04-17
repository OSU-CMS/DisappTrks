from DisappTrks.ToyModels.config_cfg import *
from DisappTrks.StandardAnalysis.customize import *

if not os.environ["CMSSW_VERSION"].startswith ("CMSSW_8_0_"):
    print "Please use a CMSSW_8_0_X release..."
    sys.exit (0)

process = customize (process, 
					 "2016BC", 
					 applyPUReweighting = True, 
					 applyISRReweighting = False, 
					 applyTriggerReweighting = False, 
					 applyMissingHitsCorrections = False, 
					 runMETFilters = False)

moveVariableProducer(process, "ParticleGunMuonVarProducer", "MuonGunSkim")

# When using these channels for calculating a new weight in MC, use the following customization instead:
# ZtoMuMuISRStudy, ZtoMuMuISRStudyJet30
# hitsSystematicsCtrlSelection, muonCtrlSelection
# process = customize (process, "2016BC", applyPUReweighting = True, applyISRReweighting = False, applyTriggerReweighting = False, applyMissingHitsCorrections = False, runMETFilters = False)
