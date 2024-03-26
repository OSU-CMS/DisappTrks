import ROOT as r

def makeComparrisonPlot(trees, plot):

    histograms = []

    for i in enumerate(trees):
        h = r.TH1F()
        histograms.append(h)

    for ih, (key, value) in enumerate(trees.items()):
        try:
            histograms[ih] = value.Get(key+'/'+plot)
        except:
            print("Could not create histogram {}".format(plot))
        
    return histograms



def plotTogether(trees, histos, plot, fout, pos=[0.6, 0.6, 0.8, 0.8]):
    
    c1 = r.TCanvas("c1", "c1", 600, 600)
    c1.cd()
    
    names = list(trees.keys())
    
    l1=r.TLegend(pos[0], pos[1], pos[2], pos[3])

    if len(histos) == 2:
        if plot.GetClassName()=="TH1D":
            histName = histos[0].GetTitle()
            if histName == "": 
                print("hist has no title", plot.GetName())
                histName = plot.GetName()
            histos[0].SetTitle(histName)
            histos[1].SetLineColor(2)
            ratio = r.TRatioPlot(histos[0], histos[1])
            l1.AddEntry(histos[0], names[0], 'l')
            l1.AddEntry(histos[1], names[1], 'l')
            ratio.Draw()
            ratio.GetUpperPad().cd()
            l1.Draw()
        elif plot.GetClassName()=="TH2D":
            h1 = histos[0].Clone()
            h1.Divide(histos[1])
            h1.Draw("colz")
            h1.SetTitle("{} \n Ratio {} / {}".format(plot.GetName(), names[0], names[1]))
    else:
        for ih, h in enumerate(histos):
            if plot.GetClassName()=='TH1D':
                if ih == 0: 
                    h.Draw("hist")
                    h.SetTitle(plot.GetName())
                else: 
                    h.SetLineColor(2)
                    h.Draw("hist same")
                l1.AddEntry(h, names[ih], 'l')
                l1.Draw()

            elif plot.GetClassName()=="TH2D":
                print("TH2")
            else:
                print("Plot is not of type TH1D or TH2D, skipping...")
    
    fout.cd()
    c1.Write(plot.GetName())
    c1.Delete()
    

if __name__ == "__main__":

    r.gROOT.SetBatch(1)

    vertex = r.TFile.Open("condor/EGamma_2022/EGamma_2022F_vertexOnly/EGamma_2022F.root")
    basic = r.TFile.Open("condor/EGamma_2022/EGamma_2022F_basicSelection/EGamma_2022F.root")

    vertex.cd('VertexCutOnlyPlotter/Track Plots')
    basic.cd('BasicSelectionPlotter/Track Plots')

    trees = {"VertexCutOnlyPlotter": vertex, "BasicSelectionPlotter": basic}

    fout = r.TFile.Open("combinedPlots.root", 'recreate')

    for key in vertex.VertexCutOnlyPlotter.GetListOfKeys():
        sub = key.ReadObj()
        for ikey2, key2 in enumerate(sub.GetListOfKeys()):
            print(key2.GetName())
            pltName = key.GetName()+'/'+key2.GetName()
            histos = makeComparrisonPlot(trees, pltName)
            plotTogether(trees, histos, key2, fout)
        
    #fout.Close()