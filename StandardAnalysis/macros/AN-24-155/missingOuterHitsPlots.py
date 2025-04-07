import ROOT as r
import cmsstyle as CMS
import numpy as np

def addPlots(files, plotName, scale=None):
    for i, f in enumerate(files):
        if i == 0:
            h = f.Get(plotName).Clone()
            h.SetDirectory(0)
            test = h.GetBinContent(1)
            if test-round(test) == 0:
                print(f'index {i} may not be scaled')
                print(test, round(test))
        else:
            h_tmp = f.Get(plotName)
            test = h_tmp.GetBinContent(1)
            if test - round(test) ==0:
                print(f'index {i} may not be scaled')
                print(test, round(test))

            h.Add(f.Get(plotName))
        f.Close()

    if scale:
        h.Scale(scale/h.GetBinContent(1))
    h.Sumw2()
    
    return h

# File reading 

r.gStyle.SetHatchesLineWidth=0.1
r.gStyle.SetHatchesLineSpacing=1

#plotName = 'MuonCtrlSelectionPlotter/Track Plots/trackNHitsMissingOuter'
plotName = 'HitsSystematicsCtrlSelectionPlotter/Track Plots/trackNHitsMissingOuter'

signal = r.TFile.Open('/data/users/mcarrigan/condor/MET_2022/MET_2022F_MissingHitsCorrection/MET_2022F.root')
h_signal = signal.Get(plotName)
firstBin = h_signal.GetBinContent(1)

# correctedMC = r.TFile.Open('hitAndTOBDropHistogram_postTOB.root')
# correctedMC = r.TFile.Open('hitAndTOBDropHistogram_preTOB.root')
# correctedMC = r.TFile.Open('hitAndTOBDropHistogram_postTOB_halfP.root')
# correctedMC = r.TFile.Open('hitAndTOBDropHistogram_preTOB_halfP.root')
# correctedMC = r.TFile.Open('hitAndTOBDropHistogram_postTOB_doubleP.root')
correctedMC = r.TFile.Open('hitAndTOBDropHistogram_preTOB_doubleP.root')
h_correctedMC = correctedMC.Get('correctedMC')

totalCountcorrectedMC = np.zeros(h_correctedMC.GetNbinsX())
for b in range(h_correctedMC.GetNbinsX()):
        totalCountcorrectedMC[b] += h_correctedMC.GetBinContent(b+1)

h_correctedMC.Scale(firstBin/totalCountcorrectedMC[0])

wlnu = r.TFile.Open('/abyss/users/mcarrigan/MissingHitsCorrections/WToLNu_4Jets_2022EE/WToLNu_4Jets_2022EE_2022F.root')
h_wlnu = addPlots([wlnu], plotName)

zll100 = r.TFile.Open('/abyss/users/mcarrigan/MissingHitsCorrections/Zto2Nu_4Jets_HT100to200_2022EE/Zto2Nu_4Jets_HT100to200_2022EE_2022F.root')
zll200 = r.TFile.Open('/abyss/users/mcarrigan/MissingHitsCorrections/Zto2Nu_4Jets_HT200to400_2022EE/Zto2Nu_4Jets_HT200to400_2022EE_2022F.root')
zll400 = r.TFile.Open('/abyss/users/mcarrigan/MissingHitsCorrections/Zto2Nu_4Jets_HT400to800_2022EE/Zto2Nu_4Jets_HT400to800_2022EE_2022F.root')
zll800 = r.TFile.Open('/abyss/users/mcarrigan/MissingHitsCorrections/Zto2Nu_4Jets_HT800to1500_2022EE/Zto2Nu_4Jets_HT800to1500_2022EE_2022F.root')
zll1500 = r.TFile.Open('/abyss/users/mcarrigan/MissingHitsCorrections/Zto2Nu_4Jets_HT1500to2500_2022EE/Zto2Nu_4Jets_HT1500to2500_2022EE_2022F.root')
zll2500 = r.TFile.Open('/abyss/users/mcarrigan/MissingHitsCorrections/Zto2Nu_4Jets_HT2500_2022EE/Zto2Nu_4Jets_HT2500_2022EE_2022F.root')

zll = [zll100, zll200, zll400, zll800, zll1500, zll2500]
print("Combining Z->ll plots")
h_zll = addPlots(zll, plotName)


