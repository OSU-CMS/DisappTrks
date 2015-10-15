from OSUT3Analysis.Configuration.configurationOptions_13TeV import *

config_file = "protoConfig_cfg.py"

intLumi = 628.76

datasets = [
  'SingleTop_MiniAOD',
  'TTJets_Lept_MiniAOD',
  'WJetsToLNu_MiniAOD',

  'MET_2015D_05Oct2015',
]

labels["WJetsToLNu_MiniAOD"] = "W+jets"
