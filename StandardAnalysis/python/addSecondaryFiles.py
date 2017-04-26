import FWCore.ParameterSet.Config as cms
import OSUT3Analysis.DBTools.osusub_cfg as osusub
import re
import os

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
    if re.search (r'root://', fileName):
        parents.append (fileName)
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
