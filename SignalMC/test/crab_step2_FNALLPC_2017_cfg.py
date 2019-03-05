#!/usr/bin/env python

from CRABClient.UserUtilities import config, getUsernameFromSiteDB
config = config()

config.General.requestName = ''
config.General.workArea = 'crab'
config.General.transferOutputs = True
config.General.transferLogs = True

config.JobType.pluginName = 'Analysis'
config.JobType.psetName = 'step2/AMSB_chargino_step2_2017_cfg.py'
config.JobType.numCores = 4

config.Data.inputDataset = ''
config.Data.useParent = False
config.Data.inputDBS = 'phys03'
config.Data.splitting = 'LumiBased'
config.Data.unitsPerJob = 1
config.Data.outLFNDirBase = '/store/group/lpclonglived/DisappTrks/'
config.Data.publication = True
config.Data.outputDatasetTag = 'RunIIFall17DRPremix-PU2017_94X_mc2017_realistic_v11-v1_step2'

config.Site.storageSite = 'T3_US_FNALLPC'

config.JobType.maxMemoryMB = 8000

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

    reallySubmitMass = { x : False for x in range(100, 1000, 100)}
    reallySubmitLifetime = { x : False for x in [1, 10, 100, 1000, 10000]}

    step1s = {
        (100, 10000) : '/AMSB_chargino_M-100_CTau-10000_TuneCP5_13TeV_pythia8/bfrancis-RunIIFall17DRPremix-93X_mc2017_realistic_v3-v1-8f30c862a2e310601257f49ed10a37fc/USER',
        (100, 1000)  : '/AMSB_chargino_M-100_CTau-1000_TuneCP5_13TeV_pythia8/bfrancis-RunIIFall17DRPremix-93X_mc2017_realistic_v3-v1-e1d6ba56cf85041ba62142bc939d1bd3/USER',
        (100, 100)   : '/AMSB_chargino_M-100_CTau-100_TuneCP5_13TeV_pythia8/bfrancis-RunIIFall17DRPremix-93X_mc2017_realistic_v3-v1-cf8c30f4b2428110b4761729d3263260/USER',
        (100, 10)    : '/AMSB_chargino_M-100_CTau-10_TuneCP5_13TeV_pythia8/bfrancis-RunIIFall17DRPremix-93X_mc2017_realistic_v3-v1-e5b2f34dae25faba8e4e28bb411dc9e5/USER',
        (100, 1)     : '/AMSB_chargino_M-100_CTau-1_TuneCP5_13TeV_pythia8/bfrancis-RunIIFall17DRPremix-93X_mc2017_realistic_v3-v1-eb31ee302755b27df62e11e274dc3008/USER',
        (300, 10000) : '/AMSB_chargino_M-300_CTau-10000_TuneCP5_13TeV_pythia8/bfrancis-RunIIFall17DRPremix-93X_mc2017_realistic_v3-v1-f5807fd0e196055641b7ddc6ceace6ca/USER',
        (300, 1000)  : '/AMSB_chargino_M-300_CTau-1000_TuneCP5_13TeV_pythia8/bfrancis-RunIIFall17DRPremix-93X_mc2017_realistic_v3-v1-b250cec959e00399c40030d54e2425cf/USER',
        (300, 100)   : '/AMSB_chargino_M-300_CTau-100_TuneCP5_13TeV_pythia8/bfrancis-RunIIFall17DRPremix-93X_mc2017_realistic_v3-v1-7500d92349ee3da0a2ff20a9d55b5357/USER',
        (300, 10)    : '/AMSB_chargino_M-300_CTau-10_TuneCP5_13TeV_pythia8/bfrancis-RunIIFall17DRPremix-93X_mc2017_realistic_v3-v1-ad4ede569870d70dfe1ff30ad78a738d/USER',
        (300, 1)     : '/AMSB_chargino_M-300_CTau-1_TuneCP5_13TeV_pythia8/bfrancis-RunIIFall17DRPremix-93X_mc2017_realistic_v3-v1-739a9417e172ca83f46c34f8d36a4673/USER',
        (500, 10000) : '/AMSB_chargino_M-500_CTau-10000_TuneCP5_13TeV_pythia8/bfrancis-RunIIFall17DRPremix-93X_mc2017_realistic_v3-v1-096b5dbf79c2c9168492febd40a0f73d/USER',
        (500, 1000)  : '/AMSB_chargino_M-500_CTau-1000_TuneCP5_13TeV_pythia8/bfrancis-RunIIFall17DRPremix-93X_mc2017_realistic_v3-v1-8fe6d8ade01a794f50c1b0cce9bad36f/USER',
        (500, 100)   : '/AMSB_chargino_M-500_CTau-100_TuneCP5_13TeV_pythia8/bfrancis-RunIIFall17DRPremix-93X_mc2017_realistic_v3-v1-4017d9883ff47786d440f4a736ab941f/USER',
        (500, 10)    : '/AMSB_chargino_M-500_CTau-10_TuneCP5_13TeV_pythia8/bfrancis-RunIIFall17DRPremix-93X_mc2017_realistic_v3-v1-db560f62f49a378a2f16ee3655686b42/USER',
        (500, 1)     : '/AMSB_chargino_M-500_CTau-1_TuneCP5_13TeV_pythia8/bfrancis-RunIIFall17DRPremix-93X_mc2017_realistic_v3-v1-c0e28f39920d65f24a46019fff52a708/USER',
        (700, 10000) : '/AMSB_chargino_M-700_CTau-10000_TuneCP5_13TeV_pythia8/bfrancis-RunIIFall17DRPremix-93X_mc2017_realistic_v3-v1-9a4ea3d8f8ee9761e77ae2f0c0f63909/USER',
        (700, 1000)  : '/AMSB_chargino_M-700_CTau-1000_TuneCP5_13TeV_pythia8/bfrancis-RunIIFall17DRPremix-93X_mc2017_realistic_v3-v1-0797f6d8753af63b969b9d5e6fc16707/USER',
        (700, 100)   : '/AMSB_chargino_M-700_CTau-100_TuneCP5_13TeV_pythia8/bfrancis-RunIIFall17DRPremix-93X_mc2017_realistic_v3-v1-9ea4b8af9527196a42626e98645b1414/USER',
        (700, 10)    : '/AMSB_chargino_M-700_CTau-10_TuneCP5_13TeV_pythia8/bfrancis-RunIIFall17DRPremix-93X_mc2017_realistic_v3-v1-fc414e5445e2eed6f619d86d0a447611/USER',
        (700, 1)     : '/AMSB_chargino_M-700_CTau-1_TuneCP5_13TeV_pythia8/bfrancis-RunIIFall17DRPremix-93X_mc2017_realistic_v3-v1-7cfe42c01da68083fb1199321791773a/USER',
        (900, 10000) : '/AMSB_chargino_M-900_CTau-10000_TuneCP5_13TeV_pythia8/bfrancis-RunIIFall17DRPremix-93X_mc2017_realistic_v3-v1-7438a1535b27efa6fa461f8774add27d/USER',
        (900, 1000)  : '/AMSB_chargino_M-900_CTau-1000_TuneCP5_13TeV_pythia8/bfrancis-RunIIFall17DRPremix-93X_mc2017_realistic_v3-v1-ea0d1d54843ac199026b3395cc649bb2/USER',
        (900, 100)   : '/AMSB_chargino_M-900_CTau-100_TuneCP5_13TeV_pythia8/bfrancis-RunIIFall17DRPremix-93X_mc2017_realistic_v3-v1-17bd959458bf0d14310d8019ecee8fe9/USER',
        (900, 10)    : '/AMSB_chargino_M-900_CTau-10_TuneCP5_13TeV_pythia8/bfrancis-RunIIFall17DRPremix-93X_mc2017_realistic_v3-v1-c35d7d3bd4588b6e8ea988ca69280e24/USER',
        (900, 1)     : '/AMSB_chargino_M-900_CTau-1_TuneCP5_13TeV_pythia8/bfrancis-RunIIFall17DRPremix-93X_mc2017_realistic_v3-v1-49a412556abb89fc7f5ed91849940397/USER',
        (1000, 10000): '/AMSB_chargino_M-1000_CTau-10000_TuneCP5_13TeV_pythia8/kwei-RunIIFall17DRPremix-93X_mc2017_realistic_v3-v1-afec53a3f60a40f78d0da7ec56780075/USER',
        (1000, 1000) : '/AMSB_chargino_M-1000_CTau-1000_TuneCP5_13TeV_pythia8/kwei-RunIIFall17DRPremix-93X_mc2017_realistic_v3-v1-b06d7b090876be221c6ec2e3d02c2e38/USER',
        (1000, 100)  : '/AMSB_chargino_M-1000_CTau-100_TuneCP5_13TeV_pythia8/kwei-RunIIFall17DRPremix-93X_mc2017_realistic_v3-v1-9e634ecfee9926e0e6d1d25bf0c79b2a/USER',
        (1000, 10)   : '/AMSB_chargino_M-1000_CTau-10_TuneCP5_13TeV_pythia8/kwei-RunIIFall17DRPremix-93X_mc2017_realistic_v3-v1-05363df24a1ae49ec61c8114f642d1ef/USER',
        (1000, 1)    : '/AMSB_chargino_M-1000_CTau-1_TuneCP5_13TeV_pythia8/kwei-RunIIFall17DRPremix-93X_mc2017_realistic_v3-v1-5ac1b9ea78c792d1d09583a28a0a511c/USER',
        (1100, 10000): '/AMSB_chargino_M-1100_CTau-10000_TuneCP5_13TeV_pythia8/kwei-RunIIFall17DRPremix-93X_mc2017_realistic_v3-v1-dcf138a33bb2f64973758fda0cce82e1/USER',
        (1100, 1000) : '/AMSB_chargino_M-1100_CTau-1000_TuneCP5_13TeV_pythia8/kwei-RunIIFall17DRPremix-93X_mc2017_realistic_v3-v1-8d48e22b97b49dd4c2e89020f0dd3465/USER',
        (1100, 100)  : '/AMSB_chargino_M-1100_CTau-100_TuneCP5_13TeV_pythia8/kwei-RunIIFall17DRPremix-93X_mc2017_realistic_v3-v1-dfcf3596e186e8fc030e8c726258b3c6/USER',
        (1100, 10)   : '/AMSB_chargino_M-1100_CTau-10_TuneCP5_13TeV_pythia8/kwei-RunIIFall17DRPremix-93X_mc2017_realistic_v3-v1-a3c684656432f6ff2fb765404b0e4510/USER',
        (1100, 1)    : '/AMSB_chargino_M-1100_CTau-1_TuneCP5_13TeV_pythia8/kwei-RunIIFall17DRPremix-93X_mc2017_realistic_v3-v1-aa9a6833cd67adc214279fc63d70a353/USER',
    }

    for mass in range(1000, 1200, 100):
        for ctau in [1, 10, 100, 1000, 10000]:
            if not (mass, ctau) in step1s:
                print 'Skipping (%d GeV, %d cm)' % (mass, ctau)
                continue
            config.General.requestName = 'AMSB_chargino%dGeV_ctau%dcm_step2' % (mass, ctau)
            config.Data.inputDataset = step1s[(mass, ctau)]
            if reallySubmitMass[mass] and reallySubmitLifetime[ctau]:
                forkAndSubmit(config)
            else:
                print 'Skipping submission of request:', config.General.requestName
