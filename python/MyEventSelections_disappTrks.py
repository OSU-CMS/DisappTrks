import FWCore.ParameterSet.Config as cms
import copy

###########################################################
##### Set up the event selections (channels) #####
###########################################################

##### List of valid input collections #####   
# jets, muons, electrons, taus, photons, mets,
# events, tracks, primaryvertexs,
# genjets, mcparticles,
# bxlumis, superclusters


#Standard Preselection Cuts

PreSelection = cms.PSet(
    name = cms.string("PreSelection"),
    cuts = cms.VPSet (
      cms.PSet (
        inputCollection = cms.string("tracks"),
        cutString = cms.string("pt > 20"),
        numberRequired = cms.string(">= 1")
      ),    
      cms.PSet (
        inputCollection = cms.string("tracks"),
        cutString = cms.string("fabs(eta) < 2.1"),
        numberRequired = cms.string(">= 1")
      ),
      
      cms.PSet (
         inputCollection = cms.string("tracks"),
         cutString = cms.string("fabs(d0wrtBS) < 0.05"),
         numberRequired = cms.string(">= 1")
         ),
      cms.PSet (
             inputCollection = cms.string("tracks"),
             cutString = cms.string("fabs(dZwrtBS) < 15"),
             numberRequired = cms.string(">= 1")
             ),
      cms.PSet (
            inputCollection = cms.string("tracks"),
            cutString = cms.string("numValidHits > 4"),
            numberRequired = cms.string(">= 1")
                              ),

    cms.PSet (
            inputCollection = cms.string("tracks"),
            cutString = cms.string("nHitsMissingMiddle == 0"),
            numberRequired = cms.string(">= 1")
                              ),

    cms.PSet (
            inputCollection = cms.string("tracks"),
            cutString = cms.string("isIso == 1"),
            numberRequired = cms.string(">= 1")
                              ),

                              
      cms.PSet (
           inputCollection = cms.string("muons"),
           cutString = cms.string("pt > -1"),
           numberRequired = cms.string("= 0")
           ),

      cms.PSet (
           inputCollection = cms.string("electrons"),
           cutString = cms.string("pt > -1"),
           numberRequired = cms.string("= 0")
           ),

           cms.PSet (
           inputCollection = cms.string("tracks"),
           cutString = cms.string("isMatchedDeadEcal == 0"),
           numberRequired = cms.string(">= 1")
           ),

           cms.PSet (
           inputCollection = cms.string("tracks"),
           cutString = cms.string("fabs(eta) < 1.42 | fabs(eta) > 1.65"),
           numberRequired = cms.string(">= 1")
           ),
      
      
   )   
)



#Standard PreSelection Cuts with the Trigger, Jet pT, and MET cuts applied
PreSelectionWithTrigJetMet = cms.PSet(
    name = cms.string("PreSelection With Trig, Jet, Met"),
    triggers = cms.vstring("HLT_MonoCentralPFJet80_PFMETnoMu95_NHEF0p95_v", "HLT_MonoCentralPFJet80_PFMETnoMu105_NHEF0p95_v", "HLT_MET120_HBHENoiseCleaned_v"),
    cuts  = copy.deepcopy(PreSelection.cuts),
    )

cutMET = cms.PSet (
        inputCollection = cms.string("mets"),
        cutString = cms.string("et > 220"),
        numberRequired = cms.string(">= 1")
)

cutJetPt = cms.PSet (
        inputCollection = cms.string("jets"),
        cutString = cms.string("pt > 110"),
        numberRequired = cms.string(">= 1")
)

PreSelectionWithTrigJetMet.cuts.insert(0,cutJetPt)  
PreSelectionWithTrigJetMet.cuts.insert(0,cutMET)


#Cuts that define the signal region after the PreSelection with Trig, Jet, and MET
SigRegWithTrigJetMet = copy.deepcopy(PreSelectionWithTrigJetMet)
SigRegWithTrigJetMet.name = cms.string("Signal Region with Trig, Jet, and MET")
cutMaxCaloByP = cms.PSet (
        inputCollection = cms.string("tracks"),
        cutString = cms.string("caloTotDeltaRp5ByP < 0.1"),
        numberRequired = cms.string(">= 1")
)

cutNMissingOuterHits = cms.PSet (
        inputCollection = cms.string("tracks"),
        cutString = cms.string("nHitsMissingOuter >= 3"),
        numberRequired = cms.string(">= 1")
)


SigRegWithTrigJetMet.cuts.append(cutNMissingOuterHits)
SigRegWithTrigJetMet.cuts.append(cutMaxCaloByP)



#Cuts that define the control region after the PreSelection with Trig, Jet, and MET
CtrlRegWithTrigJetMet = copy.deepcopy(PreSelectionWithTrigJetMet)
CtrlRegWithTrigJetMet.name = cms.string("Control Region with Trig, Jet, and MET")

cutNMissingOuterHitsCtrlReg = cms.PSet (
        inputCollection = cms.string("tracks"),
        cutString = cms.string("nHitsMissingOuter == 0"),
        numberRequired = cms.string(">= 1")
)


CtrlRegWithTrigJetMet.cuts.append(cutNMissingOuterHitsCtrlReg)

#Cuts that define the fit region after the PreSelection with Trig, Jet, and MET
FitReg = copy.deepcopy(PreSelection)
FitReg.name = cms.string("Fit Region")

cutMaxCaloFitReg = cms.PSet (
        inputCollection = cms.string("tracks"),
        cutString = cms.string("caloTotDeltaRp5ByP < 0.5"),
        numberRequired = cms.string(">= 1")
)

FitReg.cuts.append(cutMaxCaloFitReg)

#Cuts that define the signal region without Trig, Jet, and MET
SigReg = copy.deepcopy(PreSelection)
SigReg.name = cms.string("Signal Region")
SigReg.cuts.append(cutNMissingOuterHits)
SigReg.cuts.append(cutMaxCaloByP)


#Cuts that define the control region after the PreSelection with Trig, Jet, and MET
CtrlReg = copy.deepcopy(PreSelection)
CtrlReg.name = cms.string("Control Region")
CtrlReg.cuts.append(cutNMissingOuterHitsCtrlReg)

#Cuts that define the fit region after the PreSelection with Trig, Jet, and MET
FitRegWithTrigJetMet = copy.deepcopy(PreSelectionWithTrigJetMet)
FitRegWithTrigJetMet.name = cms.string("Fit Region with Trig, Jet, and MET")
FitRegWithTrigJetMet.cuts.append(cutMaxCaloFitReg)








