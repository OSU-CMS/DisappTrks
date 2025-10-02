import argparse
import cmsstyle as CMS
import functools
import ROOT

BASE_PATH = "/abyss/users/lnestor/DisappTrks/MissingHits"

PATHS_2022_PRE_EE = {
  "data": f"{BASE_PATH}/2022_PreEE/Data/2022CD_Data.root",
  "mc_uncorrected": f"{BASE_PATH}/2022_PreEE/MC/2022CD_MC_Raw.root",
  "mc_corrected_middle": f"{BASE_PATH}/2022_PreEE/MC/2022CD_MC_CorrectedMiddle.root",
  "mc_corrected_outer": f"{BASE_PATH}/2022_PreEE/MC/2022CD_MC_CorrectedOuter.root",
  "DYto2L_4jets_M10to50": f"{BASE_PATH}/2022_PreEE/MC/DYto2L_4jets_M10to50_2022/2022CD.root",
  "DYJetsToLL_M50": f"{BASE_PATH}/2022_PreEE/MC/DYJetsToLL_M50_2022/2022CD.root",
  "TbarBtoLminusNuB": f"{BASE_PATH}/2022_PreEE/MC/TbarBtoLminusNuB_2022/2022CD.root",
  "TBbartoLplusNuBbar": f"{BASE_PATH}/2022_PreEE/MC/TBbartoLplusNuBbar_2022/2022CD.root",
  "TbarQtoLNu": f"{BASE_PATH}/2022_PreEE/MC/TbarQtoLNu_2022/2022CD.root",
  "TQbartoLNu": f"{BASE_PATH}/2022_PreEE/MC/TQbartoLNu_2022/2022CD.root",
  "TbarWplusto2L2Nu": f"{BASE_PATH}/2022_PreEE/MC/TbarWplusto2L2Nu_2022/2022CD.root",
  "TbarWplustoLNu2Q": f"{BASE_PATH}/2022_PreEE/MC/TbarWplustoLNu2Q_2022/2022CD.root",
  "TWminusto2L2Nu": f"{BASE_PATH}/2022_PreEE/MC/TWminusto2L2Nu_2022/2022CD.root",
  "TWminustoLNu2Q": f"{BASE_PATH}/2022_PreEE/MC/TWminustoLNu2Q_2022/2022CD.root",
  "TTto2L2Nu": f"{BASE_PATH}/2022_PreEE/MC/TTto2L2Nu_2022/2022CD.root",
  "TTtoLNu2Q": f"{BASE_PATH}/2022_PreEE/MC/TTtoLNu2Q_2022/2022CD.root",
  "TTto4Q": f"{BASE_PATH}/2022_PreEE/MC/TTto4Q_2022/2022CD.root",
  "WW": f"{BASE_PATH}/2022_PreEE/MC/WW_2022/2022CD.root",
  "WZ": f"{BASE_PATH}/2022_PreEE/MC/WZ_2022/2022CD.root",
  "ZZ": f"{BASE_PATH}/2022_PreEE/MC/ZZ_2022/2022CD.root",
  "WToLNu_4Jets": f"{BASE_PATH}/2022_PreEE/MC/WToLNu_4Jets_2022/2022CD.root",
  "Zto2Nu_4Jets_HT100to200": f"{BASE_PATH}/2022_PreEE/MC/Zto2Nu_4Jets_HT100to200_2022/2022CD.root",
  "Zto2Nu_4Jets_HT200to400": f"{BASE_PATH}/2022_PreEE/MC/Zto2Nu_4Jets_HT200to400_2022/2022CD.root",
  "Zto2Nu_4Jets_HT400to800": f"{BASE_PATH}/2022_PreEE/MC/Zto2Nu_4Jets_HT400to800_2022/2022CD.root",
  "Zto2Nu_4Jets_HT800to1500": f"{BASE_PATH}/2022_PreEE/MC/Zto2Nu_4Jets_HT800to1500_2022/2022CD.root",
  "Zto2Nu_4Jets_HT1500to2500": f"{BASE_PATH}/2022_PreEE/MC/Zto2Nu_4Jets_HT1500to2500_2022/2022CD.root",
  "Zto2Nu_4Jets_HT2500": f"{BASE_PATH}/2022_PreEE/MC/Zto2Nu_4Jets_HT2500_2022/2022CD.root",
  "QCD_PT15to30": f"{BASE_PATH}/2022_PreEE/MC/QCD_PT15to30_2022/2022CD.root",
  "QCD_PT30to50": f"{BASE_PATH}/2022_PreEE/MC/QCD_PT30to50_2022/2022CD.root",
  "QCD_PT50to80": f"{BASE_PATH}/2022_PreEE/MC/QCD_PT50to80_2022/2022CD.root",
  "QCD_PT80to120": f"{BASE_PATH}/2022_PreEE/MC/QCD_PT80to120_2022/2022CD.root",
  "QCD_PT120to170": f"{BASE_PATH}/2022_PreEE/MC/QCD_PT120to170_2022/2022CD.root",
  "QCD_PT170to300": f"{BASE_PATH}/2022_PreEE/MC/QCD_PT170to300_2022/2022CD.root",
  "QCD_PT300to470": f"{BASE_PATH}/2022_PreEE/MC/QCD_PT300to470_2022/2022CD.root",
  "QCD_PT470to600": f"{BASE_PATH}/2022_PreEE/MC/QCD_PT470to600_2022/2022CD.root",
  "QCD_PT600to800": f"{BASE_PATH}/2022_PreEE/MC/QCD_PT600to800_2022/2022CD.root",
  "QCD_PT800to1000": f"{BASE_PATH}/2022_PreEE/MC/QCD_PT800to1000_2022/2022CD.root",
  "QCD_PT1000to1400": f"{BASE_PATH}/2022_PreEE/MC/QCD_PT1000to1400_2022/2022CD.root",
  "QCD_PT1400to1800": f"{BASE_PATH}/2022_PreEE/MC/QCD_PT1400to1800_2022/2022CD.root",
  "QCD_PT1800to2400": f"{BASE_PATH}/2022_PreEE/MC/QCD_PT1800to2400_2022/2022CD.root",
  "QCD_PT2400to3200": f"{BASE_PATH}/2022_PreEE/MC/QCD_PT2400to3200_2022/2022CD.root",
  "QCD_PT3200": f"{BASE_PATH}/2022_PreEE/MC/QCD_PT3200_2022/2022CD.root"
}

