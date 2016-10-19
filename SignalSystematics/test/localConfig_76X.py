from OSUT3Analysis.Configuration.configurationOptions import *
from DisappTrks.StandardAnalysis.miniAODV2Samples import *
import copy

config_file = "protoConfig_76X.py"

intLumi = 2590.0 # https://cmshead.mps.ohio-state.edu:8080/DisappearingTracks/595

InputCondorArguments = {'request_memory': '2048MB', 'request_cpus': '1'}

datasetsSig = [
    'AMSB_chargino_100GeV_10cm',
    'AMSB_chargino_100GeV_100cm',
    'AMSB_chargino_100GeV_1000cm',

    'AMSB_chargino_200GeV_10cm',
    'AMSB_chargino_200GeV_100cm',
    'AMSB_chargino_200GeV_1000cm',

    'AMSB_chargino_300GeV_10cm',
    'AMSB_chargino_300GeV_100cm',
    'AMSB_chargino_300GeV_1000cm',

    'AMSB_chargino_400GeV_10cm',
    'AMSB_chargino_400GeV_100cm',
    'AMSB_chargino_400GeV_1000cm',

    'AMSB_chargino_500GeV_10cm',
    'AMSB_chargino_500GeV_100cm',
    'AMSB_chargino_500GeV_1000cm',

    'AMSB_chargino_600GeV_10cm',
    'AMSB_chargino_600GeV_100cm',
    'AMSB_chargino_600GeV_1000cm',

    'AMSB_chargino_700GeV_10cm',
    'AMSB_chargino_700GeV_100cm',
    'AMSB_chargino_700GeV_1000cm',
]

datasetsSigShort = copy.deepcopy(datasetsSig)

datasetsSigVeryShort = [
    'AMSB_chargino_500GeV_10cm',
    'AMSB_chargino_500GeV_100cm',
    'AMSB_chargino_500GeV_1000cm',
]

################################################################################
# add the lifetime reweighted samples
################################################################################
new_datasetsSig = []
for dataset0 in datasetsSig:
    if not re.match (r'AMSB_chargino_[^_]*GeV_[^_]*cm', dataset0):
        continue
    mass = re.sub (r'AMSB_chargino_([^_]*)GeV_[^_]*cm', r'\1', dataset0)
    ctau0 = float (re.sub (r'AMSB_chargino_[^_]*GeV_([^_]*)cm', r'\1', dataset0))
    for i in range (2, 10):
        ctau = ctauP = 0.1 * i * ctau0
        if int (ctau) * 10 == int (ctau * 10):
            ctau = ctauP = str (int (ctau))
        else:
            ctau = ctauP = str (ctau)
            ctauP = re.sub (r'\.', r'p', ctau)
        dataset = 'AMSB_chargino_' + mass + 'GeV_' + ctauP + 'cm'

        new_datasetsSig.append (dataset)

datasetsSig.extend (new_datasetsSig)
################################################################################

datasets = datasetsSigVeryShort
