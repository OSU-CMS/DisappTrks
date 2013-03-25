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
            numberRequired = cms.string(">= 1"),
            alias = cms.string("pT > 20 GeV")
            ),    
        cms.PSet (
            inputCollection = cms.string("tracks"),
            cutString = cms.string("fabs(eta) < 2.1"),
            numberRequired = cms.string(">= 1"),
            alias = cms.string("|eta| < 2.1")
            ),
        cms.PSet (
            inputCollection = cms.string("tracks"),
            cutString = cms.string("fabs(d0wrtBS) < 0.05"),
            numberRequired = cms.string(">= 1"),
            alias = cms.string("|d0| < 0.05 cm")
            ),
        cms.PSet (
            inputCollection = cms.string("tracks"),
            cutString = cms.string("fabs(dZwrtBS) < 15"),
            numberRequired = cms.string(">= 1"),
            alias = cms.string("|dz| < 15 cm")
            ),
        cms.PSet (
            inputCollection = cms.string("tracks"),
            cutString = cms.string("numValidHits > 4"),
            numberRequired = cms.string(">= 1"),
            alias = cms.string("Valid Hits > 4")
            ),
        cms.PSet (
            inputCollection = cms.string("tracks"),
            cutString = cms.string("nHitsMissingMiddle == 0"),
            numberRequired = cms.string(">= 1"),
            alias = cms.string("Missing Middle Hits = 0")
            ),
        cms.PSet (
            inputCollection = cms.string("tracks"),
            cutString = cms.string("isIso == 1"),
            numberRequired = cms.string(">= 1"),
            alias = cms.string("Track Isolation")
            ),
        cms.PSet (
            inputCollection = cms.string("muons"),
            cutString = cms.string("pt > -1"),
            numberRequired = cms.string("= 0"),
            alias = cms.string("Muon Veto")
            ),
        cms.PSet (
            inputCollection = cms.string("electrons"),
            cutString = cms.string("pt > -1"),
            numberRequired = cms.string("= 0"),
            alias = cms.string("Electron Veto")
            ),
        cms.PSet (
            inputCollection = cms.string("tracks"),
            cutString = cms.string("isMatchedDeadEcal == 0"),
            numberRequired = cms.string(">= 1"),
            alias = cms.string("deadEcal Veto")
            ),
        cms.PSet (
            inputCollection = cms.string("tracks"),
            cutString = cms.string("fabs(eta) < 1.42 | fabs(eta) > 1.65"),
            numberRequired = cms.string(">= 1"),
            alias = cms.string("Crack Veto")
            ),
        )   
) # End PreSelection = cms.PSet(
 


#Channels for cut on PDG Id
##GenElec
cutElectronId = cms.PSet(
    inputCollection = cms.string("tracks"),
    cutString = cms.string("fabs(genMatchedPdgId) == 11"),
    numberRequired = cms.string(">= 1"),
    alias = cms.string("GenElec")
    )
PreSelectionElectronId = cms.PSet(
    name = cms.string("PreSelectionElectronId"),
    cuts = copy.deepcopy(PreSelection.cuts),
    )
PreSelectionElectronId.cuts.append(cutElectronId)
##GenPion
cutPionId =cms.PSet(
    inputCollection = cms.string("tracks"),
    cutString = cms.string("fabs(genMatchedPdgId) == 211"),
    numberRequired = cms.string(">= 1"),
    alias = cms.string("GenPion")
    )
PreSelectionPionId = cms.PSet(
    name = cms.string("PreSelectionPionId"),
    cuts = copy.deepcopy(PreSelection.cuts),
    )
PreSelectionPionId.cuts.append(cutPionId)

cutNotGenMatched = cms.PSet(
    inputCollection = cms.string("tracks"),
    cutString = cms.string("fabs(genMatchedPdgId) == 0"),
    numberRequired = cms.string(">= 1"),
    alias = cms.string("No Gen Match")
    )
PreSelectionNotGenMatched = cms.PSet(
    name = cms.string("PreSelectionNotGenMatched"),
    cuts = copy.deepcopy(PreSelection.cuts),
    )
PreSelectionPionId.cuts.append(cutNotGenMatched)


PreSelectionPt20 = cms.PSet(
    name = cms.string("PreSelectionPt20"),
    cuts  = copy.deepcopy(PreSelection.cuts),
    )

cutPt20 = cms.PSet (
    inputCollection = cms.string("tracks"),
    cutString = cms.string("pt > 20 & pt < 50"),
    numberRequired = cms.string(">= 1"),
    alias = cms.string("20 GeV < pT < 50 GeV ")
    )

PreSelectionPt20.cuts.append(cutPt20)

