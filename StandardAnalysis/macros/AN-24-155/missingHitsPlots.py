import ROOT as r
import cmsstyle as CMS
import numpy as np
import sys

def addPlots(files, plotName, scale=None):
    for i, f in enumerate(files):
        if i == 0:
            h = f.Get(plotName).Clone()
            h.SetDirectory(0)
            test = h.GetBinContent(1)
        else:
            h_tmp = f.Get(plotName)
            test = h_tmp.GetBinContent(1)

            h.Add(f.Get(plotName))
        f.Close()

    if scale:
        h.Scale(scale/h.GetBinContent(1))
    h.Sumw2()
    
    return h

def plotMissingHits(data, th1s, th1_names, era, outputName, outer=False, correctionsOuter=None, correctionsMiddle=None):

    totalCount = np.zeros(th1s[0].GetNbinsX())
    firstBin = data.GetBinContent(1) 
    for h in th1s:
        for b in range(h.GetNbinsX()):
            totalCount[b] += h.GetBinContent(b+1)

    if correctionsOuter is not None:
        for ih, h in enumerate(th1s):
            for ibin in range(1, h.GetNbinsX()+1):
                val = h.GetBinContent(ibin)
                print(th1_names[ih], ibin, val, correctionsOuter[1][ibin-1])
                if ibin >= 6:
                    h.SetBinContent(ibin, val*correctionsOuter[1][ibin-1])
                else:
                    h.SetBinContent(ibin, val*correctionsOuter[0][ibin-1])
            h.Scale(firstBin/totalCount[0])

    elif correctionsMiddle is not None:
        for h in th1s:
            for ibin in range(1, h.GetNbinsX()+1):
                val = h.GetBinContent(ibin)
                h.SetBinContent(ibin, val*correctionsMiddle[ibin-1])
            h.Scale(firstBin/totalCount[0])

    else:
        for ih, h in enumerate(th1s):
            h.Scale(firstBin/totalCount[0])
            print(th1_names[ih], h.GetBinContent(1))

    errors = np.sqrt(totalCount)

    # Styling
    CMS.SetExtraText("Preliminary")
    iPos = 0
    canv_name = 'hist1d_root'
    CMS.SetLumi("")
    CMS.SetEnergy("13.6")
    CMS.ResetAdditionalInfo()


    # Plotting
    stack = r.THStack("stack", "Stacked")
    if outer:
        canv = CMS.cmsCanvas(canv_name,-0.5,15,1e-3,7e6,"Missing Outer Hits","Events",square=CMS.kSquare,extraSpace=0.05,iPos=iPos)
    else:
        canv = CMS.cmsCanvas(canv_name,-0.5,5,1e-3,7e6,"Missing Middle Hits","Events",square=CMS.kSquare,extraSpace=0.05,iPos=iPos)

    leg = CMS.cmsLeg(0.61, 0.89 - 0.05 * 7, 0.99, 0.89, textSize=0.04)
    leg.AddEntry(data, f'MET {era}', 'lp')

    # Put samples in a dict {sample: th1} and draw
    hist_dict = dict(zip([name.split("_")[-1] for name in th1_names], th1s))
    CMS.cmsDrawStack(stack, leg, hist_dict)
    CMS.GetcmsCanvasHist(canv).GetYaxis().SetTitleOffset(1.6)
    CMS.cmsDraw(data, "P", mcolor=r.kBlack)

    canv.Draw()
    canv.SetLogy()

    for i, h in enumerate(th1s):
        if i==0:
            hTotal = h
        else:
            hTotal.Add(h)

    n = th1s[0].GetNbinsX()+1

    # Create the graph with asymmetric errors
    graph = r.TGraphAsymmErrors(hTotal)

    # Style the graph
    graph.SetTitle("Box Plot with Errors;X-axis;Y-axis")
    # Set cross-hatched style for errors

    # Draw the error band on the canvas
    CMS.cmsDraw(graph, "E2", fstyle=3744, fcolor=r.kBlack, alpha=0.01)
    leg.AddEntry(graph, 'MC Error', 'f')
    r.gPad.RedrawAxis()

    print("saving canvas as ", outputName)
    canv.SaveAs(outputName)

