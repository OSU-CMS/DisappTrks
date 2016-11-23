import FWCore.ParameterSet.Config as cms
from DisappTrks.StandardAnalysis.MissingHitsCorrections_cff import *
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
            for y in MissingHitsCorrections[correction]:
                setattr (x, y, MissingHitsCorrections[correction][y])
