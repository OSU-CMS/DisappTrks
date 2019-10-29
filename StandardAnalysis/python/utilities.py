import FWCore.ParameterSet.Config as cms
from DisappTrks.StandardAnalysis.MissingHitsCorrections_cff import *
from OSUT3Analysis.Configuration.cutUtilities import replaceSingleCut
import re
import os
import copy
import sys

# this is not yet used anywhere; eraName would need to be switched from 2016BC to 2016DEFGH somewhere
class AnalysisEra:
    is2015 = False
    is2016 = False
    is2017 = False
    is2017 = False
    release = ''
    eraName = ''

    def __init__(self):
        self.release = os.environ["CMSSW_VERSION"]
        if self.release.startswith('CMSSW_7_6_'):
            self.is2015 = True
            self.eraName = '2015'
            self.availableSubEras = ['D']
        elif self.release.startswith('CMSSW_8_0_'):
            self.is2016 = True
            self.eraName = '2016BC' # BC by default
        elif self.release.startswith('CMSSW_9_4_'):
            self.is2017 = True
            self.eraName = '2017'
        elif self.release.startswith('CMSSW_10_2_'):
            self.is2018 = True
            self.eraName = '2018'
        else:
            print self.release + ' is not a valid release. Quitting.'
            sys.exit(0)
            
    def availableSubEras(self):
        if self.is2015:
            return ['D']
        if self.is2016:
            return [x for x in self.eraName[4:]]
        if self.is2017:
            return ['B', 'C', 'D', 'E', 'F']
        if self.is2018:
            return ['A', 'B', 'C', 'D']
        return []


def addLifetimeReweighting (datasets, isHiggsino = False):
    new_datasets = []
    matchPattern = r'Higgsino_([^_]*)GeV_([^_]*)cm_(.*)' if isHiggsino else r'AMSB_chargino_([^_]*)GeV_([^_]*)cm_(.*)'
    for dataset0 in datasets:
        if not re.match (matchPattern, dataset0):
            continue
        mass = re.sub (matchPattern, r'\1', dataset0)
        ctau0 = float (re.sub (matchPattern, r'\2', dataset0))
        suffix = re.sub (matchPattern, r'\3', dataset0)
        for i in range (2, 10):
            ctau = ctauP = 0.1 * i * ctau0
            if int (ctau) * 10 == int (ctau * 10):
                ctau = ctauP = str (int (ctau))
            else:
                ctau = ctauP = str (ctau)
                ctauP = re.sub (r'\.', r'p', ctau)
            dataset = ('Higgsino_' if isHiggsino else 'AMSB_chargino_') + mass + 'GeV_' + ctauP + 'cm_' + suffix
            new_datasets.append (dataset)
    datasets.extend (new_datasets)
    
def getUser():
    dirs = {}
    cwd = os.getcwd()
    if "wulsin" in cwd:
        dirs['Andrew'] = "hartCondor/"
        dirs['Brian']  = "francisCondor/"
        dirs['Wells']  = ""
        dirs['Kai']    = "weiCondor/"
        user = "wulsin"
    elif "hart" in cwd:
        dirs['Andrew'] = ""
        dirs['Brian']  = "francisCondor/"
        dirs['Wells']  = "wellsCondor/"
        dirs['Kai']    = "weiCondor/"
        user = "hart"
    elif "bfrancis" in cwd:
        dirs['Andrew'] = "hartCondor/"
        dirs['Brian']  = ""
        dirs['Wells']  = "wellsCondor/"
        dirs['Zach']   = "pollockCondor/"
        dirs['Kai']    = "weiCondor/"
        user = "bfrancis"
    elif "zpollock" in cwd:
        dirs['Andrew'] = "hartCondor/"
        dirs['Brian']  = "francisCondor/"
        dirs['Wells']  = "wellsCondor/"
        dirs['Zach']   = ""
        dirs['Kai']    = "weiCondor/"
        user = "zpollock"
    elif "kwei" in cwd:
        dirs['Andrew'] = "hartCondor/"
        dirs['Brian']  = "francisCondor/"
        dirs['Wells']  = "wellsCondor/"
        dirs['Zach']   = "pollockCondor/"
        dirs['Kai']    = ""
        users = "kwei"
    else:
        print "Error:  could not identify user as bfrancis, hart, wulsin, or zpollock."
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

def invMassWithMassless (obj):
    energySquared = "(" + obj + ".energy + sqrt(track.px*track.px + track.py*track.py + track.pz*track.pz))"
    energySquared = energySquared + " * " + energySquared
    px = "(" + obj + ".px + track.px)"
    py = "(" + obj + ".py + track.py)"
    pz = "(" + obj + ".pz + track.pz)"
    momentumSquared = px + " * " + px + " + " + py + " * " + py + " + " + pz + " * " + pz
    return energySquared + " - (" + momentumSquared + ")"

