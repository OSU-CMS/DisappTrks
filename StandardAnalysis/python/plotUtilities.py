# Note: these imports are necessary for plot styling, however importing them in a CMSSW framework
#       configuration causes a segfault when saving skims. The ROOT modules seem to not play nicely
#       with CMSSW, so be sure to only use this for plot-making scripts.

from OSUT3Analysis.Configuration.histogramUtilities import *
from DisappTrks.StandardAnalysis.tdrstyle import *
from DisappTrks.StandardAnalysis.utilities import *

def setStyle(h, color = 1):
    h.SetLineColor(color)
    h.SetLineStyle(1)
    h.SetLineWidth(2)
    h.SetMarkerColor(color)
    h.SetMarkerStyle(20)
    h.SetMarkerSize(1.5)
    h.SetTitle("")

def setCanvasStyle(canvas):
    canvas.SetHighLightColor(2)
    canvas.SetFillColor(0)
    canvas.SetBorderMode(0)
    canvas.SetBorderSize(2)
    canvas.SetTickx(1)
    canvas.SetTicky(1)
    canvas.SetLeftMargin(0.128141)
    canvas.SetRightMargin(0.0414573)
    canvas.SetBottomMargin(0.0971503)
    canvas.SetTopMargin(0.0712435)
    canvas.SetFrameFillStyle(0)
    canvas.SetFrameBorderMode(0)
    canvas.SetFrameFillStyle(0)
    canvas.SetFrameBorderMode(0)

def setAxisStyle(h, xTitle = "", yTitle = "", xRange = (0, 0), yRange = (0, 0)):
    h.GetXaxis().SetNdivisions(505)
    h.GetXaxis().SetLabelOffset(0.005)
    h.GetXaxis().SetLabelSize(0.04)
    h.GetXaxis().SetTitleOffset(1.0)
    h.GetXaxis().SetTitleSize(0.04)
    if xTitle is not "":
        h.GetXaxis().SetTitle(xTitle)
    if xRange[0] != 0 or xRange[1] != 0:
        h.GetXaxis().SetRangeUser(xRange[0], xRange[1])
    h.GetYaxis().SetNdivisions(505)
    h.GetYaxis().SetLabelOffset(0.005)
    h.GetYaxis().SetLabelSize(0.04)
    h.GetYaxis().SetTitleOffset(1.5)
    h.GetYaxis().SetTitleSize(0.04)
    if yTitle is not "":
        h.GetYaxis().SetTitle(yTitle)
    if yRange[0] != 0 or yRange[1] != 0:
        h.GetYaxis().SetRangeUser(yRange[0], yRange[1])

def getHistFromProjectionZ(sample, condor_dir, channel, hist, fiducialElectronSigmaCut, fiducialMuonSigmaCut, alternate1DHist = ""):
    countProjections = 0 if not hasattr (getHistFromProjectionZ, "countProjections") else getattr (getHistFromProjectionZ, "countProjections")
    h3d = getHist (sample, condor_dir, channel, hist)
    if not h3d:
        h = None
        if alternate1DHist:
            print "WARNING: not applying fiducial cuts via projections."
            h = getHist (sample, condor_dir, channel, alternate1DHist)
        return h

    h = h3d.ProjectionZ (hist + "_pz" + str(countProjections),
                         0, h3d.GetXaxis().FindBin(fiducialElectronSigmaCut) - 1,
                         0, h3d.GetYaxis().FindBin(fiducialMuonSigmaCut) - 1, "e")

    countProjections += 1
    setattr (getHistFromProjectionZ, "countProjections", countProjections)
    return h

def getHistIntegralFromProjectionZ(sample, condor_dir, channel, fiducialElectronSigmaCut, fiducialMuonSigmaCut):
    hist = "Track-met Plots/metNoMuMinusOnePtVsMaxSigmaForFiducialTracks"
    h = getHistFromProjectionZ (sample, condor_dir, channel, hist, fiducialElectronSigmaCut, fiducialMuonSigmaCut, alternate1DHist = "Met Plots/metNoMu")
    statError_ = Double(0.0)
    yield_ = h.IntegralAndError(0, -1, statError_)
    return (yield_, statError_)

def getYield(sample,condor_dir,channel):
    dataset_file = "condor/%s/%s.root" % (condor_dir,sample)
    inputFile = TFile(dataset_file)
    metPtHistogram = inputFile.Get(channel + "/Met Plots/metPt")
    if not metPtHistogram:
        print "ERROR: didn't find histogram ", channel+str("/Met Plots/metPt"), "in file ", dataset_file
        return 0
    statError_ = Double (0.0)
    yield_     = float(metPtHistogram.IntegralAndError (0, metPtHistogram.GetNbinsX () + 1, statError_))

    inputFile.Close()
    return (yield_, statError_)
