from CRABClient.UserUtilities import config, getUsernameFromSiteDB
config = config()

iteration = 9  # change by hand for different job submission  
isMC = True

# Common settings for all jobs  
config.General.workArea = 'crab_projects'
config.General.transferOutputs = True
config.General.transferLogs = True
config.JobType.pluginName = 'Analysis'
config.Data.inputDBS = 'global'
config.Data.splitting = 'FileBased'
config.Data.unitsPerJob = 1
config.Data.outLFNDirBase = '/store/user/%s/' % (getUsernameFromSiteDB())
config.Data.publication = True
config.Site.storageSite = 'T3_US_OSU'  

# Adjust settings for each iteration
if iteration == 0:
    config.General.requestName = 'step4_MC_onefile'
    config.Data.useParent = False
    config.Data.inputDataset   = '/WJetsToLNu_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISpring15DR74-Asympt25ns_MCRUN2_74_V9-v1/AODSIM' 
    config.Data.publishDataName = 'WJetsToLNu_TuneCUETP8M1_13TeV-madgraphMLM-pythia8_RunIISpring15DR74-Asympt25ns_MCRUN2_74_V9-v1_ExtendedMiniAOD_onefile'
elif iteration == 1:
    config.General.requestName = 'step4_MC_twofiles' 
    config.Data.useParent = True
    config.Data.inputDataset   = '/WJetsToLNu_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISpring15DR74-Asympt25ns_MCRUN2_74_V9-v1/MINIAODSIM' 
    config.Data.publishDataName = 'WJetsToLNu_TuneCUETP8M1_13TeV-madgraphMLM-pythia8_RunIISpring15DR74-Asympt25ns_MCRUN2_74_V9-v1_ExtendedMiniAOD_onefile'
elif iteration == 2:
    config.General.requestName = 'WJets_HT-2500ToInf_onefile' 
    config.Data.useParent = False
    config.Data.inputDataset   = '/WJetsToLNu_HT-2500ToInf_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISpring15DR74-Asympt25ns_MCRUN2_74_V9-v2/AODSIM' 
    config.Data.publishDataName = 'WJetsToLNu_HT-2500ToInf_TuneCUETP8M1_13TeV-madgraphMLM-pythia8_RunIISpring15DR74-Asympt25ns_MCRUN2_74_V9-v2_MiniAODExt_onefile' 
elif iteration == 3:
    config.General.requestName = 'WJets_HT-2500ToInf_twofiles' 
    config.Data.useParent = True
    config.Data.inputDataset   = '/WJetsToLNu_HT-2500ToInf_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISpring15DR74-Asympt25ns_MCRUN2_74_V9-v2/MINIAODSIM' 
    config.Data.publishDataName = 'WJetsToLNu_HT-2500ToInf_TuneCUETP8M1_13TeV-madgraphMLM-pythia8_RunIISpring15DR74-Asympt25ns_MCRUN2_74_V9-v2_MiniAODExt_twofiles'
elif iteration == 4:
    config.General.requestName = 'WJets_HT-1200To2500_onefile' 
    config.Data.useParent = False
    config.Data.inputDataset   = '/WJetsToLNu_HT-1200To2500_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISpring15DR74-Asympt25ns_MCRUN2_74_V9-v1/AODSIM'
    config.Data.publishDataName = 'WJetsToLNu_HT-1200To2500_TuneCUETP8M1_13TeV-madgraphMLM-pythia8_RunIISpring15DR74-Asympt25ns_MCRUN2_74_V9-v1_MiniAODExt_onefile'
elif iteration == 5:
    config.General.requestName = 'WJets_HT-1200To2500_twofiles' 
    config.Data.useParent = True
    config.Data.inputDataset   = '/WJetsToLNu_HT-1200To2500_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISpring15DR74-Asympt25ns_MCRUN2_74_V9-v1/MINIAODSIM'
    config.Data.publishDataName = 'WJetsToLNu_HT-1200To2500_TuneCUETP8M1_13TeV-madgraphMLM-pythia8_RunIISpring15DR74-Asympt25ns_MCRUN2_74_V9-v1_MiniAODExt_twofiles'
elif iteration == 6:
    config.General.requestName = 'ZJetsToNuNu_HT-600ToInf_onefile' 
    config.Data.useParent = False
    config.Data.inputDataset   = '/ZJetsToNuNu_HT-600ToInf_13TeV-madgraph/RunIISpring15DR74-Asympt25ns_MCRUN2_74_V9-v1/AODSIM'
    config.Data.publishDataName = 'ZJetsToNuNu_HT-600ToInf_13TeV-madgraph_RunIISpring15DR74-Asympt25ns_MCRUN2_74_V9-v1_MiniAODExt_onefile'
elif iteration == 7:
    config.General.requestName = 'ZJetsToNuNu_HT-600ToInf_twofiles' 
    config.Data.useParent = True
    config.Data.inputDataset   = '/ZJetsToNuNu_HT-600ToInf_13TeV-madgraph/RunIISpring15DR74-Asympt25ns_MCRUN2_74_V9-v1/MINIAODSIM'
    config.Data.publishDataName = 'ZJetsToNuNu_HT-600ToInf_13TeV-madgraph_RunIISpring15DR74-Asympt25ns_MCRUN2_74_V9-v1_MiniAODExt_twofiles'
elif iteration == 8:
    config.General.requestName = 'WGToLNuG_PtG-500_onefile' 
    config.Data.useParent = False
    config.Data.inputDataset   = '/WGToLNuG_PtG-500_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISpring15DR74-Asympt25ns_MCRUN2_74_V9-v1/AODSIM'
    config.Data.publishDataName = 'WGToLNuG_PtG-500_TuneCUETP8M1_13TeV-madgraphMLM-pythia8_RunIISpring15DR74-Asympt25ns_MCRUN2_74_V9-v1_MiniAODExt_onefile'
elif iteration == 9:
    config.General.requestName = 'WGToLNuG_PtG-500_twofiles' 
    config.Data.useParent = True
    config.Data.inputDataset   = '/WGToLNuG_PtG-500_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISpring15DR74-Asympt25ns_MCRUN2_74_V9-v1/MINIAODSIM'
    config.Data.publishDataName = 'WGToLNuG_PtG-500_TuneCUETP8M1_13TeV-madgraphMLM-pythia8_RunIISpring15DR74-Asympt25ns_MCRUN2_74_V9-v1_MiniAODExt_twofiles'
else:
    print "ERROR:  Invalid iteration!!!!"

# Choose the correct pset  
if config.Data.useParent:
    config.JobType.psetName = 'candidateTrackProducer_cfg.py'
else:  
    config.JobType.psetName = 'AMSB_chargino_step4_cfg.py'


