from localConfig import * 

#intLumi = 2672.2 # unprescaled
intLumi = 225.17 # luminosity for HLT_LooseIsoPFTau50_Trk30_eta2p1_v* path

datasetsData = [
    'Tau_2015D',  
]

datasetsBkgd.remove("WJetsToLNu_HT")  
datasetsBkgd.append("WJetsToLNu")  

datasets = datasetsBkgd + datasetsData 