def get2022CDPlots(plotName, era='2022CD'):

    signal = r.TFile.Open('/abyss/users/mcarrigan/MET_run3/MET_2022CD_MissingHitsSelection/MET_2022CD.root')
    h_signal = signal.Get(plotName)
    h_signal.SetDirectory(0)
    firstBin = h_signal.GetBinContent(1)

    wlnu = r.TFile.Open('/abyss/users/mcarrigan/MissingHitsCorrections/2022_preEE/MissingHits_WtoLNu-4Jets_2022_preEE_v2/WToLNu_4Jets_2022.root')
    h_wlnu = addPlots([wlnu], plotName)

    DYJetsToLL = r.TFile.Open('/abyss/users/mcarrigan/MissingHitsCorrections/2022_preEE/MissingHits_DYJetsToLL_M50_2022_preEE/DYJetsToLL_M50_2022.root')
    DYto2L_4Jets = r.TFile.Open('/abyss/users/mcarrigan/MissingHitsCorrections/2022_preEE/MissingHits_DYto2L_4jets_M10to50_2022_preEE/DYto2L_4jets_M10to50_2022.root')
    zll = [DYJetsToLL, DYto2L_4Jets]
    print("Combining Z->ll plots")
    h_zll = addPlots(zll, plotName)


    ttb_l = r.TFile.Open('/abyss/users/mcarrigan/MissingHitsCorrections/2022_preEE/MissingHits_TTto2L2Nu_2022_preEE/TTto2L2Nu_2022.root')
    ttb_q = r.TFile.Open('/abyss/users/mcarrigan/MissingHitsCorrections/2022_preEE/MissingHits_TTto4Q_2022_preEE/TTto4Q_2022.root')
    ttb = [ttb_l, ttb_q]
    print("Combining TT plots")
    h_ttb = addPlots(ttb, plotName)

    qcd15 = r.TFile.Open('/abyss/users/mcarrigan/MissingHitsCorrections/2022_preEE/MissingHits_QCD_PT15to30_2022_preEE/QCD_PT15to30_2022.root')
    qcd30 = r.TFile.Open('/abyss/users/mcarrigan/MissingHitsCorrections/2022_preEE/MissingHits_QCD_PT30to50_2022_preEE/QCD_PT30to50_2022.root')
    qcd50 = r.TFile.Open('/abyss/users/mcarrigan/MissingHitsCorrections/2022_preEE/MissingHits_QCD_PT50to80_2022_preEE/QCD_PT50to80_2022.root')
    qcd80 = r.TFile.Open('/abyss/users/mcarrigan/MissingHitsCorrections/2022_preEE/MissingHits_QCD_PT80to120_2022_preEE/QCD_PT80to120_2022.root')
    qcd120 = r.TFile.Open('/abyss/users/mcarrigan/MissingHitsCorrections/2022_preEE/MissingHits_QCD_PT120to170_2022_preEE/QCD_PT120to170_2022.root')
    qcd170 = r.TFile.Open('/abyss/users/mcarrigan/MissingHitsCorrections/2022_preEE/MissingHits_QCD_PT170to300_2022_preEE/QCD_PT170to300_2022.root')
    qcd300 = r.TFile.Open('/abyss/users/mcarrigan/MissingHitsCorrections/2022_preEE/MissingHits_QCD_PT300to470_2022_preEE/QCD_PT300to470_2022.root')
    qcd470 = r.TFile.Open('/abyss/users/mcarrigan/MissingHitsCorrections/2022_preEE/MissingHits_QCD_PT470to600_2022_preEE/QCD_PT470to600_2022.root')
    qcd600 = r.TFile.Open('/abyss/users/mcarrigan/MissingHitsCorrections/2022_preEE/MissingHits_QCD_PT600to800_2022_preEE/QCD_PT600to800_2022.root')
    qcd800 = r.TFile.Open('/abyss/users/mcarrigan/MissingHitsCorrections/2022_preEE/MissingHits_QCD_PT800to1000_2022_preEE/QCD_PT800to1000_2022.root')
    qcd1000 = r.TFile.Open('/abyss/users/mcarrigan/MissingHitsCorrections/2022_preEE/MissingHits_QCD_PT1000to1400_2022_preEE/QCD_PT1000to1400_2022.root')
    qcd1400 = r.TFile.Open('/abyss/users/mcarrigan/MissingHitsCorrections/2022_preEE/MissingHits_QCD_PT1400to1800_2022_preEE/QCD_PT1400to1800_2022.root')
    qcd1800 = r.TFile.Open('/abyss/users/mcarrigan/MissingHitsCorrections/2022_preEE/MissingHits_QCD_PT1800to2400_2022_preEE/QCD_PT1800to2400_2022.root')
    qcd2400 = r.TFile.Open('/abyss/users/mcarrigan/MissingHitsCorrections/2022_preEE/MissingHits_QCD_PT2400to3200_2022_preEE/QCD_PT2400to3200_2022.root')
    qcd3200 = r.TFile.Open('/abyss/users/mcarrigan/MissingHitsCorrections/2022_preEE/MissingHits_QCD_PT3200_2022_preEE/QCD_PT3200_2022.root')
    qcd = [qcd15, qcd30, qcd50, qcd80, qcd120, qcd170, qcd300, qcd470, qcd600, qcd800, qcd1000, qcd1400, qcd1800, qcd2400, qcd3200]
    print("Combining QCD plots")
    h_qcd = addPlots(qcd, plotName)

    tbarB = r.TFile.Open('/abyss/users/mcarrigan/MissingHitsCorrections/2022_preEE/MissingHits_TbarBtoLminusNuB_2022_preEE/TbarBtoLminusNuB_2022.root')
    tBbar = r.TFile.Open('/abyss/users/mcarrigan/MissingHitsCorrections/2022_preEE/MissingHits_TBbartoLplusNuBbar_2022_preEE/TBbartoLplusNuBbar_2022.root')
    tbarQ = r.TFile.Open('/abyss/users/mcarrigan/MissingHitsCorrections/2022_preEE/MissingHits_TbarQtoLNu_2022_preEE/TbarQtoLNu_2022.root')
    tqBar = r.TFile.Open('/abyss/users/mcarrigan/MissingHitsCorrections/2022_preEE/MissingHits_TQbartoLNu_2022_preEE/TQbartoLNu_2022.root')
    tbarW2L = r.TFile.Open('/abyss/users/mcarrigan/MissingHitsCorrections/2022_preEE/MissingHits_TbarWplusto2L2Nu_2022_preEE/TbarWplusto2L2Nu_2022.root')
    tbarWL = r.TFile.Open('/abyss/users/mcarrigan/MissingHitsCorrections/2022_preEE/MissingHits_TbarWplustoLNu2Q_2022_preEE/TbarWplustoLNu2Q_2022.root')
    tW2L = r.TFile.Open('/abyss/users/mcarrigan/MissingHitsCorrections/2022_preEE/MissingHits_TWminusto2L2Nu_2022_preEE/TWminusto2L2Nu_2022.root')
    tWL = r.TFile.Open('/abyss/users/mcarrigan/MissingHitsCorrections/2022_preEE/MissingHits_TWminustoLNu2Q_2022_preEE/TWminustoLNu2Q_2022.root')
    singleT = [tbarB, tBbar, tbarQ, tqBar, tbarW2L, tbarWL, tW2L, tWL]
    print("Combining single t plots")
    h_t = addPlots(singleT, plotName)

    ww = r.TFile.Open('/abyss/users/mcarrigan/MissingHitsCorrections/2022_preEE/MissingHits_WW_2022_preEE/WW_2022.root')
    wz = r.TFile.Open('/abyss/users/mcarrigan/MissingHitsCorrections/2022_preEE/MissingHits_WZ_2022_preEE/WZ_2022.root')
    zz = r.TFile.Open('/abyss/users/mcarrigan/MissingHitsCorrections/2022_preEE/MissingHits_ZZ_2022_preEE/ZZ_2022.root')
    diboson = [ww, wz, zz]
    print("Combining diboson plots")
    h_diboson = addPlots(diboson, plotName)

    znu100 = r.TFile.Open('/abyss/users/mcarrigan/MissingHitsCorrections/2022_preEE/MissingHits_Zto2Nu_4Jets_HT100to200_2022_preEE/Zto2Nu_4Jets_HT100to200_2022.root')
    znu200 = r.TFile.Open('/abyss/users/mcarrigan/MissingHitsCorrections/2022_preEE/MissingHits_Zto2Nu_4Jets_HT200to400_2022_preEE/Zto2Nu_4Jets_HT200to400_2022.root')
    znu400 = r.TFile.Open('/abyss/users/mcarrigan/MissingHitsCorrections/2022_preEE/MissingHits_Zto2Nu_4Jets_HT400to800_2022_preEE/Zto2Nu_4Jets_HT400to800_2022.root')
    znu800 = r.TFile.Open('/abyss/users/mcarrigan/MissingHitsCorrections/2022_preEE/MissingHits_Zto2Nu_4Jets_HT800to1500_2022_preEE/Zto2Nu_4Jets_HT800to1500_2022.root')
    znu1500 = r.TFile.Open('/abyss/users/mcarrigan/MissingHitsCorrections/2022_preEE/MissingHits_Zto2Nu_4Jets_HT1500to2500_2022_preEE/Zto2Nu_4Jets_HT1500to2500_2022.root')
    znu2500 = r.TFile.Open('/abyss/users/mcarrigan/MissingHitsCorrections/2022_preEE/MissingHits_Zto2Nu_4Jets_HT2500_2022_preEE/Zto2Nu_4Jets_HT2500_2022.root')
    znu = [znu100, znu200, znu400, znu800, znu1500, znu2500]
    print("Combining Z->nunu plots")
    h_znu = addPlots(znu, plotName)

    th1_names = ['Z#rightarrow#nu#bar{#nu}', 'Diboson', 'Single top', 'QCD', 't#bar{t}', 'Z#rightarrowll', 'W#rightarrowl#nu']

    th1s = [h_znu, h_diboson, h_t, h_qcd, h_ttb, h_zll, h_wlnu]

    for h in th1s:
        h.SetDirectory(0)

    return th1s, th1_names, h_signal

