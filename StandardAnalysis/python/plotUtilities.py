# Note: these imports are necessary for plot styling, however importing them in a CMSSW framework
#       configuration causes a segfault when saving skims. The ROOT modules seem to not play nicely
#       with CMSSW, so be sure to only use this for plot-making scripts.

from OSUT3Analysis.Configuration.histogramUtilities import *
from DisappTrks.StandardAnalysis.tdrstyle import *
from DisappTrks.StandardAnalysis.utilities import *

from ctypes import c_double # see https://root-forum.cern.ch/t/issue-with-using-integralanderror-with-pyroot/53182/2

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
    canvas.SetRightMargin(0.12782)
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
    if xTitle != "":
        h.GetXaxis().SetTitle(xTitle)
    if xRange[0] != 0 or xRange[1] != 0:
        h.GetXaxis().SetRangeUser(xRange[0], xRange[1])
    h.GetYaxis().SetNdivisions(505)
    h.GetYaxis().SetLabelOffset(0.005)
    h.GetYaxis().SetLabelSize(0.04)
    h.GetYaxis().SetTitleOffset(1.5)
    h.GetYaxis().SetTitleSize(0.04)
    if yTitle != "":
        h.GetYaxis().SetTitle(yTitle)
    if yRange[0] != 0 or yRange[1] != 0:
        h.GetYaxis().SetRangeUser(yRange[0], yRange[1])

def getHist(sample, condor_dir, channel, hist, quietFailure = False):
    dataset_file = "condor/%s/%s.root" % (condor_dir,sample)
    inputFile = TFile(dataset_file)
    h0 = inputFile.Get(channel + "/" + hist)
    if not h0:
        if not quietFailure: print("ERROR [getHist]: didn't find histogram ", channel+str("/")+hist, "in file", dataset_file)
        return 0
    h = h0.Clone()
    h.SetDirectory(0)
    inputFile.Close()
    return h

def getHistFromProjectionZ(sample, condor_dir, channel, hist, fiducialElectronSigmaCut, fiducialMuonSigmaCut, alternate1DHist = "", verbose = False):
    countProjections = 0 if not hasattr (getHistFromProjectionZ, "countProjections") else getattr (getHistFromProjectionZ, "countProjections")
    h3d = getHist (sample, condor_dir, channel, hist, quietFailure = True)
    if not h3d:
        h = None
        if alternate1DHist:
            if verbose: print("WARNING: not applying fiducial cuts via projections.")
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
    statError_ = c_double(0.0) # changed from Double to c_double; see https://root-forum.cern.ch/t/issue-with-using-integralanderror-with-pyroot/53182/2
    yield_ = h.IntegralAndError(0, -1, statError_)
    return (yield_, statError_.value)

def getYield(sample,condor_dir,channel):
    dataset_file = "condor/%s/%s.root" % (condor_dir,sample)
    inputFile = TFile(dataset_file)
    metPtHistogram = inputFile.Get(channel + "/Met Plots/metPt")
    if not metPtHistogram:
        print("ERROR: didn't find histogram ", channel+str("/Met Plots/metPt"), "in file ", dataset_file)
        return 0
    statError_ = c_double(0.0) # changed from Double to c_double; see https://root-forum.cern.ch/t/issue-with-using-integralanderror-with-pyroot/53182/2
    yield_     = float(metPtHistogram.IntegralAndError (0, metPtHistogram.GetNbinsX () + 1, statError_))

    inputFile.Close()
    return (yield_, statError_.value)

def getHistFromChannelDict(channel, hist, quietFailure = False):
    if "sample" not in channel or "condorDir" not in channel or "name" not in channel:
        print("Bad channel given to getHistFromChannelDict: " + str(channel))
        return
    dataset_file = "condor/%s/%s.root" % (channel["condorDir"], channel["sample"])
    inputFile = TFile(dataset_file)
    h0 = inputFile.Get(channel["name"] + "Plotter/" + hist)
    if not h0:
        if not quietFailure: print("ERROR [quietFailure]: didn't find histogram ", channel["name"] + str("Plotter/") + hist, "in file", dataset_file)
        return 0
    h = h0.Clone()
    h.SetDirectory(0)
    inputFile.Close()
    return h

def addChannelExtensions(histogram, channel, histName):
    if "extensions" in channel:
        for x in channel["extensions"]:
            histogram.Add (getHistFromChannelDict (x, histName))
            
