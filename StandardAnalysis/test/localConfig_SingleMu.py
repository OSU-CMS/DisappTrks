from localConfig import * 

intLumi = 2670.0 # https://cmshead.mps.ohio-state.edu:8080/DisappearingTracks/670

datasetsData = [
    'SingleMu_2015D',  
]

datasetsBkgd.remove("WJetsToLNu_HT")  
datasetsBkgd.append("WJetsToLNu")  

datasets = datasetsBkgd + datasetsData 

# datasets = [
#     'SingleMu_2015D',  
# ]


