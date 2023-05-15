#!/usr/bin/env python3

import os
from CRABClient.UserUtilities import config #, getUsernameFromSiteDB
config = config()

config.General.requestName = ''
config.General.workArea = 'crab'
config.General.transferOutputs = True
config.General.transferLogs = True

config.JobType.pluginName = 'PrivateMC'
config.JobType.psetName = ''
config.JobType.allowUndistributedCMSSW = True

config.Data.outputPrimaryDataset = ''
config.Data.splitting = 'EventBased'
config.Data.unitsPerJob = 100
NJOBS = 100  # This is not a configuration parameter, but an auxiliary variable that we use in the next line.
config.Data.totalUnits = config.Data.unitsPerJob * NJOBS
config.Data.publication = True
config.Data.outputDatasetTag = 'Run3Winter21DRMiniAOD-FlatPU20to70_112X_mcRun3_2021_realistic_v15'

# Uncomment one of the following pairs

#config.Data.outLFNDirBase = '/store/group/lpclonglived/DisappTrks/'
#config.Site.storageSite = 'T3_US_FNALLPC'

#config.Data.outLFNDirBase = '/store/user/%s/' % (getUsernameFromSiteDB())
#config.Site.storageSite = 'T2_US_Purdue'

#config.Data.outLFNDirBase = '/store/group/phys_exotica/disappearingTracks/'
#config.Site.storageSite = 'T2_CH_CERN'

if __name__ == '__main__':

    from CRABAPI.RawCommand import crabCommand
    from CRABClient.ClientExceptions import ClientException
    from httplib import HTTPException
    from multiprocessing import Process

    def submit(config):
        try:
            crabCommand('submit', config = config)
        except HTTPException as hte:
            print "Failed submitting task: %s" % (hte.headers)
        except ClientException as cle:
            print "Failed submitting task: %s" % (cle)

    def forkAndSubmit(config):
        p = Process(target=submit, args=(config,))
        p.start()
        p.join()

    #############################################################################################
    ## From now on that's what users should modify: this is the a-la-CRAB2 configuration part. ##
    #############################################################################################

    reallySubmitEWK = False
    reallySubmitStrong = False
    reallySubmitHiggsinoEWK = False

    reallySubmitMass = { x : False for x in range(100, 1200, 100)}
    reallySubmitGluinoMass = { x : False for x in range(700, 2300, 100)}
    reallySubmitLifetime = { x : False for x in [1, 10, 100, 1000, 10000]}
    numJobsPerLifetime = { x : (2500 if x == 10000 else 500) for x in [1, 10, 100, 1000, 10000]}
    numJobsPerLifetimeForStrong = {
        10    : 800,
        100   : 50,
        1000  : 200,
        10000 : 2000
    }

    if reallySubmitEWK:
      for mass in range(100, 1200, 100):
          for ctau in [1, 10, 100, 1000, 10000]:
              config.General.requestName = 'AMSB_chargino%dGeV_ctau%dcm_step1' % (mass, ctau)
              config.JobType.psetName = 'step1/pythia8/AMSB_chargino_M-%dGeV_CTau-%dcm_TuneCP5_PSweights_14TeV_pythia8_step1.py' % (mass, ctau)
              config.Data.outputPrimaryDataset = 'AMSB_chargino_M-%dGeV_CTau-%dcm_TuneCP5_PSweights_14TeV_pythia8' % (mass, ctau)
              config.Data.totalUnits = config.Data.unitsPerJob * numJobsPerLifetime[ctau]
              if reallySubmitMass[mass] and reallySubmitLifetime[ctau]:
                  forkAndSubmit(config)
              else:
                  print 'Skipping submission of request:', config.General.requestName
    elif reallySubmitStrong:
      for mass in range(100, 1000, 100):
          for gluinoMass in range(700, 2300, 100):
              for ctau in [10, 100, 1000, 10000]:
                  config.General.requestName = 'AMSB_gluino%dGeVToChargino%dGeV_ctau%dcm_step1' % (gluinoMass, mass, ctau)
                  config.JobType.psetName = 'step1/pythia8/AMSB_gluinoToChargino_M-%dGeV_M-%dGeV_CTau-%dcm_step1.py' % (gluinoMass, mass, ctau)
                  config.Data.outputPrimaryDataset = 'AMSB_gluinoToChargino_M-%d_M-%d_CTau-%d_TuneCP5_14TeV_pythia8' % (gluinoMass, mass, ctau)
                  config.Data.totalUnits = config.Data.unitsPerJob * numJobsPerLifetimeForStrong[ctau]
                  if reallySubmitMass[mass] and reallySubmitGluinoMass[gluinoMass] and reallySubmitLifetime[ctau]:
                      if os.path.isfile(config.JobType.psetName):
                          forkAndSubmit(config)
                  else:
                      print 'Skipping submission of request:', config.General.requestName
    elif reallySubmitHiggsinoEWK:
      for mass in range(100, 1000, 100):
          for ctau in [1, 10, 100, 1000, 10000]:
              config.General.requestName = 'Higgsino%dGeV_ctau%dcm_step1' % (mass, ctau)
              config.JobType.psetName = 'step1/pythia8/Higgsino_M-%dGeV_ctau%dcm_TuneCP5_PSweights_14TeV_pythia8_step1.py' % (mass, ctau)
              config.Data.outputPrimaryDataset = 'Higgsino_M-%dGeV_CTau-%dcm_TuneCP5_PSweights_14TeV_pythia8' % (mass, ctau)
              config.Data.totalUnits = config.Data.unitsPerJob * numJobsPerLifetime[ctau]
              if reallySubmitMass[mass] and reallySubmitLifetime[ctau]:
                  forkAndSubmit(config)
              else:
                  print 'Skipping submission of request:', config.General.requestName
