#!/usr/bin/env python
#
# Takes as input a cutFlow.tex file created using makeCutFlows.py  
# Creates a .tex file that can be copied to the AN.
# Keeps only the first section of the cutflow table.
# Omits the \begin{table} and \end{table} statements.  
#
# Example usage:
# > makeTableForAN.py -i condor/condor_2014_02_12_FullSelectionNHits4/cutFlow.tex  

from optparse import OptionParser
parser = OptionParser()

parser.add_option("-i", "--inputFileName", dest="inputFileName",
                  help="specify an input file name for the cutFlow.tex file")  

(arguments, args) = parser.parse_args()  

print "Will create new cutFlow table from " + arguments.inputFileName  

newName = arguments.inputFileName  
newName = newName.replace(".tex", "_AN.tex")  


inputfile  = open(arguments.inputFileName, 'r')  
outputfile = open(newName, 'w')

started = False  # started writing out
for line in inputfile:
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