PreSelectionPt50 = cms.PSet(
    name = cms.string("PreSelectionPt50"),
    cuts  = copy.deepcopy(PreSelection.cuts),
    )

cutPt50 = cms.PSet (
    inputCollection = cms.string("tracks"),
    cutString = cms.string("pt > 50 & pt < 75"),
    numberRequired = cms.string(">= 1"),
    alias = cms.string("50 GeV < pT < 75 GeV ")
    )


PreSelectionPt50.cuts.append(cutPt50)

PreSelectionPt75 = cms.PSet(
    name = cms.string("PreSelectionPt75"),
    cuts  = copy.deepcopy(PreSelection.cuts),
    )

cutPt75 = cms.PSet (
    inputCollection = cms.string("tracks"),
    cutString = cms.string("pt > 75 & pt < 100"),
    numberRequired = cms.string(">= 1"),
    alias = cms.string("75 GeV < pT < 100 GeV ")
    )

PreSelectionPt75.cuts.append(cutPt75)

PreSelectionPt100 = cms.PSet(
    name = cms.string("PreSelectionPt100"),
    cuts  = copy.deepcopy(PreSelection.cuts),
    )

cutPt100 = cms.PSet (
    inputCollection = cms.string("tracks"),
    cutString = cms.string("pt > 100 & pt < 125"),
    numberRequired = cms.string(">= 1"),
    alias = cms.string("100 GeV < pT < 125 GeV ")
    )


PreSelectionPt100.cuts.append(cutPt100)

PreSelectionPt125 = cms.PSet(
    name = cms.string("PreSelectionPt125"),
    cuts  = copy.deepcopy(PreSelection.cuts),
    )

cutPt125 = cms.PSet (
    inputCollection = cms.string("tracks"),
    cutString = cms.string("pt > 125"),
    numberRequired = cms.string(">= 1"),
    alias = cms.string("125 GeV < pT ")
    )


PreSelectionPt125.cuts.append(cutPt125)

#Standard PreSelection Cuts with the Trigger, Jet pT, and MET cuts applied
PreSelectionWithTrigJetMet = cms.PSet(
    name = cms.string("PreSelectionWithTrigJetMet"),
    triggers = cms.vstring("HLT_MonoCentralPFJet80_PFMETnoMu95_NHEF0p95_v", "HLT_MonoCentralPFJet80_PFMETnoMu105_NHEF0p95_v", "HLT_MET120_HBHENoiseCleaned_v"),
    cuts  = copy.deepcopy(PreSelection.cuts),
    )

cutMET = cms.PSet (
    inputCollection = cms.string("mets"),
    cutString = cms.string("pt > 220"),
    numberRequired = cms.string(">= 1"),
    alias = cms.string("MET > 220 Gev")
    )

cutJetPt = cms.PSet (
    inputCollection = cms.string("jets"),
    cutString = cms.string("pt > 110"),
    numberRequired = cms.string(">= 1"),
    alias = cms.string("jet pT > 110 GeV")
    )

PreSelectionWithTrigJetMet.cuts.insert(0,cutJetPt)  
PreSelectionWithTrigJetMet.cuts.insert(0,cutMET)


#Cuts that define the signal region after the PreSelection with Trig, Jet, and MET
##NMissingHits + Eiso/p
SigRegWithTrigJetMet = copy.deepcopy(PreSelectionWithTrigJetMet)
SigRegWithTrigJetMet.name = cms.string("SigRegWithTrigJetMet")
cutMaxCaloByP = cms.PSet (
    inputCollection = cms.string("tracks"),
    cutString = cms.string("caloTotDeltaRp5ByP < 0.1"),
    numberRequired = cms.string(">= 1"),
    alias = cms.string("Eiso/p < 0.1")
    )

cutNMissingOuterHits = cms.PSet (
    inputCollection = cms.string("tracks"),
    cutString = cms.string("nHitsMissingOuter >= 3"),
    numberRequired = cms.string(">= 1"),
    alias = cms.string("Missing Outer Hits > 2")
    )


SigRegWithTrigJetMet.cuts.append(cutNMissingOuterHits)
SigRegWithTrigJetMet.cuts.append(cutMaxCaloByP)

##NMissingHits + Eiso
SigRegWithMaxCalo = copy.deepcopy(PreSelection)
SigRegWithMaxCalo.name = cms.string("SigRegWithMaxCalo")
cutMaxCalo = cms.PSet(
    inputCollection = cms.string("tracks"),
    cutString = cms.string("caloTotDeltaRp5 < 10"),
    numberRequired = cms.string(">= 1"),
    alias = cms.string("CaloTot < 10 GeV")
    )
