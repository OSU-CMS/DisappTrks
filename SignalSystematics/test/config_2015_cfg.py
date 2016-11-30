from DisappTrks.SignalSystematics.config_cfg import *
import sys

if not os.environ["CMSSW_VERSION"].startswith ("CMSSW_7_6_"):
    print "Please use a CMSSW_7_6_X release..."
    sys.exit (0)

process.PUScalingFactorProducer.PU     = cms.string (os.environ['CMSSW_BASE'] + '/src/DisappTrks/StandardAnalysis/data/pu_disappTrks_run2.root')
process.PUScalingFactorProducer.target = cms.string ("data2015")

setMissingHitsCorrection (process, "2015")
