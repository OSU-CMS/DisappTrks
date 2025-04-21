import ROOT as r
import cmsstyle as cms
import latex

jetVetoMapFiles = [
    '../../../../OSUT3Analysis/Configuration/data/Summer22_23Sep2023_RunCD_v1.root',
    '../../../../OSUT3Analysis/Configuration/data/Summer22EE_23Sep2023_RunEFG_v1.root',
    '../../../../OSUT3Analysis/Configuration/data/Summer23Prompt23_RunC_v1.root',
    '../../../../OSUT3Analysis/Configuration/data/Summer23BPixPrompt23_RunD_v1.root',

]

ecalStatusMaps = [
    "/data/users/mcarrigan/condor/ecalStatusMaps/badEcalChannels_2022CD.root",
    "/data/users/mcarrigan/condor/ecalStatusMaps/badEcalChannels_2022EFG.root",
    "/data/users/mcarrigan/condor/ecalStatusMaps/badEcalChannels_2023C.root",
    "/data/users/mcarrigan/condor/ecalStatusMaps/badEcalChannels_2023D.root",
]

def plotJetVetoMaps():

    for f in jetVetoMapFiles:
        fin = r.TFile.Open(f)

        name = 'jetVetoMap_' + f.split('/')[-1].replace('.root', '.png')

        jetvetomap = fin.Get("jetvetomap")
        r.gStyle.SetOptStat(0)
        jetvetomap.SetMarkerSize(1)
        jetvetomap.SetMarkerStyle(1)
        jetvetomap.SetMarkerColor(2)
        cms.SetExtraText('Preliminary')
        cms.SetLumi("")
        c1 = cms.cmsCanvas('canv', -4, 4, -3.4, 3.4, '\eta', '\phi', square = True, extraSpace=0.01, with_z_axis=False, iPos=0)
        jetvetomap.Draw("same")
        c1.Draw()

        c1.SaveAs(name)

def plotEcalStatusMaps():

    cms.SetCMSPalette()

    for f in ecalStatusMaps:
        fin = r.TFile.Open(f)
        badChannels = fin.Get('badChannels')
        
        era = f.split('/')[-1].split('_')[-1].replace('.root', '')

        name = f'ecalStatusMap_{era}.png'

        r.gStyle.SetOptStat(0)
        badChannels.SetMarkerSize(1)
        badChannels.SetMarkerStyle(1)
        badChannels.SetMarkerColor(2)
        cms.SetExtraText('Preliminary')
        #cms.SetLumi(f"Era {era}", "")
        cms.SetEnergy("13.6")
        badChannels.SetMarkerColor(2)
        cms.SetCMSPalette()
        c1 = cms.cmsCanvas('canv', -3, 3, -3.4, 3.4, '\eta', '\phi', square = True, extraSpace=0.01, with_z_axis=False, iPos=0)
        badChannels.Draw("same")
        c1.Update()
        r.gPad.Update()

        c1.SaveAs(name)


if __name__ == "__main__":

    r.gROOT.SetBatch(1)

    plotJetVetoMaps()
    plotEcalStatusMaps()