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
config.Data.publication = True
config.Data.outputDatasetTag = 'RunIIFall17DRPremix-PU2017_94X_mc2017_realistic_v11-v1_step2'

config.JobType.maxMemoryMB = 8000

# Uncomment one of the following pairs

#config.Data.outLFNDirBase = '/store/group/lpclonglived/DisappTrks/'
#config.Site.storageSite = 'T3_US_FNALLPC'

config.Data.outLFNDirBase = '/store/user/%s/' % (getUsernameFromSiteDB())
config.Site.storageSite = 'T2_US_Purdue'

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

    reallySubmitMass = { x : False for x in range(100, 1200, 100)}
    reallySubmitLifetime = { x : True for x in [1, 10, 100, 1000, 10000]}

    reallySubmitMass[1000] = True
    reallySubmitMass[1100] = True

    step1s = {
        (100,  10000) : '/AMSB_chargino_M-100_CTau-10000_TuneCP5_13TeV_pythia8/bfrancis-RunIIFall17DRPremix-93X_mc2017_realistic_v3-v1-8f30c862a2e310601257f49ed10a37fc/USER',
        (100,  1000)  : '/AMSB_chargino_M-100_CTau-1000_TuneCP5_13TeV_pythia8/bfrancis-RunIIFall17DRPremix-93X_mc2017_realistic_v3-v1-e1d6ba56cf85041ba62142bc939d1bd3/USER',
        (100,  100)   : '/AMSB_chargino_M-100_CTau-100_TuneCP5_13TeV_pythia8/bfrancis-RunIIFall17DRPremix-93X_mc2017_realistic_v3-v1-cf8c30f4b2428110b4761729d3263260/USER',
        (100,  10)    : '/AMSB_chargino_M-100_CTau-10_TuneCP5_13TeV_pythia8/bfrancis-RunIIFall17DRPremix-93X_mc2017_realistic_v3-v1-e5b2f34dae25faba8e4e28bb411dc9e5/USER',
        (100,  1)     : '/AMSB_chargino_M-100_CTau-1_TuneCP5_13TeV_pythia8/bfrancis-RunIIFall17DRPremix-93X_mc2017_realistic_v3-v1-eb31ee302755b27df62e11e274dc3008/USER',
        (200,  10000) : "/AMSB_chargino_M-200_CTau-10000_TuneCP5_13TeV_pythia8/ahart-RunIIFall17DRPremix-93X_mc2017_realistic_v3-v1-9ad4861888de96dd9d73af421a9bf5e2/USER",
        (200,  1000)  : "/AMSB_chargino_M-200_CTau-1000_TuneCP5_13TeV_pythia8/ahart-RunIIFall17DRPremix-93X_mc2017_realistic_v3-v1-559f98139024a3580d1321903829bd3b/USER",
        (200,  100)   : "/AMSB_chargino_M-200_CTau-100_TuneCP5_13TeV_pythia8/ahart-RunIIFall17DRPremix-93X_mc2017_realistic_v3-v1-1a60df69c9471a7d0384c815556f4aba/USER",
        (200,  10)    : "/AMSB_chargino_M-200_CTau-10_TuneCP5_13TeV_pythia8/ahart-RunIIFall17DRPremix-93X_mc2017_realistic_v3-v1-a0b84f3f7eef20df7b84ac8edbd03a0d/USER",
        (200,  1)     : "/AMSB_chargino_M-200_CTau-1_TuneCP5_13TeV_pythia8/ahart-RunIIFall17DRPremix-93X_mc2017_realistic_v3-v1-92b3dfa0c3d7cc063345e14b1e40e5d2/USER",
        (300,  10000) : '/AMSB_chargino_M-300_CTau-10000_TuneCP5_13TeV_pythia8/bfrancis-RunIIFall17DRPremix-93X_mc2017_realistic_v3-v1-f5807fd0e196055641b7ddc6ceace6ca/USER',
        (300,  1000)  : '/AMSB_chargino_M-300_CTau-1000_TuneCP5_13TeV_pythia8/bfrancis-RunIIFall17DRPremix-93X_mc2017_realistic_v3-v1-b250cec959e00399c40030d54e2425cf/USER',
        (300,  100)   : '/AMSB_chargino_M-300_CTau-100_TuneCP5_13TeV_pythia8/bfrancis-RunIIFall17DRPremix-93X_mc2017_realistic_v3-v1-7500d92349ee3da0a2ff20a9d55b5357/USER',
        (300,  10)    : '/AMSB_chargino_M-300_CTau-10_TuneCP5_13TeV_pythia8/bfrancis-RunIIFall17DRPremix-93X_mc2017_realistic_v3-v1-ad4ede569870d70dfe1ff30ad78a738d/USER',
        (300,  1)     : '/AMSB_chargino_M-300_CTau-1_TuneCP5_13TeV_pythia8/bfrancis-RunIIFall17DRPremix-93X_mc2017_realistic_v3-v1-739a9417e172ca83f46c34f8d36a4673/USER',
        (400,  10000) : "/AMSB_chargino_M-400_CTau-10000_TuneCP5_13TeV_pythia8/ahart-RunIIFall17DRPremix-93X_mc2017_realistic_v3-v1-6af8ec28324a53ac1246bc9fb9d6a2f8/USER",
        (400,  1000)  : "/AMSB_chargino_M-400_CTau-1000_TuneCP5_13TeV_pythia8/ahart-RunIIFall17DRPremix-93X_mc2017_realistic_v3-v1-07137fafe5bee6c94dc0be21276283d5/USER",
        (400,  100)   : "/AMSB_chargino_M-400_CTau-100_TuneCP5_13TeV_pythia8/ahart-RunIIFall17DRPremix-93X_mc2017_realistic_v3-v1-7eafcdf70819ad77581968f99cefd0e6/USER",
        (400,  10)    : "/AMSB_chargino_M-400_CTau-10_TuneCP5_13TeV_pythia8/ahart-RunIIFall17DRPremix-93X_mc2017_realistic_v3-v1-140b3fc4fabfc6eb228939c1563565b2/USER",
        (400,  1)     : "/AMSB_chargino_M-400_CTau-1_TuneCP5_13TeV_pythia8/ahart-RunIIFall17DRPremix-93X_mc2017_realistic_v3-v1-decc465faecc7f317065a80154bc7555/USER",
        (500,  10000) : '/AMSB_chargino_M-500_CTau-10000_TuneCP5_13TeV_pythia8/bfrancis-RunIIFall17DRPremix-93X_mc2017_realistic_v3-v1-096b5dbf79c2c9168492febd40a0f73d/USER',
        (500,  1000)  : '/AMSB_chargino_M-500_CTau-1000_TuneCP5_13TeV_pythia8/bfrancis-RunIIFall17DRPremix-93X_mc2017_realistic_v3-v1-8fe6d8ade01a794f50c1b0cce9bad36f/USER',
        (500,  100)   : '/AMSB_chargino_M-500_CTau-100_TuneCP5_13TeV_pythia8/bfrancis-RunIIFall17DRPremix-93X_mc2017_realistic_v3-v1-4017d9883ff47786d440f4a736ab941f/USER',
        (500,  10)    : '/AMSB_chargino_M-500_CTau-10_TuneCP5_13TeV_pythia8/bfrancis-RunIIFall17DRPremix-93X_mc2017_realistic_v3-v1-db560f62f49a378a2f16ee3655686b42/USER',
        (500,  1)     : '/AMSB_chargino_M-500_CTau-1_TuneCP5_13TeV_pythia8/bfrancis-RunIIFall17DRPremix-93X_mc2017_realistic_v3-v1-c0e28f39920d65f24a46019fff52a708/USER',
        (600,  10000) : "/AMSB_chargino_M-600_CTau-10000_TuneCP5_13TeV_pythia8/ahart-RunIIFall17DRPremix-93X_mc2017_realistic_v3-v1-04dab7e8194d493f2997656d5c152c56/USER",
        (600,  1000)  : "/AMSB_chargino_M-600_CTau-1000_TuneCP5_13TeV_pythia8/ahart-RunIIFall17DRPremix-93X_mc2017_realistic_v3-v1-6b0a69faea53cf67116fe7a01c934f5d/USER",
        (600,  100)   : "/AMSB_chargino_M-600_CTau-100_TuneCP5_13TeV_pythia8/ahart-RunIIFall17DRPremix-93X_mc2017_realistic_v3-v1-6e71d3bd813ab3dcf7b9d1f0d350cd47/USER",
        (600,  10)    : "/AMSB_chargino_M-600_CTau-10_TuneCP5_13TeV_pythia8/ahart-RunIIFall17DRPremix-93X_mc2017_realistic_v3-v1-1de02c2fd139009e4ede1c745c02b544/USER",
        (600,  1)     : "/AMSB_chargino_M-600_CTau-1_TuneCP5_13TeV_pythia8/ahart-RunIIFall17DRPremix-93X_mc2017_realistic_v3-v1-edfcf393832b582f203487438997e719/USER",
        (700,  10000) : '/AMSB_chargino_M-700_CTau-10000_TuneCP5_13TeV_pythia8/bfrancis-RunIIFall17DRPremix-93X_mc2017_realistic_v3-v1-9a4ea3d8f8ee9761e77ae2f0c0f63909/USER',
        (700,  1000)  : '/AMSB_chargino_M-700_CTau-1000_TuneCP5_13TeV_pythia8/bfrancis-RunIIFall17DRPremix-93X_mc2017_realistic_v3-v1-0797f6d8753af63b969b9d5e6fc16707/USER',
        (700,  100)   : '/AMSB_chargino_M-700_CTau-100_TuneCP5_13TeV_pythia8/bfrancis-RunIIFall17DRPremix-93X_mc2017_realistic_v3-v1-9ea4b8af9527196a42626e98645b1414/USER',
        (700,  10)    : '/AMSB_chargino_M-700_CTau-10_TuneCP5_13TeV_pythia8/bfrancis-RunIIFall17DRPremix-93X_mc2017_realistic_v3-v1-fc414e5445e2eed6f619d86d0a447611/USER',
        (700,  1)     : '/AMSB_chargino_M-700_CTau-1_TuneCP5_13TeV_pythia8/bfrancis-RunIIFall17DRPremix-93X_mc2017_realistic_v3-v1-7cfe42c01da68083fb1199321791773a/USER',
        (800,  10000) : "/AMSB_chargino_M-800_CTau-10000_TuneCP5_13TeV_pythia8/ahart-RunIIFall17DRPremix-93X_mc2017_realistic_v3-v1-c3b8d366f86e2eb10ae3d66098d0838d/USER",
        (800,  1000)  : "/AMSB_chargino_M-800_CTau-1000_TuneCP5_13TeV_pythia8/ahart-RunIIFall17DRPremix-93X_mc2017_realistic_v3-v1-5c576dff88f6c39fe2dc77e9551eb6f1/USER",
        (800,  100)   : "/AMSB_chargino_M-800_CTau-100_TuneCP5_13TeV_pythia8/ahart-RunIIFall17DRPremix-93X_mc2017_realistic_v3-v1-41fb787a4ea33568cfdaa5d64c7bcf57/USER",
        (800,  10)    : "/AMSB_chargino_M-800_CTau-10_TuneCP5_13TeV_pythia8/ahart-RunIIFall17DRPremix-93X_mc2017_realistic_v3-v1-1b340a6e1c58337f1c23be88760a548f/USER",
        (800,  1)     : "/AMSB_chargino_M-800_CTau-1_TuneCP5_13TeV_pythia8/ahart-RunIIFall17DRPremix-93X_mc2017_realistic_v3-v1-575f0ef3ad654b4b85f9c377bc83dfa5/USER",
        (900,  10000) : '/AMSB_chargino_M-900_CTau-10000_TuneCP5_13TeV_pythia8/bfrancis-RunIIFall17DRPremix-93X_mc2017_realistic_v3-v1-7438a1535b27efa6fa461f8774add27d/USER',
        (900,  1000)  : '/AMSB_chargino_M-900_CTau-1000_TuneCP5_13TeV_pythia8/bfrancis-RunIIFall17DRPremix-93X_mc2017_realistic_v3-v1-ea0d1d54843ac199026b3395cc649bb2/USER',
        (900,  100)   : '/AMSB_chargino_M-900_CTau-100_TuneCP5_13TeV_pythia8/bfrancis-RunIIFall17DRPremix-93X_mc2017_realistic_v3-v1-17bd959458bf0d14310d8019ecee8fe9/USER',
        (900,  10)    : '/AMSB_chargino_M-900_CTau-10_TuneCP5_13TeV_pythia8/bfrancis-RunIIFall17DRPremix-93X_mc2017_realistic_v3-v1-c35d7d3bd4588b6e8ea988ca69280e24/USER',
        (900,  1)     : '/AMSB_chargino_M-900_CTau-1_TuneCP5_13TeV_pythia8/bfrancis-RunIIFall17DRPremix-93X_mc2017_realistic_v3-v1-49a412556abb89fc7f5ed91849940397/USER',
        (1000, 10000) : '/AMSB_chargino_M-1000_CTau-10000_TuneCP5_13TeV_pythia8/ahart-RunIIFall17DRPremix-93X_mc2017_realistic_v3-v1-bf6422b9b821a9e33008b55cdc44a13e/USER',
        (1000, 1000)  : '/AMSB_chargino_M-1000_CTau-1000_TuneCP5_13TeV_pythia8/ahart-RunIIFall17DRPremix-93X_mc2017_realistic_v3-v1-939e827078d4dd8af0c9babdf0836f0a/USER',
        (1000, 100)   : '/AMSB_chargino_M-1000_CTau-100_TuneCP5_13TeV_pythia8/ahart-RunIIFall17DRPremix-93X_mc2017_realistic_v3-v1-fe7de942de122c0adb5ea222376584a1/USER',
        (1000, 10)    : '/AMSB_chargino_M-1000_CTau-10_TuneCP5_13TeV_pythia8/ahart-RunIIFall17DRPremix-93X_mc2017_realistic_v3-v1-acfd3c20b49760794fc7a59fe0af0dd0/USER',
        (1000, 1)     : '/AMSB_chargino_M-1000_CTau-1_TuneCP5_13TeV_pythia8/ahart-RunIIFall17DRPremix-93X_mc2017_realistic_v3-v1-6478be0300e36a854e3019fec4be815c/USER',
        (1100, 10000) : '/AMSB_chargino_M-1100_CTau-10000_TuneCP5_13TeV_pythia8/ahart-RunIIFall17DRPremix-93X_mc2017_realistic_v3-v1-aadfe16393e50a0b40908618d3ebc50b/USER',
        (1100, 1000)  : '/AMSB_chargino_M-1100_CTau-1000_TuneCP5_13TeV_pythia8/ahart-RunIIFall17DRPremix-93X_mc2017_realistic_v3-v1-5c409922a8cae824b30982929627b7c2/USER',
        (1100, 100)   : '/AMSB_chargino_M-1100_CTau-100_TuneCP5_13TeV_pythia8/ahart-RunIIFall17DRPremix-93X_mc2017_realistic_v3-v1-f11d01cd28da8fd3d1e6e5a0a6e7c0fe/USER',
        (1100, 10)    : '/AMSB_chargino_M-1100_CTau-10_TuneCP5_13TeV_pythia8/ahart-RunIIFall17DRPremix-93X_mc2017_realistic_v3-v1-372921df8b2b39431618b367ec88edbc/USER',
        (1100, 1)     : '/AMSB_chargino_M-1100_CTau-1_TuneCP5_13TeV_pythia8/ahart-RunIIFall17DRPremix-93X_mc2017_realistic_v3-v1-5d316b20c9e189c01bcaf037f3f34353/USER',
    }

    for mass in range(100, 1200, 100):
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
