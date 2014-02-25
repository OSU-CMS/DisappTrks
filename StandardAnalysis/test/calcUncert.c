// Compile with:
// > g++ calcUncert.c -o calcUncert  
// 
// Usage: 
// ./calcUncert <filename> <npdf> [PDFSET]
// filename: file containing the sums of weights
// npdf: NUmber of PDF members: 45 for CTEQ 41 for MSTW (?) 101 for NNPDF (?)
// PDFSET: Optional argument: 1 for cteq, 2 for mstw, 3 for nnpdf (the only one different)`

// Example usage:
// $ ./calcUncert trackAnalyzerSystSig_cfg-cteq66.log 45 1


#include <iostream>
#include <math.h>
#include <fstream>
#include <stdlib.h>
#include <iomanip>
#include <string.h>
using std::string;  
using std::cout;
using std::endl;

int main(int argc, char * argv[]){


    int pdfSet=1;

    bool print_all=true;

    if(argc<3){
      std::cout<<"Usage: "<<argv[0]<< " "<<" <file name> <nPdfMembers> [pdfset] [print_all_info]"<<std::endl;
      return 0;
    
    }

    if(argc>4)
      print_all=true;

    char *  fname = argv[1];
    int nmembers = atoi(argv[2]);
    pdfSet = atoi(argv[3]);

    std::ifstream rndat;
    
    rndat.open(fname);
    
    if(!rndat.is_open()){
        std::cout<<"File not found!"<<std::endl;
        return 0;
    }


    double weightedEvents_[101];
    double weightedSelectedEvents_[101];
    double weighted2SelectedEvents_;
    double weighted2Events_;

    double sum2_all,sum2_selected;

    
    int originalEvents_, selectedEvents_;
    
    double sum_all, sum_selected;
    
    string tmp;
    tmp = "";  
    while (tmp != "XXX") { 
      rndat >> tmp; 
    } 
    
    rndat >> originalEvents_;
    rndat >> selectedEvents_;
    rndat >> sum_all;
    rndat >> sum_selected;

    rndat >> sum2_all;
    rndat >> sum2_selected;


    rndat >> weighted2Events_;
    rndat >> weighted2SelectedEvents_;



    
    std::cout << "Debug:  original events = " << originalEvents_
	      << "; selectedEvents_=" << selectedEvents_ 
	      << "; sum_all=" << sum_all
	      << "; sum_selected=" << sum_selected 
	      << endl; 

    cout << "Printing weighted selected events: " << endl;  
    for(int i=0; i<nmembers; i++){        
	double we=0.0;
	double ws=0.0;
        rndat>>we;
	weightedEvents_[i]=we;
        rndat>>ws;
	weightedSelectedEvents_[i]=ws;

	std::cout << weightedSelectedEvents_[i]<<" "<<weightedEvents_[i]<<std::endl;
	
    }
    cout << endl;  
    rndat.close();
    

    
    
    bool nnpdfFlag = false;
    
    if(pdfSet==3) nnpdfFlag=true;
    
    unsigned int npairs = (nmembers-1)/2;
    
    //double originalAcceptance = double(selectedEvents_)/originalEvents_;

    double originalAcceptance = sum_selected/sum_all;

    originalEvents_=sum_all;

    if(print_all) std::cerr<<"Original Acceptance: "<<originalAcceptance*100.0<<"%"<<std::endl;
    double acc_central = 0.;
    double acc2_central = 0.;

    if (weightedEvents_[0]>0) {
      acc_central  = weightedSelectedEvents_[0]/weightedEvents_[0]; 
      acc2_central = weighted2SelectedEvents_  /weightedEvents_[0]; 
    }


    double waverage = weightedEvents_[0]/originalEvents_;

    double acc_central_error = (((acc2_central/waverage)-(acc_central*acc_central))/originalEvents_);
    //std::cout << acc_central_error << endl;
    if(print_all) std::cerr<< "\tEstimate for central PDF member acceptance: [" << acc_central*100 << " +- " << 100 * sqrt(acc_central_error) << "] %"<<std::endl;
    double xi = acc_central-originalAcceptance;

    double deltaxi = (acc2_central-(originalAcceptance+2*xi+xi*xi))/originalEvents_;
    
    //std::cout<<"deltaxi2: "<<deltaxi<<std::endl;
    if (deltaxi>0) deltaxi = sqrt(deltaxi); //else deltaxi = 0.;
    if(print_all) std::cerr<< "\ti.e. [" << std::setprecision(4) << 100*xi/originalAcceptance << " +- " << std::setprecision(4) << 100*deltaxi/originalAcceptance << "] % relative variation with respect to the original PDF"<<std::endl;
    
    
    
    double wplus = 0.;
    double wminus = 0.;
    unsigned int nplus = 0;
    unsigned int nminus = 0;
    for (unsigned int j=0; j<npairs; ++j) {
        double wa = 0.;
        if (weightedEvents_[2*j+1]>0) wa = (weightedSelectedEvents_[2*j+1]/weightedEvents_[2*j+1])/acc_central-1.;
        double wb = 0.;
        if (weightedEvents_[2*j+2]>0) wb = (weightedSelectedEvents_[2*j+2]/weightedEvents_[2*j+2])/acc_central-1.;
        if (nnpdfFlag) {
            if (wa>0.) {
                wplus += wa*wa; 
                nplus++;
            } else {
                wminus += wa*wa;
                nminus++;
            }
            if (wb>0.) {
                wplus += wb*wb; 
                nplus++;
            } else {
                wminus += wb*wb;
                nminus++;
            }
        } else {
            if (wa>wb) {
                if (wa<0.) wa = 0.;
                if (wb>0.) wb = 0.;
                wplus += wa*wa;
                wminus += wb*wb;
            } else {
                if (wb<0.) wb = 0.;
                if (wa>0.) wa = 0.;
                wplus += wb*wb;
                wminus += wa*wa;
            }
        }
    }

    if (wplus>0) wplus = sqrt(wplus);
    if (wminus>0) wminus = sqrt(wminus);
    if (nnpdfFlag) {
        if (nplus>0) wplus /= sqrt(nplus);
        if (nminus>0) wminus /= sqrt(nminus);
    }

    if(print_all) std::cerr << "\tRelative uncertainty with respect to central member: +" << std::setprecision(4) << 100.*wplus << " / -" << std::setprecision(4) << 100.*wminus << " [%]"<<std::endl;


    //printout for bulk processing

    std::cout <<originalAcceptance<< " "<<acc_central<<" "<<wplus<<" "<<wminus<<std::endl;
    std::cout <<                                            wplus<<" "<<wminus<<std::endl;

    return 0;
 
}
