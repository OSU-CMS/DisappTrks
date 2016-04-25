import FWCore.ParameterSet.Config as cms
import das_client
import re

def getDASData (query):
    results = []
    jsondict = das_client.get_data ('https://cmsweb.cern.ch', query, 0, 0, False)
    status = jsondict['status']
    if status != 'ok':
        print "DAS query status: %s"%(status)
        return results

    mongo_query = jsondict['mongo_query']
    filters = mongo_query['filters']
    data = jsondict['data']

    for row in data:
        result = [r for r in das_client.get_value (row, filters['grep'])][0]
        if len (result) > 0 and not result in results:
            results.append (result)

    return results

def addSecondaryFilesAODSIM (fileName):
    parents = []
    fileName = re.sub (r'^.*/store/', r'/store/', fileName)
    parent = getDASData ('parent file=' + fileName + ' instance=prod/phys03 | grep parent.name')
    for p in parent:
        if re.search (r'/AODSIM/', p) and not p in parents:
            parents.append (p)

    return parents

def addSecondaryFilesAOD (fileName):
    parents = []
    fileName = re.sub (r'^.*/store/', r'/store/', fileName)
    parent = getDASData ('parent file=' + fileName + ' instance=prod/phys03 | grep parent.name')
    for p in parent:
        sibling = getDASData ('child file=' + p + ' | grep child.name')
        for s in sibling:
              if re.search (r'/AOD/16Dec2015', s) and not s in parents:
                  parents.append (s)

    return parents

def addSecondaryFiles (source):
    parents = []
    for fileName in source.fileNames:
        if re.search (r'Run201', fileName):
            parents += addSecondaryFilesAOD (fileName)
        else:
            parents += addSecondaryFilesAODSIM (fileName)

    source.secondaryFileNames = cms.untracked.vstring (parents)
