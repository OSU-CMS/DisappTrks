#!/usr/bin/env python3
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
parser.add_option("-m", "--marginal", dest="marginal", action="store_true", default=False,
                  help="make table of marginal efficiencies")
parser.add_option("-e", "--efficiency", dest="efficiency", action="store_true", default=False,
                  help="make table of total efficiencies")

(arguments, args) = parser.parse_args()

print "Will create new cutFlow table from " + arguments.inputFileName

newName = arguments.inputFileName
if arguments.channelName:
    newName = newName.replace(".tex", "_" + arguments.channelName + "_AN.tex")
else:
    newName = newName.replace(".tex", "_AN.tex")
if arguments.marginal:
    newName = newName.replace("_AN.tex", "_ANmarginal.tex")
if arguments.efficiency:
    newName = newName.replace("_AN.tex", "_ANefficiency.tex")

inputfile  = open(arguments.inputFileName, 'r')
outputfile = open(newName, 'w')

outputfile.write("% Created by running:  makeTableForAN.py -i " + arguments.inputFileName + "\n")
outputfile.write("% File name:  " + newName + "\n\n\n")

## timeStamp = datetime.now().strftime('%Y%m%d%H%M%S')
## outputfile.write(timeStamp)

started = False  # started writing out
foundChannel = False
foundYields = True
if not arguments.channelName:
    foundChannel = True
if arguments.marginal or arguments.efficiency:
    foundYields = False
output = ""  # Text to be written to output file
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
        output += line
        if (arguments.efficiency or arguments.marginal) and not foundYields:
            output = ""       # clear buffer...
            started = False   # ... and start over
        else:
            break
    if started:
        if "{Efficiency}" in line and arguments.efficiency:
            foundYields = True;
        if "{Marginal efficiency}" in line and arguments.marginal:
            foundYields = True;
        output += line

outputfile.write(output)

inputfile.close()
outputfile.close()

print "Finished writing output file to: " + newName