PATHS_2022_POST_EE = {
  "data": f"{BASE_PATH}/2022_PostEE/Data/2022EFG_Data.root",
  "mc_uncorrected": f"{BASE_PATH}/2022_PostEE/MC/2022EFG_MC_Raw.root",
  "mc_corrected_middle": f"{BASE_PATH}/2022_PostEE/MC/2022EFG_MC_CorrectedMiddle.root",
  "mc_corrected_outer": f"{BASE_PATH}/2022_PostEE/MC/2022EFG_MC_CorrectedOuter.root",
  "DYto2L_4jets_M10to50": f"{BASE_PATH}/2022_PostEE/MC/DYto2L_4jets_M10to50_2022EE/2022EFG.root",
  "DYJetsToLL_M50": f"{BASE_PATH}/2022_PostEE/MC/DYJetsToLL_M50_2022EE/2022EFG.root",
  "TbarBtoLminusNuB": f"{BASE_PATH}/2022_PostEE/MC/TbarBtoLminusNuB_2022EE/2022EFG.root",
  "TBbartoLplusNuBbar": f"{BASE_PATH}/2022_PostEE/MC/TBbartoLplusNuBbar_2022EE/2022EFG.root",
  "TbarQtoLNu": f"{BASE_PATH}/2022_PostEE/MC/TbarQtoLNu_2022EE/2022EFG.root",
  "TQbartoLNu": f"{BASE_PATH}/2022_PostEE/MC/TQbartoLNu_2022EE/2022EFG.root",
  "TbarWplusto2L2Nu": f"{BASE_PATH}/2022_PostEE/MC/TbarWplusto2L2Nu_2022EE/2022EFG.root",
  "TbarWplustoLNu2Q": f"{BASE_PATH}/2022_PostEE/MC/TbarWplustoLNu2Q_2022EE/2022EFG.root",
  "TWminusto2L2Nu": f"{BASE_PATH}/2022_PostEE/MC/TWminusto2L2Nu_2022EE/2022EFG.root",
  "TWminustoLNu2Q": f"{BASE_PATH}/2022_PostEE/MC/TWminustoLNu2Q_2022EE/2022EFG.root",
  "TTto2L2Nu": f"{BASE_PATH}/2022_PostEE/MC/TTto2L2Nu_2022EE/2022EFG.root",
  "TTtoLNu2Q": f"{BASE_PATH}/2022_PostEE/MC/TTtoLNu2Q_2022EE/2022EFG.root",
  "TTto4Q": f"{BASE_PATH}/2022_PostEE/MC/TTto4Q_2022EE/2022EFG.root",
  "WW": f"{BASE_PATH}/2022_PostEE/MC/WW_2022EE/2022EFG.root",
  "WZ": f"{BASE_PATH}/2022_PostEE/MC/WZ_2022EE/2022EFG.root",
  "ZZ": f"{BASE_PATH}/2022_PostEE/MC/ZZ_2022EE/2022EFG.root",
  "WToLNu_4Jets": f"{BASE_PATH}/2022_PostEE/MC/WToLNu_4Jets_2022EE/2022EFG.root",
  "Zto2Nu_4Jets_HT100to200": f"{BASE_PATH}/2022_PostEE/MC/Zto2Nu_4Jets_HT100to200_2022EE/2022EFG.root",
  "Zto2Nu_4Jets_HT200to400": f"{BASE_PATH}/2022_PostEE/MC/Zto2Nu_4Jets_HT200to400_2022EE/2022EFG.root",
  "Zto2Nu_4Jets_HT400to800": f"{BASE_PATH}/2022_PostEE/MC/Zto2Nu_4Jets_HT400to800_2022EE/2022EFG.root",
  "Zto2Nu_4Jets_HT800to1500": f"{BASE_PATH}/2022_PostEE/MC/Zto2Nu_4Jets_HT800to1500_2022EE/2022EFG.root",
  "Zto2Nu_4Jets_HT1500to2500": f"{BASE_PATH}/2022_PostEE/MC/Zto2Nu_4Jets_HT1500to2500_2022EE/2022EFG.root",
  "Zto2Nu_4Jets_HT2500": f"{BASE_PATH}/2022_PostEE/MC/Zto2Nu_4Jets_HT2500_2022EE/2022EFG.root",
  "QCD_PT15to30": f"{BASE_PATH}/2022_PostEE/MC/QCD_PT15to30_2022EE/2022EFG.root",
  "QCD_PT30to50": f"{BASE_PATH}/2022_PostEE/MC/QCD_PT30to50_2022EE/2022EFG.root",
  "QCD_PT50to80": f"{BASE_PATH}/2022_PostEE/MC/QCD_PT50to80_2022EE/2022EFG.root",
  "QCD_PT80to120": f"{BASE_PATH}/2022_PostEE/MC/QCD_PT80to120_2022EE/2022EFG.root",
  "QCD_PT120to170": f"{BASE_PATH}/2022_PostEE/MC/QCD_PT120to170_2022EE/2022EFG.root",
  "QCD_PT170to300": f"{BASE_PATH}/2022_PostEE/MC/QCD_PT170to300_2022EE/2022EFG.root",
  "QCD_PT300to470": f"{BASE_PATH}/2022_PostEE/MC/QCD_PT300to470_2022EE/2022EFG.root",
  "QCD_PT470to600": f"{BASE_PATH}/2022_PostEE/MC/QCD_PT470to600_2022EE/2022EFG.root",
  "QCD_PT600to800": f"{BASE_PATH}/2022_PostEE/MC/QCD_PT600to800_2022EE/2022EFG.root",
  "QCD_PT800to1000": f"{BASE_PATH}/2022_PostEE/MC/QCD_PT800to1000_2022EE/2022EFG.root",
  "QCD_PT1000to1400": f"{BASE_PATH}/2022_PostEE/MC/QCD_PT1000to1400_2022EE/2022EFG.root",
  "QCD_PT1400to1800": f"{BASE_PATH}/2022_PostEE/MC/QCD_PT1400to1800_2022EE/2022EFG.root",
  "QCD_PT1800to2400": f"{BASE_PATH}/2022_PostEE/MC/QCD_PT1800to2400_2022EE/2022EFG.root",
  "QCD_PT2400to3200": f"{BASE_PATH}/2022_PostEE/MC/QCD_PT2400to3200_2022EE/2022EFG.root",
  "QCD_PT3200": f"{BASE_PATH}/2022_PostEE/MC/QCD_PT3200_2022EE/2022EFG.root"
}

