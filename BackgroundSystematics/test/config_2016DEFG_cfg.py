from DisappTrks.StandardAnalysis.config_cfg import *
import sys

if not os.environ["CMSSW_VERSION"].startswith ("CMSSW_8_0_"):
    print "Please use a CMSSW_8_0_X release..."
    sys.exit (0)

process.PUScalingFactorProducer.PU     = cms.string (os.environ['CMSSW_BASE'] + '/src/DisappTrks/StandardAnalysis/data/pu_disappTrks_run2.root')
process.PUScalingFactorProducer.target = cms.string ("data2016_DEFG")

process.ISRWeightProducer.weightFile = cms.string(os.environ['CMSSW_BASE'] + '/src/DisappTrks/StandardAnalysis/data/isrWeight_disappTrks_run2.root')
process.ISRWeightProducer.weightHist = cms.string('SingleMu_2016')
process.ISRWeightProducer.pdgIds = cms.vint32(1000022, 1000024)

process.TriggerWeightProducer.efficiencyFile = cms.string(os.environ['CMSSW_BASE'] + '/src/DisappTrks/StandardAnalysis/data/triggerEfficiencies_disappTrks_run2.root')
process.TriggerWeightProducer.dataset = cms.string('SingleMu_2016DEFG')
process.TriggerWeightProducer.target = cms.string('WJetsToLNu')

setMissingHitsCorrection (process, "2016DEFG")