SigRegWithMaxCalo.cuts.append(cutMaxCalo)
SigRegWithMaxCalo.cuts.append(cutNMissingOuterHits)


#Cuts that define the control region after the PreSelection with Trig, Jet, and MET
CtrlRegWithTrigJetMet = copy.deepcopy(PreSelectionWithTrigJetMet)
CtrlRegWithTrigJetMet.name = cms.string("CtrlRegWithTrigJetMet")

cutNMissingOuterHitsCtrlReg = cms.PSet (
    inputCollection = cms.string("tracks"),
    cutString = cms.string("nHitsMissingOuter == 0"),
    numberRequired = cms.string(">= 1"),
    alias = cms.string("Missing Outer Hits = 0")
    )


CtrlRegWithTrigJetMet.cuts.append(cutNMissingOuterHitsCtrlReg)

#Cuts that define the fit region after the PreSelection with Trig, Jet, and MET
##NMissingHits + Eiso/p
FitReg = copy.deepcopy(PreSelection)
FitReg.name = cms.string("FitReg")

cutMaxCaloByPFitReg = cms.PSet (
    inputCollection = cms.string("tracks"),
    cutString = cms.string("caloTotDeltaRp5ByP < 0.5"),
    numberRequired = cms.string(">= 1"),
    alias = cms.string("Eiso/p < 0.5")
    )

FitReg.cuts.append(cutMaxCaloByPFitReg)
FitReg.cuts.append(cutNMissingOuterHits)


##NMissingHits + Eiso
cutMaxCaloFitReg = cms.PSet (
    inputCollection = cms.string("tracks"),
    cutString = cms.string("caloTotDeltaRp5 < 30"),
    numberRequired = cms.string(">= 1"),
    alias = cms.string("Eiso < 30")
    )

FitRegWithMaxCalo = copy.deepcopy(PreSelection)
FitRegWithMaxCalo.name = cms.string("FitRegWithMaxCalo")

FitRegWithMaxCalo.cuts.append(cutMaxCaloFitReg)
FitRegWithMaxCalo.cuts.append(cutNMissingOuterHits)

#Cuts that define the signal region without Trig, Jet, and MET
SigReg = copy.deepcopy(PreSelection)
SigReg.name = cms.string("SigReg")
SigReg.cuts.append(cutNMissingOuterHits)
SigReg.cuts.append(cutMaxCaloByP)

#PreSelection + NHitsMissing
PreSelectionPMissing = copy.deepcopy(PreSelection)
PreSelectionPMissing.name = cms.string("PreSelectionPMissing")
PreSelectionPMissing.cuts.append(cutNMissingOuterHits)

PreSelectionPMissingPionId = copy.deepcopy(PreSelectionPMissing)
PreSelectionPMissingPionId.name = cms.string("PreSelectionPMissingPionId")
PreSelectionPMissingPionId.cuts.append(cutPionId)

PreSelectionPMissingElectronId = copy.deepcopy(PreSelectionPMissing)
PreSelectionPMissingElectronId.name = cms.string("PreSelectionPMissingElectronId")
PreSelectionPMissingElectronId.cuts.append(cutElectronId)

PreSelectionPMissingNotGenMatched = copy.deepcopy(PreSelectionPMissing)
PreSelectionPMissingNotGenMatched.name = cms.string("PreSelectionPMissingNotGenMatched")
PreSelectionPMissingNotGenMatched.cuts.append(cutNotGenMatched)


#PreSelection + Eiso/p
PreSelectionPEiso = copy.deepcopy(PreSelection)
PreSelectionPEiso.name = cms.string("PreSelectionPEiso")
PreSelectionPEiso.cuts.append(cutMaxCaloByP)

#Cuts that define the control region after the PreSelection with Trig, Jet, and MET
CtrlReg = copy.deepcopy(PreSelection)
CtrlReg.name = cms.string("CtrlReg")
CtrlReg.cuts.append(cutNMissingOuterHitsCtrlReg)

#Cuts that define the fit region after the PreSelection with Trig, Jet, and MET
FitRegWithTrigJetMet = copy.deepcopy(PreSelectionWithTrigJetMet)
FitRegWithTrigJetMet.name = cms.string("FitRegWithTrigJetMet")
FitRegWithTrigJetMet.cuts.append(cutMaxCaloByPFitReg)
FitRegWithTrigJetMet.cuts.append(cutNMissingOuterHits)

#Divided up into Pt Slices
PreSelectionPt20 = cms.PSet(
    name = cms.string("PreSelectionPt20"),
    cuts  = copy.deepcopy(PreSelection.cuts),
    )