PATHS_2023_PRE_BPIX = {
  "data": f"{BASE_PATH}/2023_PreBPix/Data/2023C_Data.root",
  "mc_uncorrected": f"{BASE_PATH}/2023_PreBPix/MC/2023C_MC_Raw.root",
  "mc_corrected_middle": f"{BASE_PATH}/2023_PreBPix/MC/2023C_MC_CorrectedMiddle.root",
  "mc_corrected_outer": f"{BASE_PATH}/2023_PreBPix/MC/2023C_MC_CorrectedOuter.root",
  "DYto2L_4jets_M10to50": f"{BASE_PATH}/2023_PreBPix/MC/DYto2L_4jets_M10to50_2023/2023C.root",
  "DYJetsToLL_M50": f"{BASE_PATH}/2023_PreBPix/MC/DYto2L_4jets_M50_2023/2023C.root",
  "TbarBtoLminusNuB": f"{BASE_PATH}/2023_PreBPix/MC/TbarBtoLminusNuB_2023/2023C.root",
  "TBbartoLplusNuBbar": f"{BASE_PATH}/2023_PreBPix/MC/TBbartoLplusNuBbar_2023/2023C.root",
  "TbarQtoLNu": f"{BASE_PATH}/2023_PreBPix/MC/TbarQtoLNu_2023/2023C.root",
  "TQbartoLNu": f"{BASE_PATH}/2023_PreBPix/MC/TQbartoLNu_2023/2023C.root",
  "TbarWplusto2L2Nu": f"{BASE_PATH}/2023_PreBPix/MC/TbarWplusto2L2Nu_2023/2023C.root",
  "TbarWplustoLNu2Q": f"{BASE_PATH}/2023_PreBPix/MC/TbarWplustoLNu2Q_2023/2023C.root",
  "TWminusto2L2Nu": f"{BASE_PATH}/2023_PreBPix/MC/TWminusto2L2Nu_2023/2023C.root",
  "TWminustoLNu2Q": f"{BASE_PATH}/2023_PreBPix/MC/TWminustoLNu2Q_2023/2023C.root",
  "TTto2L2Nu": f"{BASE_PATH}/2023_PreBPix/MC/TTto2L2Nu_2023/2023C.root",
  "TTtoLNu2Q": f"{BASE_PATH}/2023_PreBPix/MC/TTtoLNu2Q_2023/2023C.root",
  "TTto4Q": f"{BASE_PATH}/2023_PreBPix/MC/TTto4Q_2023/2023C.root",
  "WW": f"{BASE_PATH}/2023_PreBPix/MC/WW_2023/2023C.root",
  "WZ": f"{BASE_PATH}/2023_PreBPix/MC/WZ_2023/2023C.root",
  "ZZ": f"{BASE_PATH}/2023_PreBPix/MC/ZZ_2023/2023C.root",
  "WToLNu_4Jets": f"{BASE_PATH}/2023_PreBPix/MC/WToLNu_4Jets_2023/2023C.root",
  "Zto2Nu_4Jets_HT100to200": f"{BASE_PATH}/2023_PreBPix/MC/Zto2Nu_4Jets_HT100to200_2023/2023C.root",
  "Zto2Nu_4Jets_HT200to400": f"{BASE_PATH}/2023_PreBPix/MC/Zto2Nu_4Jets_HT200to400_2023/2023C.root",
  "Zto2Nu_4Jets_HT400to800": f"{BASE_PATH}/2023_PreBPix/MC/Zto2Nu_4Jets_HT400to800_2023/2023C.root",
  "Zto2Nu_4Jets_HT800to1500": f"{BASE_PATH}/2023_PreBPix/MC/Zto2Nu_4Jets_HT800to1500_2023/2023C.root",
  "Zto2Nu_4Jets_HT1500to2500": f"{BASE_PATH}/2023_PreBPix/MC/Zto2Nu_4Jets_HT1500to2500_2023/2023C.root",
  "Zto2Nu_4Jets_HT2500": f"{BASE_PATH}/2023_PreBPix/MC/Zto2Nu_4Jets_HT2500_2023/2023C.root",
  "QCD_PT15to30": f"{BASE_PATH}/2023_PreBPix/MC/QCD_PT15to30_2023/2023C.root",
  "QCD_PT30to50": f"{BASE_PATH}/2023_PreBPix/MC/QCD_PT30to50_2023/2023C.root",
  "QCD_PT50to80": f"{BASE_PATH}/2023_PreBPix/MC/QCD_PT50to80_2023/2023C.root",
  "QCD_PT80to120": f"{BASE_PATH}/2023_PreBPix/MC/QCD_PT80to120_2023/2023C.root",
  "QCD_PT120to170": f"{BASE_PATH}/2023_PreBPix/MC/QCD_PT120to170_2023/2023C.root",
  "QCD_PT170to300": f"{BASE_PATH}/2023_PreBPix/MC/QCD_PT170to300_2023/2023C.root",
  "QCD_PT300to470": f"{BASE_PATH}/2023_PreBPix/MC/QCD_PT300to470_2023/2023C.root",
  "QCD_PT470to600": f"{BASE_PATH}/2023_PreBPix/MC/QCD_PT470to600_2023/2023C.root",
  "QCD_PT600to800": f"{BASE_PATH}/2023_PreBPix/MC/QCD_PT600to800_2023/2023C.root",
  "QCD_PT800to1000": f"{BASE_PATH}/2023_PreBPix/MC/QCD_PT800to1000_2023/2023C.root",
  "QCD_PT1000to1400": f"{BASE_PATH}/2023_PreBPix/MC/QCD_PT1000to1400_2023/2023C.root",
  "QCD_PT1400to1800": f"{BASE_PATH}/2023_PreBPix/MC/QCD_PT1400to1800_2023/2023C.root",
  "QCD_PT1800to2400": f"{BASE_PATH}/2023_PreBPix/MC/QCD_PT1800to2400_2023/2023C.root",
  "QCD_PT2400to3200": f"{BASE_PATH}/2023_PreBPix/MC/QCD_PT2400to3200_2023/2023C.root",
  "QCD_PT3200": f"{BASE_PATH}/2023_PreBPix/MC/QCD_PT3200_2023/2023C.root"
}

