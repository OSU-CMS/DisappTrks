#!/usr/bin/env python

import time
import os
import sys
import math
import copy
import re
import subprocess
import shutil
from array import *
from optparse import OptionParser


parser = OptionParser()
parser.add_option("-l", "--localConfig", dest="localConfig",
                  help="local configuration file")
parser.add_option("-c", "--outputDir", dest="outputDir",
                                    help="output directory")
parser.add_option("-M", "--method", dest="method", default="Asymptotic",
                                    help="which method of combine to use: currently supported options are Asymptotic (default), MarkovChainMC and HybridNew")
parser.add_option("-i", "--iterations", dest="Niterations", default="10000",
                  help="how many points are proposed to fill a single Markov chain, default = 10k")
parser.add_option("-r", "--tries", dest="Ntries", default="10",
                  help="how many times the algorithm will run for observed limits, default = 10")
parser.add_option("-t", "--toys", dest="Ntoys", default="1",
                  help="how many toy MC to throw for expected limits, default = 1")
parser.add_option("-b", "--batchMode", action="store_true", dest="batchMode", default=False,
                                    help="run on the condor queue")

(arguments, args) = parser.parse_args()

if arguments.localConfig:
    sys.path.append(os.getcwd())
    exec("from " + re.sub (r".py$", r"", arguments.localConfig) + " import *")
else:
    print "No local config specified, shame on you"
    sys.exit(0)
if not arguments.outputDir:
    print "No output directory specified, shame on you"
    sys.exit(0)


if arguments.outputDir:
    if not os.path.exists ("limits/"+arguments.outputDir):
            os.system("mkdir limits/%s" % (arguments.outputDir))
#   os.mkdir("limits/"+arguments.outputDir)

                

def output_condor(command, options):
    script = "#!/usr/bin/env bash\n\n"
    script += command+" "+options+"\n"
    f = open ("condor.sh", "w")
    f.write (script)
    f.close ()
    os.chmod ("condor.sh", 0775)
    command = os.getcwd () + "/condor.sh"

    sub_file = ""
#    if os.path.exists(os.environ["CMSSW_BASE"]+"/src/DisplacedSUSY/LimitsCalculation/data/condor.sub"):
    if os.path.exists(os.environ["CMSSW_BASE"]+"/src/DisappTrks/StandardAnalysis/data/condor.sub"):
        f = open (os.environ["CMSSW_BASE"]+"/src/DisappTrks/StandardAnalysis/data/condor.sub", "r")
        sub_file = f.read ()
        f.close ()
        sub_file = re.sub (r"\$combine", command, sub_file)
    else:
        sub_file += "Executable              = "+command+"\n"
        sub_file += "Universe                = vanilla\n"
        sub_file += "Getenv                  = True\n"
        sub_file += "\n"
        sub_file += "Output                  = condor_$(Process).out\n"
        sub_file += "Error                   = condor_$(Process).err\n"
        sub_file += "Log                     = condor_$(Process).log\n"
        sub_file += "\n"
        sub_file += "+IsLocalJob             = true\n"
        sub_file += "Rank                    = TARGET.IsLocalSlot\n"
        sub_file += "\n"
        sub_file += "Queue 1\n"

    f = open ("condor.sub", "w")
    f.write (sub_file)
    f.close ()


### create a file to keep track of which combine method was used
### (since extracting the limits is different for each one)
#methodFile = open(os.environ["CMSSW_BASE"]+"/src/DisplacedSUSY/LimitsCalculation/test/limits/"+arguments.outputDir+"/method.txt", "w")
print os.environ["CMSSW_BASE"]+"/src/DisappTrks/StandardAnalysis/test/limits/"+arguments.outputDir+"/method.txt"
methodFile = open(os.environ["CMSSW_BASE"]+"/src/DisappTrks/StandardAnalysis/test/limits/"+arguments.outputDir+"/method.txt", "w")

methodFile.write(arguments.method)
methodFile.close()

