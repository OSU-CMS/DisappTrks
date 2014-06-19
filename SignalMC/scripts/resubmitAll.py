#!/usr/bin/env python
#
# Resubmit crab jobs 
# 
# Usage:
# DisappTrks/SignalMC/test> ../scripts/resubmitAll.py -m multicrab.cfg 

# Take directories from multicrab*.cfg files

import os 
import sys 
import re  
from optparse import OptionParser

parser = OptionParser()
parser.add_option("-l", "--localConfig", dest="localConfig", 
                  help="local configuration file (to specify list of directories)")  
parser.add_option("-m", "--multicrab", dest="multicrab", 
                  help="multicrab file used to get list of directories")  
parser.add_option("-g", "--get", action="store_true", dest="get", default=False,
                  help="run crab -getoutput")  
parser.add_option("-r", "--resubmit", action="store_true", dest="resubmit", default=False,
                  help="run crab -resubmit")  
parser.add_option("-p", "--publish", action="store_true", dest="publish", default=False,
                  help="run crab -publish")  
parser.add_option("-q", "--quick", action="store_true", dest="quick", default=False,
                  help="Run only the first job in the list.") 
parser.add_option("-t", "--test", action="store_true", dest="test", default=False,
                  help="Do not run crab commands; only print the list of directories.")  
(arguments, args) = parser.parse_args()

if arguments.localConfig:
    sys.path.append(os.getcwd())
    exec("from " + re.sub (r".py$", r"", arguments.localConfig) + " import *")

if arguments.multicrab:
    if arguments.localConfig:
        print "Warning:  you have specified -l and -m options; will overwrite the list of directories in " + arguments.localConfig + " with the list from " + arguments.multicrab  
    directories = []  
    fin = open(arguments.multicrab, "r")
    for line in fin.readlines():  
        if "#" in line: 
            line = line[:line.index('#')]   # strip anything after a "#" comment symbol  
        if "[" in line and "]" in line and "AMSB" in line:   # require directory to include "AMSB" in name
            line = line.replace("[", "")
            line = line[:line.index(']')]   # strip anything after the "]" 
            directories.append(line)    
    fin.close()

for d in directories:  
    print "Will process directory: " + d  

if arguments.test:
    sys.exit(0)    

for d in directories:  
    print "Doing dir: " + d
    cmd = "crab -status -c " + d; os.system(cmd)  
    if arguments.get or arguments.resubmit:
        cmd = "crab -getoutput -c " + d; os.system(cmd)  
        cmd = "crab -status -c " + d + " > " + d + "/status.log"; os.system(cmd)  
    if arguments.resubmit or arguments.resubmit:
        cmd = "cat " + d + "/status.log | ../scripts/resubmitJobs.pl > resubmitOne.sh "; os.system(cmd) # can use resubmitStuckJobs.pl or resubmitStillbornJobs.pl instead
        cmd = "cp resubmitOne.sh " + d; os.system(cmd)
        cmd = "chmod +x resubmitOne.sh"; os.system(cmd)
        cmd = "./resubmitOne.sh  > " + d + "/resubmitOne.log"; os.system(cmd)
        cmd = "cat " + d + "/resubmitOne.log"; os.system(cmd)  # so user can see it
    if arguments.publish:  # Only do once jobs have finished
        cmd = "crab -report -c " + d; os.system(cmd) 
        cmd = "crab -publishNoInp -c " + d; os.system(cmd)  
    if arguments.quick:
        sys.exit(0)
    