PATHS_2023_POST_BPIX = {
  "data": f"{BASE_PATH}/2023_PostBPix/Data/2023D_Data.root",
  "mc_uncorrected": f"{BASE_PATH}/2023_PostBPix/MC/2023D_MC_Raw.root",
  "mc_corrected_middle": f"{BASE_PATH}/2023_PostBPix/MC/2023D_MC_CorrectedMiddle.root",
  "mc_corrected_outer": f"{BASE_PATH}/2023_PostBPix/MC/2023D_MC_CorrectedOuter.root",
  "DYto2L_4jets_M10to50": f"{BASE_PATH}/2023_PostBPix/MC/DYto2L_4jets_M10to50_2023/2023D.root",
  "DYJetsToLL_M50": f"{BASE_PATH}/2023_PostBPix/MC/DYJetsToLL_M50_2023/2023D.root",
  "TbarBtoLminusNuB": f"{BASE_PATH}/2023_PostBPix/MC/TbarBtoLminusNuB_2023/2023D.root",
  "TBbartoLplusNuBbar": f"{BASE_PATH}/2023_PostBPix/MC/TBbartoLplusNuBbar_2023/2023D.root",
  "TbarQtoLNu": f"{BASE_PATH}/2023_PostBPix/MC/TbarQtoLNu_2023/2023D.root",
  "TQbartoLNu": f"{BASE_PATH}/2023_PostBPix/MC/TQbartoLNu_2023/2023D.root",
  "TbarWplusto2L2Nu": f"{BASE_PATH}/2023_PostBPix/MC/TbarWplusto2L2Nu_2023/2023D.root",
  "TbarWplustoLNu2Q": f"{BASE_PATH}/2023_PostBPix/MC/TbarWplustoLNu2Q_2023/2023D.root",
  "TWminusto2L2Nu": f"{BASE_PATH}/2023_PostBPix/MC/TWminusto2L2Nu_2023/2023D.root",
  "TWminustoLNu2Q": f"{BASE_PATH}/2023_PostBPix/MC/TWminustoLNu2Q_2023/2023D.root",
  "TTto2L2Nu": f"{BASE_PATH}/2023_PostBPix/MC/TTto2L2Nu_2023/2023D.root",
  "TTtoLNu2Q": f"{BASE_PATH}/2023_PostBPix/MC/TTtoLNu2Q_2023/2023D.root",
  "TTto4Q": f"{BASE_PATH}/2023_PostBPix/MC/TTto4Q_2023/2023D.root",
  "WW": f"{BASE_PATH}/2023_PostBPix/MC/WW_2023/2023D.root",
  "WZ": f"{BASE_PATH}/2023_PostBPix/MC/WZ_2023/2023D.root",
  "ZZ": f"{BASE_PATH}/2023_PostBPix/MC/ZZ_2023/2023D.root",
  "WToLNu_4Jets": f"{BASE_PATH}/2023_PostBPix/MC/WToLNu_4Jets_2023/2023D.root",
  "Zto2Nu_4Jets_HT100to200": f"{BASE_PATH}/2023_PostBPix/MC/Zto2Nu_4Jets_HT100to200_2023/2023D.root",
  "Zto2Nu_4Jets_HT200to400": f"{BASE_PATH}/2023_PostBPix/MC/Zto2Nu_4Jets_HT200to400_2023/2023D.root",
  "Zto2Nu_4Jets_HT400to800": f"{BASE_PATH}/2023_PostBPix/MC/Zto2Nu_4Jets_HT400to800_2023/2023D.root",
  "Zto2Nu_4Jets_HT800to1500": f"{BASE_PATH}/2023_PostBPix/MC/Zto2Nu_4Jets_HT800to1500_2023/2023D.root",
  "Zto2Nu_4Jets_HT1500to2500": f"{BASE_PATH}/2023_PostBPix/MC/Zto2Nu_4Jets_HT1500to2500_2023/2023D.root",
  "Zto2Nu_4Jets_HT2500": f"{BASE_PATH}/2023_PostBPix/MC/Zto2Nu_4Jets_HT2500_2023/2023D.root",
  "QCD_PT15to30": f"{BASE_PATH}/2023_PostBPix/MC/QCD_PT15to30_2023/2023D.root",
  "QCD_PT30to50": f"{BASE_PATH}/2023_PostBPix/MC/QCD_PT30to50_2023/2023D.root",
  "QCD_PT50to80": f"{BASE_PATH}/2023_PostBPix/MC/QCD_PT50to80_2023/2023D.root",
  "QCD_PT80to120": f"{BASE_PATH}/2023_PostBPix/MC/QCD_PT80to120_2023/2023D.root",
  "QCD_PT120to170": f"{BASE_PATH}/2023_PostBPix/MC/QCD_PT120to170_2023/2023D.root",
  "QCD_PT170to300": f"{BASE_PATH}/2023_PostBPix/MC/QCD_PT170to300_2023/2023D.root",
  "QCD_PT300to470": f"{BASE_PATH}/2023_PostBPix/MC/QCD_PT300to470_2023/2023D.root",
  "QCD_PT470to600": f"{BASE_PATH}/2023_PostBPix/MC/QCD_PT470to600_2023/2023D.root",
  "QCD_PT600to800": f"{BASE_PATH}/2023_PostBPix/MC/QCD_PT600to800_2023/2023D.root",
  "QCD_PT800to1000": f"{BASE_PATH}/2023_PostBPix/MC/QCD_PT800to1000_2023/2023D.root",
  "QCD_PT1000to1400": f"{BASE_PATH}/2023_PostBPix/MC/QCD_PT1000to1400_2023/2023D.root",
  "QCD_PT1400to1800": f"{BASE_PATH}/2023_PostBPix/MC/QCD_PT1400to1800_2023/2023D.root",
  "QCD_PT1800to2400": f"{BASE_PATH}/2023_PostBPix/MC/QCD_PT1800to2400_2023/2023D.root",
  "QCD_PT2400to3200": f"{BASE_PATH}/2023_PostBPix/MC/QCD_PT2400to3200_2023/2023D.root",
  "QCD_PT3200": f"{BASE_PATH}/2023_PostBPix/MC/QCD_PT3200_2023/2023D.root"
}

