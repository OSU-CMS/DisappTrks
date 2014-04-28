#SLHA_FILE =  'DisappTrks/SignalMC/data/TestMuonDecay.slha' 

import FWCore.ParameterSet.Config as cms

from Configuration.Generator.PythiaUEZ2starSettings_cfi import *

generator = cms.EDFilter("Pythia6GeneratorFilter",
    pythiaHepMCVerbosity = cms.untracked.bool(False),
    maxEventsToPrint = cms.untracked.int32(1),
    pythiaPylistVerbosity = cms.untracked.int32(1),
    filterEfficiency = cms.untracked.double(1.0),
    comEnergy = cms.double(8000.),
    PythiaParameters = cms.PSet(
        pythiaUESettingsBlock,
        processParameters = cms.vstring(
# Take pythia commands for Z->ll from https://cmssdt.cern.ch/SDT/lxr/source/Configuration/Generator/python/DYToLL_M_50_TuneZ2star_8TeV_pythia6_tauola_cff.py  
#            'IMSS(1)     = 11    ! Spectrum from external SLHA file',
            'MSEL        = 0     ! full user control',
            'MSUB(1)=1         !Incl Z0/gamma* production', 
            'MSTP(43)=3        !Both Z0 and gamma*', 
            'MDME(174,1)=0     !Z decay into d dbar', 
            'MDME(175,1)=0     !Z decay into u ubar', 
            'MDME(176,1)=0     !Z decay into s sbar', 
            'MDME(177,1)=0     !Z decay into c cbar', 
            'MDME(178,1)=0     !Z decay into b bbar', 
            'MDME(179,1)=0     !Z decay into t tbar', 
            'MDME(182,1)=0     !Z decay into e- e+', 
            'MDME(183,1)=0     !Z decay into nu_e nu_ebar', 
            'MDME(184,1)=0     !Z decay into mu- mu+', 
            'MDME(185,1)=0     !Z decay into nu_mu nu_mubar', 
            'MDME(186,1)=1     !Z decay into tau- tau+', 
            'MDME(187,1)=0     !Z decay into nu_tau nu_taubar', 
            'CKIN(1)=50.       !Minimum sqrt(s_hat) value (=Z mass)',
            'PMAS(15,4) = 1000  ! set lifetime of tau to be ctau in mm', 
            ),
# Take setting particle widths from:
# https://twiki.cern.ch/twiki/bin/view/CMSPublic/SWGuidePythia6Interface#Example_8_How_to_modify_particle  
# http://cvs.web.cern.ch/cvs/cgi-bin/viewcvs.cgi/CMSSW/Configuration/Generator/python/Pythia_H0_pyupda_cfi.py?revision=1.3&content-type=text%2Fplain
         ## PYUPDAParameters = cms.vstring(
         ##     'PYUPDAFILE =  pyupda.out',
         ##     'PYUPDAWRITE'
         ##     ), 
#         PYUPDAParameters = cms.vstring(
#              "PYUPDAFILE = 'DisappTrks/SignalMC/data/TestMuonDecay.pyupda'", 
# #             "PYUPDAFILE = 'DisappTrks/SignalMC/data/TestMuonDecay-orig.pyupda'", 
#              ),
        parameterSets = cms.vstring('pythiaUESettings', 'processParameters'),
#        parameterSets = cms.vstring('pythiaUESettings', 'processParameters', 'PYUPDAParameters')  
#        parameterSets = cms.vstring('pythiaUESettings', 'processParameters', 'SLHAParameters'),
#        SLHAParameters = cms.vstring('SLHAFILE = ' + SLHA_FILE),
    ),
)

