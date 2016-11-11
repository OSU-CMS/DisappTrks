from OSUT3Analysis.Configuration.configurationOptions import *
from DisappTrks.TriggerAnalysis.miniAODSamples_76X import *

config_file = "protoConfig_2015_cfg.py"

intLumi = 2670.0 # https://cmshead.mps.ohio-state.edu:8080/DisappearingTracks/670

InputCondorArguments = {'request_memory': '2048MB', 'request_cpus': '1'}

datasetsData = [
    'SingleMu_2015D',
]

datasetsBkg = [
    'WJetsToLNu',
]

datasetsSig = [
    'AMSB_chargino_100GeV_10cm_76X',
    'AMSB_chargino_100GeV_100cm_76X',
    'AMSB_chargino_100GeV_1000cm_76X',
    'AMSB_chargino_100GeV_10000cm_76X',

    'AMSB_chargino_200GeV_10cm_76X',
    'AMSB_chargino_200GeV_100cm_76X',
    'AMSB_chargino_200GeV_1000cm_76X',
    'AMSB_chargino_200GeV_10000cm_76X',

    'AMSB_chargino_300GeV_10cm_76X',
    'AMSB_chargino_300GeV_100cm_76X',
    'AMSB_chargino_300GeV_1000cm_76X',
    'AMSB_chargino_300GeV_10000cm_76X',

    'AMSB_chargino_400GeV_10cm_76X',
    'AMSB_chargino_400GeV_100cm_76X',
    'AMSB_chargino_400GeV_1000cm_76X',
    'AMSB_chargino_400GeV_10000cm_76X',

    'AMSB_chargino_500GeV_10cm_76X',
    'AMSB_chargino_500GeV_100cm_76X',
    'AMSB_chargino_500GeV_1000cm_76X',
    'AMSB_chargino_500GeV_10000cm_76X',

    'AMSB_chargino_600GeV_10cm_76X',
    'AMSB_chargino_600GeV_100cm_76X',
    'AMSB_chargino_600GeV_1000cm_76X',
    'AMSB_chargino_600GeV_10000cm_76X',

    'AMSB_chargino_700GeV_10cm_76X',
    'AMSB_chargino_700GeV_100cm_76X',
    'AMSB_chargino_700GeV_1000cm_76X',
    'AMSB_chargino_700GeV_10000cm_76X',
]

datasetsSigShort = copy.deepcopy(datasetsSig)

datasetsSigVeryShort = [
    'AMSB_chargino_500GeV_10cm_76X',
    'AMSB_chargino_500GeV_100cm_76X',
    'AMSB_chargino_500GeV_1000cm_76X',
    'AMSB_chargino_500GeV_10000cm_76X',
]

################################################################################
# add the lifetime reweighted samples
################################################################################
new_datasetsSig = []
for dataset0 in datasetsSig:
    if not re.match (r'AMSB_chargino_[^_]*GeV_[^_]*cm_76X', dataset0):
        continue
    mass = re.sub (r'AMSB_chargino_([^_]*)GeV_[^_]*cm_76X', r'\1', dataset0)
    ctau0 = float (re.sub (r'AMSB_chargino_[^_]*GeV_([^_]*)cm_76X', r'\1', dataset0))
    for i in range (2, 10):
        ctau = ctauP = 0.1 * i * ctau0
        if int (ctau) * 10 == int (ctau * 10):
            ctau = ctauP = str (int (ctau))
        else:
            ctau = ctauP = str (ctau)
            ctauP = re.sub (r'\.', r'p', ctau)
        dataset = 'AMSB_chargino_' + mass + 'GeV_' + ctauP + 'cm_76X'

        new_datasetsSig.append (dataset)

datasetsSig.extend (new_datasetsSig)
################################################################################

datasets = datasetsBkg + datasetsData
#datasets = datasetsSigShort