def get2022EFGPlots(plotName, era='2022EFG'):

    signal = r.TFile.Open(f'/abyss/users/mcarrigan/MET_run3/MET_2022EFG_MissingHitsSelection/MET_{era}.root')
    h_signal = signal.Get(plotName)
    h_signal.SetDirectory(0)
    firstBin = h_signal.GetBinContent(1)

    backgroundDir = '/abyss/users/mcarrigan/MissingHitsCorrections/2022_postEE/'

    wlnu = r.TFile.Open(f'{backgroundDir}/WToLNu_4Jets_2022EE/WToLNu_4Jets_2022EE_{era}.root')
    h_wlnu = addPlots([wlnu], plotName)

    DYJetsToLL = r.TFile.Open(f'{backgroundDir}/DYJetsToLL_M50_2022EE/DYJetsToLL_M50_2022EE_{era}.root ')
    DYto2L_4Jets = r.TFile.Open(f'{backgroundDir}/DYto2L_4jets_M10to50_2022EE/DYto2L_4jets_M10to50_2022EE_{era}.root')

    zll = [DYJetsToLL, DYto2L_4Jets]
    print("Combining Z->ll plots")
    h_zll = addPlots(zll, plotName)


    ttb_l = r.TFile.Open(f'{backgroundDir}/TTto2L2Nu_2022EE/TTto2L2Nu_2022EE_{era}.root')
    ttb_q = r.TFile.Open(f'{backgroundDir}/TTto4Q_2022EE/TTto4Q_2022EE_{era}.root')
    ttb = [ttb_l, ttb_q]
    print("Combining TT plots")
    h_ttb = addPlots(ttb, plotName)

    qcd15 = r.TFile.Open(f'{backgroundDir}/QCD_PT15to30_2022EE/QCD_PT15to30_2022EE_{era}.root')
    qcd30 = r.TFile.Open(f'{backgroundDir}/QCD_PT30to50_2022EE/QCD_PT30to50_2022EE_{era}.root')
    qcd50 = r.TFile.Open(f'{backgroundDir}/QCD_PT50to80_2022EE/QCD_PT50to80_2022EE_{era}.root')
    qcd80 = r.TFile.Open(f'{backgroundDir}/QCD_PT80to120_2022EE/QCD_PT80to120_2022EE_{era}.root')
    qcd120 = r.TFile.Open(f'{backgroundDir}/QCD_PT120to170_2022EE/QCD_PT120to170_2022EE_{era}.root')
    qcd170 = r.TFile.Open(f'{backgroundDir}/QCD_PT170to300_2022EE/QCD_PT170to300_2022EE_{era}.root')
    qcd300 = r.TFile.Open(f'{backgroundDir}/QCD_PT300to470_2022EE/QCD_PT300to470_2022EE_{era}.root')
    qcd470 = r.TFile.Open(f'{backgroundDir}/QCD_PT470to600_2022EE/QCD_PT470to600_2022EE_{era}.root')
    qcd600 = r.TFile.Open(f'{backgroundDir}/QCD_PT600to800_2022EE/QCD_PT600to800_2022EE_{era}.root')
    qcd800 = r.TFile.Open(f'{backgroundDir}/QCD_PT800to1000_2022EE/QCD_PT800to1000_2022EE_{era}.root')
    qcd1000 = r.TFile.Open(f'{backgroundDir}/QCD_PT1000to1400_2022EE/QCD_PT1000to1400_2022EE_{era}.root')
    qcd1400 = r.TFile.Open(f'{backgroundDir}/QCD_PT1400to1800_2022EE/QCD_PT1400to1800_2022EE_{era}.root')
    qcd1800 = r.TFile.Open(f'{backgroundDir}/QCD_PT1800to2400_2022EE/QCD_PT1800to2400_2022EE_{era}.root')
    qcd2400 = r.TFile.Open(f'{backgroundDir}/QCD_PT2400to3200_2022EE/QCD_PT2400to3200_2022EE_{era}.root')
    qcd3200 = r.TFile.Open(f'{backgroundDir}/QCD_PT3200_2022EE/QCD_PT3200_2022EE_{era}.root')
    qcd = [qcd15, qcd30, qcd50, qcd80, qcd120, qcd170, qcd300, qcd470, qcd600, qcd800, qcd1000, qcd1400, qcd1800, qcd2400, qcd3200]
    print("Combining QCD plots")
    h_qcd = addPlots(qcd, plotName)

    tbarB = r.TFile.Open(f'{backgroundDir}/TbarBtoLminusNuB_2022EE/TbarBtoLminusNuB_2022EE_{era}.root')
    tBbar = r.TFile.Open(f'{backgroundDir}/TBbartoLplusNuBbar_2022EE/TBbartoLplusNuBbar_2022EE_{era}.root')
    tbarQ = r.TFile.Open(f'{backgroundDir}/TbarQtoLNu_2022EE/TbarQtoLNu_2022EE_{era}.root')
    tqBar = r.TFile.Open(f'{backgroundDir}/TQbartoLNu_2022EE/TQbartoLNu_2022EE_{era}.root')
    tbarW2L = r.TFile.Open(f'{backgroundDir}/TbarWplusto2L2Nu_2022EE/TbarWplusto2L2Nu_2022EE_{era}.root')
    tbarWL = r.TFile.Open(f'{backgroundDir}/TbarWplustoLNu2Q_2022EE/TbarWplustoLNu2Q_2022EE_{era}.root')
    tW2L = r.TFile.Open(f'{backgroundDir}/TWminusto2L2Nu_2022EE/TWminusto2L2Nu_2022EE_{era}.root')
    tWL = r.TFile.Open(f'{backgroundDir}/TWminustoLNu2Q_2022EE/TWminustoLNu2Q_2022EE_{era}.root')
    singleT = [tbarB, tBbar, tbarQ, tqBar, tbarW2L, tbarWL, tW2L, tWL]
    print("Combining single t plots")
    h_t = addPlots(singleT, plotName)

    ww = r.TFile.Open(f'{backgroundDir}/WW_2022EE/WW_2022EE_{era}.root')
    wz = r.TFile.Open(f'{backgroundDir}/WZ_2022EE/WZ_2022EE_{era}.root')
    zz = r.TFile.Open(f'{backgroundDir}/ZZ_2022EE/ZZ_2022EE_{era}.root')
    diboson = [ww, wz, zz]
    print("Combining diboson plots")
    h_diboson = addPlots(diboson, plotName)

    znu100 = r.TFile.Open(f'{backgroundDir}/Zto2Nu_4Jets_HT100to200_2022EE/Zto2Nu_4Jets_HT100to200_2022EE_{era}.root')
    znu200 = r.TFile.Open(f'{backgroundDir}/Zto2Nu_4Jets_HT200to400_2022EE/Zto2Nu_4Jets_HT200to400_2022EE_{era}.root')
    znu400 = r.TFile.Open(f'{backgroundDir}/Zto2Nu_4Jets_HT400to800_2022EE/Zto2Nu_4Jets_HT400to800_2022EE_{era}.root')
    znu800 = r.TFile.Open(f'{backgroundDir}/Zto2Nu_4Jets_HT800to1500_2022EE/Zto2Nu_4Jets_HT800to1500_2022EE_{era}.root')
    znu1500 = r.TFile.Open(f'{backgroundDir}/Zto2Nu_4Jets_HT1500to2500_2022EE/Zto2Nu_4Jets_HT1500to2500_2022EE_{era}.root')
    znu2500 = r.TFile.Open(f'{backgroundDir}/Zto2Nu_4Jets_HT2500_2022EE/Zto2Nu_4Jets_HT2500_2022EE_{era}.root')
    znu = [znu100, znu200, znu400, znu800, znu1500, znu2500]
    print("Combining Z->nunu plots")
    h_znu = addPlots(znu, plotName)

    th1_names = ['Z#rightarrow#nu#bar{#nu}', 'Diboson', 'Single top', 'QCD', 't#bar{t}', 'Z#rightarrowll', 'W#rightarrowl#nu']

    th1s = [h_znu, h_diboson, h_t, h_qcd, h_ttb, h_zll, h_wlnu]

    for h in th1s:
        h.SetDirectory(0)

    return th1s, th1_names, h_signal

