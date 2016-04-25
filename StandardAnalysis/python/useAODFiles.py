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

def addSecondaryFilesAODSIM (source):
    parents = []
    for fileName in source.fileNames:
        fileName = re.sub (r'^.*/store/', r'/store/', fileName)
        parent = getDASData ('parent file=' + fileName + ' instance=prod/phys03 | grep parent.name')
        for p in parent:
            if re.search (r'/AODSIM/', p) and not p in parents:
                parents.append (p)

    source.secondaryFileNames = cms.untracked.vstring (parents)
