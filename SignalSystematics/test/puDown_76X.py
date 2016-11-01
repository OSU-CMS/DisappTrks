from centralValue_76X import *

systematic = 'pileup'
fluctuate  = 'up'

if systematic == 'pileup':
    if fluctuate == 'up':
        process.PUScalingFactorProducer.target = cms.string("data2015Up")
    if fluctuate == 'down':
        process.PUScalingFactorProducer.target = cms.string("data2016Down")

if systematic == 'isr':
    # durp

if systematic == 'MetUncertainty':
    