def threeBodyInvMassWithMassless (obj1, obj2):
    energySquared = "(" + obj1 + ".energy + " + obj2 + ".energy + sqrt(track.px*track.px + track.py*track.py + track.pz*track.pz))"
    energySquared = energySquared + " * " + energySquared
    px = "(" + obj1 + ".px + " + obj2 + ".px + track.px)"
    py = "(" + obj1 + ".py + " + obj2 + ".px + track.py)"
    pz = "(" + obj1 + ".pz + " + obj2 + ".px + track.pz)"
    momentumSquared = px + " * " + px + " + " + py + " * " + py + " + " + pz + " * " + pz
    return energySquared + " - (" + momentumSquared + ")"

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

def setThresholdForFiducialMapVeto (process, threshold):
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

def setUseEraByEraFiducialMaps (process, doUse = True):
    for a in dir (process):
        x = getattr (process, a)
        if not hasattr (x, "type_"):
            continue
        if x.type_ () == "OSUTrackProducer":
            print "# Setting era-by-era implementation of fiducial maps to " + str (doUse)
            setattr (x, "useEraByEraFiducialMaps", cms.bool (doUse))

moveVariableProducerIndex = -1

def moveVariableProducer (process, producerName, channelName):

    global moveVariableProducerIndex
    moveVariableProducerIndex = moveVariableProducerIndex + 1

    producer = treemaker = plotter = eventvariableProducer = None
    producerLabel = treemakerLabel = plotterLabel = ""
    plotterPath = treemakerPath = None

    # find the variable producer and Plotter and TreeMaker (if it exists)
    for a in dir (process):
        x = getattr (process, a)
        if hasattr (x, "type_"):
            if x.type_ () == producerName and 'Copy' not in a:
                producer = copy.deepcopy (x)
                producerLabel = copy.deepcopy (a)
            if x.type_ () == "Plotter" and a == channelName+"Plotter":
                plotter = copy.deepcopy (x)
                plotterLabel = copy.deepcopy (a)
            if x.type_ () == "TreeMaker" and a == channelName+"TreeMaker":
                treemaker = copy.deepcopy (x)
                treemakerLabel = copy.deepcopy (a)

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

    # change the input tags for the TreeMaker, if it exists, which points to the products of the
    # variable producer to those produced by the copy of the variable producer
    # we created above
    if treemaker is not None:
        if hasattr (treemaker.collections, "eventvariables") and hasattr (treemaker.collections, "uservariables"):
            eventvariables = getattr (treemaker.collections, "eventvariables")
            uservariables = getattr (treemaker.collections, "uservariables")
            for i in range (0, min (len (eventvariables), len (uservariables))):
                if eventvariables[i].getModuleLabel () == producerLabel or uservariables[i].getModuleLabel () == producerLabel:
                    eventvariables[i].setModuleLabel ("objectProducerCopy" + str (moveVariableProducerIndex))
                    uservariables[i].setModuleLabel ("objectProducerCopy" + str (moveVariableProducerIndex))
            setattr (treemaker.collections, "eventvariables", eventvariables)
            setattr (treemaker.collections, "uservariables", uservariables)
        setattr (process, treemakerLabel, treemaker)
        treemaker = getattr (process, treemakerLabel)

    # insert the copy of the variable producer created above into the path
    # of the channel, right before the plotter and the TreeMaker if it exists
    channelPath = getattr (process, channelName)
    channelPath.remove (getattr (process, plotterLabel))
    if treemaker is not None:
        channelPath.remove (getattr (process, treemakerLabel))
    channelPath += producer
    channelPath += eventvariableProducer
    if treemaker is not None:
        channelPath += treemaker
    channelPath += plotter
    setattr (process, channelName, channelPath)

# Arbitration cuts (i.e. pick a random one amongst however many objects are left) have to be done at the end
# of the selection, otherwise you might be throwing out a possible passing object if there are any more cuts
# on that collection. 
def moveArbitrationToEnd (process, channelName):
    if hasattr (process, channelName + "CutCalculator"):
        x = getattr (process, channelName + "CutCalculator")
        cuts = x.cuts.cuts
        for cut in cuts:
            if hasattr (cut, "arbitration"):
                cuts.append(cuts.pop(cuts.index(cut)))

def getListOfChannels (process):
    channels = []
    for path in process.schedule:
        if hasattr (path, "label"):
            label = path.label ()
            if label != "variableProducerPath" and label != "endPath" and label != "egmGsfElectronIDSequence_step" and label != "egmGsfElectronIDSequenceOriginalElectrons_step" and label != "fullPatMetSequenceModifiedMETPath":
                channels.append (path.label ())

    return channels

# Create copies of a channel but replacing one cut with a range of replacements
# i.e. Cut --> [CutV1, CutV2, CutV3]...
# if Cut is None, just add CutV[n]
# In the calling module, you will need to use globals().update() on the resulting dict
def createChannelVariations (channel, channelName, cutToReplace, replacements):
    newChannels = {}
    for suffix in replacements:
        newChannels[channelName + suffix] = copy.deepcopy (channel)
        newChannels[channelName + suffix].name = cms.string (channel.name.value () + suffix)
        if cutToReplace is None:
            newChannels[channelName + suffix].cuts.append(replacements[suffix])
        else:
            replaceSingleCut (newChannels[channelName + suffix].cuts, replacements[suffix], cutToReplace)
    return newChannels