def getCorrectionsOuter(era):
    
    correctionsPRE = []
    correctionsPOST = []

    if era=='2022CD':
        correctedPRE = r.TFile.Open('/abyss/users/mcarrigan/MissingHitsCorrections/2022_preEE/missingOuterPRETOBCorrected_2022CD.root')
        correctedPOST = r.TFile.Open('/abyss/users/mcarrigan/MissingHitsCorrections/2022_preEE/missingOuterPOSTTOBCorrected_2022CD.root')

        raw = r.TFile.Open('/abyss/users/mcarrigan/MissingHitsCorrections/2022_preEE/MissingHits_2022.root')

        h_raw = raw.Get('HitsSystematicsCtrlSelectionPlotter/Track Plots/trackNHitsMissingOuter')
        h_correctedPRE = correctedPRE.Get('correctedMC')
        h_correctedPOST = correctedPOST.Get('correctedMC')
    
    elif era=='2022EFG':
        correctedPRE = r.TFile.Open('/abyss/users/mcarrigan/MissingHitsCorrections/2022_postEE/missingOuterPRETOBCorrected_2022EFG.root')
        correctedPOST = r.TFile.Open('/abyss/users/mcarrigan/MissingHitsCorrections/2022_postEE/missingOuterPOSTTOBCorrected_2022EFG.root')

        raw = r.TFile.Open('/abyss/users/mcarrigan/MissingHitsCorrections/2022_postEE/MissingHits_2022EFG.root')

        h_raw = raw.Get('HitsSystematicsCtrlSelectionPlotter/Track Plots/trackNHitsMissingOuter')
        h_correctedPRE = correctedPRE.Get('correctedMC')
        h_correctedPOST = correctedPOST.Get('correctedMC')

    else:
        print("Era provided is not available")
        sys.exit(1)

    for i in range(1, h_raw.GetNbinsX()+1):
        n_raw = h_raw.GetBinContent(i)
        n_corPRE = h_correctedPRE.GetBinContent(i)
        n_corPOST = h_correctedPOST.GetBinContent(i)

        if n_raw >0:
            ratioPRE = n_corPRE/n_raw
            ratioPOST = n_corPOST/n_raw
        else:
            ratio = 0
        #print(f"raw {n_raw}, corrected {n_cor}, ratio: {ratio}")
        correctionsPRE.append(ratioPRE)
        correctionsPOST.append(ratioPOST)
    
    return correctionsPRE, correctionsPOST

