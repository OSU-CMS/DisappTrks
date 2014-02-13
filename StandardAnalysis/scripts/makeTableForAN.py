#!/usr/bin/env python
#
# Takes as input a cutFlow.tex file created using makeCutFlows.py  
# Creates a .tex file that can be copied to the AN.
# Keeps only the first section of the cutflow table.
# Omits the \begin{table} and \end{table} statements.  
#
# Example usage:
# > makeTableForAN.py -i condor/condor_2014_02_12_FullSelectionNHits4/cutFlow.tex  

import datetime
from optparse import OptionParser
parser = OptionParser()

parser.add_option("-i", "--inputFileName", dest="inputFileName",
                  help="specify an input file name for the cutFlow.tex file")  
parser.add_option("-c", "--channel", dest="channelName",
                  help="specify the desired channel; if unspecified, the first channel is used") 

(arguments, args) = parser.parse_args()  

print "Will create new cutFlow table from " + arguments.inputFileName  

newName = arguments.inputFileName
if arguments.channelName: 
    newName = newName.replace(".tex", "_" + arguments.channelName + "_AN.tex")  
else:
    newName = newName.replace(".tex", "_AN.tex")  
    

inputfile  = open(arguments.inputFileName, 'r')  
outputfile = open(newName, 'w')

outputfile.write("% Created by running:  makeTableForAN.py -i " + arguments.inputFileName + "\n")
outputfile.write("% File name:  " + newName + "\n\n\n") 

## timeStamp = datetime.now().strftime('%Y%m%d%H%M%S')  
## outputfile.write(timeStamp)  

started = False  # started writing out
foundChannel = False
if not arguments.channelName:
    foundChannel = True
for line in inputfile:
    if not foundChannel:
        if arguments.channelName in line:
            foundChannel = True
        else:
            continue  
    if "\\begin{table}" in line:  
        started = True
        line = line.replace("\\begin{table}[htbp]", "")        
    if "\\end{table}" in line:
        line = line.replace("\\end{table}", "")
        outputfile.write(line) 
        break
    if started:
        outputfile.write(line) 
        

    
inputfile.close()
outputfile.close()
    
print "Finished writing output file to: " + newName  

