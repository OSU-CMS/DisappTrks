#!/bin/csh

# makeStdTablesPlots.csh
#
# Script to run makeCutFlows.py and makePlots.py in a standard way
# Usage:
# > makeStdTablesPlots.csh localOptions.py condorDir

                makeCutFlows.py -r -l $1 -c $2 -o cutFlow
echo Finished:  makeCutFlows.py -r -l $1 -c $2 -o cutFlow
                makeCutFlows.py -t -l $1 -c $2 -o cutFlowTot
echo Finished:  makeCutFlows.py -t -l $1 -c $2 -o cutFlowTot
                makePlots.py    -y -O -r -l $1 -c $2 -o stacked_histograms.root
echo Finished:  makePlots.py    -y -O -r -l $1 -c $2 -o stacked_histograms.root
#                makePlots.py    -y -O -r -l $1 -c $2 -o stacked_histogramsRebin2.root -b 2
#echo Finished:  makePlots.py    -y -O -r -l $1 -c $2 -o stacked_histogramsRebin2.root -b 2
#                makePlots.py    -y -O -r -l $1 -c $2 -o stacked_histogramsRebin5.root -b 5
#echo Finished:  makePlots.py    -y -O -r -l $1 -c $2 -o stacked_histogramsRebin5.root -b 5
#                makePlots.py -p -f -l $1 -c $2 -o stacked_histogramsAN.root
#echo Finished:  makePlots.py -p -f -l $1 -c $2 -o stacked_histogramsAN.root




