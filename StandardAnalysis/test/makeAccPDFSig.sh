#!/bin/sh                                                                  

PDFSETS="condor_2014_02_24_FullSelSystSig_PDFWt"  
#PDFSETS="PDFSET1FINAL"
BASEPATH=/data/users/wulsin/condor/analysisTemplateV3/ 

CALCULATORFILE=${PWD}/calcUncert

for pdfSet in ${PDFSETS}; do
    
    PDFSCF=1.64485 #C90 for CTEQ                                                                                                                                            
    NPDFSETS=45 #For CTEQ                                                                                                                   
    NFIELDS=47 #FOR CTEQ 44 pdf memebrs + 2 astrong + 1 nominal                                                                                           
    ASSCF=0.83333333 #C59=5/6 for CTEQ                                                                                                                    
    PDFSETNO=1
    if [ ${pdfSet} == "PDFSET2FINAL" ]
	then
	PDFSCF=1 #for MSTW                                                                                                                                                   
	NPDFSETS=41 #for MSTW                                                                                                                                             
	NFIELDS=43 #FOR MSTW 40 pdf members + 2 astrogn +  1 nominal                                                               
	ASSCF=1.25 #C79=5/4 for MSTW                                                                                                                                        
	PDFSETNO=2
    elif [ ${pdfSet} == "PDFSET3FINAL" ]
	then
    #not used for NNPDF except NPDFSETS                                                                                                                                      
	PDFSCF=1 #for NNPDF NEED TO CHECK                                                                                                                          
	NPDFSETS=101 #for NNPDF CHECK CHEC                                                                                                                                
	NFIELDS=101 #FOR NNPDF 100 pdf members + 1 nominal K                                                                                                               
	ASSCF=1 #CHECK                                                                                                                                                   
	PDFSETNO=3
    fi

    PDFPATH=/data/users/wulsin/condor/analysisTemplateV3/${pdfSet}

    echo "#############################################"
    echo "Working on set "${pdfSet}" in path "${PDFPATH}

    echo "%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%"
    echo "Working on Signal Samples"

    for sampleSet in `find ${PDFPATH} -type d -name "AMSB*" -printf '%P\n'`; do


	echo "**********************************************"
	echo "Working with sample "${sampleSet}

	ALLPDFFILE=${PDFPATH}/all_${sampleSet}.txt
	SUMSFILE=${PDFPATH}/sums_${sampleSet}.txt
	MINMAXFILE=${PDFPATH}/minMax_${sampleSet}.txt
	UPDOWNFILE=${PDFPATH}/upDown_${sampleSet}.txt
	
	rm -f ${ALLPDFFILE}
	rm -f ${SUMSFILE}
	rm -f ${MINMAXFILE}
	rm -f ${UPDOWNFILE}

	dir=${PDFPATH}/${sampleSet}
	echo $dir
	cd $dir
	
#	grep -h "XXX" *.out | sed 's/XXX //g' > ${ALLPDFFILE} #This file has all the PDF weights for the set of samples
	grep -h "XXX" *.out > ${ALLPDFFILE} #This file has all the PDF weights for the set of samples

	if [ -s ${ALLPDFFILE} ]; #check if empty
	    then
	    #echo "File not empty, proceeding with sums"
	    echo ""
	else
	    #fill with zeros according to Number of fields
	    echo "$!$!$! File "${ALLPDFFILE}" has no events, filling with "${NFIELDS}" zeros"
	    awk -v nfields=${NFIELDS} 'BEGIN{for (i=0; i<nfields; ++i){printf "0.0 "}; printf "\n"}' > ${ALLPDFFILE}
	fi


	cd ..

	echo "Producing sums of pdf weights in file "${SUMSFILE}
        awk '{for (i=1; i<=NF; ++i) sum[i] += $i; j=NF } END {for (i=1; i <= j; ++i) {printf "%s ",sum[i]}; printf "\n"}' ${ALLPDFFILE} > ${SUMSFILE}

	echo "Putting nominal eff, centr eff and errors on central in file "${UPDOWNFILE}
        echo "Running command:  ${CALCULATORFILE} ${ALLPDFFILE} ${NPDFSETS} ${PDFSETNO} 1 > ${UPDOWNFILE}"  
        ${CALCULATORFILE} ${ALLPDFFILE} ${NPDFSETS} ${PDFSETNO} 1 > ${UPDOWNFILE}

    done


    echo "Combining signal errors"


#    #loop over stopToBT, doesnt matter
#    for mFile in  `find ${PDFPATH} -type d -name "stop*toBT_*mm" -printf '%P\n'`; do
#
#      echo "Using "${mFile}" to find mass and tau"
#      stopMass=`expr match ${mFile:4} '\([0-9]*\)'`
#      idx=`expr index ${mFile} "_"`
#      stopTau=${mFile:idx}
#
#      mergedFile=${PDFPATH}/upDown_signal_${stopMass}_${stopTau}.txt
#
#      echo "Merging samples with mass "${stopMass}" and ctau "${stopTau}
#
#      tmpFile=${PDFPATH}/upDown_tempFile.txt
#      #Merge all in one temp file to sum later.Multiply with the BR factor br50, BR(bl) = 0 => stop->topnu and BR(bl) = 100 => stop->bl
#      #BT: 50%
#      awk '{print $1*0.50,$2*0.50,$3*0.50,$4*0.50}' ${PDFPATH}/upDown_stop${stopMass}toBT_${stopTau}.txt > ${tmpFile}
#      #Bl: 25%
#      awk '{print $1*0.25,$2*0.25,$3*0.25,$4*0.25}' ${PDFPATH}/upDown_stop${stopMass}toBl_${stopTau}.txt >> ${tmpFile}
#      #Tnu: 25%
#      awk '{print $1*0.25,$2*0.25,$3*0.25,$4*0.25}' ${PDFPATH}/upDown_stop${stopMass}toTnu_${stopTau}.txt >> ${tmpFile}
#
#      #Now sum using AWK. Note NF = 4, in this file we have originalAcceptance acc_central wplus wminus
#      echo "TOTAL COMBINED UNCERTAINTIES IN FILE "${mergedFile}
#      awk '{for(i=1; i<=NF; ++i) sum[i] += $i;} END {for (i=1; i<=NF; ++i) {printf "%s ",sum[i]}; printf "\n"}' ${tmpFile} > ${mergedFile}
#      rm -f ${tmpFile}
#    done
done