MIDDLE_HITS_DATA_HIST_NAME = "HitsSystematicsCtrlSelectionPlotter/Track Plots/trackNHitsMissingMiddle"
OUTER_HITS_DATA_HIST_NAME = "HitsSystematicsCtrlSelectionPlotter/Track Plots/trackNHitsMissingOuter"

# Needs to be set by script that calculates corrections
CORRECTED_MIDDLE_HIST_NAME = "CorrectedMiddleHits"
CORRECTED_OUTER_HIST_NAME = "CorrectedOuterHits"

def getargs():
  parser = argparse.ArgumentParser()
  parser.add_argument("--era", default="all", choices=["all", "2022CD", "2022EFG", "2023C", "2023D"])
  parser.add_argument("--hit-type", default="all", choices=["all", "middle", "outer"])
  parser.add_argument("--no-correction", action="store_true", help="If set, only plot the uncorrected comparison.")
  return parser.parse_args()

def get_canvas(name, title, num_bins):
  return CMS.cmsCanvas(name,
    -0.5, num_bins, 1e-3, 7e6,
    title,
    "Events",
    square=CMS.kSquare,
    extraSpace=0.05,
    iPos=0
  )

  return CMS.cmsDiCanvas(
    name,
    -0.5, num_bins, 1e-3, 7e6,
    0.1, 100.0,
    title,
    "Events",
    "Data / MC",
    square=CMS.kSquare,
    extraSpace=0.05,
    iPos=0
  )