ttb_l = r.TFile.Open('/abyss/users/mcarrigan/MissingHitsCorrections/TTto2L2Nu_2022EE/TTto2L2Nu_2022EE_2022F.root')
ttb_q = r.TFile.Open('/abyss/users/mcarrigan/MissingHitsCorrections/TTto4Q_2022EE/TTto4Q_2022EE_2022F.root')
ttb = [ttb_l, ttb_q]
print("Combining TT plots")
h_ttb = addPlots(ttb, plotName)

qcd15 = r.TFile.Open('/abyss/users/mcarrigan/MissingHitsCorrections/QCD_PT15to30_2022EE/QCD_PT15to30_2022EE_2022F.root')
qcd30 = r.TFile.Open('/abyss/users/mcarrigan/MissingHitsCorrections/QCD_PT30to50_2022EE/QCD_PT30to50_2022EE_2022F.root')
qcd50 = r.TFile.Open('/abyss/users/mcarrigan/MissingHitsCorrections/QCD_PT50to80_2022EE/QCD_PT50to80_2022EE_2022F.root')
qcd80 = r.TFile.Open('/abyss/users/mcarrigan/MissingHitsCorrections/QCD_PT80to120_2022EE/QCD_PT80to120_2022EE_2022F.root')
qcd120 = r.TFile.Open('/abyss/users/mcarrigan/MissingHitsCorrections/QCD_PT120to170_2022EE/QCD_PT120to170_2022EE_2022F.root')
qcd170 = r.TFile.Open('/abyss/users/mcarrigan/MissingHitsCorrections/QCD_PT170to300_2022EE/QCD_PT170to300_2022EE_2022F.root')
qcd300 = r.TFile.Open('/abyss/users/mcarrigan/MissingHitsCorrections/QCD_PT300to470_2022EE/QCD_PT300to470_2022EE_2022F.root')
qcd470 = r.TFile.Open('/abyss/users/mcarrigan/MissingHitsCorrections/QCD_PT470to600_2022EE/QCD_PT470to600_2022EE_2022F.root')
qcd600 = r.TFile.Open('/abyss/users/mcarrigan/MissingHitsCorrections/QCD_PT600to800_2022EE/QCD_PT600to800_2022EE_2022F.root')
qcd800 = r.TFile.Open('/abyss/users/mcarrigan/MissingHitsCorrections/QCD_PT800to1000_2022EE/QCD_PT800to1000_2022EE_2022F.root')
qcd1000 = r.TFile.Open('/abyss/users/mcarrigan/MissingHitsCorrections/QCD_PT1000to1400_2022EE/QCD_PT1000to1400_2022EE_2022F.root')
qcd1400 = r.TFile.Open('/abyss/users/mcarrigan/MissingHitsCorrections/QCD_PT1400to1800_2022EE/QCD_PT1400to1800_2022EE_2022F.root')
qcd1800 = r.TFile.Open('/abyss/users/mcarrigan/MissingHitsCorrections/QCD_PT1800to2400_2022EE/QCD_PT1800to2400_2022EE_2022F.root')
qcd2400 = r.TFile.Open('/abyss/users/mcarrigan/MissingHitsCorrections/QCD_PT2400to3200_2022EE/QCD_PT2400to3200_2022EE_2022F.root')
qcd3200 = r.TFile.Open('/abyss/users/mcarrigan/MissingHitsCorrections/QCD_PT3200_2022EE/QCD_PT3200_2022EE_2022F.root')
qcd = [qcd15, qcd30, qcd50, qcd80, qcd120, qcd170, qcd300, qcd470, qcd600, qcd800, qcd1000, qcd1400, qcd1800, qcd2400, qcd3200]
print("Combining QCD plots")
h_qcd = addPlots(qcd, plotName)

tbarB = r.TFile.Open('/abyss/users/mcarrigan/MissingHitsCorrections/TbarBtoLminusNuB_2022EE/TbarBtoLminusNuB_2022EE_2022F.root')
tBbar = r.TFile.Open('/abyss/users/mcarrigan/MissingHitsCorrections/TBbartoLplusNuBbar_2022EE/TBbartoLplusNuBbar_2022EE_2022F.root')
tbarQ = r.TFile.Open('/abyss/users/mcarrigan/MissingHitsCorrections/TbarQtoLNu_2022EE/TbarQtoLNu_2022EE_2022F.root')
tqBar = r.TFile.Open('/abyss/users/mcarrigan/MissingHitsCorrections/TQbartoLNu_2022EE/TQbartoLNu_2022EE_2022F.root')
tbarW2L = r.TFile.Open('/abyss/users/mcarrigan/MissingHitsCorrections/TbarWplusto2L2Nu_2022EE/TbarWplusto2L2Nu_2022EE_2022F.root')
tbarWL = r.TFile.Open('/abyss/users/mcarrigan/MissingHitsCorrections/TbarWplustoLNu2Q_2022EE/TbarWplustoLNu2Q_2022EE_2022F.root')
tW2L = r.TFile.Open('/abyss/users/mcarrigan/MissingHitsCorrections/TWminusto2L2Nu_2022EE/TWminusto2L2Nu_2022EE_2022F.root')
tWL = r.TFile.Open('/abyss/users/mcarrigan/MissingHitsCorrections/TWminustoLNu2Q_2022EE/TWminustoLNu2Q_2022EE_2022F.root')
singleT = [tbarB, tBbar, tbarQ, tqBar, tbarW2L, tbarWL, tW2L, tWL]
print("Combining single t plots")
h_t = addPlots(singleT, plotName)