def getCorrectionsMiddle(era):
    corrections = []

    if era=='2022CD':
        corrected = r.TFile.Open('/abyss/users/mcarrigan/MissingHitsCorrections/2022_preEE/missingMiddleCorrected_2022CD.root')
        raw = r.TFile.Open('/abyss/users/mcarrigan/MissingHitsCorrections/2022_preEE/MissingHits_2022.root')

        h_raw = raw.Get('HitsSystematicsCtrlSelectionPlotter/Track Plots/trackNHitsMissingMiddle')
        h_corrected = corrected.Get('correctedMC')
    
    elif era=='2022EFG':
        corrected = r.TFile.Open('/abyss/users/mcarrigan/MissingHitsCorrections/2022_postEE/missingMiddleCorrected_2022EFG.root')
        raw = r.TFile.Open('/abyss/users/mcarrigan/MissingHitsCorrections/2022_postEE/MissingHits_2022EFG.root')

        h_raw = raw.Get('HitsSystematicsCtrlSelectionPlotter/Track Plots/trackNHitsMissingMiddle')
        h_corrected = corrected.Get('correctedMC')

    else:
        print("era provided is not available")
        sys.exit(1)


    for i in range(1, h_raw.GetNbinsX()+1):
        n_raw = h_raw.GetBinContent(i)
        n_cor = h_corrected.GetBinContent(i)
        if n_raw >0:
            ratio = n_cor/n_raw
        else:
            ratio = 0
        print(f"raw {n_raw}, corrected {n_cor}, ratio: {ratio}")
        corrections.append(ratio)

    return corrections

