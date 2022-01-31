import FWCore.ParameterSet.Config as cms
import OSUT3Analysis.DBTools.osusub_cfg as osusub
import das_client
import re
import os

def getDASData (query):
    results = []
    jsondict = das_client.get_data ('https://cmsweb.cern.ch', query, 0, 0, False)
    status = jsondict['status']
    if status != 'ok':
        print("DAS query status: %s"%(status))
        return results

    mongo_query = jsondict['mongo_query']
    filters = mongo_query['filters']
    data = jsondict['data']

    for row in data:
        result = [r for r in das_client.get_value (row, filters['grep'])][0]
        if len (result) > 0 and not result in results:
            results.append (result)

    return results

def addSecondaryFileAOD (fileName):
    parents = []
    fileName = fileName.rstrip ('\n')
    fileName = re.sub (r'^.*/store/', r'/store/', fileName)
    parent = getDASData ('parent file=' + fileName + ' instance=prod/phys03 | grep parent.name')
    for p in parent:
        p = p.rstrip ('\n')
        if (re.search (r'/AOD/', p) or re.search (r'/AODSIM/', p)) and not p in parents:
            parents.append (p)

    return parents

def addSecondaryFileFromSkim (fileName):
    parents = []
    fileName = fileName.rstrip ('\n')
    fileName = re.sub (r'^file:', r'', fileName)
    jobNumber = re.sub (r'.*/skim_([^/]*)\.root$', r'\1', fileName)
    parentDir = re.sub (r'(.*)/[^/]*/skim_[^/]*\.root$', r'\1/', fileName)
    condorErr = open (parentDir + "condor_" + jobNumber + ".err")
    for line in condorErr:
        if re.search (r'Successfully opened file', line):
            p = re.sub (r'.* Successfully opened file (.*)', r'\1', line)
            p = p.rstrip ('\n')
            if not p in parents:
                parents.append (p)

    return sorted (list (set (parents)))

def addSecondaryFile (fileName):
    parents = []
    fileName = fileName.rstrip ('\n')
    if re.search (r'/store/', fileName):
        parents = addSecondaryFileAOD (fileName)
    else:
        skimParents = addSecondaryFileFromSkim (fileName)
        for p in skimParents:
            parents += addSecondaryFile (p)

    return parents

def addSecondaryFiles (source):
    parents = []
    fileNames = source.fileNames
    if osusub.batchMode:
        fileNames = osusub.runList
    for fileName in fileNames:
        parents += addSecondaryFile (fileName)

    source.secondaryFileNames = cms.untracked.vstring (parents)