def combine_hists(hists):
  merged = hists[0].Clone()
  for hist in hists[1:]:
    clone = hist.Clone()
    clone.SetDirectory(0)
    merged.Add(hist.Clone())

  merged.SetDirectory(0)
  return merged

def plot_on_canvas(canvas, data_hist, mc_hists, era, title="Missing Hits", num_bins=5, filename="missingHits.png"):
  canvas = get_canvas("hist", title, num_bins)

  # Scale so MC and data first bin matches. We clone so we don't mutate the original hists.
  process_hists = {}
  for process, hist in mc_hists["process"].items():
    clone = hist.Clone()
    clone.SetDirectory(0)
    clone.Scale(data_hist.GetBinContent(1) / mc_hists["total"].GetBinContent(1))
    process_hists[process] = clone

  total_hist = mc_hists["total"].Clone()
  total_hist.SetDirectory(0)
  total_hist.Scale(data_hist.GetBinContent(1) / mc_hists["total"].GetBinContent(1))

  canvas.cd(1)
  legend = CMS.cmsLeg(0.61, 0.89-0.05*7, 0.99, 0.89, textSize=0.04)
  legend.AddEntry(data_hist, f"MET {era}", "lp")

  stack = ROOT.THStack("stack", "Stacked")
  CMS.cmsDrawStack(stack, legend, process_hists)
  CMS.GetcmsCanvasHist(ROOT.gPad).GetYaxis().SetTitleOffset(1.6)
  CMS.cmsDraw(data_hist, "P", mcolor=ROOT.kBlack)

  ROOT.gPad.SetLogy()

  graph = ROOT.TGraphAsymmErrors(total_hist)
  graph.SetTitle("Box Plot with Errors;X-axis;Y-axis")
  CMS.cmsDraw(graph, "E2", fstyle=3744, fcolor=ROOT.kBlack, alpha=0.01)

  legend.AddEntry(graph, "MC Error", "f")
  CMS.UpdatePad()

  canvas.SaveAs(filename)

