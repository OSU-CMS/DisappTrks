import FWCore.ParameterSet.Config as cms
import OSUT3Analysis.DBTools.osusub_cfg as osusub
from DisappTrks.StandardAnalysis.utilities import *
from OSUT3Analysis.Configuration.Color import *
from DisappTrks.StandardAnalysis.Triggers import *
from DisappTrks.TriggerAnalysis.AllTriggers import *
from OSUT3Analysis.Configuration.configurationOptions import *
from DisappTrks.BackgroundEstimation.EventMETTriggerProducer_cfi import customizeForMETTriggerProducer
from DisappTrks.BackgroundEstimation.EventL1ETMProducer_cfi import customizeForL1ETMProducer
import os
from Configuration.AlCa.GlobalTag import GlobalTag

def customize (process,
               runPeriod,
               runEra,
               realData = True,
               applyPUReweighting = True,
               applyISRReweighting = True,
               applyTriggerReweighting = True,
               applyMissingHitsCorrections = True,
               runMETFilters = True,
               runEcalBadCalibFilters = True):

    if osusub.batchMode and (osusub.datasetLabel in types) and types[osusub.datasetLabel] != "signalMC":
        applyISRReweighting = False
    if realData:
        applyISRReweighting = False

    if runPeriod == "2015":

        data_global_tag = '76X_dataRun2_v15'
        mc_global_tag = '76X_mcRun2_asymptotic_v12'

        process.PUScalingFactorProducer.PU     = cms.FileInPath ('DisappTrks/StandardAnalysis/data/pu_disappTrks_run2.root')
        process.PUScalingFactorProducer.target = cms.string ("data2015")
        process.PUScalingFactorProducer.targetUp = cms.string ("data2015Up")
        process.PUScalingFactorProducer.targetDown = cms.string ("data2015Down")

        process.ISRWeightProducer.weightFile = cms.FileInPath ('DisappTrks/StandardAnalysis/data/isrWeight_disappTrks_run2.root')
        process.ISRWeightProducer.weightHist = cms.vstring('madgraphOverPythia', 'SingleMu_2015D')
        process.ISRWeightProducer.pdgIds = cms.vint32(1000022, 1000024)
        process.ISRWeightProducer.motherIdsToReject = cms.vint32()
        process.ISRWeightProducer.requireLastNotFirstCopy = cms.bool(False) # Pythia6 + Geant style

        process.LifetimeWeightProducer.requireLastNotFirstCopy = cms.bool(False) # Pythia6 + Geant style

        process.TriggerWeightProducer.efficiencyFile = cms.FileInPath ('DisappTrks/StandardAnalysis/data/triggerEfficiencies_disappTrks_run2.root')
        process.TriggerWeightProducer.dataset = cms.string('SingleMu_2015D')
        process.TriggerWeightProducer.target = cms.string('WJetsToLNu')
        process.TriggerWeightProducer.inclusiveMetTriggers = triggersMetInclusive
        process.TriggerWeightProducer.produceMetLeg = cms.bool(False)
        process.TriggerWeightProducer.produceTrackLeg = cms.bool(False)
        process.TriggerWeightProducer.produceGrandOr = cms.bool(True)

        setFiducialMaps (process, electrons="OSUT3Analysis/Configuration/data/electronFiducialMap_2015_data.root", muons="OSUT3Analysis/Configuration/data/muonFiducialMap_2015_data.root")
        setThresholdForFiducialMapVeto (process, 2.0)

        setMissingHitsCorrection (process, "2015")

    elif runPeriod == "2016BC":

        data_global_tag = '80X_dataRun2_2016SeptRepro_v6'
        mc_global_tag = '80X_mcRun2_asymptotic_2016_v3'

        process.PUScalingFactorProducer.PU     = cms.FileInPath ('DisappTrks/StandardAnalysis/data/pu_disappTrks_run2.root')
        process.PUScalingFactorProducer.target = cms.string ("data2016_BC")
        process.PUScalingFactorProducer.targetUp = cms.string ("data2016_BCUp")
        process.PUScalingFactorProducer.targetDown = cms.string ("data2016_BCDown")

        process.ISRWeightProducer.weightFile = cms.FileInPath ('DisappTrks/StandardAnalysis/data/isrWeight_disappTrks_run2.root')
        process.ISRWeightProducer.weightHist = cms.vstring('madgraphOverPythia', 'SingleMu_2016')
        process.ISRWeightProducer.pdgIds = cms.vint32(1000022, 1000024)
        process.ISRWeightProducer.motherIdsToReject = cms.vint32()
        process.ISRWeightProducer.requireLastNotFirstCopy = cms.bool(False) # Pythia6 + Geant style

        process.LifetimeWeightProducer.requireLastNotFirstCopy = cms.bool(False) # Pythia6 + Geant style

        process.TriggerWeightProducer.efficiencyFile = cms.FileInPath ('DisappTrks/StandardAnalysis/data/triggerEfficiencies_disappTrks_run2.root')
        process.TriggerWeightProducer.dataset = cms.string('SingleMu_2016BC')
        process.TriggerWeightProducer.target = cms.string('WJetsToLNu')
        process.TriggerWeightProducer.inclusiveMetTriggers = triggersMetInclusive
        process.TriggerWeightProducer.produceMetLeg = cms.bool(False)
        process.TriggerWeightProducer.produceTrackLeg = cms.bool(False)
        process.TriggerWeightProducer.produceGrandOr = cms.bool(True)

        setFiducialMaps (process, electrons="OSUT3Analysis/Configuration/data/electronFiducialMap_2016_data.root", muons="OSUT3Analysis/Configuration/data/muonFiducialMap_2016_data.root")
        setThresholdForFiducialMapVeto (process, 2.0)

        setMissingHitsCorrection (process, "2016BC")

        if hasattr (process, "prefiringweight"):
            process.prefiringweight.DataEra = cms.string("2016BtoH")
            process.L1PrefiringWeightProducer.DataEra = cms.string("2016BtoH")

    elif runPeriod == "2016DEFGH":
        
        data_global_tag = '80X_dataRun2_2016SeptRepro_v6'
        mc_global_tag = '80X_mcRun2_asymptotic_2016_v3'

        process.PUScalingFactorProducer.PU     = cms.FileInPath ('DisappTrks/StandardAnalysis/data/pu_disappTrks_run2.root')
        process.PUScalingFactorProducer.target = cms.string ("data2016_DEFGH")
        process.PUScalingFactorProducer.targetUp = cms.string ("data2016_DEFGHUp")
        process.PUScalingFactorProducer.targetDown = cms.string ("data2016_DEFGHDown")

        process.ISRWeightProducer.weightFile = cms.FileInPath ('DisappTrks/StandardAnalysis/data/isrWeight_disappTrks_run2.root')
        process.ISRWeightProducer.weightHist = cms.vstring('madgraphOverPythia', 'SingleMu_2016')
        process.ISRWeightProducer.pdgIds = cms.vint32(1000022, 1000024)
        process.ISRWeightProducer.motherIdsToReject = cms.vint32()
        process.ISRWeightProducer.requireLastNotFirstCopy = cms.bool(False) # Pythia6 + Geant style

        process.LifetimeWeightProducer.requireLastNotFirstCopy = cms.bool(False) # Pythia6 + Geant style

        process.TriggerWeightProducer.efficiencyFile = cms.FileInPath ('DisappTrks/StandardAnalysis/data/triggerEfficiencies_disappTrks_run2.root')
        process.TriggerWeightProducer.dataset = cms.string('SingleMu_2016DEFGH')
        process.TriggerWeightProducer.target = cms.string('WJetsToLNu')
        process.TriggerWeightProducer.inclusiveMetTriggers = triggersMetInclusive
        process.TriggerWeightProducer.produceMetLeg = cms.bool(False)
        process.TriggerWeightProducer.produceTrackLeg = cms.bool(False)
        process.TriggerWeightProducer.produceGrandOr = cms.bool(True)

        setFiducialMaps (process, electrons="OSUT3Analysis/Configuration/data/electronFiducialMap_2016_data.root", muons="OSUT3Analysis/Configuration/data/muonFiducialMap_2016_data.root")
        setThresholdForFiducialMapVeto (process, 2.0)

        setMissingHitsCorrection (process, "2016DEFGH")

        if hasattr (process, "prefiringweight"):
            process.prefiringweight.DataEra = cms.string("2016BtoH")
            process.L1PrefiringWeightProducer.DataEra = cms.string("2016BtoH")

    elif runPeriod == "2017":

        data_global_tag = '94X_dataRun2_ReReco_EOY17_v6'
        mc_global_tag = '94X_mc2017_realistic_v15'

        process.PUScalingFactorProducer.PU     = cms.FileInPath ('DisappTrks/StandardAnalysis/data/pu_disappTrks_run2.root')
        process.PUScalingFactorProducer.target = cms.string ("data2017")
        process.PUScalingFactorProducer.targetUp = cms.string ("data2017Up")
        process.PUScalingFactorProducer.targetDown = cms.string ("data2017Down")

        process.ISRWeightProducer.weightFile = cms.FileInPath ('DisappTrks/StandardAnalysis/data/isrWeight_disappTrks_run2.root')
        process.ISRWeightProducer.weightHist = cms.vstring('madgraphOverPythia8_94X', 'SingleMu_2017')
        process.ISRWeightProducer.pdgIds = cms.vint32(1000022, 1000024)
        process.ISRWeightProducer.motherIdsToReject = cms.vint32()
        process.ISRWeightProducer.requireLastNotFirstCopy = cms.bool(True) # Pythia8 style

        process.LifetimeWeightProducer.requireLastNotFirstCopy = cms.bool(True) # Pythia8 style

        process.TriggerWeightProducer.efficiencyFile = cms.FileInPath ('DisappTrks/StandardAnalysis/data/triggerEfficiencies_disappTrks_run2.root')
        process.TriggerWeightProducer.dataset = cms.string('SingleMu_2017')
        process.TriggerWeightProducer.target = cms.string('WJetsToLNu_94X')
        process.TriggerWeightProducer.inclusiveMetTriggers = triggersMetInclusive
        process.TriggerWeightProducer.produceMetLeg = cms.bool(False)
        process.TriggerWeightProducer.produceTrackLeg = cms.bool(False)
        process.TriggerWeightProducer.produceGrandOr = cms.bool(True)

        setFiducialMaps (process, electrons="OSUT3Analysis/Configuration/data/electronFiducialMap_2017_data.root", muons="OSUT3Analysis/Configuration/data/muonFiducialMap_2017_data.root")
        setThresholdForFiducialMapVeto (process, 2.0)
        setUseEraByEraFiducialMaps (process, True)

        setMissingHitsCorrection (process, "2017")

        if hasattr (process, "prefiringweight"):
            process.prefiringweight.DataEra = cms.string("2017BtoF")
            process.L1PrefiringWeightProducer.DataEra = cms.string("2017BtoF")

    elif runPeriod == "2018":

        data_global_tag = '102X_dataRun2_Sep2018ABC_v2'
        mc_global_tag = '102X_upgrade2018_realistic_v18'

        process.PUScalingFactorProducer.PU     = cms.FileInPath ('DisappTrks/StandardAnalysis/data/pu_disappTrks_run2.root')
        process.PUScalingFactorProducer.target = cms.string ("data2018")
        process.PUScalingFactorProducer.targetUp = cms.string ("data2018Up")
        process.PUScalingFactorProducer.targetDown = cms.string ("data2018Down")

        process.ISRWeightProducer.weightFile = cms.FileInPath ('DisappTrks/StandardAnalysis/data/isrWeight_disappTrks_run2.root')
        process.ISRWeightProducer.weightHist = cms.vstring('madgraphOverPythia8_102X', 'SingleMu_2018')
        process.ISRWeightProducer.pdgIds = cms.vint32(1000022, 1000024)
        process.ISRWeightProducer.motherIdsToReject = cms.vint32()
        process.ISRWeightProducer.requireLastNotFirstCopy = cms.bool(True) # Pythia8 style

        process.LifetimeWeightProducer.requireLastNotFirstCopy = cms.bool(True) # Pythia8 style

        process.TriggerWeightProducer.efficiencyFile = cms.FileInPath ('DisappTrks/StandardAnalysis/data/triggerEfficiencies_disappTrks_run2.root')
        process.TriggerWeightProducer.dataset = cms.string('SingleMu_2018')
        process.TriggerWeightProducer.target = cms.string('WJetsToLNu_102X')
        process.TriggerWeightProducer.inclusiveMetTriggers = triggersMetInclusive
        process.TriggerWeightProducer.produceMetLeg = cms.bool(False)
        process.TriggerWeightProducer.produceTrackLeg = cms.bool(False)
        process.TriggerWeightProducer.produceGrandOr = cms.bool(True)

        setFiducialMaps (process, electrons="OSUT3Analysis/Configuration/data/electronFiducialMap_2018_data.root", muons="OSUT3Analysis/Configuration/data/muonFiducialMap_2018_data.root")
        setThresholdForFiducialMapVeto (process, 2.0)
        setUseEraByEraFiducialMaps (process, True)

        setMissingHitsCorrection (process, "2018")

    elif runPeriod == "2022":

        data_global_tag = '124X_dataRun3_Prompt_v4'
        mc_global_tag = '124X_mcRun3_2022_realistic_v12'
    
        if runEra in ['C','D','E']:
            data_global_tag = '130X_dataRun3_v2'
        elif runEra in ['F','G']:
            data_global_tag = '130X_dataRun3_PromptAnalysis_v1'
        
        if runEra in ['C', 'D']:
            mc_global_tag = '130X_mcRun3_2022_realistic_v5'
        elif runEra in ['E', 'F', 'G']:
            mc_global_tag = '130X_mcRun3_2022_realistic_postEE_v6'

        if runEra in ['C', 'D']:

            changeMuonTriggerFilter(process,'HLT_IsoMu24_v','hltIterL3MuonCandidates::HLT','hltL3crIsoL1sSingleMu22L1f0L2f10QL3f24QL3trkIsoFiltered0p08')

            if not realData:

                changeScaleFactorsRun3(process,'2022CD')
                changeLeptonWeightsRun3(process,'2022CD')

        process.PUScalingFactorProducer.PU = cms.FileInPath ('DisappTrks/StandardAnalysis/data/pu_disappTrks_run3.root')
        process.PUScalingFactorProducer.target = cms.string ("data2022")
        process.PUScalingFactorProducer.targetUp = cms.string ("data2022Up")
        process.PUScalingFactorProducer.targetDown = cms.string ("data2022Down")
        process.PUScalingFactorProducer.dataset = cms.string ("mc2022_22Sep2023") # This is usually not added in here, but it makes things easier

        process.ISRWeightProducer.weightFile = cms.FileInPath ('DisappTrks/StandardAnalysis/data/isrWeight_disappTrks_run3.root')
        process.ISRWeightProducer.weightHist = cms.vstring('Muon_2022F')
        process.ISRWeightProducer.pdgIds = cms.vint32(1000022, 1000024)
        process.ISRWeightProducer.motherIdsToReject = cms.vint32()
        process.ISRWeightProducer.requireLastNotFirstCopy = cms.bool(True) # Pythia8 style

        process.LifetimeWeightProducer.requireLastNotFirstCopy = cms.bool(True) # Pythia8 style

        process.TriggerWeightProducer.efficiencyFile = cms.FileInPath ('DisappTrks/StandardAnalysis/data/triggerEfficiencies_disappTrks_run3.root')
        process.TriggerWeightProducer.dataset = cms.string('Muon_2022')
        process.TriggerWeightProducer.target = cms.string('WJetsToLNu_2022')
        process.TriggerWeightProducer.inclusiveMetTriggers = triggersMetInclusive
        process.TriggerWeightProducer.produceMetLeg = cms.bool(False)
        process.TriggerWeightProducer.produceTrackLeg = cms.bool(False)
        process.TriggerWeightProducer.produceGrandOr = cms.bool(True)

        if runEra in ['E', 'F', 'G']:
            process.EventJetVarProducer.jetVetoMap = cms.FileInPath ('OSUT3Analysis/Configuration/data/Summer22EE_23Sep2023_RunEFG_v1.root')
            print("Using jet veto map for 2022 eras E/F/G")
        else:
            process.EventJetVarProducer.jetVetoMap = cms.FileInPath ('OSUT3Analysis/Configuration/data/Summer22_23Sep2023_RunCD_v1.root')
            print("Using jet veto map for 2022 eras C/D")

        if runEra == 'C':
            setFiducialMaps (process, electrons="OSUT3Analysis/Configuration/data/electronFiducialMap_2022C_data.root", muons="OSUT3Analysis/Configuration/data/muonFiducialMap_2022C_data.root")
        elif runEra == 'D':
            setFiducialMaps (process, electrons="OSUT3Analysis/Configuration/data/electronFiducialMap_2022D_data.root", muons="OSUT3Analysis/Configuration/data/muonFiducialMap_2022D_data.root")
        elif runEra =='E':
            setFiducialMaps (process, electrons="OSUT3Analysis/Configuration/data/electronFiducialMap_2022E_data.root", muons="OSUT3Analysis/Configuration/data/muonFiducialMap_2022E_data.root")
        elif runEra=='F':
            setFiducialMaps (process, electrons="OSUT3Analysis/Configuration/data/electronFiducialMap_2022F_data.root", muons="OSUT3Analysis/Configuration/data/muonFiducialMap_2022F_data.root")
        elif runEra=='G':
            setFiducialMaps (process, electrons="OSUT3Analysis/Configuration/data/electronFiducialMap_2022G_data.root", muons="OSUT3Analysis/Configuration/data/muonFiducialMap_2022G_data.root")
        else:
            print("Warning fiducial maps not found for era {} in customize.py, will use 2022F as default".format(runEra))
            setFiducialMaps (process, electrons="OSUT3Analysis/Configuration/data/electronFiducialMap_2022F_data.root", muons="OSUT3Analysis/Configuration/data/muonFiducialMap_2022F_data.root")

        setThresholdForFiducialMapVeto (process, 2.0)
        setUseEraByEraFiducialMaps (process, True)
        setMissingHitsCorrection (process, "uncorrected")

    elif runPeriod == "2023":

        data_global_tag = '130X_dataRun3_PromptAnalysis_v1'
        if runEra in ['C']:
            mc_global_tag = '130X_mcRun3_2023_realistic_v14'
        elif runEra in ['D']:
            mc_global_tag = '130X_mcRun3_2023_realistic_postBPix_v2'

        if runEra in ['C']:

            if not realData:

                changeScaleFactorsRun3(process,'2023C')
                changeLeptonWeightsRun3(process,'2023C')

        if runEra in ['D']:

            if not realData:

                changeScaleFactorsRun3(process,'2023D',prefix='NoHole')
                changeLeptonWeightsRun3(process,'2023D',prefix='NoHole')

            strsPlotter = []
            strsObjectScalingFactorProducer = []

        process.PUScalingFactorProducer.PU     = cms.FileInPath ('DisappTrks/StandardAnalysis/data/pu_disappTrks_run3.root')
        process.PUScalingFactorProducer.target = cms.string ("data2023")
        process.PUScalingFactorProducer.targetUp = cms.string ("data2023Up")
        process.PUScalingFactorProducer.targetDown = cms.string ("data2023Down")
        process.PUScalingFactorProducer.dataset = cms.string ("mc2023_22Sep2023") # This is usually not added in here, but it makes things easier

        # These come from the 2018 corrections - need to be fixed
        process.ISRWeightProducer.weightFile = cms.FileInPath ('DisappTrks/StandardAnalysis/data/isrWeight_disappTrks_run2.root')
        process.ISRWeightProducer.weightHist = cms.vstring('madgraphOverPythia8_102X', 'SingleMu_2018')
        process.ISRWeightProducer.pdgIds = cms.vint32(1000022, 1000024)
        process.ISRWeightProducer.motherIdsToReject = cms.vint32()
        process.ISRWeightProducer.requireLastNotFirstCopy = cms.bool(True) # Pythia8 style

        process.LifetimeWeightProducer.requireLastNotFirstCopy = cms.bool(True) # Pythia8 style

        process.TriggerWeightProducer.efficiencyFile = cms.FileInPath ('DisappTrks/StandardAnalysis/data/triggerEfficiencies_disappTrks_run3.root')
        process.TriggerWeightProducer.dataset = cms.string('Muon_2023')
        process.TriggerWeightProducer.target = cms.string('WJetsToLNu_2023')
        process.TriggerWeightProducer.inclusiveMetTriggers = triggersMetInclusive
        process.TriggerWeightProducer.produceMetLeg = cms.bool(False)
        process.TriggerWeightProducer.produceTrackLeg = cms.bool(False)
        process.TriggerWeightProducer.produceGrandOr = cms.bool(True)

        if runEra in ['C']:
            process.EventJetVarProducer.jetVetoMap = cms.FileInPath ('OSUT3Analysis/Configuration/data/Summer23Prompt23_RunC_v1.root')
            print("Using jet veto map for 2023 eras C")
        elif runEra in ['D']:
            process.EventJetVarProducer.jetVetoMap = cms.FileInPath ('OSUT3Analysis/Configuration/data/Summer23BPixPrompt23_RunD_v1.root')
            print("Using jet veto map for 2023 eras D")
        else:
            print("There is no jet veto map set up for this era, please add it to OSUT3Analysis/Configuration/data/")

        setFiducialMaps (process, electrons="OSUT3Analysis/Configuration/data/electronFiducialMap_2022F_data.root", muons="OSUT3Analysis/Configuration/data/muonFiducialMap_2022F_data.root")
        setThresholdForFiducialMapVeto (process, 2.0)
        setUseEraByEraFiducialMaps (process, True)
        
        setMissingHitsCorrection (process, "uncorrected")

    #set the global tag
    process.load('Configuration.StandardSequences.GeometryRecoDB_cff')
    process.load('Configuration.StandardSequences.FrontierConditions_GlobalTag_cff')
    if realData:
        print("# Global tag: " + A_BRIGHT_CYAN + data_global_tag + A_RESET)
        process.GlobalTag = GlobalTag(process.GlobalTag, data_global_tag, '')
    else:
        print("# Global tag: " + A_BRIGHT_CYAN + mc_global_tag + A_RESET)
        process.GlobalTag = GlobalTag(process.GlobalTag, mc_global_tag, '')

    if not applyPUReweighting:
        # process.PUScalingFactorProducer.PU     = cms.FileInPath ("") # Path of FileInPath can't be empty; module won't do anything because the rest is empty
        process.PUScalingFactorProducer.target = cms.string ("")
        process.PUScalingFactorProducer.targetUp = cms.string ("")
        process.PUScalingFactorProducer.targetDown = cms.string ("")

    if not applyISRReweighting:
        # process.ISRWeightProducer.weightFile = cms.FileInPath("") # Path of FileInPath can't be empty; module won't do anything because the rest is empty
        process.ISRWeightProducer.weightHist = cms.vstring()

    if not applyTriggerReweighting:
        # process.TriggerWeightProducer.efficiencyFile  =  cms.FileInPath  ("") # Path of FileInPath can't be empty; module won't do anything because the rest is empty
        process.TriggerWeightProducer.dataset         =  cms.string  ("")
        process.TriggerWeightProducer.target          =  cms.string  ("")
        process.TriggerWeightProducer.produceMetLeg = cms.bool(False)
        process.TriggerWeightProducer.produceTrackLeg = cms.bool(False)

    if not applyMissingHitsCorrections:
        setMissingHitsCorrection (process, "uncorrected")

    for channel in getListOfChannels (process):
        moveVariableProducer (process, "TriggerWeightProducer", channel)
        if hasattr (process, "DeDxHitInfoVarProducer"):
            moveVariableProducer (process, "DeDxHitInfoVarProducer", channel)

        doFilter    = ("WithFilter" in channel)
        doLooseFilter    = ("WithLooseFilter" in channel)
        doSSFilter  = ("WithSSFilter" in channel)
        doLooseSSFilter  = ("WithLooseSSFilter" in channel)
        doJetFilter = ("WithJetFilter" in channel)

        if hasattr (process, "EventElectronTPProducer"):
            getattr (process, "EventElectronTPProducer").doFilter = cms.bool (doFilter)
            getattr (process, "EventElectronTPProducer").doLooseFilter = cms.bool (doLooseFilter)
            getattr (process, "EventElectronTPProducer").doSSFilter = cms.bool (doSSFilter)
            getattr (process, "EventElectronTPProducer").doLooseSSFilter = cms.bool (doLooseSSFilter)
            getattr (process, "EventElectronTPProducer").doJetFilter = cms.bool (doJetFilter)
            getattr (process, "EventElectronTPProducer").triggerCollectionName = cms.string (triggerFiltersElectron[0])
            getattr (process, "EventElectronTPProducer").triggerFilterName = cms.string (triggerFiltersElectron[1])
            getattr (process, "EventElectronTPProducer").triggerMatchingDR = cms.double (0.3)
            getattr (process, "EventElectronTPProducer").probeTagMatchingDR = cms.double (0.3)
            moveVariableProducer (process, "EventElectronTPProducer", channel)
        if hasattr (process, "EventMuonTPProducer"):
            getattr (process, "EventMuonTPProducer").doFilter = cms.bool (doFilter)
            getattr (process, "EventMuonTPProducer").doLooseFilter = cms.bool (doLooseFilter)
            getattr (process, "EventMuonTPProducer").doSSFilter = cms.bool (doSSFilter)
            getattr (process, "EventMuonTPProducer").doLooseSSFilter = cms.bool (doLooseSSFilter)
            getattr (process, "EventMuonTPProducer").doJetFilter = cms.bool (doJetFilter)
            getattr (process, "EventMuonTPProducer").triggerCollectionName = cms.string (triggerFiltersMuon[0])
            getattr (process, "EventMuonTPProducer").triggerFilterName = cms.string (triggerFiltersMuon[1])
            if runPeriod == "2022" and runEra in ['C', 'D']: getattr (process, "EventMuonTPProducer").triggerFilterName = cms.string ("hltL3crIsoL1sSingleMu22L1f0L2f10QL3f24QL3trkIsoFiltered0p08")
            getattr (process, "EventMuonTPProducer").triggerMatchingDR = cms.double (0.3)
            getattr (process, "EventMuonTPProducer").probeTagMatchingDR = cms.double (0.3)
            moveVariableProducer (process, "EventMuonTPProducer", channel)
        if hasattr (process, "EventTauToElectronTPProducer"):
            getattr (process, "EventTauToElectronTPProducer").doFilter = cms.bool (doFilter)
            getattr (process, "EventTauToElectronTPProducer").doLooseFilter = cms.bool (doLooseFilter)
            getattr (process, "EventTauToElectronTPProducer").doSSFilter = cms.bool (doSSFilter)
            getattr (process, "EventTauToElectronTPProducer").doLooseSSFilter = cms.bool (doLooseSSFilter)
            getattr (process, "EventTauToElectronTPProducer").doJetFilter = cms.bool (doJetFilter)
            getattr (process, "EventTauToElectronTPProducer").triggerCollectionName = cms.string (triggerFiltersTau[0])
            getattr (process, "EventTauToElectronTPProducer").triggerFilterName = cms.string (triggerFiltersTau[1])
            getattr (process, "EventTauToElectronTPProducer").triggerMatchingDR = cms.double (0.3)
            getattr (process, "EventTauToElectronTPProducer").probeTagMatchingDR = cms.double (0.3)
            moveVariableProducer (process, "EventTauToElectronTPProducer", channel)
        if hasattr (process, "EventTauToMuonTPProducer"):
            getattr (process, "EventTauToMuonTPProducer").doFilter = cms.bool (doFilter)
            getattr (process, "EventTauToMuonTPProducer").doLooseFilter = cms.bool (doLooseFilter)
            getattr (process, "EventTauToMuonTPProducer").doSSFilter = cms.bool (doSSFilter)
            getattr (process, "EventTauToMuonTPProducer").doLooseSSFilter = cms.bool (doLooseSSFilter)
            getattr (process, "EventTauToMuonTPProducer").doJetFilter = cms.bool (doJetFilter)
            getattr (process, "EventTauToMuonTPProducer").triggerCollectionName = cms.string (triggerFiltersTau[0])
            getattr (process, "EventTauToMuonTPProducer").triggerFilterName = cms.string (triggerFiltersTau[1])
            getattr (process, "EventTauToMuonTPProducer").triggerMatchingDR = cms.double (0.3)
            getattr (process, "EventTauToMuonTPProducer").probeTagMatchingDR = cms.double (0.3)
            moveVariableProducer (process, "EventTauToMuonTPProducer", channel)

        if hasattr (process, "EventElectronMETTriggerProducer"):
            customizeForMETTriggerProducer (getattr (process, "EventElectronMETTriggerProducer"))
            moveVariableProducer (process, "EventElectronMETTriggerProducer", channel)
        if hasattr (process, "EventMuonMETTriggerProducer"):
            customizeForMETTriggerProducer (getattr (process, "EventMuonMETTriggerProducer"))
            moveVariableProducer (process, "EventMuonMETTriggerProducer", channel)
        if hasattr (process, "EventTauMETTriggerProducer"):
            customizeForMETTriggerProducer (getattr (process, "EventTauMETTriggerProducer"))
            moveVariableProducer (process, "EventTauMETTriggerProducer", channel)

        if hasattr (process, "EventElectronL1ETMProducer"):
            customizeForL1ETMProducer (getattr (process, "EventElectronL1ETMProducer"), runPeriod)
            moveVariableProducer (process, "EventElectronL1ETMProducer", channel)
        if hasattr (process, "EventMuonL1ETMProducer"):
            customizeForL1ETMProducer (getattr (process, "EventMuonL1ETMProducer"), runPeriod)
            moveVariableProducer (process, "EventMuonL1ETMProducer", channel)
        if hasattr (process, "EventTauL1ETMProducer"):
            customizeForL1ETMProducer (getattr (process, "EventTauL1ETMProducer"), runPeriod)
            moveVariableProducer (process, "EventTauL1ETMProducer", channel)

        moveArbitrationToEnd (process, channel)

    if runMETFilters:
        process.schedule.insert (0, process.metFilterPath)

    if runEcalBadCalibFilters:
        process.schedule.insert (0, process.passecalBadCalibFilterUpdatePath)

    if hasattr (process, "EventJetVarProducer") and not hasattr (process.EventJetVarProducer, "triggerNames"):
        process.EventJetVarProducer.triggerNames = cms.vstring ()

    return process
