#!/usr/bin/env python3

import sys
import tempfile
import shutil
import os
import subprocess
import copy

if len(sys.argv) != 4 and len(sys.argv) != 3:
  print '\nUsage: getSiblings.py Dataset SisterDataset outFile'
  print 'or for one file: getSiblings.py file SisterDataset\n'
  sys.exit(1)

getOneFile = False

userDataset = sys.argv[1]
sisterDataset = sys.argv[2]
if len(sys.argv) == 4:
  outFile = sys.argv[3]
  print '\nGetting siblings for dataset ' + userDataset + ' in sister dataset ' + sisterDataset
else:
  getOneFile = True

# Function for getting siblings of a given file from a given dataset
def getSiblings (fileName, dataset):
  try:
    from dbs.apis.dbsClient import DbsApi
    from CRABClient.ClientUtilities import DBSURLS
  except ImportError:
    print "getSiblings() relies on CRAB. Please set up the environment for CRAB before using."
    sys.exit (1)

  dbsurl_global = DBSURLS["reader"].get ("global", "global")
  dbsurl_phys03 = DBSURLS["reader"].get ("phys03", "phys03")
  dbs3api_phys03 = DbsApi (url = dbsurl_phys03)
  dbs3api_global = DbsApi (url = dbsurl_global)

  # if there is an xrootd prefix, strip it
  if "/store/" in fileName:
    i = fileName.find ("/store/")
    fileName = fileName[i:]

  # first get the parents
  parents = dbs3api_phys03.listFileParents (logical_file_name = fileName)

  # for each of the parents, get the grandparents
  grandparents = []
  for parent in parents:
    for parent_file_name in parent["parent_logical_file_name"]:
      grandparents.extend (dbs3api_global.listFileParents (logical_file_name = parent_file_name))

  # then for each of the grandparents, get their children
  children = []
  for grandparent in grandparents:
    for grandparent_file_name in grandparent["parent_logical_file_name"]:
      children.extend (dbs3api_global.listFileChildren (logical_file_name = grandparent_file_name))

  # put the children in a set
  miniaod = set ([])
  for child in children:
    for child_file_name in child["child_logical_file_name"]:
      miniaod.add (child_file_name)

  # put the files of the target dataset in another set
  dataset = dbs3api_global.listFiles (dataset = dataset)
  miniaodSuperset = set ([])
  for f in dataset:
    miniaodSuperset.add (f["logical_file_name"])

  # return the intersection of the two sets
  return list (miniaodSuperset.intersection (miniaod))

##########################################################

if getOneFile:
    results = getSiblings(userDataset, sisterDataset)
    print 'Siblings of file ' + userDataset + ' in ' + sisterDataset + ':'
    for r in results:
	print r
    sys.exit(0)

tmpDir = tempfile.mkdtemp ()
subprocess.call('das_client --query="file dataset=' + userDataset + ' instance=' + ('prod/global' if not userDataset.endswith ('/USER') else 'prod/phys03') + '" --limit 0 > ' + tmpDir + "/AAAFileList.txt", shell = True)
inputFileList = open(tmpDir + "/AAAFileList.txt", "r")
inputFiles = inputFileList.read().split('\n')
inputFileList.close ()
shutil.rmtree (tmpDir)

result = {}

output = open(outFile, 'w')

output.write('sibling_file_dict[\'' + userDataset + '\'] = {\n')

for f in inputFiles:
    fileName = copy.deepcopy(f)
    output.write('    \'' + fileName + '\' : [')
    results = getSiblings(f, sisterDataset)
    for r in results:
	output.write('\'' + r + '\', ')
    output.write('],\n')
    output.flush()

output.write('}\n')
output.close()
