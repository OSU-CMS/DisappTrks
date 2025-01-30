from DisappTrks.SignalSystematics.config_cfg import *
from DisappTrks.StandardAnalysis.customize import *
from FWCore.ParameterSet.VarParsing import VarParsing

if not os.environ["CMSSW_VERSION"].startswith ("CMSSW_12_4_") and not os.environ["CMSSW_VERSION"].startswith ("CMSSW_13_0_"):
    print("Please use a CMSSW_12_4_X or CMSSW_13_0_X release...")
    sys.exit (0)

options = VarParsing ('analysis')
options.register ('doLifetimeReweighting',
              False,
              VarParsing.multiplicity.singleton,
              VarParsing.varType.bool,
              "turn on For LifetimeReweighting")
options.register ('massForLifetimeReweighting',
              1000,
              VarParsing.multiplicity.singleton,
              VarParsing.varType.int,
              "mass For LifetimeReweighting")
options.register ('lifetimeForLifetimeReweighting',
              1000,
              VarParsing.multiplicity.singleton,
              VarParsing.varType.int,
              "lifetime For LifetimeReweighting")
options.parseArguments()

process = customize (process, "2022", "F", realData=True, applyPUReweighting = True, applyISRReweighting = True, applyTriggerReweighting = True, applyMissingHitsCorrections = True, runMETFilters = False)

if options.doLifetimeReweighting:
    if hasattr(process, 'LifetimeWeightProducer'):
        exec('from OSUT3Analysis.Configuration.configurationOptions import *')
        rules = []
        rules.extend(rulesForLifetimeReweighting['AMSB_chargino_' + str(options.massForLifetimeReweighting) + 'GeV_' + str(options.lifetimeForLifetimeReweighting) + 'cm_130X'])
        process.LifetimeWeightProducer.reweightingRules = cms.VPSet([
            cms.PSet(
                pdgIds = cms.vint32(r.pdgIds),
                srcCTaus = cms.vdouble(r.srcCTaus),
                dstCTaus = cms.vdouble(r.dstCTaus),
                isDefaultRule = cms.bool(r.isDefaultRule)
            ) for r in rules])

# When using these channels for calculating a new weight in MC, use the following customization instead:
# ZtoMuMuISRStudy, ZtoMuMuISRStudyJet30
# hitsSystematicsCtrlSelection, muonCtrlSelection
# process = customize (process, "2018", applyPUReweighting = True, applyISRReweighting = False, applyTriggerReweighting = False, applyMissingHitsCorrections = False, runMETFilters = False)