def load_and_combine_hists(hist_name, *filenames):
  hists = []
  for f in filenames:
    tfile = ROOT.TFile.Open(f)
    hist = tfile.Get(hist_name)
    hist.SetDirectory(0)
    hists.append(hist)
    tfile.Close()

  merged_hist = combine_hists(hists)
  merged_hist.Sumw2()
  return merged_hist

def load_hist_from_file(filename, hist_name):
  tfile = ROOT.TFile.Open(filename)
  hist = tfile.Get(hist_name)
  hist.SetDirectory(0)
  tfile.Close()
  return hist

def load_process_hists(filepaths, hist_name):
  wlnu_hist = load_and_combine_hists(hist_name, filepaths["WToLNu_4Jets"])
  zll_hist = load_and_combine_hists(hist_name, filepaths["DYJetsToLL_M50"], filepaths["DYto2L_4jets_M10to50"])
  ttb_hist = load_and_combine_hists(hist_name, filepaths["TTto2L2Nu"], filepaths["TTtoLNu2Q"], filepaths["TTto4Q"])
  diboson_hist = load_and_combine_hists(hist_name, filepaths["WW"], filepaths["WZ"], filepaths["ZZ"])

  qcd_hist = load_and_combine_hists(
    hist_name,
    filepaths["QCD_PT15to30"],
    filepaths["QCD_PT30to50"],
    filepaths["QCD_PT50to80"],
    filepaths["QCD_PT80to120"],
    filepaths["QCD_PT120to170"],
    filepaths["QCD_PT170to300"],
    filepaths["QCD_PT300to470"],
    filepaths["QCD_PT470to600"],
    filepaths["QCD_PT600to800"],
    filepaths["QCD_PT800to1000"],
    filepaths["QCD_PT1000to1400"],
    filepaths["QCD_PT1400to1800"],
    filepaths["QCD_PT1800to2400"],
    filepaths["QCD_PT2400to3200"],
    filepaths["QCD_PT3200"]
  )

  t_hist = load_and_combine_hists(
    hist_name,
    filepaths["TbarBtoLminusNuB"],
    filepaths["TBbartoLplusNuBbar"],
    filepaths["TbarQtoLNu"],
    filepaths["TQbartoLNu"],
    filepaths["TbarWplusto2L2Nu"],
    filepaths["TbarWplustoLNu2Q"],
    filepaths["TWminusto2L2Nu"],
    filepaths["TWminustoLNu2Q"]
  )

  znu_hist = load_and_combine_hists(
    hist_name,
    filepaths["Zto2Nu_4Jets_HT100to200"],
    filepaths["Zto2Nu_4Jets_HT200to400"],
    filepaths["Zto2Nu_4Jets_HT400to800"],
    filepaths["Zto2Nu_4Jets_HT800to1500"],
    filepaths["Zto2Nu_4Jets_HT1500to2500"],
    filepaths["Zto2Nu_4Jets_HT2500"]
  )

  mc_hists = {
    "Z#rightarrow#nu#bar{#nu}": znu_hist,
    "Diboson": diboson_hist,
    "Single top": t_hist,
    "QCD": qcd_hist,
    "t#bar{t}": ttb_hist,
    "Z#rightarrowll": zll_hist,
    "W#rightarrowl#nu": wlnu_hist
  }

  return mc_hists

