##########The script used to generate cff cards for EWK chargino step1 production
#! /usr/bin/python
import sys
import os

masses = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000, 1100]
lifetimes = [10, 100, 1000, 10000, 100000]

PATH_OUT = os.environ.get('CMSSW_BASE') + '/src/DisappTrks/SignalMC/python/pythia8GeantDecay/'
PATH_SLHA = os.environ.get('CMSSW_BASE') + '/src/DisappTrks/SignalMC/data/SLHA/'

for mass in masses:
  for lifetime in lifetimes:
    FILE_out  = 'AMSB_chargino' + str(mass) + 'GeV_ctau' + str(lifetime/10) + 'cm_NoFilter_13TeV.py'
    SLHA_file = 'AMSB_chargino_' + str(mass) + 'GeV_Isajet780.slha'
  
    fin  = open( PATH_SLHA + SLHA_file, "r" )
    fout = open( PATH_OUT  + FILE_out , "w" )
    
    fout.write('''
COM_ENERGY = 13000.
CROSS_SECTION = 1.0
MCHI = %s  # GeV
CTAU = %s  # mm
''' %(mass,lifetime))
    fout.write('SLHA_TABLE="""\n')

    slhalines = fin.readlines()
    for lines in slhalines:
      fout.write(lines)
    fout.write('"""')

    fout.write('''
import FWCore.ParameterSet.Config as cms

from Configuration.Generator.Pythia8CommonSettings_cfi import *
from Configuration.Generator.MCTunes2017.PythiaCP5Settings_cfi import *

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
      pythia8CP5SettingsBlock,
      processParameters = cms.vstring(
        'SUSY:all = off',
        'SUSY:qqbar2chi+chi- = on',
        'SUSY:qqbar2chi+-chi0 = on',
        '1000024:mayDecay = false',
        '-1000024:mayDecay = false',
      ),
      parameterSets = cms.vstring(
        'pythia8CommonSettings',
        'pythia8CP5Settings',
        'processParameters',
      )
  ),
  # The following parameters are required by Exotica_HSCP_SIM_cfi:
  slhaFile = cms.untracked.string(''),   # value not used
  processFile = cms.untracked.string('SimG4Core/CustomPhysics/data/RhadronProcessList.txt'),
  useregge = cms.bool(False),
  hscpFlavor = cms.untracked.string('stau'),
  massPoint = cms.untracked.int32(MCHI),  # value not used
  particleFile = cms.untracked.string('DisappTrks/SignalMC/data/geant4/geant4_AMSB_chargino_%sGeV_ctau%scm.slha' % (MCHI, CTAU/10))
)

ProductionFilterSequence = cms.Sequence(generator)

''')
    fout.close()
    print FILE_out + " has been generated\n"

   

    