### looping over signal models and running a combine job for each one
for mass in masses:
    print chiMasses[mass]['value']
    if float(chiMasses[mass]['value']) < 150:
        print "Chi mass is less than 150"
        for lifetime in lifetimes:
            lifetime = lifetime.replace(".0", "")
            lifetime = lifetime.replace("0.5", "0p5")
            signal_name = "AMSB_mChi"+chiMasses[mass]['value']+"_"+lifetime+"ns"
            condor_expected_dir = "limits/"+arguments.outputDir+"/"+signal_name+"_expected"
            condor_observed_dir = "limits/"+arguments.outputDir+"/"+signal_name+"_observed"
            datacard_name = "datacard_"+signal_name+".txt"
            datacard_src_name = "limits/"+arguments.outputDir+"/"+datacard_name
            datacard_dst_expected_name = condor_expected_dir+"/"+datacard_name
            datacard_dst_observed_name = condor_observed_dir+"/"+datacard_name
            combine_expected_options = combine_observed_options = "-s -1 -H ProfileLikelihood "
            if arguments.method == "HybridNew":
                combine_expected_options += "-M " + arguments.method + " "
                combine_observed_options += "-M " + arguments.method + " "
                combine_expected_options = combine_expected_options + "-t " + arguments.Ntoys + " "
                combine_observed_options = combine_observed_options + "--frequentist --testStat LHC" + " "
            elif arguments.method == "MarkovChainMC":
                combine_expected_options += "-M " + arguments.method + " "
                combine_observed_options += "-M " + arguments.method + " "
                combine_expected_options = combine_expected_options + "-t " + arguments.Ntoys + " --tries " + arguments.Ntries + " -i " + arguments.Niterations + " "
                combine_observed_options = combine_observed_options + "--tries " + arguments.Ntries + " -i " + arguments.Niterations + " "
            else:
                combine_expected_options += "-M Asymptotic --minimizerStrategy 1 --picky --minosAlgo stepping --rMin 0.00000001 --rMax 2"
                combine_observed_options += "-M Asymptotic --minimizerStrategy 1 --picky --minosAlgo stepping --rMin 0.00000001 --rMax 2"

            combine_command = subprocess.Popen(["which", "combine"], stdout=subprocess.PIPE).communicate()[0]
            combine_command = combine_command.rstrip()
             
            shutil.rmtree(condor_expected_dir, True)
            os.mkdir(condor_expected_dir)
            shutil.copy(datacard_src_name, datacard_dst_expected_name)
            os.chdir(condor_expected_dir)
            if not arguments.batchMode:
            #            command = "(combine "+datacard_name+" "+combine_expected_options+" --name "+signal_name+" | tee /dev/null) > combine_log_"+signal_name+".log"
                command = "(combine "+datacard_name+" "+combine_expected_options+" --name "+signal_name+" | tee /dev/null) > combine_log_"+signal_name+".txt"
                print command
                os.system(command)
                
            else:
                print "combine "+datacard_name+" "+combine_expected_options+" --name "+signal_name
                output_condor(combine_command, datacard_name+" "+combine_expected_options+" --name "+signal_name+" | tee /dev/null")
                os.system("LD_LIBRARY_PATH=/usr/lib64/condor:$LD_LIBRARY_PATH condor_submit condor.sub")
         
            os.chdir("../../..")
         
            shutil.rmtree(condor_observed_dir, True)
            os.mkdir(condor_observed_dir)
            shutil.copy(datacard_src_name, datacard_dst_observed_name)
            os.chdir(condor_observed_dir)
         
            if not arguments.batchMode:
            #            command = "(combine "+datacard_name+" "+combine_observed_options+" --name "+signal_name+" | tee /dev/null) > combine_log_"+signal_name+".log"
                command = "(combine "+datacard_name+" "+combine_observed_options+" --name "+signal_name+" | tee /dev/null) > combine_log_"+signal_name+".txt"
                print command
                os.system(command)
             
            else:
                print "combine "+datacard_name+" "+combine_observed_options+" --name "+signal_name
                output_condor(combine_command, datacard_name+" "+combine_observed_options+" --name "+signal_name+" | tee /dev/null")
                os.system("LD_LIBRARY_PATH=/usr/lib64/condor:$LD_LIBRARY_PATH condor_submit condor.sub")
             
            os.chdir("../../..")
                
    if float(chiMasses[mass]['value']) > 150:
        for lifetime in lifetimes:
            lifetime = lifetime.replace(".0", "")
            lifetime = lifetime.replace("0.5", "0p5")
            signal_name = "AMSB_mChi"+chiMasses[mass]['value']+"_"+lifetime+"ns"
            condor_expected_dir = "limits/"+arguments.outputDir+"/"+signal_name+"_expected"
            condor_observed_dir = "limits/"+arguments.outputDir+"/"+signal_name+"_observed"
            datacard_name = "datacard_"+signal_name+".txt"
            datacard_src_name = "limits/"+arguments.outputDir+"/"+datacard_name
            datacard_dst_expected_name = condor_expected_dir+"/"+datacard_name
            datacard_dst_observed_name = condor_observed_dir+"/"+datacard_name
            combine_expected_options = combine_observed_options = "-s -1 -H ProfileLikelihood "
            if arguments.method == "HybridNew":
                combine_expected_options += "-M " + arguments.method + " "
                combine_observed_options += "-M " + arguments.method + " "
                combine_expected_options = combine_expected_options + "-t " + arguments.Ntoys + " "
                combine_observed_options = combine_observed_options + "--frequentist --testStat LHC" + " "
            elif arguments.method == "MarkovChainMC":
                combine_expected_options += "-M " + arguments.method + " "
                combine_observed_options += "-M " + arguments.method + " "
                combine_expected_options = combine_expected_options + "-t " + arguments.Ntoys + " --tries " + arguments.Ntries + " -i " + arguments.Niterations + " "
                combine_observed_options = combine_observed_options + "--tries " + arguments.Ntries + " -i " + arguments.Niterations + " "
            else:
                combine_expected_options += "-M Asymptotic --minimizerStrategy 1 --picky --minosAlgo stepping "
                combine_observed_options += "-M Asymptotic --minimizerStrategy 1 --picky --minosAlgo stepping "
                
            combine_command = subprocess.Popen(["which", "combine"], stdout=subprocess.PIPE).communicate()[0]
            combine_command = combine_command.rstrip()
        
            shutil.rmtree(condor_expected_dir, True)
            os.mkdir(condor_expected_dir)
            shutil.copy(datacard_src_name, datacard_dst_expected_name)
            os.chdir(condor_expected_dir)
            
            if not arguments.batchMode:
