COM_ENERGY = 13000.
CROSS_SECTION = 1.0
MCHI = 500  # GeV
CTAU = 100  # cm
SLHA_TABLE="""
## Important note!
## This file has been modified by hand to give the gluino and the 
## stop_1 a very narrow width, such that it can be used to try out
## the R-hadron machinery. It is not a realistic SUSY scenario.
##
##******************************************************************
##                      MadGraph/MadEvent                          *
##******************************************************************
##                                                                 *
##  param_card corresponding the SPS point 1a (by SoftSusy 2.0.5)  *
##                                                                 *
##******************************************************************
## Les Houches friendly file for the (MS)SM parameters of MadGraph *
##      SM parameter set and decay widths produced by MSSMCalc     *
##******************************************************************
##*Please note the following IMPORTANT issues:                     *
##                                                                 *
##0. REFRAIN from editing this file by hand! Some of the parame-   *
##   ters are not independent. Always use a calculator.            *
##                                                                 *
##1. alpha_S(MZ) has been used in the calculation of the parameters*
##   This value is KEPT by madgraph when no pdf are used lpp(i)=0, *
##   but, for consistency, it will be reset by madgraph to the     *
##   value expected IF the pdfs for collisions with hadrons are    *
##   used.                                                         *
##                                                                 *
##2. Values of the charm and bottom kinematic (pole) masses are    *
##   those used in the matrix elements and phase space UNLESS they *
##   are set to ZERO from the start in the model (particles.dat)   *
##   This happens, for example,  when using 5-flavor QCD where     *
##   charm and bottom are treated as partons in the initial state  *
##   and a zero mass might be hardwired in the model definition.   *
##                                                                 *
##       The SUSY decays have calculated using SDECAY 1.1a         *
##                                                                 *
##******************************************************************
#
BLOCK DCINFO  # Decay Program information
     1   SDECAY      # decay calculator
     2   1.1a        # version number
#
BLOCK SPINFO  # Spectrum calculator information
     1   SOFTSUSY    # spectrum calculator                 
     2   2.0.5         # version number                    
#
BLOCK MODSEL  # Model selection
     1     1   sugra
#
BLOCK SMINPUTS  # Standard Model inputs
     1     1.27934000E+02   # alpha_em^-1(M_Z)^MSbar
     2     1.16637000E-05   # G_F [GeV^-2]
     3     1.18000000E-01   # alpha_S(M_Z)^MSbar
     4     9.11876000E+01   # M_Z pole mass
     5     4.25000000E+00   # mb(mb)^MSbar
     6     1.75000000E+02   # mt pole mass
     7     1.77700000E+00   # mtau pole mass
#
BLOCK MINPAR  # Input parameters - minimal models
     1     1.00000000E+02   # m0                  
     2     2.50000000E+02   # m12                 
     3     1.00000000E+01   # tanb                
     4     1.00000000E+00   # sign(mu)            
     5    -1.00000000E+02   # A0                  
#
BLOCK MASS  # Mass Spectrum
# PDG code           mass       particle
   1000022     499.0        # ~chi_10
   1000024     500.0        # ~chi_1+
   1000023     1.0E+06      # ~chi_20
   1000025     1.0E+06      # ~chi_30
   1000035     1.0E+06      # ~chi_40
   1000037     1.0E+06      # ~chi_2+
#
#
#
#                             =================
#                             |The decay table|
#                             =================
#
#         PDG            Width
DECAY   1000024     1.9732e-17  # chargino decay
#          BR         NDA      ID1       ID2
	   1.0        2        1000022   211
"""

import FWCore.ParameterSet.Config as cms

from Configuration.Generator.Pythia8CommonSettings_cfi import *
from Configuration.Generator.Pythia8CUEP8M1Settings_cfi import *


generator = cms.EDFilter("Pythia8GeneratorFilter",
    pythiaPylistVerbosity = cms.untracked.int32(0),
    filterEfficiency = cms.untracked.double(-1),
    pythiaHepMCVerbosity = cms.untracked.bool(False),
    SLHATableForPythia8 = cms.string('%s' % SLHA_TABLE),
    comEnergy = cms.double(COM_ENERGY),
    crossSection = cms.untracked.double(CROSS_SECTION),
    maxEventsToPrint = cms.untracked.int32(0),
    PythiaParameters = cms.PSet(
		 pythia8CommonSettingsBlock,
        pythia8CUEP8M1SettingsBlock,
        processParameters = cms.vstring(
            'Tune:pp  = 5', 
            'SUSY:all = off',
            'SUSY:qqbar2chi+chi- = on', 
            '1000024:tau0 = 3000.',                                        
            'ParticleDecays:tau0Max = 10000',
       ), 
        parameterSets = cms.vstring(
	    'pythia8CommonSettings',
	    'pythia8CUEP8M1Settings',
            'processParameters')
    ),
    # The following parameters are required by Exotica_HSCP_SIM_cfi: 
    slhaFile = cms.untracked.string(''),   # value not used 
    processFile = cms.untracked.string('SimG4Core/CustomPhysics/data/RhadronProcessList.txt'),
    useregge = cms.bool(False),
    hscpFlavor = cms.untracked.string('stau'),
    massPoint = cms.untracked.int32(MCHI),  # value not used
#    particleFile = cms.untracked.string('DisappTrks/SignalMC/data/geant4_AMSB_chargino_%sGeV_ctau%scm.slha' % (MCHI, CTAU))
    particleFile = cms.untracked.string('DisappTrks/SignalMC/data/empty.slha' % (MCHI, CTAU))  
)

ProductionFilterSequence = cms.Sequence(generator)