def calc_correction_ratios(total_uncorr_hist, total_corr_hist):
  corrections = []
  for bin_idx in range(1, total_uncorr_hist.GetNbinsX() + 1):
    count_uncorr = total_uncorr_hist.GetBinContent(bin_idx)
    count_corr = total_corr_hist.GetBinContent(bin_idx)

    ratio = count_corr / count_uncorr if count_uncorr > 0 else 0
    corrections.append(ratio)

  return corrections

def correct_process_hists(uncorr_hists, correction_ratios):
  corr_mc_hists = {}
  for process_name, uncorr_hist in uncorr_hists.items():
    corr_hist = uncorr_hist.Clone()
    corr_hist.SetDirectory(0)

    for bin_idx in range(1, uncorr_hist.GetNbinsX() + 1):
      count = uncorr_hist.GetBinContent(bin_idx)
      err = uncorr_hist.GetBinError(bin_idx)
      corr_hist.SetBinContent(bin_idx, count * correction_ratios[bin_idx - 1])
      corr_hist.SetBinError(bin_idx, err * correction_ratios[bin_idx - 1])
      corr_mc_hists[process_name] = corr_hist

  return corr_mc_hists

def create_comparison_plots(filepaths, args, era):
  if args.hit_type == "all" or args.hit_type == "middle":
    hists = {
      "data": load_hist_from_file(filepaths["data"], MIDDLE_HITS_DATA_HIST_NAME),
      "mc_uncorr": {
        "total": load_hist_from_file(filepaths["mc_uncorrected"], MIDDLE_HITS_DATA_HIST_NAME),
        "process": load_process_hists(filepaths, MIDDLE_HITS_DATA_HIST_NAME)
      }
    }

    plot_on_canvas(
      uncorr_canvas,
      hists["data"],
      hists["mc_uncorr"],
      era,
      title="Missing Middle Hits",
      num_bins=5,
      filename=f"missingMiddleHits_{era}.png"
    )

    if not args.no_correction:
      hists["mc_corr"] = {"total": load_hist_from_file(filepaths["mc_corrected_middle"], CORRECTED_MIDDLE_HIST_NAME)}
      correction_ratios = calc_correction_ratios(hists["mc_uncorr"]["total"], hists["mc_corr"]["total"])
      hists["mc_corr"]["process"] = correct_process_hists(hists["mc_uncorr"]["process"], correction_ratios)

      plot_on_canvas(
        corr_canvas,
        hists["data"],
        hists["mc_corr"],
        era,
        title="Missing Middle Hits",
        num_bins=5,
        filename=f"missingMiddleHitsCorrected_{era}.png"
      )

  if args.hit_type == "all" or args.hit_type == "outer":
    hists = {
      "data": load_hist_from_file(filepaths["data"], OUTER_HITS_DATA_HIST_NAME),
      "mc_uncorr": {
        "total": load_hist_from_file(filepaths["mc_uncorrected"], OUTER_HITS_DATA_HIST_NAME),
        "process": load_process_hists(filepaths, OUTER_HITS_DATA_HIST_NAME)
      }
    }

    plot_on_canvas(
      uncorr_canvas,
      hists["data"],
      hists["mc_uncorr"],
      era,
      title="Missing Outer Hits",
      num_bins=15,
      filename=f"missingOuterHits_{era}.png"
    )

    if not args.no_correction:
      hists["mc_corr"] = {"total": load_hist_from_file(filepaths["mc_corrected_outer"], CORRECTED_OUTER_HIST_NAME)}
      correction_ratios = calc_correction_ratios(hists["mc_uncorr"]["total"], hists["mc_corr"]["total"])
      hists["mc_corr"]["process"] = correct_process_hists(hists["mc_uncorr"]["process"], correction_ratios)

      plot_on_canvas(
        corr_canvas,
        hists["data"],
        hists["mc_corr"],
        era,
        title="Missing Outer Hits",
        num_bins=15,
        filename=f"missingOuterHitsCorrected_{era}.png"
      )

def main():
  args = getargs()

  ROOT.gROOT.SetBatch(1)
  CMS.setCMSStyle()
  CMS.SetExtraText("Preliminary")
  CMS.SetLumi("")
  CMS.SetEnergy("13.6")
  CMS.ResetAdditionalInfo()

  if args.era == "all" or args.era == "2022CD":
    create_comparison_plots(PATHS_2022_PRE_EE, args, "2022CD")

  if args.era == "all" or args.era == "2022EFG":
    create_comparison_plots(PATHS_2022_POST_EE, args, "2022EFG")

  if args.era == "all" or args.era == "2023C":
    create_comparison_plots(PATHS_2023_PRE_BPIX, args, "2023C")

  if args.era == "all" or args.era == "2023D":
    create_comparison_plots(PATHS_2023_POST_BPIX, args, "2023D")

if __name__ == "__main__":
  main()
