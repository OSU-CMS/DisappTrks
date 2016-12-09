import FWCore.ParameterSet.Config as cms
from OSUT3Analysis.Configuration.histogramUtilities import *
from DisappTrks.StandardAnalysis.MissingHitsCorrections_cff import *
from DisappTrks.StandardAnalysis.tdrstyle import *
import re
import os

def addLifetimeReweighting (datasets):
    new_datasets = []
    for dataset0 in datasets:
        if not re.match (r'AMSB_chargino_[^_]*GeV_[^_]*cm_.*', dataset0):
            continue
        mass = re.sub (r'AMSB_chargino_([^_]*)GeV_[^_]*cm_.*', r'\1', dataset0)
        ctau0 = float (re.sub (r'AMSB_chargino_[^_]*GeV_([^_]*)cm_.*', r'\1', dataset0))
        suffix = re.sub (r'AMSB_chargino_[^_]*GeV_[^_]*cm_(.*)', r'\1', dataset0)
        for i in range (2, 10):
            ctau = ctauP = 0.1 * i * ctau0
            if int (ctau) * 10 == int (ctau * 10):
                ctau = ctauP = str (int (ctau))
            else:
                ctau = ctauP = str (ctau)
                ctauP = re.sub (r'\.', r'p', ctau)
            dataset = 'AMSB_chargino_' + mass + 'GeV_' + ctauP + 'cm_' + suffix

            new_datasets.append (dataset)

    datasets.extend (new_datasets)

def getUser():
    dirs = {}
    cwd = os.getcwd()
    if "wulsin" in cwd:
        dirs['Andrew'] = "hartCondor/"
        dirs['Brian']  = "francisCondor/"
        dirs['Wells']  = ""
        user = "wulsin"
    elif "hart" in cwd:
        dirs['Andrew'] = ""
        dirs['Brian']  = "francisCondor/"
        dirs['Wells']  = "wellsCondor/"
        user = "hart"
    elif "bfrancis" in cwd:
        dirs['Andrew'] = "hartCondor/"
        dirs['Brian']  = ""
        dirs['Wells']  = "wellsCondor/"
        user = "bfrancis"
    else:
        print "Error:  could not identify user as brancis, hart, or wulsin."
        os.exit(0)
    return dirs

################################################################################
# Functions for getting the invariant mass of an object and a track, given
# different mass assumptions for the track.
################################################################################

def invMassGivenEnergy (obj, energy):
    return "sqrt ((" + obj + ".energy + track." + energy + ") * (" + obj + ".energy + track." + energy + ") - (" + obj + ".px + track.px) * (" + obj + ".px + track.px) - (" + obj + ".py + track.py) * (" + obj + ".py + track.py) - (" + obj + ".pz + track.pz) * (" + obj + ".pz + track.pz))"

def invMassWithElectron (obj):
    return invMassGivenEnergy (obj, "energyOfElectron")

def invMassWithMuon (obj):
    return invMassGivenEnergy (obj, "energyOfMuon")

def invMassWithTau (obj):
    return invMassGivenEnergy (obj, "energyOfTau")

def invMassWithPion (obj):
    return invMassGivenEnergy (obj, "energyOfPion")

def invMassWithProton (obj):
    return invMassGivenEnergy (obj, "energyOfProton")

################################################################################

def switchToBestTrack (channel, histogramSets):
    for cut in channel.cuts:
        cutString = cut.cutString.pythonValue ()[1:-1]
        if re.search (r"missingOuterHits", cutString):
            cutString = re.sub (r"missingOuterHits", r"bestTrackMissingOuterHits", cutString)
        cut.cutString = cms.string (cutString)

    for histogramSet in histogramSets:
        for histogram in histogramSet.histograms:
            i = 0
            for inputVariable in histogram.inputVariables:
                if re.search (r"missingOuterHits", inputVariable):
                    inputVariable = re.sub (r"missingOuterHits", r"bestTrackMissingOuterHits", inputVariable)
                histogram.inputVariables[i] = inputVariable
                i += 1

