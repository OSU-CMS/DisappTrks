import FWCore.ParameterSet.Config as cms
from DisappTrks.StandardAnalysis.MissingHitsCorrections_cff import *
import re
import os
import copy

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
            print "# Missing hits corrections (" + a + "): " + correction
            for y in MissingHitsCorrections[correction]:
                setattr (x, y, MissingHitsCorrections[correction][y])
                print "#   " + y + ": " + str (getattr (x, y).value ())
    # this is the last customization that prints info, so now print a big line to clean things up
    print "########################################################################"

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
                            print "# Setting thresholdForVeto for " + x.label () + ".fiducialMaps." + fiducialMap + "[" + str (i) + "] to " + str (threshold) + "..."
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
                            print "# Setting histFile for " + x.label () + ".fiducialMaps." + fiducialMap + "[" + str (i) + "] to \"" + histFile + "\"..."
                            setattr (z[i], "histFile", cms.FileInPath (histFile))

moveVariableProducerIndex = -1

def moveVariableProducer (process, producerName, channelName):

    global moveVariableProducerIndex
    moveVariableProducerIndex = moveVariableProducerIndex + 1

    producer = plotter = eventvariableProducer = None
    producerLabel = plotterLabel = ""
    plotterPath = None

    # find the variable producer and Plotter
    for a in dir (process):
        x = getattr (process, a)
        if hasattr (x, "type_"):
            if x.type_ () == producerName and 'Copy' not in a:
                producer = copy.deepcopy (x)
                producerLabel = copy.deepcopy (a)
            if x.type_ () == "Plotter" and a == channelName+"Plotter":
                plotter = copy.deepcopy (x)
                plotterLabel = copy.deepcopy (a)

    # find the eventvariable producer associated to the channel
    # by way of the channels' cms.Path
    for a in getattr (process, channelName).moduleNames():
        x = getattr (process, a)
        if hasattr (x, "type_") and x.type_ () == "EventvariableProducer":
            eventvariableProducer = copy.deepcopy (x)

    # change the tracks and leptons input tags for the variable producer to
    # that used by the Plotter and create a copy of the variable producer which
    # we will put before the Plotter
    if hasattr (plotter.collections, "tracks"):
        producer.collections.tracks = copy.deepcopy (plotter.collections.tracks)
        producer.collections.electrons = copy.deepcopy (plotter.collections.electrons)
        producer.collections.muons = copy.deepcopy (plotter.collections.muons)
        producer.collections.taus = copy.deepcopy (plotter.collections.taus)
    
    setattr (process, producerLabel + "Copy" + str(moveVariableProducerIndex), producer)
    producer = getattr (process, producerLabel + "Copy" + str(moveVariableProducerIndex))

    # create an EventvariableProducer for the copy of the variable producer we
    # created above with input tags pointing to the products of the copy
    if hasattr (eventvariableProducer.collections, "eventvariables") and hasattr (eventvariableProducer.collections, "uservariables"):
        eventvariables = getattr (eventvariableProducer.collections, "eventvariables")
        uservariables = getattr (eventvariableProducer.collections, "uservariables")
        eventvariables.setModuleLabel (producerLabel + "Copy" + str(moveVariableProducerIndex))
        for i in range (0, len (uservariables)):
            if uservariables[i].getModuleLabel () == producerLabel or uservariables[i].getModuleLabel () == producerLabel:
                uservariables[i].setModuleLabel (producerLabel + "Copy" + str(moveVariableProducerIndex))
        setattr (eventvariableProducer.collections, "eventvariables", eventvariables)
        setattr (eventvariableProducer.collections, "uservariables", uservariables)
    setattr (process, "objectProducerCopy" + str (moveVariableProducerIndex), eventvariableProducer)
    eventvariableProducer = getattr (process, "objectProducerCopy" + str (moveVariableProducerIndex))

    # change the input tags for the Plotter which point to products of the
    # variable producer to those produced by the copy of the variable producer
    # we created above
    if hasattr (plotter.collections, "eventvariables") and hasattr (plotter.collections, "uservariables"):
        eventvariables = getattr (plotter.collections, "eventvariables")
        uservariables = getattr (plotter.collections, "uservariables")
        for i in range (0, min (len (eventvariables), len (uservariables))):
            if eventvariables[i].getModuleLabel () == producerLabel or uservariables[i].getModuleLabel () == producerLabel:
                eventvariables[i].setModuleLabel ("objectProducerCopy" + str (moveVariableProducerIndex))
                uservariables[i].setModuleLabel ("objectProducerCopy" + str (moveVariableProducerIndex))
        setattr (plotter.collections, "eventvariables", eventvariables)
        setattr (plotter.collections, "uservariables", uservariables)
    setattr (process, plotterLabel, plotter)
    plotter = getattr (process, plotterLabel)

    # insert the copy of the variable producer we created above into the path
    # of the Plotter, right before the Plotter
    #process.variableProducerPath.remove (getattr (process, producerLabel))
    plotterPath = getattr (process, channelName)
    plotterPath.remove (getattr (process, plotterLabel))
    plotterPath += producer
    plotterPath += eventvariableProducer
    plotterPath += plotter
    setattr (process, channelName, plotterPath)

def getListOfChannels (process):
    channels = []
    for path in process.schedule:
        if hasattr (path, "label"):
            label = path.label ()
            if label != "variableProducerPath" and label != "endPath" and label != "egmGsfElectronIDSequence_step":
                channels.append (path.label ())

    return channels
