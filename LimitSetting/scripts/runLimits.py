#!/usr/bin/env python3

# Documentation of the combine tool:  https://twiki.cern.ch/twiki/bin/viewauth/CMS/SWGuideHiggsAnalysisCombinedLimit

import time
import os
import sys
import math
import copy
import re
import subprocess
import shutil
from array import *

from DisappTrks.LimitSetting.limitOptions import *

if not arguments.era in validEras:
  print( "Invalid or empty data-taking era specific (-e). Allowed eras:")
  print( str(validEras))
  sys.exit(0)

if arguments.limitType not in validLimitTypes:
    print( "Invalid or empty limit type to run (-l). Allowed types:")
    print( str(validLimitTypes))
    sys.exit(0)

if arguments.method not in ["HybridNew", "MarkovChainMC", "AsymptoticLimits", "AsymptoticSignificance"]:
    print( "Invalid method (-M). Allowed methods:")
    for x in ["HybridNew", "MarkovChainMC", "AsymptoticLimits", "AsymptoticSignificance"]:
        print( "\t" + x)
    sys.exit(0)

if arguments.limitType == "wino":
    from DisappTrks.LimitSetting.winoElectroweakLimits import *
elif arguments.limitType == "higgsino":
    from DisappTrks.LimitSetting.higgsinoElectroweakLimits import *

if not arguments.outputDir:
    print( "No output directory specified, shame on you")
    sys.exit(0)

if arguments.outputDir:
    if not os.path.exists ("limits/"+arguments.outputDir):
        os.system("mkdir limits/%s" % (arguments.outputDir))

def output_condor(combine_command, datacard, options):
    script = "#!/usr/bin/env bash\n\n"
    script += "./combine "+options+"\n"
    f = open ("condor.sh", "w")
    f.write (script)
    f.close ()
    os.chmod ("condor.sh", 775)
    command = "condor.sh"

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
        sub_file += "should_transfer_files   = yes\n"
        print("Combine command", type(combine_command), combine_command)
        print("datacard", type(datacard), datacard)
        sub_file += "transfer_input_files    = " + combine_command + "," + datacard + "\n"
        sub_file += "\n"
        sub_file += "request_memory          = 2048MB\n"
        sub_file += "request_cpus            = 1\n"
        sub_file += "\n"
        sub_file += "Queue 1\n"

    f = open ("condor.sub", "w")
    f.write (sub_file)
    f.close ()


### create a file to keep track of which combine method was used
### (since extracting the limits is different for each one)
#methodFile = open(os.environ["CMSSW_BASE"]+"/src/DisplacedSUSY/LimitsCalculation/test/limits/"+arguments.outputDir+"/method.txt", "w")
print( os.environ["CMSSW_BASE"]+"/src/DisappTrks/StandardAnalysis/test/limits/"+arguments.outputDir+"/method.txt")
methodFile = open(os.environ["CMSSW_BASE"]+"/src/DisappTrks/StandardAnalysis/test/limits/"+arguments.outputDir+"/method.txt", "w")

methodFile.write(arguments.method)
methodFile.close()