def setNJobs (datasets, composite_dataset_definitions, nJobs, newNJobs):
    for dataset in datasets:
        if dataset in composite_dataset_definitions:
            for constituent_dataset in composite_dataset_definitions[dataset]:
                nJobs[constituent_dataset] = newNJobs
        else:
            nJobs[dataset] = newNJobs

def setDatasetType (datasets, composite_dataset_definitions, types, newType):
    for dataset in datasets:
        types[dataset] = newType
        if dataset in composite_dataset_definitions:
            for constituent in composite_dataset_definitions[dataset]:
                types[constituent] = newType

def setMissingHitsCorrection (process, correction):
    for a in dir (process):
        x = getattr (process, a)
        if not hasattr (x, "type_"):
            continue
        if x.type_ () == "OSUTrackProducer":
            print "Setting missing hits corrections for \"" + correction + "\"..."
            for y in MissingHitsCorrections[correction]:
                setattr (x, y, MissingHitsCorrections[correction][y])
                print "  " + y + ": " + str (getattr (x, y).value ())

def setThresholdForVeto (process, threshold):
    fiducialMaps = ["electrons", "muons"]

    for a in dir (process):
        x = getattr (process, a)
        if not hasattr (x, "type_"):
            continue
        if x.type_ () == "OSUTrackProducer":
            if hasattr (x, "fiducialMaps"):
                y = getattr (x, "fiducialMaps")
                for fiducialMap in fiducialMaps:
                    if hasattr (y, fiducialMap):
                        z = getattr (y, fiducialMap)
                        for i in range (0, len (z)):
                            print "Setting thresholdForVeto for " + x.label () + ".fiducialMaps." + fiducialMap + "[" + str (i) + "] to " + str (threshold) + "..."
                            setattr (z[i], "thresholdForVeto", cms.double (threshold))

def setFiducialMaps (process, electrons, muons):
    fiducialMaps = ["electrons", "muons"]

    for a in dir (process):
        x = getattr (process, a)
        if not hasattr (x, "type_"):
            continue
        if x.type_ () == "OSUTrackProducer":
            if hasattr (x, "fiducialMaps"):
                y = getattr (x, "fiducialMaps")
                for fiducialMap in fiducialMaps:
                    if hasattr (y, fiducialMap):
                        z = getattr (y, fiducialMap)
                        histFile = electrons if fiducialMap == "electrons" else muons
                        for i in range (0, len (z)):
                            print "Setting histFile for " + x.label () + ".fiducialMaps." + fiducialMap + "[" + str (i) + "] to \"" + histFile + "\"..."
                            setattr (z[i], "histFile", cms.FileInPath (histFile))

def setStyle(h):
    h.SetLineColor(1)
    h.SetLineStyle(1)
    h.SetLineWidth(1)
    h.SetMarkerColor(1)
    h.SetMarkerStyle(20)
    h.SetMarkerSize(1.0)
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

def getHistFromProjectionZ(sample, condor_dir, channel, hist, fiducialElectronSigmaCut, fiducialMuonSigmaCut):
    countProjections = 0 if not hasattr (getHistFromProjectionZ, "countProjections") else getattr (getHistFromProjectionZ, "countProjections")
    h3d = getHist (sample, condor_dir, channel, hist)
    h = h3d.ProjectionZ (hist + "_pz" + str(countProjections),
                         0, h3d.GetXaxis().FindBin(fiducialElectronSigmaCut) - 1,
                         0, h3d.GetYaxis().FindBin(fiducialMuonSigmaCut) - 1, "e")

    countProjections += 1
    setattr (getHistFromProjectionZ, "countProjections", countProjections)
    return h

def getHistIntegralFromProjectionZ(sample, condor_dir, channel, fiducialElectronSigmaCut, fiducialMuonSigmaCut):
    hist = "Track-met Plots/metNoMuMinusOnePtVsMaxSigmaForFiducialTracks"
    h = getHistFromProjectionZ (sample, condor_dir, channel, hist, fiducialElectronSigmaCut, fiducialMuonSigmaCut)
    statError_ = Double(0.0)
    yield_ = h.IntegralAndError(0, -1, statError_)
    return (yield_, statError_)