if __name__ == "__main__":

    r.gStyle.SetHatchesLineWidth=0.3
    r.gStyle.SetHatchesLineSpacing=0.5
    r.gROOT.SetBatch(1)

    print("running main")

    plotOuterName = 'HitsSystematicsCtrlSelectionPlotter/Track Plots/trackNHitsMissingOuter'
    plotMiddleName = 'HitsSystematicsCtrlSelectionPlotter/Track Plots/trackNHitsMissingMiddle'

    hists, names, data = get2022EFGPlots(plotOuterName)
    plotMissingHits(data, hists, names, '2022EFG', 'missingOuterHits_2022EFG.png', outer=True)

    hists, names, data = get2022EFGPlots(plotOuterName)
    correctionsOuter = getCorrectionsOuter('2022EFG')
    plotMissingHits(data, hists, names, '2022EFG', 'missingOuterHitsCorrected_2022EFG.png', outer=True, correctionsOuter=correctionsOuter)

    hists, names, data = get2022EFGPlots(plotMiddleName)
    plotMissingHits(data, hists, names, '2022EFG', 'missingMiddleHits_2022EFG.png', outer=False)

    hists, names, data = get2022EFGPlots(plotMiddleName)
    correctionsMiddle = getCorrectionsMiddle('2022EFG')
    plotMissingHits(data, hists, names, '2022EFG', 'missingMiddleHitsCorrected_2022EFG.png', outer=False, correctionsMiddle=correctionsMiddle)
        
    hists, names, data = get2022CDPlots(plotOuterName)
    plotMissingHits(data, hists, names, '2022CD', 'missingOuterHits_2022CD.png', outer=True)
    
    hists, names, data = get2022CDPlots(plotOuterName)
    correctionsOuter = getCorrectionsOuter('2022CD')
    plotMissingHits(data, hists, names, '2022CD', 'missingOuterHitsCorrected_2022CD.png', outer=True, correctionsOuter=correctionsOuter)

    hists, names, data = get2022CDPlots(plotMiddleName)
    plotMissingHits(data, hists, names, '2022CD', 'missingMiddleHits_2022CD.png', outer=False)
    
    hists, names, data = get2022CDPlots(plotMiddleName)
    correctionsMiddle = getCorrectionsMiddle('2022CD')
    plotMissingHits(data, hists, names, '2022CD', 'missingMiddleHitsCorrected_2022CD.png', outer=False, correctionsMiddle=correctionsMiddle)