### looping over signal models and running a combine job for each one
for mass in masses:
    for lifetime in lifetimes:
        lifetime = lifetime.replace(".0", "")
        lifetime = lifetime.replace("0.", "0p")
        if arguments.limitType == "wino":
            if samplesByGravitinoMass:
                signal_name = "AMSB_mChi" + chiMasses[mass]['value'] + "_" + lifetime + "ns"
            else:
                signal_name = "AMSB_mChi" + mass + "_" + lifetime + "cm"
        elif arguments.limitType == "higgsino":
            signal_name = "Higgsino_mChi" + mass + "_" + lifetime + "cm"
        condor_expected_dir = "limits/"+arguments.outputDir+"/"+signal_name+"_expected"
        condor_observed_dir = "limits/"+arguments.outputDir+"/"+signal_name+"_observed"
        datacard_name = "datacard_"+signal_name+".txt"
        print("OutputDir:", arguments.outputDir)
        print("Datacard name", datacard_name)
        datacard_src_name = "limits/"+arguments.outputDir+"/"+datacard_name
        datacard_dst_expected_name = condor_expected_dir+"/"+datacard_name
        datacard_dst_observed_name = condor_observed_dir+"/"+datacard_name

        combine_expected_options = combine_observed_options = " "  # default random number seed = 123456
 
        if arguments.method == "HybridNew":
            combine_expected_options += "-M " + arguments.method + " "
            combine_observed_options += "-M " + arguments.method + " "
            hybridExtraOptions = "--fork 4 --frequentist --testStat LHC --rAbsAcc 0.00001 -T 2000 "
            combine_expected_options = combine_expected_options + hybridExtraOptions + " --expectedFromGrid 0.5 "
            combine_observed_options = combine_observed_options + hybridExtraOptions
        elif arguments.method == "MarkovChainMC":
            combine_expected_options += "-M " + arguments.method + " "
            combine_observed_options += "-M " + arguments.method + " "
            combine_expected_options = combine_expected_options + "-t " + arguments.Ntoys + " --tries " + arguments.Ntries + " -i " + arguments.Niterations + " "
            combine_observed_options = combine_observed_options + "--tries " + arguments.Ntries + " -i " + arguments.Niterations + " "
        elif arguments.method == "AsymptoticSignificance":
            combine_expected_options += "-M Significance --pval -t -1 --expectSignal=1 "
            combine_observed_options += "-M Significance --pval "
        elif arguments.method == "AsymptoticLimits":
            if not arguments.noPicky:
                combine_expected_options += "-M AsymptoticLimits --cminDefaultMinimizerStrategy 1 --picky --minosAlgo stepping "
                combine_observed_options += "-M AsymptoticLimits --cminDefaultMinimizerStrategy 1 --picky --minosAlgo stepping "
            else:
                combine_expected_options += "-M AsymptoticLimits --cminDefaultMinimizerStrategy 1 --minosAlgo stepping "
                combine_observed_options += "-M AsymptoticLimits --cminDefaultMinimizerStrategy 1 --minosAlgo stepping "
        if (samplesByGravitinoMass and float(chiMasses[mass]['value']) < 150) or (not samplesByGravitinoMass and float(mass) < 150):
            lifetimeFloat = float(lifetime.replace('0p', '0.'))
            if lifetimeFloat > 9 and lifetimeFloat < 300:   # Use a smaller maximum for lifetimes with a larger signal yield
                combine_expected_options += " --rMin 0.00000001 --rMax 0.1 "
                combine_observed_options += " --rMin 0.00000001 --rMax 0.1 "
            else:
                combine_expected_options += " --rMin 0.00000001 --rMax 2 "
                combine_observed_options += " --rMin 0.00000001 --rMax 2 "

        combine_command = subprocess.Popen(["which", "combine"], stdout=subprocess.PIPE).communicate()[0].decode('UTF-8')
        combine_command = combine_command.rstrip()

        shutil.rmtree(condor_expected_dir, True)
        os.mkdir(condor_expected_dir)
        print("Output:", datacard_src_name, datacard_dst_expected_name)
        shutil.copy(datacard_src_name, datacard_dst_expected_name)
        os.chdir(condor_expected_dir)

        if not arguments.batchMode:
            command = "(combine "+datacard_name+" "+combine_expected_options+" --name "+signal_name+" | tee /dev/null) > combine_log_"+signal_name+".txt"
            print( command)
            os.system(command)
        else:
            print( "combine "+datacard_name+" "+combine_expected_options+" --name "+signal_name)
            output_condor(combine_command, datacard_name, datacard_name+" "+combine_expected_options+" --name "+signal_name+" | tee /dev/null")
            os.system("LD_LIBRARY_PATH=/usr/lib64/condor:$LD_LIBRARY_PATH condor_submit condor.sub")

        if arguments.method == "HybridNew":  # for full CLs, run each expected limit separately
            expectedVariations = [("up1", "0.84"), ("up2", "0.975"), ("down1", "0.16"), ("down2", "0.025")]
            for vary in expectedVariations:
                os.chdir("../../..")
                condor_expected_dirVary = condor_expected_dir + "_" + vary[0]
                shutil.rmtree(condor_expected_dirVary, True)
                os.mkdir(condor_expected_dirVary)
                shutil.copy(datacard_src_name, condor_expected_dirVary + "/" + datacard_name)
                os.chdir(condor_expected_dirVary)
                if not arguments.batchMode:
                    commandVary = command.replace("expectedFromGrid 0.5", "expectedFromGrid " + vary[1])
                    print( commandVary)
                    os.system(commandVary)
                else:
                    combine_expected_optionsVary = combine_expected_options.replace("expectedFromGrid 0.5", "expectedFromGrid " + vary[1])
                    print( "combine "+datacard_name+" "+combine_expected_optionsVary+" --name "+signal_name)
                    output_condor(combine_command, datacard_name, datacard_name+" "+combine_expected_optionsVary+" --name "+signal_name+" | tee /dev/null")
                    os.system("LD_LIBRARY_PATH=/usr/lib64/condor:$LD_LIBRARY_PATH condor_submit condor.sub")

        os.chdir("../../..")

        shutil.rmtree(condor_observed_dir, True)
        os.mkdir(condor_observed_dir)
        shutil.copy(datacard_src_name, datacard_dst_observed_name)
        os.chdir(condor_observed_dir)

        if not arguments.batchMode:
            #            command = "(combine "+datacard_name+" "+combine_observed_options+" --name "+signal_name+" | tee /dev/null) > combine_log_"+signal_name+".log"
            command = "(combine "+datacard_name+" "+combine_observed_options+" --name "+signal_name+" | tee /dev/null) > combine_log_"+signal_name+".txt"
            print( command)
            os.system(command)


        else:
            print( "combine "+datacard_name+" "+combine_observed_options+" --name "+signal_name)
            output_condor(combine_command, datacard_name, datacard_name+" "+combine_observed_options+" --name "+signal_name+" | tee /dev/null")
            os.system("LD_LIBRARY_PATH=/usr/lib64/condor:$LD_LIBRARY_PATH condor_submit condor.sub")

        os.chdir("../../..")

        if arguments.quick:
            sys.exit("Finished running one point.")