ww = r.TFile.Open('/abyss/users/mcarrigan/MissingHitsCorrections/WW_2022EE/WW_2022EE_2022F.root')
wz = r.TFile.Open('/abyss/users/mcarrigan/MissingHitsCorrections/WZ_2022EE/WZ_2022EE_2022F.root')
zz = r.TFile.Open('/abyss/users/mcarrigan/MissingHitsCorrections/ZZ_2022EE/ZZ_2022EE_2022F.root')
diboson = [ww, wz, zz]
print("Combining diboson plots")
h_diboson = addPlots(diboson, plotName)

znu100 = r.TFile.Open('/abyss/users/mcarrigan/MissingHitsCorrections/Zto2Nu_4Jets_HT100to200_2022EE/Zto2Nu_4Jets_HT100to200_2022EE_2022F.root')
znu200 = r.TFile.Open('/abyss/users/mcarrigan/MissingHitsCorrections/Zto2Nu_4Jets_HT200to400_2022EE/Zto2Nu_4Jets_HT200to400_2022EE_2022F.root')
znu400 = r.TFile.Open('/abyss/users/mcarrigan/MissingHitsCorrections/Zto2Nu_4Jets_HT400to800_2022EE/Zto2Nu_4Jets_HT400to800_2022EE_2022F.root')
znu800 = r.TFile.Open('/abyss/users/mcarrigan/MissingHitsCorrections/Zto2Nu_4Jets_HT800to1500_2022EE/Zto2Nu_4Jets_HT800to1500_2022EE_2022F.root')
znu1500 = r.TFile.Open('/abyss/users/mcarrigan/MissingHitsCorrections/Zto2Nu_4Jets_HT1500to2500_2022EE/Zto2Nu_4Jets_HT1500to2500_2022EE_2022F.root')
znu2500 = r.TFile.Open('/abyss/users/mcarrigan/MissingHitsCorrections/Zto2Nu_4Jets_HT2500_2022EE/Zto2Nu_4Jets_HT2500_2022EE_2022F.root')
znu = [znu100, znu200, znu400, znu800, znu1500, znu2500]
print("Combining Z->nunu plots")
h_znu = addPlots(znu, plotName)

# prob = 'postTOB'
# prob = 'preTOB'
prob = 'mixed'

binnedCorrection = []

threshold = 6

binnedCorrectionPostTOB = [1.0, 1.0028952226015364, 0.9954615790217907, 1.5360008974664505, 1.5706034974119751, 2.657997768458255, 3.2044129988363164, 2.6713030277892793, 4.881716485767847, 2.6039717235626934, 20.705377143774587, 60.339286841916966, 17.978981535817983, 59.34346038287958, 1.0] # postTOB
binnedCorrectionPreTOB = [1.0, 1.0407596592724577, 1.1063213373961471, 3.8623416144748632, 5.065828801442446, 14.483421061701453, 23.27161434455519, 0.829440658392452, 0.764700097612659, 0.05202090429706944, 0.3735172204174315, 0.9787658397137555, 0.0002898523845860886, 0.0, 1.0] # preTOB
# binnedCorrectionPostTOB = [1.0, 1.0023616932407697, 0.9858398741643297, 1.3231201683994342, 1.2769400574228331, 2.1583475308597984, 2.614379628748534, 1.519037978945389, 1.5371326064022055, 0.2806804668936552, 1.5217345019003696, 2.041607646380763, 0.1948119785373079, 0.33284734819746037, 1.0] # postTOB halfP
# binnedCorrectionPreTOB = [1.0, 1.0173617018463652, 1.0396402395838893, 2.4623467447715432, 2.9810717123625237, 7.794231175887937, 12.08435285860861, 0.8284874153250804, 0.7648125354966799, 0.05178310424658222, 0.3731353684405556, 0.9787065907424558, 0.00014485189910422557, 0.0, 1.0] # preTOB halfP
# binnedCorrectionPostTOB = [1.0, 0.984445463121978, 0.9370145200869698, 0.43330049489742034, 0.3038231321287695, 0.14598022859946477, 0.3740507192135412, 0.6676699079849372, 1.9926191801416129, 19.567156934994145, 64.32312753709212, 265.19766797480696, 1214.2464237106074, 2315.8774419639303, 1.0] # postTOB doubleP
# binnedCorrectionPreTOB = [1.0, 1.054886774891832, 1.18876105395044, 2.716490024305133, 3.1074915930578997, 3.585629746968489, 122.42117394975367, 1.2423424112419548, 0.3855996098917745, 0.0026830935668460676, 0.005812822352839629, 0.0036961836820489265, 4.777333142276629e-07, 0.0, 1.0] # preTOB doubleP
binnedCorrectionMixed = binnedCorrectionPreTOB[:threshold]+binnedCorrectionPostTOB[threshold:]

