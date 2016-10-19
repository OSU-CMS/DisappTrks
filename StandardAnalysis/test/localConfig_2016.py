from OSUT3Analysis.Configuration.configurationOptions import *
from DisappTrks.StandardAnalysis.miniAOD_80X_Samples import *

config_file = "protoConfig_2016_cfg.py"

# https://cmshead.mps.ohio-state.edu:8080/DisappearingTracks/741
intLumi = 12884.361

InputCondorArguments = {'request_memory': '2048MB', 'request_cpus': '1'}

datasetsData = [
    'MET_2016B',
    'MET_2016C',
    'MET_2016D',
    'MET_2016E',
    'MET_2016F',
    'MET_2016G',
]

datasetsSig = [
    'AMSB_chargino_100GeV_10cm_80X',
    'AMSB_chargino_100GeV_100cm_80X',
    'AMSB_chargino_100GeV_1000cm_80X',
    'AMSB_chargino_100GeV_10000cm_80X',

    'AMSB_chargino_200GeV_10cm_80X',
    'AMSB_chargino_200GeV_100cm_80X',
    'AMSB_chargino_200GeV_1000cm_80X',
    'AMSB_chargino_200GeV_10000cm_80X',

    'AMSB_chargino_300GeV_10cm_80X',
    'AMSB_chargino_300GeV_100cm_80X',
    'AMSB_chargino_300GeV_1000cm_80X',
    'AMSB_chargino_300GeV_10000cm_80X',

    'AMSB_chargino_400GeV_10cm_80X',
    'AMSB_chargino_400GeV_100cm_80X',
    'AMSB_chargino_400GeV_1000cm_80X',
    'AMSB_chargino_400GeV_10000cm_80X',

    'AMSB_chargino_500GeV_10cm_80X',
    'AMSB_chargino_500GeV_100cm_80X',
    'AMSB_chargino_500GeV_1000cm_80X',
    'AMSB_chargino_500GeV_10000cm_80X',

    'AMSB_chargino_600GeV_10cm_80X',
    'AMSB_chargino_600GeV_100cm_80X',
    'AMSB_chargino_600GeV_1000cm_80X',
    'AMSB_chargino_600GeV_10000cm_80X',

    'AMSB_chargino_700GeV_10cm_80X',
    'AMSB_chargino_700GeV_100cm_80X',
    'AMSB_chargino_700GeV_1000cm_80X',
    'AMSB_chargino_700GeV_10000cm_80X',
]

datasetsSigShort = copy.deepcopy(datasetsSig)  

datasetsSigVeryShort = [
    'AMSB_chargino_500GeV_10cm_80X',
    'AMSB_chargino_500GeV_100cm_80X',
    'AMSB_chargino_500GeV_1000cm_80X',
    'AMSB_chargino_500GeV_10000cm_80X',
]

################################################################################
# add the lifetime reweighted samples
################################################################################
new_datasetsSig = []
for dataset0 in datasetsSig:
    if not re.match (r'AMSB_chargino_[^_]*GeV_[^_]*cm_.*', dataset0):
        continue
    mass = re.sub (r'AMSB_chargino_([^_]*)GeV_[^_]*cm_.*', r'\1', dataset0)
    ctau0 = float (re.sub (r'AMSB_chargino_[^_]*GeV_([^_]*)cm_.*', r'\1', dataset0))
    suffix = re.sub (r'AMSB_chargino_[^_]*GeV_[^_]*cm_(.*)', r'\1', dataset0)
    for i in range (2, 10):
        ctau = ctauP = 0.1 * i * ctau0
        if int (ctau) * 10 == int (ctau * 10):
            ctau = ctauP = str (int (ctau))
        else:
            ctau = ctauP = str (ctau)
            ctauP = re.sub (r'\.', r'p', ctau)
        dataset = 'AMSB_chargino_' + mass + 'GeV_' + ctauP + 'cm_' + suffix

        new_datasetsSig.append (dataset)

datasetsSig.extend (new_datasetsSig)
################################################################################

datasets = datasetsData + datasetsSig
