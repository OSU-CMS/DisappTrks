#!/usr/bin/env python
import os 

masses = {  # chargino mass : gravitino mass
            100 :  3.508e4, 
            200 :  6.894e4, 
            300 : 10.365e4, 
            400 : 13.895e4, 
            500 : 17.443e4, 
            600 : 21.030e4, 
}

for m in masses:

    mGrav = masses[m]  

    # Must remove the outputFile first"
    outputFile = "AMSB_chargino_" + str(m) + "GeV_Isajet780.slha"  
    os.system("rm -f " + outputFile)	 

    # Create input file
    fin = open("configIsajet.txt", "w")  
    fin.write("'isajet.out' \n")           # output filename in single quotes
    fin.write(outputFile + "\n")           # SUSY Les Houches Accord filename
    fin.write("/ \n")                      # Isawig (Herwig interface) filename
    fin.write("7 \n")                      # 7 for minimal anomaly-mediated SUSY breaking
    fin.write("1500," + str(mGrav) + ",5,1,173.07 \n") # M_0, M_(3/2), tan(beta), sgn(mu), M_t (from 2012 PDG)
    fin.write("0 \n")                      # Run Isatools?  
    fin.close()  

    os.system("rm -f isajet.out")	 # If not removed, Isajet will complain.      
    command = "./isasugra.x < configIsajet.txt" 
    print "About to execute: " + command
    os.system(command)  

    outdir = "../data/"
    os.system("mv -f " + outputFile + " " + outdir)  
    print "Created: " + outputFile  

print "Finished creating slha files"