cutPt20 = cms.PSet (
    inputCollection = cms.string("tracks"),
    cutString = cms.string("pt > 20 & pt < 50"),
    numberRequired = cms.string(">= 1"),
    alias = cms.string("20 GeV < pT < 50 GeV ")
    )


PreSelectionPt20.cuts.append(cutPt20)

PreSelectionPt50 = cms.PSet(
    name = cms.string("PreSelectionPt50"),
    cuts  = copy.deepcopy(PreSelection.cuts),
    )

cutPt50 = cms.PSet (
    inputCollection = cms.string("tracks"),
    cutString = cms.string("pt > 50 & pt < 75"),
    numberRequired = cms.string(">= 1"),
    alias = cms.string("50 GeV < pT < 75 GeV ")
    )


PreSelectionPt50.cuts.append(cutPt50)

PreSelectionPt75 = cms.PSet(
    name = cms.string("PreSelectionPt75"),
    cuts  = copy.deepcopy(PreSelection.cuts),
    )

cutPt75 = cms.PSet (
    inputCollection = cms.string("tracks"),
    cutString = cms.string("pt > 75 & pt < 100"),
    numberRequired = cms.string(">= 1"),
    alias = cms.string("75 GeV < pT < 100 GeV ")
    )


PreSelectionPt75.cuts.append(cutPt75)

PreSelectionPt100 = cms.PSet(
    name = cms.string("PreSelectionPt100"),
    cuts  = copy.deepcopy(PreSelection.cuts),
    )

cutPt100 = cms.PSet (
    inputCollection = cms.string("tracks"),
    cutString = cms.string("pt > 100 & pt < 125"),
    numberRequired = cms.string(">= 1"),
    alias = cms.string("100 GeV < pT < 125 GeV ")
    )


PreSelectionPt100.cuts.append(cutPt100)

PreSelectionPt125 = cms.PSet(
    name = cms.string("PreSelectionPt125"),
    cuts  = copy.deepcopy(PreSelection.cuts),
    )

cutPt125 = cms.PSet (
    inputCollection = cms.string("tracks"),
    cutString = cms.string("pt > 125"),
    numberRequired = cms.string(">= 1"),
    alias = cms.string("125 GeV < pT ")
    )


PreSelectionPt125.cuts.append(cutPt125)




# Selection of control samples

ZtoMuMu = cms.PSet(
    # Get this example from http://cmssw.cvs.cern.ch/cgi-bin/cmssw.cgi/UserCode/OSUT3Analysis/AnaTools/python/MyEventSelections.py?revision=1.2&view=markup  
    name = cms.string("ZtoMuMu"),
    cuts = cms.VPSet (
        cms.PSet (
            inputCollection = cms.string("muons"),
            cutString = cms.string("abs(eta) < 2.5"),
            numberRequired = cms.string(">= 2")
            ),    
        cms.PSet (
            inputCollection = cms.string("muons"),
            cutString = cms.string("pt > 25"),
            numberRequired = cms.string(">= 2")
            ),
        cms.PSet (
            inputCollection = cms.string("muons"),
            cutString = cms.string("tightID > 0"),
            numberRequired = cms.string(">= 2")
            ),
        cms.PSet (
            inputCollection = cms.string("muons"),
            cutString = cms.string("relPFdBetaIso < 0.12"),
            numberRequired = cms.string(">= 2")
            ),
        cms.PSet (
            inputCollection = cms.string("muon-muon pairs"),
            cutString = cms.string("invMass > 40 & invMass < 160"),
            numberRequired = cms.string(">= 1")
            ),
        )   
)



ZtoEE = cms.PSet(
    name = cms.string("ZtoEE"),
    cuts = cms.VPSet (
        cms.PSet (
            inputCollection = cms.string("electrons"),
            cutString = cms.string("pt > 20"),
            numberRequired = cms.string(">= 2"),
            alias = cms.string("pT > 20 GeV")
            ),    
        cms.PSet (
            inputCollection = cms.string("electrons"),
            cutString = cms.string("fabs(eta) < 2.1"),
            numberRequired = cms.string(">= 2"),
            alias = cms.string("|eta| < 2.1")
            ),
        cms.PSet (
            inputCollection = cms.string("muons"),
            cutString = cms.string("pt > -1"),
            numberRequired = cms.string("= 0"),
            alias = cms.string("Muon Veto")
            ),
        cms.PSet (
            inputCollection = cms.string("electron-electron pairs"),
            cutString = cms.string("invMass > 40 & invMass < 160"),
            numberRequired = cms.string(">= 1")
            ),
    )  # end cuts = cms.VPSet (
) # end ZtoEE = cms.PSet(

 



