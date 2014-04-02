#!/usr/bin/env python

# For usage instructions, see:
# https://twiki.cern.ch/twiki/bin/viewauth/CMS/DisappearingTracksSearch2012Recipes#Set_up_signal_MC_generation
#
# Usage:
# DisappTrks/SignalMC/test > customizeConfig.py -i AMSB_chargino_cfi_py_GEN_SIM_DIGI_L1_DIGI2RAW_HLT_RAW2DIGI_L1Reco_RECO_PU.py -o ../python/  

import sys
from optparse import OptionParser

parser = OptionParser()

parser.add_option("-i", "--infile", dest="infile",
                  help="input config file")
parser.add_option("-o", "--outfile", dest="outfile",
                  help="output file name; if ends in '/', will append infile name")
(arguments, args) = parser.parse_args()


infile = arguments.infile 
outfile = arguments.outfile
if outfile.endswith("/"):
    outfile = outfile + infile

print "Reading input file: "  + infile

fin = open(infile, "r")
configNew = fin.read()
fin.close()

# The simPartBlock runs the GenPlusSimParticleProducer and stores the output collection, so that the Geant decay
# products are saved.  
simPartBlock  = 'process.genParticlePlusGeant = cms.EDProducer("GenPlusSimParticleProducer",  \n'
simPartBlock += '                                              src           = cms.InputTag("g4SimHits"),   # use "famosSimHits" for FAMOS  \n'
simPartBlock += '                                              setStatus     = cms.int32(8),                # set status = 8 for GEANT GPs  \n'
simPartBlock += '                                              filter        = cms.vstring("pt > 0.0"),     # just for testing (optional)  \n'
simPartBlock += '                                              genParticles  = cms.InputTag("genParticles") # original genParticle list  \n'
simPartBlock += '                                              )  \n'
simPartBlock += 'process.simulation_step = cms.Path(process.psim + process.genParticlePlusGeant)  \n'
simPartBlock += 'process.RAWSIMoutput.outputCommands.extend( [  \n'
simPartBlock += '    "keep *_genParticlePlusGeant_*_*",  \n'
simPartBlock += '    ] )  \n'
  
# The configAdd block customizes the process for handling chargino interactions with matter,
# and modifies configuration parameters so that daughters of long-lived chargino decays
# are retained in the SimVertex and SimTrack collections.
finAdd = open("addToConfig.py", "r")
configAdd = finAdd.read()
finAdd.close()  

configNew = configNew.replace("process.simulation_step = cms.Path(process.psim)", simPartBlock)
configNew = configNew + configAdd 
fnew = open(outfile, "w")
fnew.write(configNew)
fnew.close()

print "Wrote output file: " + outfile







