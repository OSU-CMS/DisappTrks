from DisappTrks.StandardAnalysis.integrated_luminosity import *

intLumi = 1.0

###################
# 'color' options #
###################
## 'black'
## 'red'  
## 'green'
## 'purple'
## 'blue'  
## 'yellow'
## default: cycle through list


####################
# 'marker' options #
####################
## 'circle'
## 'square'
## 'triangle'
## default: 'circle'

####################
#  'fill' options  #
####################
## 'solid'
## 'hollow'
## default: 'solid'

cutName = 'durp'

input_sources = [
	{
		'condor_dir'   : 'hartCondor/2016_final_prompt/muonTagSkim_new',
		'dataset'      : 'SingleMu_2016B',
		'channel'      : 'MuonTagSkim',
		'legend_entry' : '2016B',
		'color'        : 'black',
	},
	{
		'condor_dir'   : '2017/muonTagSkim',
		'dataset'      : 'SingleMu_2017B',
		'channel'      : 'MuonTagSkim',
		'legend_entry' : '2017B',
		'color'        : 'red',
	},
]
