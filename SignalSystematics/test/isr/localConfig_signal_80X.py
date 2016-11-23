from OSUT3Analysis.Configuration.configurationOptions import *
from DisappTrks.StandardAnalysis.miniAOD_80X_Samples import *
import copy

config_file = "protoConfig_noReweight_80X.py"

intLumi = 12877.314

InputCondorArguments = {'request_memory': '2048MB', 'request_cpus': '1'}

datasets = [
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