if prob == 'postTOB': binnedCorrection = binnedCorrectionPostTOB
if prob == 'preTOB': binnedCorrection = binnedCorrectionPreTOB
if prob == 'mixed': binnedCorrection = binnedCorrectionMixed

th1_names = ['Z#rightarrow#nu#bar{#nu}', 'Diboson', 'Single top', 'QCD', 't#bar{t}', 'Z#rightarrowll', 'W#rightarrowl#nu']

th1s = [h_znu, h_diboson, h_t, h_qcd, h_ttb, h_zll, h_wlnu]

totalCount = np.zeros(th1s[0].GetNbinsX())
for h in th1s:
    for b in range(h.GetNbinsX()):
        if b < len(binnedCorrection):
            h.SetBinContent(b+1,h.GetBinContent(b+1)*binnedCorrection[b])
            h.SetBinError(b+1,h.GetBinError(b+1)*binnedCorrection[b])
        totalCount[b] += h.GetBinContent(b+1)

for h in th1s:
    h.Scale(firstBin/totalCount[0])

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
canv = CMS.cmsCanvas(canv_name,-0.5,15,1e-3,1e6,"Missing Outer Hits","Events",square=CMS.kSquare,extraSpace=0.05,iPos=iPos)

leg = CMS.cmsLeg(0.61, 0.89 - 0.05 * 7, 0.99, 0.89, textSize=0.04)
leg.AddEntry(h_signal, 'MET 2022F', 'lp')

# Put samples in a dict {sample: th1} and draw
hist_dict = dict(zip([name.split("_")[-1] for name in th1_names], th1s))
CMS.cmsDrawStack(stack, leg, hist_dict)
CMS.GetcmsCanvasHist(canv).GetYaxis().SetTitleOffset(1.6)
CMS.cmsDraw(h_signal, "P", mcolor=r.kBlack)
# CMS.cmsDraw(h_correctedMC, "P", mcolor=r.kBlue)

canv.Draw()
canv.SetLogy()

for i, h in enumerate(th1s):
    if i==0:
        hTotal = h
    else:
        hTotal.Add(h)

# binnedCorrection = []

# for i in range(1,hTotal.GetNbinsX()):
#     if hTotal.GetBinContent(i) > 0.0: binnedCorrection.append(h_correctedMC.GetBinContent(i)/hTotal.GetBinContent(i))
#     else: binnedCorrection.append(1.0)

# print(binnedCorrection)

n = th1s[0].GetNbinsX()+1

# Create the graph with asymmetric errors
graph = r.TGraphAsymmErrors(hTotal)

# Style the graph
graph.SetTitle("Box Plot with Errors;X-axis;Y-axis")
# Set cross-hatched style for errors

# Draw the error band on the canvas
CMS.cmsDraw(graph, "E2", lwidth=1, fstyle=3944, fcolor=r.kBlack, alpha=0.01)
leg.AddEntry(graph, 'MC Error', 'f')

# Draw the stack again to ensure proper layering
# Draw the graph
#CMS.cmsDraw(graph, 'e2 same')  # "A2P" draws shaded areas and points

# if prob != 'mixed': canv.SaveAs("corrected_missingOuterHits2022F_"+prob+".pdf")
# else: 
canv.SaveAs("corrected_missingOuterHits2022F_mixed_ANP.pdf")