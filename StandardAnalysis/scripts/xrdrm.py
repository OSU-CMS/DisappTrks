#!/usr/bin/env python
import os
import subprocess
from CRABClient.UserUtilities import config, getUsernameFromSiteDB
from optparse import OptionParser

parser = OptionParser()

parser.add_option("--site",dest="site", default="", help="Set the target site where to remove dataset from")
parser.add_option("-d","--dataset",dest="Dataset", default="",help="Set the target dataset for removing")

(arguments, args) = parser.parse_args()

RedirectorDic = {'Infn':'xrootd.ba.infn.it','FNAL':'cmsxrootd.fnal.gov','Purdue':'xrootd.rcac.purdue.edu','Global':'cms-xrd-global.cern.ch','LPC':'cmseos.fnal.gov','CERN':'eoscms.cern.ch','Rutgers':'ruhex-osgce.rutgers.edu'}

if arguments.site == "":
    raise Exception("DAS site not specified")
if arguments.Dataset  == "":
    raise Exception("dataset not specified")
  
DirBase = '/store/user/%s/' % (getUsernameFromSiteDB())

################# FINAL INSPECTION #################################
print "!!!!!!!! WARNING: DO NOT DO STUPID THINGS!!!!!!!!!!!!"
final_decision = raw_input("Are you sure to remove %s from Site:%s ?[Y/n]" %(arguments.Dataset , arguments.site))
if final_decision != 'Y':
    exit()
else:
    print "Too late for regrets"
###################################################################


def CheckDirectory( SearchPath ):
  isDir = False
  StatLists = subprocess.check_output( ["xrdfs","root://"+RedirectorDic[arguments.site],"stat",SearchPath])
  StatList = StatLists.split('\n')
  print "Processing %s"%(SearchPath)
  for StatLine in StatList:
    if "Flags:" in StatLine:
      if "IsDir" in StatLine:
        isDir = True
        ContentLists = subprocess.check_output( ["xrdfs","root://"+RedirectorDic[arguments.site],"ls",SearchPath])
        ContentList  = ContentLists.split('\n')
        for ContentLine in ContentList:
          if DirBase in ContentLine:
            NextSearchPath = ContentLine 
            CheckDirectory( NextSearchPath )
      else:
        subprocess.call(["xrdfs","root://"+RedirectorDic[arguments.site],"rm",SearchPath])
        print SearchPath
  if isDir == True:
    print "Content cleared, removing the directory: %s" %(SearchPath)
    subprocess.call(["xrdfs","root://"+RedirectorDic[arguments.site],"rm",SearchPath])
                             
if   __name__ == "__main__":

  if DirBase in arguments.Dataset:
    CheckDirectory( arguments.Dataset )
  else:
    CheckDirectory( DirBase+arguments.Dataset )