#            command = "(combine "+datacard_name+" "+combine_expected_options+" --name "+signal_name+" | tee /dev/null) > combine_log_"+signal_name+".log"
                command = "(combine "+datacard_name+" "+combine_expected_options+" --name "+signal_name+" | tee /dev/null) > combine_log_"+signal_name+".txt"
                print command
                os.system(command)
            
            else:
                print "combine "+datacard_name+" "+combine_expected_options+" --name "+signal_name
                output_condor(combine_command, datacard_name+" "+combine_expected_options+" --name "+signal_name+" | tee /dev/null")
                os.system("LD_LIBRARY_PATH=/usr/lib64/condor:$LD_LIBRARY_PATH condor_submit condor.sub")
            
            os.chdir("../../..")

            shutil.rmtree(condor_observed_dir, True)
            os.mkdir(condor_observed_dir)
            shutil.copy(datacard_src_name, datacard_dst_observed_name)
            os.chdir(condor_observed_dir)
        
            if not arguments.batchMode:
#            command = "(combine "+datacard_name+" "+combine_observed_options+" --name "+signal_name+" | tee /dev/null) > combine_log_"+signal_name+".log"
                command = "(combine "+datacard_name+" "+combine_observed_options+" --name "+signal_name+" | tee /dev/null) > combine_log_"+signal_name+".txt"
                print command
                os.system(command)
                
            else:
                print "combine "+datacard_name+" "+combine_observed_options+" --name "+signal_name
                output_condor(combine_command, datacard_name+" "+combine_observed_options+" --name "+signal_name+" | tee /dev/null")
                os.system("LD_LIBRARY_PATH=/usr/lib64/condor:$LD_LIBRARY_PATH condor_submit condor.sub")
                
            os.chdir("../../..")
