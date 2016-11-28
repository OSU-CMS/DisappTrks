from DisappTrks.StandardAnalysis.config_cfg import *
import sys

if not os.environ["CMSSW_VERSION"].startswith ("CMSSW_8_0_"):
    print "Please use a CMSSW_8_0_X release..."
    sys.exit (0)

process.PUScalingFactorProducer.PU     = cms.string (os.environ['CMSSW_BASE'] + '/src/DisappTrks/StandardAnalysis/data/pu_disappTrks_run2.root')
process.PUScalingFactorProducer.target = cms.string ("data2016_BC")

setMissingHitsCorrection (process, "2016BC")
