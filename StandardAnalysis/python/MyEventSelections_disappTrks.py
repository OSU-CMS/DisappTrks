import FWCore.ParameterSet.Config as cms
import copy
from DisappTrks.StandardAnalysis.MyCuts_disappTrks import *  # Put all the individual cuts in this file 
################################################
##### List of cut VPSets                   #####
################################################


cutsStdClean = cms.VPSet (
    cutEvtFilter,
    cutVtxGood, 
    )

cutsMET = cms.VPSet (
    cutMET,
)

cutsJets = cms.VPSet (
        cutSecJetPt,
        cutSecJetEta2p4,            
        cutSecJetNoiseChgHad,
        cutSecJetNoiseChgEM,
        cutSecJetNoiseNeuHad,
        cutSecJetNoiseNeuEM,
        cutSubLeadingJetID,
        cutJetJetDPhi,
        cutMetDeltaPhiMin2Jets0p5, 
)

cutsJetsNoNoiseClean = cms.VPSet (
##     cutSecJetPt,
##     cutSecJetEta2p4,
##     cutJetPt30,
##     cutJetEta4p5,  # Not committed
##     cutJetJetDPhi,
    )


cutsJetsNoDPhi = cms.VPSet (
    cutSecJetPt,
    cutSecJetEta2p4,
    cutSecJetNoiseChgHad,
    cutSecJetNoiseChgEM,
    cutSecJetNoiseNeuHad,
    cutSecJetNoiseNeuEM,
    cutSubLeadingJetID,
    )


cutsTrkPtEta = cms.VPSet (
    cutTrkPt,
    cutTrkEta,
    )

cutsTrkQuality = cms.VPSet (
    cutTrkD0,
    cutTrkDZ,
    cutTrkNHits,
    cutTrkHitMissMid,
    cutTrkHitMissIn,
    )

cutsTrkQualityFiveHits = cms.VPSet (
    cutTrkD0,
    cutTrkDZ,
    cutTrkNHitsIs5,
    cutTrkHitMissMid,
    cutTrkHitMissIn,
    )

cutsTrkQualityNoNHits = cms.VPSet (
    cutTrkD0,
    cutTrkDZ,
    cutTrkHitMissMid,
    cutTrkHitMissIn,
    )

cutsTrkIso = cms.VPSet (
    cutTrkRelIsoRp3,  
    cutTrkJetDeltaR,
    )

cutsTrkVetoRegions = cms.VPSet (
    cutTrkCrackVeto,
    cutTrkWheel0GapVeto, 
    cutTrkEtaMuonPk, 
    cutTrkDeadEcalVeto,
    cutTrkBadCSCVeto, 
    )

cutsTrkLeptonVeto = cms.VPSet (
    cutTauLooseHadronicVeto,  
    cutElecLooseIDVeto,
    cutMuonLooseIDVeto,
    cutSecMuonLooseIDVeto, 
    )

cutsTrkLeptonVetoNoMu = cms.VPSet (
    cutTauLooseHadronicVeto,
    cutElecLooseIDVeto,
    )


cutsTrkPreselFiveHits = \
  cutsTrkVetoRegions + \
  cutsTrkQualityFiveHits + \
  cutsTrkIso + \
  cutsTrkLeptonVeto 


cutsTrkPresel = \
              cutsTrkPtEta + \
              cutsTrkVetoRegions + \
              cutsTrkQuality + \
              cutsTrkIso + \
              cutsTrkLeptonVeto

cutsTrkPreselNoLepVeto = \
  cutsTrkPtEta + \
  cutsTrkVetoRegions + \
  cutsTrkQuality + \
  cutsTrkIso 

cutsTrkPreselNoLepVetoOrVetoRegion = \
  cutsTrkPtEta + \
  cutsTrkQuality + \
  cutsTrkIso


cutsTrkPreselNoMuCuts = \
  cutsTrkPtEta + \
  cms.VPSet(
    cutTrkCrackVeto,
    cutTrkDeadEcalVeto,
    ) + \
  cutsTrkQuality + \
  cutsTrkIso + \
  cutsTrkLeptonVeto 

cutsTrkPreselNoMuCutsNoLepVeto = \
  cutsTrkPtEta + \
  cms.VPSet(
    cutTrkCrackVeto,
    cutTrkDeadEcalVeto,
    ) + \
  cutsTrkQuality + \
  cutsTrkIso


cutsPresel = \
  cutsStdClean + \
  cutsMET + \
  cutsJets + \
  cutsTrkPresel

cutsPreselCtrlNMiss = copy.deepcopy(cutsPresel)
for cut in cutsPreselCtrlNMiss:  
    if cut.cutString == cutTrkPt.cutString:
        cut.cutString = cutTrkPt30.cutString # replace pT>50 with pT>30 cut  
cutsPreselCtrlNMiss.append(cutTrkHitMissOutInv)

cutsTrkPreselCtrlNMiss = copy.deepcopy(cutsTrkPresel)
for cut in cutsTrkPreselCtrlNMiss:  
    if cut.cutString == cutTrkPt.cutString:
        cut.cutString = cutTrkPt30.cutString # replace pT>50 with pT>30 cut  
cutsTrkPreselCtrlNMiss.append(cutTrkHitMissOutInv)  

cutsPreselCtrlEcalo = copy.deepcopy(cutsPresel)
for cut in cutsPreselCtrlEcalo:  
    if cut.cutString == cutTrkPt.cutString:
        cut.cutString = cutTrkPt30.cutString # replace pT>50 with pT>30 cut  
cutsPreselCtrlEcalo.append(cutMaxCalo10Inv)  

cutsTrkPreselCtrlEcalo = copy.deepcopy(cutsTrkPresel)
for cut in cutsTrkPreselCtrlEcalo:  
    if cut.cutString == cutTrkPt.cutString:
        cut.cutString = cutTrkPt30.cutString # replace pT>50 with pT>30 cut  
cutsTrkPreselCtrlEcalo.append(cutMaxCalo10Inv)   


cutsPreselFiveHits = \
           cutsStdClean + \
           cutsMET + \
           cutsJets + \
           cutsTrkPreselFiveHits

cutsPreselNoMet = \
  cutsJets + \
  cutsTrkPresel

cutsSigReg = cms.VPSet (
    cutMaxCalo10, 
    cutTrkHitMissOut,
    )

cutsFullSelection = \
  cutsPresel + \
  cutsSigReg

cutsTrkIdOther = cms.VPSet (
  cutTrkMuonIdInv, 
  cutTrkElecIdInv, 
  cutTrkTauIdInv, 
  cutTrkNotGenMatchedInv
  )

cutsTrkPreselSigReg = \
  cutsTrkPresel + \
  cms.VPSet (
    cutMaxCalo10, 
    cutTrkHitMissOut,
    )

cutsTagMuon = cms.VPSet (
    # See SMP-12-023 for example of W->mu nu selection  
    cutMuonPt25,
    cutMuonEta,
    cutMuonTightID,
    cutMuonPFIso,
    )

cutsTagElec = cms.VPSet (
    # See https://twiki.cern.ch/twiki/bin/view/CMS/MultivariateElectronIdentification#Triggering_MVA  
    cutElecPt30,
    cutElecEta,
    cutElecMva,
    cutElecPFIso,
    cutElecD0,
    cutElecDZ,
    cutElecPassConvVeto, 
    cutElecLostHits, 
    )


cutsMuTauHad = cms.VPSet (
    cutTauPt,
    cutTauEta,
    cutTauAgainstElectron,
    cutTauAgainstMuonTight,
    cutTauDecayModeFinding,
    cutTauLooseIso,
    cutMuonLooseIDOnlyOne,
    cutMuonEta,
    cutMuonPt25,
    cutMuonTightID,
    cutMuonPFIso,
    cutMuonD0,
    cutMuonDZ,
    cutMuonMetMT,
    )

cutsMuTrk = cms.VPSet (
#    cutTauPt,
#    cutTauEta,
#    cutTauAgainstElectron,
#    cutTauAgainstMuonTight,
#    cutTauDecayModeFinding,
#    cutTauLooseIso,
    cutMuonLooseIDOnlyOne,
    cutMuonEta,
    cutMuonPt25,
    cutMuonTightID,
    cutMuonPFIso,
    cutMuonD0,
    cutMuonDZ,
    cutMuonMetMT,
    )

cutsMuTauHadZPeak = cms.VPSet (
    cutMuTauCharge,
    cutMuTauInvMass,
#    cutMuTrkDeltaR,
#    cutTauTrkDeltaR,
    )

cutsMuTrkHadZPeak = cms.VPSet (
    cutMuTrkChgOpp,
    cutMuTrkInvMass,
    #    cutMuTrkDeltaR,
    #    cutTauTrkDeltaR,
    )

    
cutsMuTrkZPeak = cms.VPSet (
    cutMuTrkInvMass80To100,
    cutMuTrkChgOpp,
    )

cutsElecTrkZPeak = cms.VPSet (
    cutElecTrkInvMass80To100,
    cutElecTrkChgOpp,
    )


################################################
##### List of  event selections (channels) #####
################################################
TauBkgdMismeasure = cms.PSet(
    name = cms.string("TauBkgdMismeasure"),
    triggers = triggersJetMet,
    cuts =
    cutsPreselFiveHits +
    cms.VPSet ( cutTrkEta  ) +
    cms.VPSet ( cutTrkHitMissOut  ) +
    cms.VPSet ( cutTrkTauId ) 
    )

TauBkgdPreselNoTau = cms.PSet(
    name = cms.string("TauBkgdPreselNoTau"),
    triggers = triggersJetMet,
    cuts =
    cutsMET +
    cutsJets +
    cms.VPSet ( cutTrkPt30, cutTrkEta  ) +
    cutsTrkVetoRegions +
    cutsTrkQuality +
    cms.VPSet (
    cutTrkRelIsoRp3,
    cutMuonLooseIDVeto,
    cutSecMuonLooseIDVeto,
    cutElecLooseIDVeto,
    #cutTauLooseHadronicVeto,
    ),
    )

TauBkgdPresel = cms.PSet(
    name = cms.string("TauBkgdPresel"),
    triggers = triggersJetMet,
    cuts =
    cutsMET +
    cutsJets +
    cms.VPSet ( cutTrkPt30, cutTrkEta  ) +
    cutsTrkVetoRegions +
    cutsTrkQuality +
    cms.VPSet (
    cutTrkRelIsoRp3,
    cutMuonLooseIDVeto,
    cutSecMuonLooseIDVeto,
    cutElecLooseIDVeto,
    cutTauLooseHadronicVeto,
    ),
    )



NoCuts = cms.PSet(
    name = cms.string("NoCuts"),
    cuts = cms.VPSet (
       cutNoCuts,
       ),
    )

# Use for plotting the stop lifetime  
StopLifetime = cms.PSet(
    name = cms.string("StopLifetime"),
    cuts = cms.VPSet (
       cutNoCuts,
       cutMCPartStatus3Filter,
       cutMCPartSusyFilter, 
#       cutStopPt50, 
       cutStopEta2p5,
#       cutStopCtauNegative, 
#       cutStopDauIdNotPion, 
       ),
    )

NoCutsFilterMC = cms.PSet(
    name = cms.string("NoCutsFilterMC"),
    cuts = cms.VPSet (
       cutNoCuts,
       cutMCPartStatus3Filter,
       cutMCPartSusyFilter, 
       ),
    )

NoCutsFilterMCCtauZero = cms.PSet(
    name = cms.string("NoCutsFilterMCCtauZero"),
    cuts = copy.deepcopy(NoCutsFilterMC.cuts) + 
    cms.VPSet (
       cutStopCtauZero,  
       ),
    )

NoCutsFilterMCCtauNonZero = cms.PSet(
    name = cms.string("NoCutsFilterMCCtauNonZero"),
    cuts = copy.deepcopy(NoCutsFilterMC.cuts) + 
    cms.VPSet (
       cutStopCtauNonZero,  
       ),
    )

NoCutsDecayInTrackerN2 = cms.PSet(
    name = cms.string("NoCutsDecayInTrackerN2"),
    cuts = copy.deepcopy(NoCutsFilterMC.cuts) + 
    cms.VPSet (
    ##     cutStopDecayLengthNonZeroN2,
    ##     cutStopDecayLengthTrackerN2
    cutStopDecayLengthZeroVeto, 
    cutStopDecayLengthOutsideTrackerVeto, 
    ),
    )


DebugCuts = cms.PSet(
    name = cms.string("DebugCuts"),
    cuts = cms.VPSet (
       cms.PSet(
          inputCollection = cms.string("jets"),
#          cutString = cms.string("isLeadingPtJet == 1"),
          cutString = cms.string("pt > 0"),
          numberRequired = cms.string(">= 0"),
          ),
       )
    )

TriggerJetMet = cms.PSet(
    name = cms.string("TriggerJetMet"),
    triggers = triggersJetMet,
    cuts = cms.VPSet (
         cutMET,
         cutSecJetPt,  # cut on secondary jets collection so that BNTree includes all jets  
    ),
    )

TriggerMet = cms.PSet(
    name = cms.string("TriggerMet"),
    triggers = triggersJetMet,
    cuts = cms.VPSet (
         cutMET,
         ),
    )

TriggerMetNoMu = cms.PSet(
    name = cms.string("TriggerMetNoMu"),
    triggers = triggersJetMet,
    cuts = cms.VPSet (
         cutMETNoMu,
         ),
    )

Trigger = cms.PSet(
    name = cms.string("Trigger"),
    triggers = triggersJetMet,
    cuts = cms.VPSet (
    cutNoCuts,
    ),
    )

SkimMet90 = cms.PSet(
    name = cms.string("SkimMet90"),
    cuts = cms.VPSet (
    cutMET90, 
    ),
    )


SingleMuTrigger = cms.PSet(
    name = cms.string("MuTrigger"),
    triggers = triggersSingleMu,
    cuts = cms.VPSet (
      cutNoCuts,
      ),
    )


TriggerJetMetDebug = cms.PSet(
    name = cms.string("TriggerJetMetDebug"),
    triggers = triggersJetMet,
    cuts = cms.VPSet (
        cutMET,  
        cutSecJetPt,  # cut on secondary jets collection so that BNTree includes all jets  
        ),
    )

TriggerJetMetDebug2 = cms.PSet(
    name = cms.string("TriggerJetMetDebug2"),
    triggers = triggersJetMet,
    cuts = cms.VPSet (
        cutMET,  
        cutSecJetPt,  # cut on secondary jets collection so that BNTree includes all jets  
        cutElecLooseIDVeto,  # cut on secondary jets collection so that BNTree includes all jets  
        ),
    )

TriggerJetMetDebug3 = cms.PSet(
    name = cms.string("TriggerJetMetDebug3"),
    triggers = triggersJetMet,
    cuts = cms.VPSet (
        cutMET,  
        cutSecJetPt,  # cut on secondary jets collection so that BNTree includes all jets  
        cutMuonLooseIDVeto,  # cut on secondary jets collection so that BNTree includes all jets  
        ),
    )

FullSelection = cms.PSet(
    name = cms.string("FullSelection"),
    triggers = triggersJetMet,
    cuts = cutsFullSelection, 
    )

FullSelectionNoMet = cms.PSet(
    name = cms.string("FullSelectionNoMet"),
    triggers = triggersJetMet,
    cuts = cutsFullSelection, 
    )

FullSelectionFilterMC = cms.PSet(
    # Filter the MC particles to include only the status 3 SUSY particles  
    name = cms.string("FullSelectionFilterMC"),
    triggers = triggersJetMet,
    cuts = cutsFullSelection +
    cms.VPSet( 
    cutMCPartStatus3Filter,
    cutMCPartSusyFilter,
    )
    )

FullSelectionStopCtauZero = copy.deepcopy(FullSelection) 
FullSelectionStopCtauZero.name = cms.string("FullSelectionStopCtauZero") 
FullSelectionStopCtauZero.cuts.append(cutStopCtauZero)  

FullSelectionStopCtauNonZero = copy.deepcopy(FullSelection) 
FullSelectionStopCtauNonZero.name = cms.string("FullSelectionStopCtauNonZero") 
FullSelectionStopCtauNonZero.cuts.append(cutStopCtauNonZero)  



FullSelectionMet80Trig = cms.PSet(
    name = cms.string("FullSelectionMet80Trig"),
    triggers = triggersMet80,
    cuts = cutsFullSelection, 
    )

FullSelectionNoPt = cms.PSet(
    name = cms.string("FullSelectionNoPt"),
    triggers = triggersJetMet,
    cuts = copy.deepcopy(cutsFullSelection), 
    )
# remove the cuts after and including the trkRelIso cut
for i in xrange(len(FullSelectionNoPt.cuts) - 1, -1, -1):
    if FullSelectionNoPt.cuts[i].cutString == cutTrkPt.cutString:
        del FullSelectionNoPt.cuts[i]  

FullSelectionMCSig = cms.PSet(
    name = cms.string("FullSelectionMCSig"),
    triggers = triggersJetMet,
    cuts = copy.deepcopy(cutsFullSelection), 
    )
FullSelectionMCSig.cuts.append(cutMCPartStatus3)
FullSelectionMCSig.cuts.append(cutMCPartSusy)  


FullSelectionNoEta = cms.PSet(
    name = cms.string("FullSelectionNoEta"),
    triggers = triggersJetMet,
    cuts = copy.deepcopy(cutsFullSelection), 
    )
for i in xrange(len(FullSelectionNoEta.cuts) - 1, 8, -1):
    if str(FullSelectionNoEta.cuts[i].cutString).find("eta") != -1:  
        del FullSelectionNoEta.cuts[i]  

FullSelectionNoBadCSC = cms.PSet(
    name = cms.string("FullSelectionNoBadCSC"),
    triggers = triggersJetMet,
    cuts = copy.deepcopy(cutsFullSelection), 
    )
for i in xrange(len(FullSelectionNoBadCSC.cuts) - 1, -1, -1):
    if FullSelectionNoBadCSC.cuts[i].cutString == cutTrkBadCSCVeto.cutString:
        del FullSelectionNoBadCSC.cuts[i]  

FullSelectionNoD0 = cms.PSet(
    name = cms.string("FullSelectionNoD0"),
    triggers = triggersJetMet,
    cuts = copy.deepcopy(cutsFullSelection), 
    )
for i in xrange(len(FullSelectionNoD0.cuts) - 1, -1, -1):
    if FullSelectionNoD0.cuts[i].cutString == cutTrkD0.cutString:
        del FullSelectionNoD0.cuts[i]  

FullSelectionNoDZ = cms.PSet(
    name = cms.string("FullSelectionNoDZ"),
    triggers = triggersJetMet,
    cuts = copy.deepcopy(cutsFullSelection), 
    )
for i in xrange(len(FullSelectionNoDZ.cuts) - 1, -1, -1):
    if FullSelectionNoDZ.cuts[i].cutString == cutTrkDZ.cutString:
        del FullSelectionNoDZ.cuts[i]  

FullSelectionNoNhits = cms.PSet(
    name = cms.string("FullSelectionNoNhits"),
    triggers = triggersJetMet,
    cuts = copy.deepcopy(cutsFullSelection), 
    )
for i in xrange(len(FullSelectionNoNhits.cuts) - 1, -1, -1):
    if FullSelectionNoNhits.cuts[i].cutString == cutTrkNHits.cutString:
        del FullSelectionNoNhits.cuts[i]  

FullSelectionNoRelIso = cms.PSet(
    name = cms.string("FullSelectionNoRelIso"),
    triggers = triggersJetMet,
    cuts = copy.deepcopy(cutsFullSelection), 
    )
for i in xrange(len(FullSelectionNoRelIso.cuts) - 1, -1, -1):
    if FullSelectionNoRelIso.cuts[i].cutString == cutTrkRelIsoRp3.cutString or FullSelectionNoRelIso.cuts[i].cutString == cutTrkJetDeltaR.cutString: 
        del FullSelectionNoRelIso.cuts[i]  

FullSelectionNoCalo = cms.PSet(
    name = cms.string("FullSelectionNoCalo"),
    triggers = triggersJetMet,
    cuts = copy.deepcopy(cutsFullSelection), 
    )
for i in xrange(len(FullSelectionNoCalo.cuts) - 1, -1, -1):
    if FullSelectionNoCalo.cuts[i].cutString == cutMaxCalo10.cutString:
        del FullSelectionNoCalo.cuts[i]  

FullSelectionNoMissHit = cms.PSet(
    name = cms.string("FullSelectionNoMissHit"),
    triggers = triggersJetMet,
    cuts = copy.deepcopy(cutsFullSelection), 
    )
for i in xrange(len(FullSelectionNoMissHit.cuts) - 1, -1, -1):
    if FullSelectionNoMissHit.cuts[i].cutString == cutTrkHitMissOut.cutString:
        del FullSelectionNoMissHit.cuts[i]  



FullTrkSelection = cms.PSet(
    # No cuts on Met or jet or trigger
    name = cms.string("FullTrkSelection"),
    cuts = cutsTrkPreselSigReg, 
    )

FullTrkSelectionWTrig = cms.PSet(
    triggers = triggersJetMet,
    name = cms.string("FullTrkSelectionWTrig"),
    cuts = cutsTrkPreselSigReg, 
    )

FullTrkSelectionUpToMissIn = cms.PSet(
    # No cuts on Met or jet or trigger
    name = cms.string("FullTrkSelectionUpToMissIn"),
    cuts = copy.deepcopy(cutsTrkPreselSigReg), 
    )
# remove the cuts after and including the trkRelIso cut
for i in range(0, len(FullTrkSelectionUpToMissIn.cuts)):  
    if FullTrkSelectionUpToMissIn.cuts[i].cutString == cutTrkRelIsoRp3.cutString:
        idx = i
del FullTrkSelectionUpToMissIn.cuts[idx:len(FullTrkSelectionUpToMissIn.cuts)]  

FullTrkSelectionUpToElecVeto = cms.PSet(
    # No cuts on Met or jet or trigger
    name = cms.string("FullTrkSelectionUpToElecVeto"),
    cuts = copy.deepcopy(cutsTrkPreselSigReg), 
    )
# remove the cuts after and including the muon veto  
for i in range(0, len(FullTrkSelectionUpToElecVeto.cuts)):  
    if FullTrkSelectionUpToElecVeto.cuts[i].cutString == cutMuonLooseIDVeto.cutString:
        idx = i
del FullTrkSelectionUpToElecVeto.cuts[idx:len(FullTrkSelectionUpToElecVeto.cuts)]  

FullTrkSelectionUpToElecVetoWTrig = cms.PSet(
    triggers = triggersJetMet,
    name = cms.string("FullTrkSelectionUpToElecVetoWTrig"),
    cuts = copy.deepcopy(FullTrkSelectionUpToElecVeto.cuts), 
    )

FullTrkSelectionUpToMuonVeto = cms.PSet(
    # No cuts on Met or jet or trigger
    name = cms.string("FullTrkSelectionUpToMuonVeto"),
    cuts = copy.deepcopy(cutsTrkPresel), 
    )
# remove the elec veto 
for i in xrange(len(FullTrkSelectionUpToMuonVeto.cuts) - 1, -1, -1): 
    if FullTrkSelectionUpToMuonVeto.cuts[i].cutString == cutElecLooseIDVeto.cutString:
        del FullTrkSelectionUpToMuonVeto.cuts[i]

FullTrkSelectionUpToMuonVetoWTrig = cms.PSet(
    triggers = triggersJetMet,
    name = cms.string("FullTrkSelectionUpToMuonVetoWTrig"),
    cuts = copy.deepcopy(FullTrkSelectionUpToMuonVeto.cuts), 
    )

FullTrkSelectionLeadingJet = cms.PSet(
    # No cuts on Met or jet or trigger
    name = cms.string("FullTrkSelectionLeadingJet"),
    cuts = copy.deepcopy(cutsTrkPreselSigReg), 
    )
FullTrkSelectionLeadingJet.cuts.append(cutJetLeadingPt)  

FullTrkSelectionJetPt = cms.PSet(
    # No cuts on Met or jet or trigger
    name = cms.string("FullTrkSelectionJetPt"),
    cuts = copy.deepcopy(cutsTrkPreselSigReg), 
    )
FullTrkSelectionJetPt.cuts.append(cutJetPt)  


MetJet = cms.PSet(
    name = cms.string("MetJet"),
    triggers = triggersJetMet,
    cuts =
    cutsMET +
    cutsJets, 
    )

PreSelection = cms.PSet(
    name = cms.string("PreSelection"),
    triggers = triggersJetMet,
    cuts = cutsPresel, 
    )

PreSelectionElecIdNoLepVeto = cms.PSet(
    name = cms.string("PreSelectionElecIdNoElecVeto"),
    triggers = triggersJetMet,
    cuts =
    cutsMET +
    cutsJets +
    cutsTrkPtEta +
    cutsTrkQuality +
    cutsTrkIso +
    cms.VPSet ( cutTrkWheel0GapVeto ) +
    cms.VPSet ( cutTrkEtaMuonPk ) +
    cms.VPSet ( cutTrkBadCSCVeto ) +
    cms.VPSet ( cutTrkElectronId ) +
    cutsSigReg
    
    )

PreSelectionNoLepVeto = cms.PSet(
    name = cms.string("PreSelectionNoLepVeto"),
    triggers = triggersJetMet,
    cuts =
    cutsTrkPreselNoLepVeto
    )


FullSelectionNoMet = cms.PSet(
    name = cms.string("FullSelectionNoMet"),
    triggers = triggersJetMet,
    cuts = 
    cutsJets + 
    cutsTrkPresel + 
    cutsSigReg
    )

FullSelectionNoMetNoTrig = cms.PSet(
    name = cms.string("FullSelectionNoMetNoTrig"),
    cuts = copy.deepcopy(FullSelectionNoMet.cuts), 
    )


FullSelectionFakeTrk = cms.PSet(
    name = cms.string("FullSelectionFakeTrk"),
    triggers = triggersJetMet,
    cuts = copy.deepcopy(cutsFullSelection), 
    )
idx = len(cutsMET) + len(cutsJets)  
FullSelectionFakeTrk.cuts.insert(idx, cutTrkNotGenMatched) 


FullSelectionNoTrkCuts = cms.PSet(
    name = cms.string("FullSelectionNoTrkCuts"),
    triggers = triggersJetMet,
    cuts = 
    cutsMET + 
    cutsJets 
    )

FullSelectionNoMetFakeTrk = cms.PSet(
    name = cms.string("FullSelectionNoMetFakeTrk"),
    triggers = triggersJetMet,
    cuts = 
    cutsJets + 
    cms.VPSet ( cutTrkNotGenMatched ) + 
    cutsTrkPresel + 
    cutsSigReg
    )

FullSelectionNoMetNoTrkCuts = cms.PSet(
    name = cms.string("FullSelectionNoMetNoTrkCuts"),
    triggers = triggersJetMet,
    cuts = 
    cutsJets 
    )


PreSelectionNoNoiseClean = cms.PSet(
    name = cms.string("PreSelectionNoNoiseClean"),
    triggers = triggersJetMet,
    cuts =
    cutsMET +
    cutsJetsNoNoiseClean 
    )

PreSelectionNoJetJetDPhi = cms.PSet(
    name = cms.string("PreSelectionNoJetJetDPhi"),
    triggers = triggersJetMet,
    cuts =
    cutsMET +
    cutsJetsNoDPhi 
#    cutsTrkPtEta +
#    cutsTrkQuality +
#    cutsTrkVetoRegions
    )

PreSelectionNoPt = copy.deepcopy(PreSelection)
PreSelectionNoPt.name = cms.string("PreSelectionNoPt")
for i in xrange(len(PreSelectionNoPt.cuts) - 1, -1, -1):
    if PreSelectionNoPt.cuts[i].cutString == cutTrkPt.cutString:
        del PreSelectionNoPt.cuts[i] 

PreSelectionNoNHit = copy.deepcopy(PreSelection)
PreSelectionNoNHit.name = cms.string("PreSelectionNoNHit")
for i in xrange(len(PreSelectionNoNHit.cuts) - 1, -1, -1):
    if PreSelectionNoNHit.cuts[i].cutString == cutTrkNHits.cutString:
        del PreSelectionNoNHit.cuts[i] 


PreSelectionNoIso = cms.PSet(
    name = cms.string("PreSelectionNoIso"),
    triggers = triggersJetMet,
    cuts =
    cutsMET +
    cutsJets +
    cutsTrkPtEta +
    cutsTrkVetoRegions +
    cutsTrkQuality +
    cutsTrkLeptonVeto
    )

PreSelectionNoMissIn = copy.deepcopy(PreSelection)
PreSelectionNoMissIn.name = cms.string("PreSelectionNoMissIn")  
for i in xrange(len(PreSelectionNoMissIn.cuts) - 1, -1, -1):
    if PreSelectionNoMissIn.cuts[i].cutString == cutTrkHitMissIn.cutString:
        del PreSelectionNoMissIn.cuts[i] 

PreSelectionNoMissMid = copy.deepcopy(PreSelection)
PreSelectionNoMissMid.name = cms.string("PreSelectionNoMissMid")  
for i in xrange(len(PreSelectionNoMissMid.cuts) - 1, -1, -1):
    if PreSelectionNoMissMid.cuts[i].cutString == cutTrkHitMissMid.cutString:
        del PreSelectionNoMissMid.cuts[i] 


FullSelectionElecPreveto = cms.PSet(
    name = cms.string("FullSelectionElecPreveto"),
    triggers = triggersJetMet,
    cuts = copy.deepcopy(cutsFullSelection),
    )
for i in xrange(len(FullSelectionElecPreveto.cuts) - 1, -1, -1):
    cut = FullSelectionElecPreveto.cuts[i]
    if cut.cutString == cutElecLooseIDVeto.cutString or cut.cutString == cutMaxCalo10.cutString: # remove elec veto and Ecalo cut
        del FullSelectionElecPreveto.cuts[i]
        

FullSelectionTauPreveto = cms.PSet(
    name = cms.string("FullSelectionTauPreveto"),
    triggers = triggersJetMet,
    cuts = copy.deepcopy(cutsFullSelection), 
    )
for i in xrange(len(FullSelectionTauPreveto.cuts) - 1, -1, -1):
    cut = FullSelectionTauPreveto.cuts[i]
    if cut.cutString == cutTauLooseHadronicVeto.cutString or cut.cutString == cutMaxCalo10.cutString: # remove tau veto and Ecalo cut
        del FullSelectionTauPreveto.cuts[i]

FullSelectionMuPreveto = cms.PSet(
    name = cms.string("FullSelectionMuPreveto"),
    triggers = triggersJetMet,
    cuts = copy.deepcopy(cutsFullSelection), 
    )
for i in xrange(len(FullSelectionMuPreveto.cuts) - 1, -1, -1):
    cut = FullSelectionMuPreveto.cuts[i]
    if cut.cutString == cutMuonLooseIDVeto.cutString or cut.cutString == cutSecMuonLooseIDVeto.cutString: # remove muon veto 
        del FullSelectionMuPreveto.cuts[i]

FullSelectionMuPrevetoMetNoMu = cms.PSet(
    name = cms.string("FullSelectionMuPrevetoMetNoMu"),
    triggers = triggersJetMet,
    cuts = copy.deepcopy(cutsFullSelection), 
    )
for i in xrange(len(FullSelectionMuPrevetoMetNoMu.cuts) - 1, -1, -1):
    cut = FullSelectionMuPrevetoMetNoMu.cuts[i]
    if cut.cutString == cutMET.cutString:
        cut.cutString = cutMETNoMu.cutString  # replace cutMET with cutMETNoMu
    if cut.cutString == cutMuonLooseIDVeto.cutString or cut.cutString == cutSecMuonLooseIDVeto.cutString: # remove muon veto 
        del FullSelectionMuPrevetoMetNoMu.cuts[i]

FullSelectionNHits4 = cms.PSet(
    name = cms.string("FullSelectionNHits4"),
    triggers = triggersJetMet,
    cuts = copy.deepcopy(FullSelection.cuts),
    )
for i in xrange(len(FullSelectionNHits4.cuts) - 1, -1, -1):
    if FullSelectionNHits4.cuts[i].cutString == cutTrkNHits.cutString:
        FullSelectionNHits4.cuts[i].cutString = cutTrkNHits4.cutString
                
FullSelectionNHits4MinFake = cms.PSet(
    name = cms.string("FullSelectionNHits4MinFake"),
    triggers = triggersJetMet,
    cuts = copy.deepcopy(FullSelection.cuts),
    )
for i in xrange(len(FullSelectionNHits4MinFake.cuts) - 1, -1, -1):
    if FullSelectionNHits4MinFake.cuts[i].cutString == cutTrkNHits.cutString:
        FullSelectionNHits4MinFake.cuts[i].cutString = cutTrkNHits4Min.cutString
FullSelectionNHits4MinFake.cuts.append(cutTrkNotGenMatched)  


forDeadEcal = cms.PSet(
    name = cms.string("forDeadEcal"),
    triggers = triggersJetMet,
    cuts =
    cutsMET +
    cutsJets +
    cms.VPSet ( cutTrkElectronId ) +
    cutsTrkPreselNoLepVetoOrVetoRegion +
    cms.VPSet ( cutMuonLooseIDVeto, cutSecMuonLooseIDVeto,  cutTauLooseHadronicVeto, cutTrkCrackVeto  ) +
    cms.VPSet (cutTrkHitMissOut)
    )

forDeadEcal_v2 = cms.PSet(
    name = cms.string("forDeadEcal_v2"),
    triggers = triggersJetMet,
    cuts =
    cutsMET +
    cutsJets +
    cms.VPSet ( cutTrkElectronId ) +
    cutsTrkPreselNoLepVetoOrVetoRegion +
    cms.VPSet ( cutMuonLooseIDVeto, cutSecMuonLooseIDVeto,  cutTauLooseHadronicVeto  ) +
    cms.VPSet (cutTrkHitMissOut) 
    )
        
        


StudyMuVeto = cms.PSet(
    name = cms.string("StudyMuVeto"),
#    triggers = triggersJetMet,
    triggers = triggersSingleMu,
    cuts = cms.VPSet (
##         cutTrkMuonId,
##         cutMuonLooseIDVeto,
##         cutMET, 
##         cutSecJetPt,
##         cutSecJetEta2p4,            
##         cutSecJetNoiseChgHad,
##         cutSecJetNoiseChgEM,
##         cutSecJetNoiseNeuHad,
##         cutSecJetNoiseNeuEM,
##         cutSubLeadingJetID,
##         cutJetJetDPhi,
        cutTrkPt50,
        cutTrkEta,
        cutTrkD0,
        cutTrkDZ,
        cutTrkNHits,
        cutTrkHitMissMid,
        cutTrkHitMissIn,
        cutTrkDeadEcalVeto,
        cutTrkCrackVeto,
        cutTrkRelIsoRp3,  
        cutTrkJetDeltaR,
        cutElecLooseIDVeto,
        cutTauLooseHadronicVeto,
        cutTrkWheel0GapVeto, 
        cutTrkEtaMuonPk, 
        cutMuonLooseIDVeto,
        cutSecMuonLooseIDVeto,
        ),
    )

StudyMuVeto2 = cms.PSet(
    name = cms.string("StudyMuVeto2"),
    triggers = triggersJetMet,
    cuts = cms.VPSet (
        cutTrkMuonId,
        cutSecJetPt,
        cutSecJetEta2p4,            
        cutSecJetNoiseChgHad,
        cutSecJetNoiseChgEM,
        cutSecJetNoiseNeuHad,
        cutSecJetNoiseNeuEM,
        cutSubLeadingJetID,
        cutJetJetDPhi,
        cutTrkPt50,
        cutTrkEta,
        cutTrkD0,
        cutTrkDZ,
        cutTrkNHits,
        cutTrkHitMissMid,
        cutTrkHitMissIn,
        cutTrkDeadEcalVeto,
        cutTrkCrackVeto,
        cutTrkRelIsoRp3,  
        cutTrkJetDeltaR,
        cutElecLooseIDVeto,
        cutTauLooseHadronicVeto,
        cutMuonLooseIDVeto,
        cutMET, 
        ),
    )

PreSelInvMuonVeto = cms.PSet(
    name = cms.string("PreSelInvMuonVeto"),
    triggers = triggersJetMet,
    cuts = 
    cutsMET + 
    cutsJets + 
    cutsTrkPreselNoLepVeto + 
    cms.VPSet (
      cutTauLooseHadronicVeto,
      cutElecLooseIDVeto, 
      cutMuonLooseIDVetoInv
      ), 
    )

PreSelNoTauVeto = cms.PSet(
    name = cms.string("PreSelNoTauVeto"),
    triggers = triggersJetMet,
    cuts = 
    cutsMET + 
    cutsJets + 
    cutsTrkPreselNoLepVeto + 
    cms.VPSet (
      cutElecLooseIDVeto,
      cutMuonLooseIDVeto,
      cutSecMuonLooseIDVeto
      ), 
    )
PreSelNoElecVeto = cms.PSet(
    name = cms.string("PreSelNoElecVeto"),
    triggers = triggersJetMet,
    cuts =
    cutsMET +
    cutsJets +
    cutsTrkPreselNoLepVeto +
    cms.VPSet (
    cutMuonLooseIDVeto,
    cutSecMuonLooseIDVeto,
    cutTauLooseHadronicVeto,
    ),
    )

PreSelElecVeto = cms.PSet(
    name = cms.string("PreSelElecVeto"),
    triggers = triggersJetMet,
    cuts =
    cutsMET +
    cutsJets +
    cutsTrkPreselNoLepVeto +
    cms.VPSet (
    cutElecLooseIDVeto,
    cutMuonLooseIDVeto,
    cutSecMuonLooseIDVeto,
    cutTauLooseHadronicVeto,
    ),
    )

PreSelElecId = cms.PSet(
    name = cms.string("PreSelElecId"),
    triggers = triggersJetMet,
    cuts =
    cutsMET +
    cutsJets +
    cutsTrkPreselNoLepVeto +
    cms.VPSet (
    cutElecLooseIDVeto,
    cutMuonLooseIDVeto,
    cutSecMuonLooseIDVeto,
    cutTauLooseHadronicVeto,
    cutTrkElectronId,
    ),
    )

PreSelNoLepVeto = cms.PSet(
    name = cms.string("PreSelNoLepVeto"),
    triggers = triggersJetMet,
    cuts = 
    cutsMET + 
    cutsJets + 
    cutsTrkPreselNoLepVeto, 
    )

PreSelInvElecVeto = cms.PSet(
    name = cms.string("PreSelectionInvElecVeto"),
    triggers = triggersJetMet,
    cuts = copy.deepcopy(PreSelection.cuts),
    )
for cut in PreSelInvElecVeto.cuts:
    if cut.cutString == cutElecLooseIDVeto.cutString:
        cut.cutString = cutElecLooseIDVetoInv.cutString


PreSelInvTauVeto = cms.PSet(
    name = cms.string("PreSelectionInvTauVeto"),
    triggers = triggersJetMet,
    cuts = copy.deepcopy(PreSelection.cuts),
    )
for cut in PreSelInvTauVeto.cuts:
    if cut.cutString == cutTauLooseHadronicVeto.cutString:
        cut.cutString = cutTauLooseHadronicVetoInv.cutString


PreSelElecVetoEnd = cms.PSet(
    name = cms.string("PreSelElecVetoEnd"),
    triggers = triggersJetMet,
    cuts = 
    cutsMET + 
    cutsJets + 
    cutsTrkPreselNoLepVeto +
    cms.VPSet (
      cutTauLooseHadronicVeto, 
      cutMuonLooseIDVeto,
      cutSecMuonLooseIDVeto, 
      cutElecLooseIDVeto,
      ), 
    )

PreSelMuonVetoEnd = cms.PSet(
    name = cms.string("PreSelMuonVetoEnd"),
    triggers = triggersJetMet,
    cuts = copy.deepcopy(PreSelection.cuts), 
    )

PreSelTauVetoEnd = cms.PSet(
    name = cms.string("PreSelTauVetoEnd"),
    triggers = triggersJetMet,
    cuts = 
    cutsMET + 
    cutsJets + 
    cutsTrkPreselNoLepVeto +
    cms.VPSet (
      cutMuonLooseIDVeto,
      cutSecMuonLooseIDVeto, 
      cutElecLooseIDVeto,
      cutTauLooseHadronicVeto, 
      ), 
    )  

PreSelElecVetoEndInv = cms.PSet(
    name = cms.string("PreSelElecVetoEndInv"),
    triggers = triggersJetMet,
    cuts = copy.deepcopy(PreSelElecVetoEnd.cuts), 
    )
for cut in PreSelElecVetoEndInv.cuts:
    if cut.cutString == cutElecLooseIDVeto.cutString:
        cut.cutString = cutElecLooseIDVetoInv.cutString
                

PreSelMuonVetoEndInv = cms.PSet(
    name = cms.string("PreSelMuonVetoEndInv"),
    triggers = triggersJetMet,
    cuts = copy.deepcopy(PreSelInvMuonVeto.cuts),  
    )

PreSelTauVetoEndInv = cms.PSet(
    name = cms.string("PreSelTauVetoEndInv"),
    triggers = triggersJetMet,
    cuts = copy.deepcopy(PreSelTauVetoEnd.cuts),  
    )
for cut in PreSelTauVetoEndInv.cuts:
    if cut.cutString == cutTauLooseHadronicVeto.cutString:
        cut.cutString = cutTauLooseHadronicVetoInv.cutString  


ZMCPart = cms.PSet(
    # Use this to check the Pt of the MC Z particle.
    name = cms.string("ZMCPart"),
    cuts = cms.VPSet (
      cutMCPartPdgZ,
      cutMCPartStatus3, 
      ),
    )

WMCPart = cms.PSet(
    # Use this to check the Pt of the MC W particle.
    name = cms.string("WMCPart"),
    cuts = cms.VPSet (
      cutMCPartPdgW,
      cutMCPartStatus3, 
      ),
    )

WMCPtPostTrig = cms.PSet(
    # Use this to check the Pt of the MC W particle.
    name = cms.string("WMCPtPostTrig"),
    triggers = triggersJetMet,
    cuts = cms.VPSet (
      cutMET,
      cutMCPartPdgW,
      cutMCPartStatus3, 
      ),
    )




ZtoMuTrkMuIdNoTrigMet = cms.PSet(
    name = cms.string("ZtoMuTrkMuIdNoTrigMet"),
#    triggers = triggersJetMet,
    cuts = cms.VPSet (
        # See SMP-12-023 for example of W->mu nu selection  
#        cutMET,
#        cutMETNoMu,
        cutMuonPt20,
        cutMuonEta,
        cutMuonTightID,
        cutMuonPFIso, 
        cutSecJetEta2p4,            
        cutSecJetNoiseChgHad,
        cutSecJetNoiseChgEM,
        cutSecJetNoiseNeuHad,
        cutSecJetNoiseNeuEM,
        cutSubLeadingJetID,
        cutJetJetDPhi,
        cutTrkMuonId, 
        cutMuTrkDeltaR,
        cutMuTrkInvMass,
        cutTrkPt,
        cutTrkEta,
#       cutTrkEtaBarrel,
        cutTrkD0,
        cutTrkDZ,
        cutTrkNHits,
        cutTrkHitMissMid,
        cutTrkHitMissIn,
        cutTrkDeadEcalVeto,
        cutTrkCrackVeto,
        cutTrkRelIsoRp3,  
        cutTrkJetDeltaR,
        cutElecLooseIDVeto,
        cutTauLooseHadronicVeto,
        cutMuonLooseIDVeto,
        cutSecMuonLooseIDVeto,
        ),
    )



ZtoMuTrkMetTrig = cms.PSet(
    name = cms.string("ZtoMuTrk"),
    triggers = triggersJetMet,
    cuts =
    cutsTagMuon +
    cms.VPSet (cutMuonPlusMet220) +
    cutsJets + 
    cutsTrkPresel + 
    cms.VPSet (
      cutMuTrkDeltaR,
      cutMuTrkInvMass,
      )
    )

ZtoMuTrkNoVetoNoCalo = cms.PSet(
    name = cms.string("ZtoMuTrkNoVetoNoCalo"),
     triggers = triggersSingleMu, 
    cuts = 
    cutsTagMuon + 
    cutsTrkPreselNoLepVeto + 
    cms.VPSet (
      cutTauLooseHadronicVeto,
      cutElecLooseIDVeto,
      ) + 
    cutsMuTrkZPeak
    )

ZtoMuTrkNoVeto = cms.PSet(
    name = cms.string("ZtoMuTrkNoVeto"),
    triggers = triggersSingleMu, 
    cuts = 
    cutsTagMuon + 
    cutsTrkPreselNoLepVeto + 
    cms.VPSet (
      cutTauLooseHadronicVeto,
      cutElecLooseIDVeto,
      cutMaxCalo10,
      cutTrkHitMissOut,
      ) + 
    cutsMuTrkZPeak
    )

ZtoMuTrkNoVetoPreSel = cms.PSet(
    name = cms.string("ZtoMuTrkNoVetoPreSel"),
    triggers = triggersSingleMu, 
    cuts = 
    cutsTagMuon + 
    cutsTrkPreselNoLepVeto + 
    cms.VPSet (
      cutTauLooseHadronicVeto,
      cutElecLooseIDVeto,
      ) + 
    cutsMuTrkZPeak
    )


ZtoETrkEIdNoVetoPresel = cms.PSet(
    name = cms.string("ZtoETrkEIdNoVetoPresel"),
    triggers = triggersSingleElec,
    cuts =
    cutsTagElec +
    cutsTrkPreselNoLepVeto +
    cms.VPSet (
      cutTauLooseHadronicVeto,
      cutMuonLooseIDVeto,
      cutSecMuonLooseIDVeto,
#      cutTrkHitMissOut,
    ) +
    cutsElecTrkZPeak
    )

ZtoETrkEIdNoVetoPreselLoosePt = cms.PSet(
    name = cms.string("ZtoETrkEIdNoVetoPreselLoosePt"),
    triggers = triggersSingleElec,
    cuts = copy.deepcopy(ZtoETrkEIdNoVetoPresel.cuts), 
    )
for i in xrange(len(ZtoETrkEIdNoVetoPreselLoosePt.cuts) - 1, -1, -1):
    if ZtoETrkEIdNoVetoPreselLoosePt.cuts[i].cutString == cutTrkPt.cutString: # replace pt>50 with pt>20 cut
        ZtoETrkEIdNoVetoPreselLoosePt.cuts[i].cutString = cutTrkPt20.cutString

ZtoETrkEIdNoVetoPreselLoosePtNoDeadEcal = cms.PSet(
    name = cms.string("ZtoETrkEIdNoVetoPreselLoosePtNoDeadEcal"),
    triggers = triggersSingleElec,
    cuts = copy.deepcopy(ZtoETrkEIdNoVetoPreselLoosePt.cuts), 
    )
for i in xrange(len(ZtoETrkEIdNoVetoPreselLoosePtNoDeadEcal.cuts) - 1, -1, -1):
    if ZtoETrkEIdNoVetoPreselLoosePtNoDeadEcal.cuts[i].cutString == cutTrkDeadEcalVeto.cutString: 
        del ZtoETrkEIdNoVetoPreselLoosePtNoDeadEcal.cuts[i]


ZtoETrkEIdNoVeto = cms.PSet(
    name = cms.string("ZtoETrkEIdNoVeto"),
    triggers = triggersSingleElec,
    cuts =
    cutsTagElec +
    cutsTrkPreselNoLepVeto +
    cms.VPSet (
    cutTauLooseHadronicVeto,
    cutMuonLooseIDVeto,
    cutSecMuonLooseIDVeto,
#    cutTrkNHitsSeven,
#    cutMaxCalo10,
    cutTrkHitMissOut,

    ) +
    cutsElecTrkZPeak
    )


ZtoMuTauHadNoVeto = cms.PSet(
    name = cms.string("ZtoMuTauHadNoVeto"),
    triggers = triggersSingleMu,
    cuts =
    cutsMuTauHad +
    cms.VPSet (
    cutMuTrkDeltaR,
    cutTrkPt30,
    cutTrkEta2p3,
    ) +
    cutsTrkVetoRegions +
    cutsTrkQuality +
#    cutsTrkIso +
    
    cms.VPSet (
    cutTrkRelIsoRp3,
    cutElecLooseIDVeto,
 #   cutMuonLooseIDVeto,
 #   cutSecMuonLooseIDVeto,
#    cutTrkHitMissOut,
    ) +
    cutsMuTrkHadZPeak
    )

ZtoMuTauHadNoTau = cms.PSet(
    name = cms.string("ZtoMuTauHadNoTau"),
    triggers = triggersSingleMu,
    cuts =
    cutsMuTrk +
    cms.VPSet (
    cutMuTrkDeltaR,
    cutTrkPt30,
    cutTrkEta2p3,
    ) +
    cutsTrkVetoRegions +
    cutsTrkQuality +
    #    cutsTrkIso +
    
    cms.VPSet (
    cutTrkRelIsoRp3,
    cutElecLooseIDVeto,
    #   cutMuonLooseIDVeto,
    #   cutSecMuonLooseIDVeto,
    #    cutTrkHitMissOut,
    ) +
    cutsMuTrkHadZPeak
    )

MuTauHadCtrl = cms.PSet(
    name = cms.string("MuTauHadCtrl"),
    triggers = triggersSingleMu,
    cuts =
    cutsMuTrk +
    cms.VPSet (
    #cutMuTrkDeltaR,
    cutTrkPt30,
    cutTrkEta2p3,
    ) +
    cutsTrkVetoRegions +
    cutsTrkQuality +
    #    cutsTrkIso +
    
    cms.VPSet (
    cutTrkRelIsoRp3,
    cutElecLooseIDVeto,
    #   cutMuonLooseIDVeto,
    #   cutSecMuonLooseIDVeto,
    #    cutTrkHitMissOut,
    ) 
    #cutsMuTrkHadZPeak
    )



ZtoMuTauHad = cms.PSet(
    name = cms.string("ZtoMuTauHad"),
    triggers = triggersSingleMu,
    cuts =
    cutsMuTrk +
    cms.VPSet (
    cutTrkPt30,
    cutTrkEta2p3,
    ) +
    cutsTrkVetoRegions +
    cutsTrkQuality +
    cutsTrkIso +
    cutsTrkLeptonVetoNoMu  +
    cutsMuTrkHadZPeak
    )



ZtoETrkEIdNoVetoNoMissOut = cms.PSet(
    name = cms.string("ZtoETrkEIdNoVetoNoMissOut"),
    triggers = triggersSingleElec,
    cuts =
    cutsTagElec +
    cutsTrkPreselNoLepVeto +
    cms.VPSet (
      cutTauLooseHadronicVeto,
      cutMuonLooseIDVeto,
      cutSecMuonLooseIDVeto,
    ) +
    cutsElecTrkZPeak
    )


ZtoMuTrk = cms.PSet(
    name = cms.string("ZtoMuTrk"),
    triggers = triggersSingleMu, 
    cuts = 
    cutsTagMuon +
    cutsTrkPresel +
    cms.VPSet (
      cutMaxCalo10,
      cutTrkHitMissOut,
      ) + 
    cutsMuTrkZPeak
    )

ZtoMuTrkPreSel = cms.PSet(
    name = cms.string("ZtoMuTrkPreSel"),
    triggers = triggersSingleMu, 
    cuts = 
    cutsTagMuon +
    cutsTrkPresel +
    cutsMuTrkZPeak
    )

ZtoETrkEId = cms.PSet(
    name = cms.string("ZtoETrkEId"),
    triggers = triggersSingleElec,
    cuts =
    cutsTagElec +
    cutsTrkPresel +
    cms.VPSet (
      cutMaxCalo10,
      cutTrkHitMissOut,
    ) +
    cutsElecTrkZPeak
    )

ZtoETrkEIdPresel = cms.PSet(
    name = cms.string("ZtoETrkEIdPresel"),
    triggers = triggersSingleElec,
    cuts =
    cutsTagElec +
    cutsTrkPresel +
    cms.VPSet (
#    cutMaxCalo10,
#    cutTrkHitMissOut,
    ) +
    cutsElecTrkZPeak
    )

ZtoETrkEIdPresel7Hits = cms.PSet(
    name = cms.string("ZtoETrkEIdPresel7Hits"),
    triggers = triggersSingleElec,
    cuts =
    cutsTagElec +
    cutsTrkPresel +
    cms.VPSet(
    cutTrkNHits7
    ) + 
    cutsElecTrkZPeak
    )


ZtoETrkEIdPreselMaxCalo = cms.PSet(
    name = cms.string("ZtoETrkEIdPreselMaxCalo"),
    triggers = triggersSingleElec,
    cuts =
      cutsTagElec +
      cutsTrkPresel +
      cms.VPSet (
      cutTrkNHits7,
      cutMaxCalo10,
      ) +
      cutsElecTrkZPeak
    )



ZtoETrkEIdPreselLoosePt7Hits = cms.PSet(
    name = cms.string("ZtoETrkEIdPreselLoosePt7Hits"),
    triggers = triggersSingleElec,
    cuts = copy.deepcopy(ZtoETrkEIdPresel7Hits.cuts),
    )
for i in xrange(len(ZtoETrkEIdPreselLoosePt7Hits.cuts) - 1, -1, -1):
    if ZtoETrkEIdPreselLoosePt7Hits.cuts[i].cutString == cutTrkPt.cutString: # replace pt>50 with pt>20 cut
        ZtoETrkEIdPreselLoosePt7Hits.cuts[i].cutString = cutTrkPt20.cutString

ZtoETrkEIdPreselLoosePtMaxCalo = cms.PSet(
    name = cms.string("ZtoETrkEIdPreselLoosePtMaxCalo"),
    triggers = triggersSingleElec,
    cuts = copy.deepcopy(ZtoETrkEIdPreselMaxCalo.cuts),
    )
for i in xrange(len(ZtoETrkEIdPreselLoosePtMaxCalo.cuts) - 1, -1, -1):
    if ZtoETrkEIdPreselLoosePtMaxCalo.cuts[i].cutString == cutTrkPt.cutString: # replace pt>50 with pt>20 cut
        ZtoETrkEIdPreselLoosePtMaxCalo.cuts[i].cutString = cutTrkPt20.cutString


ZtoETrkEIdPreselMaxCaloNMissOut3 = cms.PSet(
    name = cms.string("ZtoETrkEIdPreselMaxCaloNMissOu3"),
    triggers = triggersSingleElec,
    cuts =
      cutsTagElec +
      cutsTrkPresel +
      cms.VPSet (
      cutTrkNHits7,
      cutMaxCalo10,
      cutTrkHitMissOut, 
      ) +
      cutsElecTrkZPeak
    )

ZtoMuTrkPreSelLoosePt = copy.deepcopy(ZtoMuTrkPreSel)
ZtoMuTrkPreSelLoosePt.name = "ZtoMuTrkPreSelLoosePt"
for i in xrange(len(ZtoMuTrkPreSelLoosePt.cuts) - 1, -1, -1):
    if ZtoMuTrkPreSelLoosePt.cuts[i].cutString == cutTrkPt.cutString: # replace pt>50 with pt>20 cut
        ZtoMuTrkPreSelLoosePt.cuts[i].cutString = cutTrkPt30.cutString

ZtoMuTrkNoVetoPreSelLoosePt = copy.deepcopy(ZtoMuTrkNoVetoPreSel)
ZtoMuTrkNoVetoPreSelLoosePt.name = "ZtoMuTrkNoVetoPreSelLoosePt"
for i in xrange(len(ZtoMuTrkNoVetoPreSelLoosePt.cuts) - 1, -1, -1):
    if ZtoMuTrkNoVetoPreSelLoosePt.cuts[i].cutString == cutTrkPt.cutString: # replace pt>50 with pt>20 cut
        ZtoMuTrkNoVetoPreSelLoosePt.cuts[i].cutString = cutTrkPt30.cutString

ZtoMuTrkLoosePt = copy.deepcopy(ZtoMuTrk)
ZtoMuTrkLoosePt.name = "ZtoMuTrkLoosePt"
for i in xrange(len(ZtoMuTrkLoosePt.cuts) - 1, -1, -1):
    if ZtoMuTrkLoosePt.cuts[i].cutString == cutTrkPt.cutString: # replace pt>50 with pt>20 cut
        ZtoMuTrkLoosePt.cuts[i].cutString = cutTrkPt30.cutString

ZtoMuTrkNoVetoLoosePt = copy.deepcopy(ZtoMuTrkNoVeto)
ZtoMuTrkNoVetoLoosePt.name = "ZtoMuTrkNoVetoLoosePt"
for i in xrange(len(ZtoMuTrkNoVetoLoosePt.cuts) - 1, -1, -1):
    if ZtoMuTrkNoVetoLoosePt.cuts[i].cutString == cutTrkPt.cutString: # replace pt>50 with pt>20 cut
        ZtoMuTrkNoVetoLoosePt.cuts[i].cutString = cutTrkPt30.cutString

ZtoMuTrkNoMissOutLoosePt = copy.deepcopy(ZtoMuTrkLoosePt)
ZtoMuTrkNoMissOutLoosePt.name = "ZtoMuTrkNoMissOutLoosePt"
for i in xrange(len(ZtoMuTrkNoMissOutLoosePt.cuts) - 1, -1, -1):
    if ZtoMuTrkNoMissOutLoosePt.cuts[i].cutString == cutTrkHitMissOut.cutString: 
        del ZtoMuTrkNoMissOutLoosePt.cuts[i] 

ZtoMuTrkNoMissOutNoVetoLoosePt = copy.deepcopy(ZtoMuTrkNoVetoLoosePt)
ZtoMuTrkNoMissOutNoVetoLoosePt.name = "ZtoMuTrkNoMissOutNoVetoLoosePt"
for i in xrange(len(ZtoMuTrkNoMissOutNoVetoLoosePt.cuts) - 1, -1, -1):
    if ZtoMuTrkNoMissOutNoVetoLoosePt.cuts[i].cutString == cutTrkHitMissOut.cutString: 
        del ZtoMuTrkNoMissOutNoVetoLoosePt.cuts[i] 

                



ZtoMuTrkNoMuCutsNoVeto = cms.PSet(
    name = cms.string("ZtoMuTrkNoMuCutsNoVeto"),
    triggers = triggersSingleMu, 
    cuts = 
    cutsTagMuon + 
    cutsTrkPreselNoMuCutsNoLepVeto + 
    cms.VPSet (
      cutTauLooseHadronicVeto,
      cutElecLooseIDVeto,
      cutMaxCalo10,
      #      cutTrkHitMissOut,
      ) + 
    cutsMuTrkZPeak
    )


ZtoMuTrkNoMuCuts = cms.PSet(
    name = cms.string("ZtoMuTrkNoMuCuts"),
    triggers = triggersSingleMu, 
    cuts = 
    cutsTagMuon +
    cutsTrkPreselNoMuCuts +
    cms.VPSet (
      cutMaxCalo10,
      #      cutTrkHitMissOut,
##       cutMuonLooseIDVeto,
##       cutSecMuonLooseIDVeto,
      ) + 
    cutsMuTrkZPeak
    )



ZtoMuTrkMuIdHiStats = cms.PSet(
    name = cms.string("ZtoMuTrkMuIdHiStats"),
#    triggers = triggersJetMetOrSingleMu, 
     triggers = triggersJetMet,
#    triggers = triggersSingleMu, 
    cuts = cms.VPSet (
        # See SMP-12-023 for example of W->mu nu selection  
#       cutMETNoMu,
       cutMET,
#       cutMuonChgNeg,
#       cutMuonChgPos,
        cutMuonPt20,
        cutMuonEta,
        cutMuonTightID,
        cutMuonPFIso,
        cutSecJetPt,
        cutSecJetEta2p4,            
        cutSecJetNoiseChgHad,
        cutSecJetNoiseChgEM,
        cutSecJetNoiseNeuHad,
        cutSecJetNoiseNeuEM,
        cutSubLeadingJetID,
        cutJetJetDPhi,
#       cutTrkMuonId, 
        cutTrkPt50,
        cutTrkEta,
        cutTrkD0,
        cutTrkDZ,
        cutTrkNHits,
        cutTrkHitMissMid,
        cutTrkHitMissIn,
        cutTrkDeadEcalVeto,
        cutTrkCrackVeto,
        cutTrkRelIsoRp3,  
        cutTrkJetDeltaR,
        cutElecLooseIDVeto,
        cutTauLooseHadronicVeto,
        cutTrkWheel0GapVeto,
        cutTrkEtaMuonPk,
        cutMaxCalo10, 
#        cutMuTrkInvMass,
        cutMuTrkInvMass80To100, 
        cutMuTrkChgOpp, 
        cutMuTrkDeltaR,
        cutTrkHitMissOut,
        cutMuonLooseIDVeto,
        cutSecMuonLooseIDVeto,
        ),
    )

ZtoMuTrkMuIdInvHits = cms.PSet(
    name = cms.string("ZtoMuTrkMuIdInvHits"),
#    triggers = triggersJetMetOrSingleMu, 
     triggers = triggersJetMet,
#    triggers = triggersSingleMu, 
    cuts = cms.VPSet (
        # See SMP-12-023 for example of W->mu nu selection  
        cutMET,
#       cutMETNoMu,
#       cutMuonChgNeg,
#       cutMuonChgPos,
        cutMuonPt20,
        cutMuonEta,
        cutMuonTightID,
        cutMuonPFIso,
        cutSecJetPt,
        cutSecJetEta2p4,            
        cutSecJetNoiseChgHad,
        cutSecJetNoiseChgEM,
        cutSecJetNoiseNeuHad,
        cutSecJetNoiseNeuEM,
        cutSubLeadingJetID,
        cutJetJetDPhi,
        cutTrkMuonId, 
        cutMuTrkDeltaR,
        cutMuTrkInvMass,
        cutMuTrkChgOpp, 
        cutTrkPt50,
        cutTrkEta,
        cutTrkD0,
        cutTrkDZ,
        cutTrkNHits,
        cutTrkHitMissMid,
        cutTrkHitMissIn,
        cutTrkDeadEcalVeto,
        cutTrkCrackVeto,
        cutTrkRelIsoRp3,  
        cutTrkJetDeltaR,
        cutElecLooseIDVeto,
        cutTauLooseHadronicVeto,
        cutMuonLooseIDVeto,
        cutSecMuonLooseIDVeto,
        cutTrkWheel0GapVeto,
        cutTrkEtaMuonPk,
        cutMaxCalo10, 
        cutTrkHitMissOutInv,
        ),
    )

## ZtoMuTrkMuId = copy.deepcopy(ZtoMuTrkMuIdNoVeto)  
## ZtoMuTrkMuId.name = "ZtoMuTrkMuId"  
## ZtoMuTrkMuId.cuts.append(cutMuonLooseIDVeto)
## ZtoMuTrkMuId.cuts.append(cutSecMuonLooseIDVeto)


## Ctrl sample for muons ##
ZtoMuTrkInvMuonVeto = cms.PSet(
    name = cms.string("ZtoMuTrkInvMuonVeto"),
    triggers = triggersJetMet,
    cuts = cms.VPSet (
        # See SMP-12-023 for example of W->mu nu selection  
        cutMuonPt20,
        cutMuonEta,
        cutMuonTightID,
        cutMuonPFIso,
        cutMuonPlusMet220, 
        cutSecJetPt,
        cutSecJetEta2p4,            
        cutSecJetNoiseChgHad,
        cutSecJetNoiseChgEM,
        cutSecJetNoiseNeuHad,
        cutSecJetNoiseNeuEM,
        cutSubLeadingJetID,
        cutJetJetDPhi,
        cutTrkPt,
        cutTrkEta,
        cutTrkD0,
        cutTrkDZ,
        cutTrkNHits,
        cutTrkHitMissMid,
        cutTrkHitMissIn,
        cutTrkDeadEcalVeto,
        cutTrkCrackVeto,
#       cutTrkRelIsoRp3,  
        cutTrkJetDeltaR,
        cutElecLooseIDVeto,
        cutTauLooseHadronicVeto,
        cutMuonLooseIDVetoInv,
        cutMuTrkDeltaR,
        cutMuTrkInvMass,
        ),
    )

BadCSCVetoRegions = cms.PSet(
    name = cms.string("BadCSCVetoRegions"),
    cuts = cms.VPSet (
      cutTrkBadCSCVetoInv, 
      ) 
    )  


FakeTrackSel = cms.PSet(
    name = cms.string("FakeTrackSel"),
    cuts = cms.VPSet (
      cutTrkNotGenMatched,
      ) +
      cutsTrkPtEta + 
      cutsTrkVetoRegions + 
      cms.VPSet (
      cutTrkDZ,
      cutTrkHitMissIn, 
      ) + 
      cutsTrkIso + 
      cutsTrkLeptonVeto
    )  



FullSelectionInvD0 = cms.PSet(
    name = cms.string("FullSelectionInvD0"),
    triggers = triggersJetMet,
    cuts = cms.VPSet (
        cutMET,
        cutSecJetPt,
        cutSecJetEta2p4,            
        cutSecJetNoiseChgHad,
        cutSecJetNoiseChgEM,
        cutSecJetNoiseNeuHad,
        cutSecJetNoiseNeuEM,
        cutSubLeadingJetID,
        cutJetJetDPhi,
        cutTrkPt,
        cutTrkEta,
        cutTrkD0Inv,
        cutTrkDZ,
        cutTrkNHits,
        cutTrkHitMissMid,
        cutTrkHitMissIn,
        cutTrkDeadEcalVeto,
        cutTrkCrackVeto,
        cutTrkRelIsoRp3,  
        cutTrkJetDeltaR,
        cutElecLooseIDVeto, 
        cutTauLooseHadronicVeto,  
        cutTrkWheel0GapVeto, 
        cutTrkEtaMuonPk, 
        cutMuonLooseIDVeto,
        cutSecMuonLooseIDVeto, 
        cutMaxCalo10, 
        cutTrkHitMissOut,
    )
)


FullSelectionInvD0Loose = cms.PSet(
    name = cms.string("FullSelectionInvD0Loose"),
    triggers = triggersJetMet,
    cuts = cms.VPSet (
#        cutMET100,
        cutSecJetPt,
        cutSecJetEta2p4,            
        cutSecJetNoiseChgHad,
        cutSecJetNoiseChgEM,
        cutSecJetNoiseNeuHad,
        cutSecJetNoiseNeuEM,
        cutSubLeadingJetID,
        cutJetJetDPhi,
        cutTrkPt,
        cutTrkEta,
        cutTrkD0Inv,
        cutTrkDZ,
        cutTrkNHits,
        cutTrkHitMissMid,
        cutTrkHitMissIn,
        cutTrkDeadEcalVeto,
        cutTrkCrackVeto,
        cutTrkRelIsoRp3,  
        cutTrkJetDeltaR,
        cutElecLooseIDVeto, 
        cutTauLooseHadronicVeto,  
        cutTrkWheel0GapVeto, 
        cutTrkEtaMuonPk, 
        cutMuonLooseIDVeto,
        cutSecMuonLooseIDVeto, 
        cutMaxCalo10, 
        cutTrkHitMissOut,
    )
)


FullSelectionInvDZ = cms.PSet(
    name = cms.string("FullSelectionInvDZ"),
    triggers = triggersJetMet,
    cuts = cms.VPSet (
        cutMET,
        cutSecJetPt,
        cutSecJetEta2p4,            
        cutSecJetNoiseChgHad,
        cutSecJetNoiseChgEM,
        cutSecJetNoiseNeuHad,
        cutSecJetNoiseNeuEM,
        cutSubLeadingJetID,
        cutJetJetDPhi,
        cutTrkPt,
        cutTrkEta,
        cutTrkD0,
        cutTrkDZInv,
        cutTrkNHits,
        cutTrkHitMissMid,
        cutTrkHitMissIn,
        cutTrkDeadEcalVeto,
        cutTrkCrackVeto,
        cutTrkRelIsoRp3,  
        cutTrkJetDeltaR,
        cutElecLooseIDVeto, 
        cutTauLooseHadronicVeto,  
        cutTrkWheel0GapVeto, 
        cutTrkEtaMuonPk, 
        cutMuonLooseIDVeto,
        cutSecMuonLooseIDVeto, 
        cutMaxCalo10, 
        cutTrkHitMissOut,
    )
)


FullSelectionInvDZLoose = cms.PSet(
    name = cms.string("FullSelectionInvDZLoose"),
    triggers = triggersJetMet,
    cuts = cms.VPSet (
#        cutMET100,
        cutSecJetPt,
        cutSecJetEta2p4,            
        cutSecJetNoiseChgHad,
        cutSecJetNoiseChgEM,
        cutSecJetNoiseNeuHad,
        cutSecJetNoiseNeuEM,
        cutSubLeadingJetID,
        cutJetJetDPhi,
        cutTrkPt,
        cutTrkEta,
        cutTrkD0,
        cutTrkDZInv,
        cutTrkNHits,
        cutTrkHitMissMid,
        cutTrkHitMissIn,
        cutTrkDeadEcalVeto,
        cutTrkCrackVeto,
        cutTrkRelIsoRp3,  
        cutTrkJetDeltaR,
        cutElecLooseIDVeto, 
        cutTauLooseHadronicVeto,  
        cutTrkWheel0GapVeto, 
        cutTrkEtaMuonPk, 
        cutMuonLooseIDVeto,
        cutSecMuonLooseIDVeto, 
        cutMaxCalo10, 
        cutTrkHitMissOut,
    )
)



FullSelectionInvNHits = cms.PSet(
    name = cms.string("FullSelectionInvNHits"),
    triggers = triggersJetMet,
    cuts = cms.VPSet (
        cutMET,
        cutSecJetPt,
        cutSecJetEta2p4,            
        cutSecJetNoiseChgHad,
        cutSecJetNoiseChgEM,
        cutSecJetNoiseNeuHad,
        cutSecJetNoiseNeuEM,
        cutSubLeadingJetID,
        cutJetJetDPhi,
        cutTrkPt,
        cutTrkEta,
        cutTrkD0,
        cutTrkDZ,
        cutTrkNHits4,
        cutTrkHitMissMid,
        cutTrkHitMissIn,
        cutTrkDeadEcalVeto,
        cutTrkCrackVeto,
        cutTrkRelIsoRp3,  
        cutTrkJetDeltaR,
        cutElecLooseIDVeto, 
        cutTauLooseHadronicVeto,  
        cutTrkWheel0GapVeto, 
        cutTrkEtaMuonPk, 
        cutMuonLooseIDVeto,
        cutSecMuonLooseIDVeto, 
        cutMaxCalo10, 
        cutTrkHitMissOut,
    )
)


FullSelectionInvNHitsLoose = cms.PSet(
    name = cms.string("FullSelectionInvNHitsLoose"),
    triggers = triggersJetMet,
    cuts = cms.VPSet (
#        cutMET100,
        cutSecJetPt,
        cutSecJetEta2p4,            
        cutSecJetNoiseChgHad,
        cutSecJetNoiseChgEM,
        cutSecJetNoiseNeuHad,
        cutSecJetNoiseNeuEM,
        cutSubLeadingJetID,
        cutJetJetDPhi,
        cutTrkPt,
        cutTrkEta,
        cutTrkD0,
        cutTrkDZ,
        cutTrkNHits4,
        cutTrkHitMissMid,
        cutTrkHitMissIn,
        cutTrkDeadEcalVeto,
        cutTrkCrackVeto,
        cutTrkRelIsoRp3,  
        cutTrkJetDeltaR,
        cutElecLooseIDVeto, 
        cutTauLooseHadronicVeto,  
        cutTrkWheel0GapVeto, 
        cutTrkEtaMuonPk, 
        cutMuonLooseIDVeto,
        cutSecMuonLooseIDVeto, 
        cutMaxCalo10, 
        cutTrkHitMissOut,
    )
)



FullSelectionInvNMissMid = cms.PSet(
    name = cms.string("FullSelectionInvNMissMid"),
    triggers = triggersJetMet,
    cuts = cms.VPSet (
        cutMET,
        cutSecJetPt,
        cutSecJetEta2p4,            
        cutSecJetNoiseChgHad,
        cutSecJetNoiseChgEM,
        cutSecJetNoiseNeuHad,
        cutSecJetNoiseNeuEM,
        cutSubLeadingJetID,
        cutJetJetDPhi,
        cutTrkPt,
        cutTrkEta,
        cutTrkD0,
        cutTrkDZ,
        cutTrkNHits,
        cutTrkHitMissMidInv,
        cutTrkHitMissIn,
        cutTrkDeadEcalVeto,
        cutTrkCrackVeto,
        cutTrkRelIsoRp3,  
        cutTrkJetDeltaR,
        cutElecLooseIDVeto, 
        cutTauLooseHadronicVeto,  
        cutTrkWheel0GapVeto, 
        cutTrkEtaMuonPk, 
        cutMuonLooseIDVeto,
        cutSecMuonLooseIDVeto, 
        cutMaxCalo10, 
        cutTrkHitMissOut,
    )
)


FullSelectionInvNMissMidLoose = cms.PSet(
    name = cms.string("FullSelectionInvNMissMidLoose"),
#    triggers = triggersJetMet,
    cuts = cms.VPSet (
##         cutMET100,
        cutSecJetPt,
        cutSecJetEta2p4,            
        cutSecJetNoiseChgHad,
        cutSecJetNoiseChgEM,
        cutSecJetNoiseNeuHad,
        cutSecJetNoiseNeuEM,
        cutSubLeadingJetID,
        cutJetJetDPhi,
        cutTrkPt,
        cutTrkEta,
        cutTrkD0,
        cutTrkDZ,
        cutTrkNHits,
        cutTrkHitMissMidInv,
        cutTrkHitMissIn,
        cutTrkDeadEcalVeto,
        cutTrkCrackVeto,
        cutTrkRelIsoRp3,  
        cutTrkJetDeltaR,
        cutElecLooseIDVeto, 
        cutTauLooseHadronicVeto,  
        cutTrkWheel0GapVeto, 
        cutTrkEtaMuonPk, 
        cutMuonLooseIDVeto,
        cutSecMuonLooseIDVeto, 
        cutMaxCalo10, 
        cutTrkHitMissOut,
    )
)



FullSelectionInvNoneLoose = cms.PSet(
    name = cms.string("FullSelectionInvNoneLoose"),
#    triggers = triggersJetMet,
    cuts = cms.VPSet (
##         cutMET100,
##         cutSecJetPt,
##         cutSecJetEta2p4,            
##         cutSecJetNoiseChgHad,
##         cutSecJetNoiseChgEM,
##         cutSecJetNoiseNeuHad,
##         cutSecJetNoiseNeuEM,
##         cutSubLeadingJetID,
##         cutJetJetDPhi,
        cutTrkPt,
        cutTrkEta,
        cutTrkD0,
        cutTrkDZ,
        cutTrkNHits,
        cutTrkHitMissMid,
        cutTrkHitMissIn,
        cutTrkDeadEcalVeto,
        cutTrkCrackVeto,
        cutTrkRelIsoRp3,  
        cutTrkJetDeltaR,
        cutElecLooseIDVeto, 
        cutTauLooseHadronicVeto,  
        cutTrkWheel0GapVeto, 
        cutTrkEtaMuonPk, 
        cutMuonLooseIDVeto,
        cutSecMuonLooseIDVeto, 
        cutMaxCalo10, 
        cutTrkHitMissOut,
    )
)


FullSelectionInvD0InvDZ = cms.PSet(
    name = cms.string("FullSelectionInvD0InvDZ"),
    triggers = triggersJetMet,
    cuts = cms.VPSet (
#        cutMET,
        cutSecJetPt,
        cutSecJetEta2p4,            
        cutSecJetNoiseChgHad,
        cutSecJetNoiseChgEM,
        cutSecJetNoiseNeuHad,
        cutSecJetNoiseNeuEM,
        cutSubLeadingJetID,
        cutJetJetDPhi,
        cutTrkPt,
        cutTrkEta,
        cutTrkD0Inv,
        cutTrkDZInv,
        cutTrkNHits,
        cutTrkHitMissMid,
        cutTrkHitMissIn,
        cutTrkDeadEcalVeto,
        cutTrkCrackVeto,
        cutTrkRelIsoRp3,  
        cutTrkJetDeltaR,
        cutElecLooseIDVeto, 
        cutTauLooseHadronicVeto,  
        cutTrkWheel0GapVeto, 
        cutTrkEtaMuonPk, 
        cutMuonLooseIDVeto,
        cutSecMuonLooseIDVeto, 
        cutMaxCalo10, 
        cutTrkHitMissOut,
    )
)


FullSelectionInvD0InvNHits = cms.PSet(
    name = cms.string("FullSelectionInvD0InvNHits"),
    triggers = triggersJetMet,
    cuts = cms.VPSet (
#        cutMET,
        cutSecJetPt,
        cutSecJetEta2p4,            
        cutSecJetNoiseChgHad,
        cutSecJetNoiseChgEM,
        cutSecJetNoiseNeuHad,
        cutSecJetNoiseNeuEM,
        cutSubLeadingJetID,
        cutJetJetDPhi,
        cutTrkPt,
        cutTrkEta,
        cutTrkD0Inv,
        cutTrkDZ,
        cutTrkNHitsInv,
        cutTrkHitMissMid,
        cutTrkHitMissIn,
        cutTrkDeadEcalVeto,
        cutTrkCrackVeto,
        cutTrkRelIsoRp3,  
        cutTrkJetDeltaR,
        cutElecLooseIDVeto, 
        cutTauLooseHadronicVeto,  
        cutTrkWheel0GapVeto, 
        cutTrkEtaMuonPk, 
        cutMuonLooseIDVeto,
        cutSecMuonLooseIDVeto, 
        cutMaxCalo10, 
        cutTrkHitMissOut,
    )
)


FullSelectionInvD0InvNMissMid = cms.PSet(
    name = cms.string("FullSelectionInvD0InvNMissMid"),
    triggers = triggersJetMet,
    cuts = cms.VPSet (
#        cutMET,
        cutSecJetPt,
        cutSecJetEta2p4,            
        cutSecJetNoiseChgHad,
        cutSecJetNoiseChgEM,
        cutSecJetNoiseNeuHad,
        cutSecJetNoiseNeuEM,
        cutSubLeadingJetID,
        cutJetJetDPhi,
        cutTrkPt,
        cutTrkEta,
        cutTrkD0Inv,
        cutTrkDZ,
        cutTrkNHits,
        cutTrkHitMissMidInv,
        cutTrkHitMissIn,
        cutTrkDeadEcalVeto,
        cutTrkCrackVeto,
        cutTrkRelIsoRp3,  
        cutTrkJetDeltaR,
        cutElecLooseIDVeto, 
        cutTauLooseHadronicVeto,  
        cutTrkWheel0GapVeto, 
        cutTrkEtaMuonPk, 
        cutMuonLooseIDVeto,
        cutSecMuonLooseIDVeto, 
        cutMaxCalo10, 
        cutTrkHitMissOut,
    )
)


FullSelectionInvDZInvNHits = cms.PSet(
    name = cms.string("FullSelectionInvDZInvNHits"),
    triggers = triggersJetMet,
    cuts = cms.VPSet (
#        cutMET,
        cutSecJetPt,
        cutSecJetEta2p4,            
        cutSecJetNoiseChgHad,
        cutSecJetNoiseChgEM,
        cutSecJetNoiseNeuHad,
        cutSecJetNoiseNeuEM,
        cutSubLeadingJetID,
        cutJetJetDPhi,
        cutTrkPt,
        cutTrkEta,
        cutTrkD0,
        cutTrkDZInv,
        cutTrkNHitsInv,
        cutTrkHitMissMid,
        cutTrkHitMissIn,
        cutTrkDeadEcalVeto,
        cutTrkCrackVeto,
        cutTrkRelIsoRp3,  
        cutTrkJetDeltaR,
        cutElecLooseIDVeto, 
        cutTauLooseHadronicVeto,  
        cutTrkWheel0GapVeto, 
        cutTrkEtaMuonPk, 
        cutMuonLooseIDVeto,
        cutSecMuonLooseIDVeto, 
        cutMaxCalo10, 
        cutTrkHitMissOut,
    )
)


FullSelectionInvDZInvNMissMid = cms.PSet(
    name = cms.string("FullSelectionInvDZInvNMissMid"),
    triggers = triggersJetMet,
    cuts = cms.VPSet (
#        cutMET,
        cutSecJetPt,
        cutSecJetEta2p4,            
        cutSecJetNoiseChgHad,
        cutSecJetNoiseChgEM,
        cutSecJetNoiseNeuHad,
        cutSecJetNoiseNeuEM,
        cutSubLeadingJetID,
        cutJetJetDPhi,
        cutTrkPt,
        cutTrkEta,
        cutTrkD0,
        cutTrkDZInv,
        cutTrkNHits,
        cutTrkHitMissMidInv,
        cutTrkHitMissIn,
        cutTrkDeadEcalVeto,
        cutTrkCrackVeto,
        cutTrkRelIsoRp3,  
        cutTrkJetDeltaR,
        cutElecLooseIDVeto, 
        cutTauLooseHadronicVeto,  
        cutTrkWheel0GapVeto, 
        cutTrkEtaMuonPk, 
        cutMuonLooseIDVeto,
        cutSecMuonLooseIDVeto, 
        cutMaxCalo10, 
        cutTrkHitMissOut,
    )
)


FullSelectionInvNHitsInvNMissMid = cms.PSet(
    name = cms.string("FullSelectionInvNHitsInvNMissMid"),
    triggers = triggersJetMet,
    cuts = cms.VPSet (
#        cutMET,
        cutSecJetPt,
        cutSecJetEta2p4,            
        cutSecJetNoiseChgHad,
        cutSecJetNoiseChgEM,
        cutSecJetNoiseNeuHad,
        cutSecJetNoiseNeuEM,
        cutSubLeadingJetID,
        cutJetJetDPhi,
        cutTrkPt,
        cutTrkEta,
        cutTrkD0,
        cutTrkDZ,
        cutTrkNHitsInv,
        cutTrkHitMissMidInv,
        cutTrkHitMissIn,
        cutTrkDeadEcalVeto,
        cutTrkCrackVeto,
        cutTrkRelIsoRp3,  
        cutTrkJetDeltaR,
        cutElecLooseIDVeto, 
        cutTauLooseHadronicVeto,  
        cutTrkWheel0GapVeto, 
        cutTrkEtaMuonPk, 
        cutMuonLooseIDVeto,
        cutSecMuonLooseIDVeto, 
        cutMaxCalo10, 
        cutTrkHitMissOut,
    )
)

FullSelectionInvD0InvDZInvNHits = cms.PSet(
    name = cms.string("FullSelectionInvD0InvDZInvNHits"),
    triggers = triggersJetMet,
    cuts = cms.VPSet (
#        cutMET,
        cutSecJetPt,
        cutSecJetEta2p4,            
        cutSecJetNoiseChgHad,
        cutSecJetNoiseChgEM,
        cutSecJetNoiseNeuHad,
        cutSecJetNoiseNeuEM,
        cutSubLeadingJetID,
        cutJetJetDPhi,
        cutTrkPt,
        cutTrkEta,
        cutTrkD0Inv,
        cutTrkDZInv,
        cutTrkNHitsInv,
        cutTrkHitMissMid,
        cutTrkHitMissIn,
        cutTrkDeadEcalVeto,
        cutTrkCrackVeto,
        cutTrkRelIsoRp3,  
        cutTrkJetDeltaR,
        cutElecLooseIDVeto, 
        cutTauLooseHadronicVeto,  
        cutTrkWheel0GapVeto, 
        cutTrkEtaMuonPk, 
        cutMuonLooseIDVeto,
        cutSecMuonLooseIDVeto, 
        cutMaxCalo10, 
        cutTrkHitMissOut,
    )
)



FullSelectionInvD0InvDZInvNMissMid = cms.PSet(
    name = cms.string("FullSelectionInvD0InvDZInvNMissMid"),
    triggers = triggersJetMet,
    cuts = cms.VPSet (
#        cutMET,
        cutSecJetPt,
        cutSecJetEta2p4,            
        cutSecJetNoiseChgHad,
        cutSecJetNoiseChgEM,
        cutSecJetNoiseNeuHad,
        cutSecJetNoiseNeuEM,
        cutSubLeadingJetID,
        cutJetJetDPhi,
        cutTrkPt,
        cutTrkEta,
        cutTrkD0Inv,
        cutTrkDZInv,
        cutTrkNHits,
        cutTrkHitMissMidInv,
        cutTrkHitMissIn,
        cutTrkDeadEcalVeto,
        cutTrkCrackVeto,
        cutTrkRelIsoRp3,  
        cutTrkJetDeltaR,
        cutElecLooseIDVeto, 
        cutTauLooseHadronicVeto,  
        cutTrkWheel0GapVeto, 
        cutTrkEtaMuonPk, 
        cutMuonLooseIDVeto,
        cutSecMuonLooseIDVeto, 
        cutMaxCalo10, 
        cutTrkHitMissOut,
    )
)


FullSelectionInvD0InvNHitsInvNMissMid = cms.PSet(
    name = cms.string("FullSelectionInvD0InvNHitsInvNMissMid"),
    triggers = triggersJetMet,
    cuts = cms.VPSet (
#        cutMET,
        cutSecJetPt,
        cutSecJetEta2p4,            
        cutSecJetNoiseChgHad,
        cutSecJetNoiseChgEM,
        cutSecJetNoiseNeuHad,
        cutSecJetNoiseNeuEM,
        cutSubLeadingJetID,
        cutJetJetDPhi,
        cutTrkPt,
        cutTrkEta,
        cutTrkD0Inv,
        cutTrkDZ,
        cutTrkNHitsInv,
        cutTrkHitMissMidInv,
        cutTrkHitMissIn,
        cutTrkDeadEcalVeto,
        cutTrkCrackVeto,
        cutTrkRelIsoRp3,  
        cutTrkJetDeltaR,
        cutElecLooseIDVeto, 
        cutTauLooseHadronicVeto,  
        cutTrkWheel0GapVeto, 
        cutTrkEtaMuonPk, 
        cutMuonLooseIDVeto,
        cutSecMuonLooseIDVeto, 
        cutMaxCalo10, 
        cutTrkHitMissOut,
    )
)



FullSelectionInvDZInvNHitsInvNMissMid = cms.PSet(
    name = cms.string("FullSelectionInvDZInvNHitsInvNMissMid"),
    triggers = triggersJetMet,
    cuts = cms.VPSet (
#        cutMET,
        cutSecJetPt,
        cutSecJetEta2p4,            
        cutSecJetNoiseChgHad,
        cutSecJetNoiseChgEM,
        cutSecJetNoiseNeuHad,
        cutSecJetNoiseNeuEM,
        cutSubLeadingJetID,
        cutJetJetDPhi,
        cutTrkPt,
        cutTrkEta,
        cutTrkD0,
        cutTrkDZInv,
        cutTrkNHitsInv,
        cutTrkHitMissMidInv,
        cutTrkHitMissIn,
        cutTrkDeadEcalVeto,
        cutTrkCrackVeto,
        cutTrkRelIsoRp3,  
        cutTrkJetDeltaR,
        cutElecLooseIDVeto, 
        cutTauLooseHadronicVeto,  
        cutTrkWheel0GapVeto, 
        cutTrkEtaMuonPk, 
        cutMuonLooseIDVeto,
        cutSecMuonLooseIDVeto, 
        cutMaxCalo10, 
        cutTrkHitMissOut,
    )
)


FullSelectionInvD0InvDZInvNHitsInvNMissMid = cms.PSet(
    name = cms.string("FullSelectionInvD0InvDZInvNHitsInvNMissMid"),
    triggers = triggersJetMet,
    cuts = cms.VPSet (
#        cutMET,
        cutSecJetPt,
        cutSecJetEta2p4,            
        cutSecJetNoiseChgHad,
        cutSecJetNoiseChgEM,
        cutSecJetNoiseNeuHad,
        cutSecJetNoiseNeuEM,
        cutSubLeadingJetID,
        cutJetJetDPhi,
        cutTrkPt,
        cutTrkEta,
        cutTrkD0Inv,
        cutTrkDZInv,
        cutTrkNHitsInv,
        cutTrkHitMissMidInv,
        cutTrkHitMissIn,
        cutTrkDeadEcalVeto,
        cutTrkCrackVeto,
        cutTrkRelIsoRp3,  
        cutTrkJetDeltaR,
        cutElecLooseIDVeto, 
        cutTauLooseHadronicVeto,  
        cutTrkWheel0GapVeto, 
        cutTrkEtaMuonPk, 
        cutMuonLooseIDVeto,
        cutSecMuonLooseIDVeto, 
        cutMaxCalo10, 
        cutTrkHitMissOut,
    )
)



MuTrigNoCuts = cms.PSet(
    name = cms.string("MuTrigNoCuts"),
    triggers = triggersSingleMu,
    cuts = cms.VPSet (
       cutNoCuts,
       )
    )

FakeTrkMuTrig = cms.PSet(
    name = cms.string("FakeTrkMuTrig"),
    triggers = triggersSingleMu,
    cuts = cms.VPSet (
#        cutMET,
##         cutSecJetPt,
##         cutSecJetEta2p4,            
##         cutSecJetNoiseChgHad,
##         cutSecJetNoiseChgEM,
##         cutSecJetNoiseNeuHad,
##         cutSecJetNoiseNeuEM,
##         cutSubLeadingJetID,
##         cutJetJetDPhi,
        cutTrkPt,
        cutTrkEta,
        cutTrkD0,
        cutTrkDZ,
        cutTrkNHits,
        cutTrkHitMissMid,
        cutTrkHitMissIn,
        cutTrkDeadEcalVeto,
        cutTrkCrackVeto,
        cutTrkRelIsoRp3,  
        cutTrkJetDeltaR,
        cutElecLooseIDVeto, 
        cutTauLooseHadronicVeto,  
        cutTrkWheel0GapVeto, 
        cutTrkEtaMuonPk, 
        cutMuonLooseIDVeto,
        cutSecMuonLooseIDVeto, 
        cutMaxCalo10, 
        cutTrkHitMissOut,
        cutTrkNotGenMatched,  
    )
)



FakeTrkTestCorr = cms.PSet(
    name = cms.string("FakeTrkTestCorr"),
    triggers = triggersJetMet,
    cuts = cms.VPSet (
#        cutMET,
        cutSecJetPt,
        cutSecJetEta2p4,            
        cutSecJetNoiseChgHad,
        cutSecJetNoiseChgEM,
        cutSecJetNoiseNeuHad,
        cutSecJetNoiseNeuEM,
        cutSubLeadingJetID,
        cutJetJetDPhi,
        cutTrkPt,
        cutTrkEta,
#        cutTrkD0,
#        cutTrkDZ,
#        cutTrkNHits,
#        cutTrkHitMissMid,
        cutTrkHitMissIn,
        cutTrkDeadEcalVeto,
        cutTrkCrackVeto,
        cutTrkRelIsoRp3,  
        cutTrkJetDeltaR,
        cutElecLooseIDVeto, 
        cutTauLooseHadronicVeto,  
        cutTrkWheel0GapVeto, 
        cutTrkEtaMuonPk, 
        cutMuonLooseIDVeto,
        cutSecMuonLooseIDVeto, 
        cutMaxCalo10, 
        cutTrkHitMissOut,
    )
)


FakeTrkTestCorrLoose = cms.PSet(
    name = cms.string("FakeTrkTestCorrLoose"),
    triggers = triggersJetMet,
    cuts = cms.VPSet (
##         cutMET,
##         cutSecJetPt,
##         cutSecJetEta2p4,            
##         cutSecJetNoiseChgHad,
##         cutSecJetNoiseChgEM,
##         cutSecJetNoiseNeuHad,
##         cutSecJetNoiseNeuEM,
##         cutSubLeadingJetID,
##         cutJetJetDPhi,
        cutTrkPt,
        cutTrkEta,
#        cutTrkD0,
#        cutTrkDZ,
#        cutTrkNHits,
#        cutTrkHitMissMid,
        cutTrkHitMissIn,
        cutTrkDeadEcalVeto,
        cutTrkCrackVeto,
        cutTrkRelIsoRp3,  
        cutTrkJetDeltaR,
        cutElecLooseIDVeto, 
        cutTauLooseHadronicVeto,  
        cutTrkWheel0GapVeto, 
        cutTrkEtaMuonPk, 
        cutMuonLooseIDVeto,
        cutSecMuonLooseIDVeto, 
        cutMaxCalo10, 
        cutTrkHitMissOut,
    )
)


FullSelectionFakeTrkCtrlInv = cms.PSet(
    name = cms.string("FullSelectionFakeTrkCtrlInv"),
    triggers = triggersJetMet,
    cuts = cms.VPSet (
        cutMET,
        cutSecJetPt,
        cutSecJetEta2p4,            
        cutSecJetNoiseChgHad,
        cutSecJetNoiseChgEM,
        cutSecJetNoiseNeuHad,
        cutSecJetNoiseNeuEM,
        cutSubLeadingJetID,
        cutJetJetDPhi,
        cutTrkPt,
        cutTrkEta,
        cutTrkD0,
#       cutTrkD0Inv,
        cutTrkDZ,
#       cutTrkDZInv,
#       cutTrkNHits,
        cutTrkNHits4,
#        cutTrkHitMissMid,
        cutTrkHitMissMidInv,
        cutTrkHitMissIn,
        cutTrkDeadEcalVeto,
        cutTrkCrackVeto,
        cutTrkRelIsoRp3,  
        cutTrkJetDeltaR,
        cutElecLooseIDVeto, 
        cutTauLooseHadronicVeto,  
        cutTrkWheel0GapVeto, 
        cutTrkEtaMuonPk, 
        cutMuonLooseIDVeto,
        cutSecMuonLooseIDVeto, 
        cutMaxCalo10, 
        cutTrkHitMissOut,
    )
)


FullSelectionFakeTrkCtrlNom = cms.PSet(
    name = cms.string("FullSelectionFakeTrkCtrlNom"),
    triggers = triggersJetMet,
    cuts = cms.VPSet (
        cutMET,
        cutSecJetPt,
        cutSecJetEta2p4,            
        cutSecJetNoiseChgHad,
        cutSecJetNoiseChgEM,
        cutSecJetNoiseNeuHad,
        cutSecJetNoiseNeuEM,
        cutSubLeadingJetID,
        cutJetJetDPhi,
        cutTrkPt,
        cutTrkEta,
        cutTrkD0,
#       cutTrkD0Inv,
        cutTrkDZ,
#       cutTrkDZInv,
#       cutTrkNHits,
        cutTrkNHits4,
        cutTrkHitMissMid,
        cutTrkHitMissIn,
        cutTrkDeadEcalVeto,
        cutTrkCrackVeto,
        cutTrkRelIsoRp3,  
        cutTrkJetDeltaR,
        cutElecLooseIDVeto, 
        cutTauLooseHadronicVeto,  
        cutTrkWheel0GapVeto, 
        cutTrkEtaMuonPk, 
        cutMuonLooseIDVeto,
        cutSecMuonLooseIDVeto, 
        cutMaxCalo10, 
        cutTrkHitMissOut,
    )
)





PreSelectionMuonVetoOnly = cms.PSet(
    name = cms.string("PreSelectionMuonVetoOnly"),
    triggers = triggersJetMet,
    cuts = cms.VPSet (
       cutMET,
       cutSecJetPt,
       cutSecJetEta2p4,
       cutSecJetNoiseChgHad,
       cutSecJetNoiseChgEM,
       cutSecJetNoiseNeuHad,
       cutSecJetNoiseNeuEM,
       cutSubLeadingJetID,
       cutElecLooseIDVeto,
       cutMuonLooseIDVeto,
       ),
    )



PreSelectionMuonLooseID = cms.PSet(
    name = cms.string("PreSelectionMuonLooseID"),
    triggers = triggersJetMet,
    cuts = cms.VPSet (
       cutMET,
       cutSecJetPt,
       cutSecJetEta2p4,
       cutSecJetNoiseChgHad,
       cutSecJetNoiseChgEM,
       cutSecJetNoiseNeuHad,
       cutSecJetNoiseNeuEM,
       cutSubLeadingJetID,
       cutElecLooseIDVeto,
       cutMuonLooseID,
       cutTauLooseHadronicVeto,
       cutTrkPt,
       cutTrkEta,
       cutTrkD0,
       cutTrkDZ,
       cutTrkNHits,
       cutTrkHitMissMid,
       cutTrkHitMissIn,
       cutTrkDeadEcalVeto,
       cutTrkCrackVeto,
       cutTrkRelIsoRp3,
       cutTrkJetDeltaR,
       cutJetJetDPhi,
       ),
    )




## Ctrl sample for electrons ##
PreSelectionPt30NoLepVeto = cms.PSet(
    name = cms.string("PreSelectionPt30NoLepVeto"),
    triggers = triggersJetMet,
    cuts = copy.deepcopy(cutsPresel), 
    )
for i in xrange(len(PreSelectionPt30NoLepVeto.cuts) - 1, -1, -1):
    if PreSelectionPt30NoLepVeto.cuts[i].cutString == cutTrkPt.cutString:
        PreSelectionPt30NoLepVeto.cuts[i].cutString = cutTrkPt30.cutString
    if PreSelectionPt30NoLepVeto.cuts[i].cutString == cutElecLooseIDVeto.cutString \
    or PreSelectionPt30NoLepVeto.cuts[i].cutString == cutTauLooseHadronicVeto.cutString \
    or PreSelectionPt30NoLepVeto.cuts[i].cutString == cutMuonLooseIDVeto.cutString \
    or PreSelectionPt30NoLepVeto.cuts[i].cutString == cutSecMuonLooseIDVeto.cutString:  
        del PreSelectionPt30NoLepVeto.cuts[i] 


## Ctrl sample for electrons ##
PreSelectionElec = cms.PSet(
    name = cms.string("PreSelectionElec"),
    triggers = triggersJetMet,
    cuts = copy.deepcopy(cutsPresel), 
    )
for i in xrange(len(PreSelectionElec.cuts) - 1, -1, -1):
    if PreSelectionElec.cuts[i].cutString == cutElecLooseIDVeto.cutString: 
        del PreSelectionElec.cuts[i] 

PreSelectionElecNoTrig = cms.PSet(
    name = cms.string("PreSelectionElecNoTrig"),
    cuts = copy.deepcopy(PreSelectionElec.cuts), 
    )

## Ctrl sample for muons ##
PreSelectionMuon = cms.PSet(
    name = cms.string("PreSelectionMuon"),  
    triggers = triggersJetMet,
    cuts = copy.deepcopy(cutsPresel), 
    )
for i in xrange(len(PreSelectionMuon.cuts) - 1, -1, -1):
    if PreSelectionMuon.cuts[i].cutString == cutMuonLooseIDVeto.cutString or PreSelectionMuon.cuts[i].cutString == cutSecMuonLooseIDVeto.cutString: 
        del PreSelectionMuon.cuts[i] 

## Use MetNoMu instead of Met cut ## 
PreSelectionMuonMetNoMu = cms.PSet(
    name = cms.string("PreSelectionMuonMetNoMu"),
    triggers = triggersJetMet,
    cuts = copy.deepcopy(PreSelectionMuon.cuts), 
    )
for i in xrange(len(PreSelectionMuonMetNoMu.cuts) - 1, -1, -1):
    if PreSelectionMuonMetNoMu.cuts[i].cutString == cutMET.cutString:
        PreSelectionMuonMetNoMu.cuts[i].cutString = cutMETNoMu.cutString    

PreSelectionMuonNoTrig = cms.PSet(
    name = cms.string("PreSelectionMuonNoTrig"),
    cuts = copy.deepcopy(PreSelectionMuon.cuts), 
    )


## Ctrl sample for taus ##
PreSelectionTau = cms.PSet(
    name = cms.string("PreSelectionTau"),
    triggers = triggersJetMet,
    cuts = copy.deepcopy(cutsPresel), 
    )
for i in xrange(len(PreSelectionTau.cuts) - 1, -1, -1):
    if PreSelectionTau.cuts[i].cutString == cutTauLooseHadronicVeto.cutString:  
        del PreSelectionTau.cuts[i]



PreSelectionPTrkJetDeltaR = cms.PSet(
    name = cms.string("PreSelectionPTrkJetDeltaR"),
    triggers = triggersJetMet,
    cuts = cms.VPSet (
         cutMET,
         cutSecJetPt,
         cutSecJetEta2p4,
         cutSecJetNoiseChgHad,
         cutSecJetNoiseChgEM,
         cutSecJetNoiseNeuHad,
         cutSecJetNoiseNeuEM,
         cutSubLeadingJetID,
         cutElecLooseIDVeto,
         cutMuonLooseIDVeto,
         cutTauLooseHadronicVeto,
         cutTrkPt,
         cutTrkEta,
         cutTrkD0,
         cutTrkDZ,
         cutTrkNHits,
         cutTrkHitMissMid,
         cutTrkHitMissIn,
         cutTrkDeadEcalVeto,
         cutTrkCrackVeto,
         cutTrkJetDeltaR
         ),
    )


PreSelectionWithTrigJetMet = cms.PSet(
    name = cms.string("PreSelectionWithTrigJetMet"),
    triggers = triggersJetMet,
    cuts = copy.deepcopy(PreSelection.cuts),
    )
## PreSelectionWithTrigJetMet.cuts.insert(0,cutJetPt)
## PreSelectionWithTrigJetMet.cuts.insert(0,cutMET)


PreSelectionDeadEcalMatch = cms.PSet(
        name = cms.string("PreSelectionDeadEcalMatch"),
        cuts = cms.VPSet (
           cutTrkPt,
           cutTrkEta,
           cutTrkD0,
           cutTrkDZ,
           cutTrkNHits,
           cutTrkHitMissMid,
           cutTrkHitMissIn,
           cutTrkIso,
           cutMuonVeto,
           cutElecVeto,
           cutTrkDeadEcalMatch,
           cutTrkCrackVeto,
           ),
        )

PreSelectionDeadEcalMatchWithTrigJetMet = cms.PSet(
        name = cms.string("PreSelectionDeadEcalMatchWithTrigJetMet"),
        triggers = triggersJetMet,
        cuts = copy.deepcopy(PreSelectionDeadEcalMatch.cuts),
        )
PreSelectionDeadEcalMatchWithTrigJetMet.cuts.insert(0,cutJetPt)
PreSelectionDeadEcalMatchWithTrigJetMet.cuts.insert(0,cutMET)

PreSelectionIsoTrkOnly = cms.PSet(
    name = cms.string("PreSelectionIsoTrkOnly"),
    cuts = cms.VPSet (
         cutTrkPt,
         cutTrkEta,
         cutTrkD0,
         cutTrkDZ,
         cutTrkNHits,
         cutTrkHitMissMid,
         cutTrkHitMissIn,
         cutTrkIso,
         ),
    )

PreSelectionIsoTrkOnlyWithNoiseClean = cms.PSet(
    name = cms.string("PreSelectionIsoTrkOnlyWithNoiseClean"),
    triggers = triggersJetMet,
    cuts = cms.VPSet (
         cutEvtFilterScraping,
         cutVtxGood,
         cutMET,
         cutJetPt,
         cutJetEta,
         cutJetNoiseChgHad,
         cutJetNoiseNeuEM,
         cutJetNoiseNeuHad,
         cutTrkPt,
         cutTrkEta,
         cutTrkD0,
         cutTrkDZ,
         cutTrkNHits,
         cutTrkHitMissMid,
         cutTrkHitMissIn,
         cutTrkIso,
         cutTrkSumPtLT,
         ),
    )

PreSelectionWithNoiseClean = cms.PSet(
    name = cms.string("PreSelectionWithNoiseClean"),
    triggers = triggersJetMet,
    cuts = cms.VPSet (
         cutEvtFilterScraping,
         cutVtxGood,
         cutMET,
         cutJetPt,
         cutJetEta,
         cutJetNoiseChgHad,
         cutJetNoiseNeuEM,
         cutJetNoiseNeuHad,
         cutTrkPt,
         cutTrkEta,
         cutTrkD0,
         cutTrkDZ,
         cutTrkNHits,
         cutTrkHitMissMid,
         cutTrkHitMissIn,
         cutTrkIso,
         cutTrkSumPtLT,
         cutMuonVeto,
         cutElecVeto,
         cutTrkDeadEcalVeto,
         cutTrkCrackVeto,
         ),
    )

PreSelectionIsoTrkOnlyWithTrigJetMet = cms.PSet(
    name = cms.string("PreSelectionIsoTrkOnlyWithTrigJetMet"),
    triggers = triggersJetMet,
    cuts = copy.deepcopy(PreSelectionIsoTrkOnly.cuts),
    )
PreSelectionIsoTrkOnlyWithTrigJetMet.cuts.insert(0,cutJetPt)
PreSelectionIsoTrkOnlyWithTrigJetMet.cuts.insert(0,cutMET)

PreSelectionIsoTrkOnlyElecMatch = cms.PSet(
    name = cms.string("PreSelectionIsoTrkOnlyElecMatch"),
    triggers = triggersJetMet,
    cuts = cms.VPSet (
        cutEvtFilterScraping,
        cutVtxGood, 
        cutMET,
        cutJetPt,
        cutJetEta,
        cutJetNoiseChgHad,
        cutJetNoiseNeuEM,
        cutJetNoiseNeuHad,
        cutNJets,
        cutElecPt20,     
        cutElecEta,    
        cutElecD0,     
        cutElecMva, 
        #        cutElecTightID,  
        cutElecPFIso,  
        cutElecNHits,  
        cutElecVetoOneMax, 
        cutMuonVetoPt10,   
        cutTrkPt,
        cutTrkEta,
        cutTrkD0,
        #        cutTrkDZ,
        cutTrkNHits,
        ## cutTrkHitMissMid,
        ## cutTrkHitMissIn,
        ## cutTrkIso,
        ## cutTrkSumPtLT,
        cutElecTrkDRSame,
    )
)


PreSelectionIsoTrkOnlyMuonMatch = cms.PSet(
    name = cms.string("PreSelectionIsoTrkOnlyMuonMatch"),
    triggers = triggersJetMet,
    cuts = cms.VPSet (
        cutEvtFilterScraping,
        cutVtxGood, 
        cutMET,
        cutJetPt,
        cutJetEta,
        cutJetNoiseChgHad,
        cutJetNoiseNeuEM,
        cutJetNoiseNeuHad,
        cutNJets,
        cutMuonPt20,
        cutMuonEta,
        cutMuonTightID,
        cutMuonDetIso,
        cutMuonOneOnly,
        cutElecVetoPt10,   
        cutTrkPt,
        cutTrkEta,
        cutTrkD0,
        #        cutTrkDZ,
        cutTrkNHits,
        ## cutTrkHitMissMid,
        ## cutTrkHitMissIn,
        #        cutTrkIso,
        #        cutTrkSumPtLT,
        cutMuonTrkDRSame,
    )
)


PreSelectionIsoTrkOnlyNoMuonMatch = copy.deepcopy(PreSelectionIsoTrkOnlyWithTrigJetMet)
PreSelectionIsoTrkOnlyNoMuonMatch.name = "PreSelectionIsoTrkOnlyNoMuonMatch"
PreSelectionIsoTrkOnlyNoMuonMatch.cuts.append(cutMuonTrkDRSameNone)
PreSelectionIsoTrkOnlyNoMuonMatch.cuts.append(cutMuonVeto)

PreSelectionIsoTrkOnlyNoElecMatch = copy.deepcopy(PreSelectionIsoTrkOnlyWithTrigJetMet)
PreSelectionIsoTrkOnlyNoElecMatch.name = "PreSelectionIsoTrkOnlyNoElecMatch"
PreSelectionIsoTrkOnlyNoElecMatch.cuts.append(cutTrkDeadEcalVeto)
PreSelectionIsoTrkOnlyNoElecMatch.cuts.append(cutTrkCrackVeto)
PreSelectionIsoTrkOnlyNoElecMatch.cuts.append(cutElecTrkDRSameNone)
PreSelectionIsoTrkOnlyNoElecMatch.cuts.append(cutElecVeto)




PreSelectionIsoTrkOnlyNoDz = cms.PSet(
    name = cms.string("PreSelectionIsoTrkOnlyNoDz"),
    cuts = cms.VPSet (
       cutTrkPt,
       cutTrkEta,
       cutTrkD0,
       cutTrkNHits,
       cutTrkHitMissMid,
       cutTrkHitMissIn,
       cutTrkIso,
       ),
    )

PreSelectionIsoTrkOnlyNoDzWithTrigJetMet = cms.PSet(
    name = cms.string("PreSelectionIsoTrkOnlyNoDzWithTrigJetMet"),
    triggers = triggersJetMet,
    cuts = copy.deepcopy(PreSelectionIsoTrkOnlyNoDz.cuts),
    )
PreSelectionIsoTrkOnlyNoDzWithTrigJetMet.cuts.insert(0,cutJetPt)
PreSelectionIsoTrkOnlyNoDzWithTrigJetMet.cuts.insert(0,cutMET)


PreSelectionIsoTrkOnlyNoD0 = cms.PSet(
    name = cms.string("PreSelectionIsoTrkOnlyNoDz"),
    cuts = cms.VPSet (
       cutTrkPt,
       cutTrkEta,
       cutTrkDZ,
       cutTrkNHits,
       cutTrkHitMissMid,
       cutTrkHitMissIn,
       cutTrkIso,
       ),
    )

PreSelectionIsoTrkOnlyNoD0WithTrigJetMet = cms.PSet(
    name = cms.string("PreSelectionIsoTrkOnlyNoD0WithTrigJetMet"),
    triggers = triggersJetMet,
    cuts = copy.deepcopy(PreSelectionIsoTrkOnlyNoD0.cuts),
    )
PreSelectionIsoTrkOnlyNoD0WithTrigJetMet.cuts.insert(0,cutJetPt)
PreSelectionIsoTrkOnlyNoD0WithTrigJetMet.cuts.insert(0,cutMET)


PreSelectionMuonVetoOnly = cms.PSet(
    name = cms.string("PreSelectionMuonVetoOnly"),
    cuts = cms.VPSet (
       cutTrkPt,
       cutTrkEta,
       cutTrkD0,
       cutTrkDZ,
       cutTrkNHits,
       cutTrkHitMissMid,
       cutTrkHitMissIn,
       cutTrkIso,
       cutMuonVeto,
       ),
    )

PreSelectionMuonVetoOnlyWithTrigJetMet = cms.PSet(
    name = cms.string("PreSelectionMuonVetoOnlyWithTrigJetMet"),
    triggers = triggersJetMet,
    cuts = copy.deepcopy(PreSelectionMuonVetoOnly.cuts),
    )
PreSelectionMuonVetoOnlyWithTrigJetMet.cuts.insert(0,cutJetPt)
PreSelectionMuonVetoOnlyWithTrigJetMet.cuts.insert(0,cutMET)

PreSelectionElectronVetoOnly = cms.PSet(
    name = cms.string("PreSelectionElectronVetoOnly"),
    cuts = cms.VPSet (
       cutTrkPt,
       cutTrkEta,
       cutTrkD0,
       cutTrkDZ,
       cutTrkNHits,
       cutTrkHitMissMid,
       cutTrkHitMissIn,
       cutTrkIso,
       cutMuonVeto,
       cutElecVeto,
       ),
    )

PreSelectionElectronVetoOnlyWithTrigJetMet = cms.PSet(
    name = cms.string("PreSelectionElectronVetoOnlyWithTrigJetMet"),
    triggers = triggersJetMet,
    cuts = copy.deepcopy(PreSelectionElectronVetoOnly.cuts),
    )
PreSelectionElectronVetoOnlyWithTrigJetMet.cuts.insert(0,cutJetPt)
PreSelectionElectronVetoOnlyWithTrigJetMet.cuts.insert(0,cutMET)

PreSelectionDeadEcalVetoOnly = cms.PSet(
        name = cms.string("PreSelectionDeadEcalVetoOnly"),
        cuts = cms.VPSet (
           cutTrkPt,
           cutTrkEta,
           cutTrkD0,
           cutTrkDZ,
           cutTrkNHits,
           cutTrkHitMissMid,
           cutTrkHitMissIn,
           cutTrkIso,
           cutMuonVeto,
           cutElecVeto,
           cutTrkDeadEcalVeto,
           ),
        )

PreSelectionDeadEcalVetoOnlyWithTrigJetMet = cms.PSet(
        name = cms.string("PreSelectionDeadEcalVetoOnlyWithTrigJetMet"),
            triggers = triggersJetMet,
            cuts = copy.deepcopy(PreSelectionDeadEcalVetoOnly.cuts),
            )
PreSelectionDeadEcalVetoOnlyWithTrigJetMet.cuts.insert(0,cutJetPt)
PreSelectionDeadEcalVetoOnlyWithTrigJetMet.cuts.insert(0,cutMET)

PreSelectionDeadEcalMatchOnly = cms.PSet(
            name = cms.string("PreSelectionDeadEcalMatchOnly"),
            cuts = cms.VPSet (
               cutTrkPt,
               cutTrkEta,
               cutTrkD0,
               cutTrkDZ,
               cutTrkNHits,
               cutTrkHitMissMid,
               cutTrkHitMissIn,
               cutTrkIso,
               cutMuonVeto,
               cutElecVeto,
               cutTrkDeadEcalMatch,
               ),
            )

PreSelectionDeadEcalMatchOnlyWithTrigJetMet = cms.PSet(
    name = cms.string("PreSelectionDeadEcalMatchOnlyWithTrigJetMet"),
    triggers = triggersJetMet,
    cuts = copy.deepcopy(PreSelectionDeadEcalMatchOnly.cuts),
    )
PreSelectionDeadEcalMatchOnlyWithTrigJetMet.cuts.insert(0,cutJetPt)
PreSelectionDeadEcalMatchOnlyWithTrigJetMet.cuts.insert(0,cutMET)

PreSelectionIsoTrkOnlyDzSide = cms.PSet(
    name = cms.string("PreSelectionIsoTrkOnlyDzSide"),
    cuts = cms.VPSet (
       cutTrkPt,
       cutTrkEta,
       cutTrkD0,
       cutTrkDZSide,
       cutTrkNHits,
       cutTrkHitMissMid,
       cutTrkHitMissIn,
       cutTrkIso,
       ),
    )
PreSelectionIsoTrkOnlyDzSideWithTrigJetMet = cms.PSet(
    name = cms.string("PreSelectionIsoTrkOnlyDzSideWithTrigJetMet"),
    triggers = triggersJetMet,
    cuts = copy.deepcopy(PreSelectionIsoTrkOnlyDzSide.cuts),
    )
PreSelectionIsoTrkOnlyDzSideWithTrigJetMet.cuts.insert(0,cutJetPt)
PreSelectionIsoTrkOnlyDzSideWithTrigJetMet.cuts.insert(0,cutMET)


PreSelectionIsoTrkOnlyD0Side = cms.PSet(
    name = cms.string("PreSelectionIsoTrkOnlyD0Side"),
    cuts = cms.VPSet (
       cutTrkPt,
       cutTrkEta,
       cutTrkD0Side,
       cutTrkDZ,
       cutTrkNHits,
       cutTrkHitMissMid,
       cutTrkHitMissIn,
       cutTrkIso,
       ),
    )
PreSelectionIsoTrkOnlyD0SideWithTrigJetMet = cms.PSet(
    name = cms.string("PreSelectionIsoTrkOnlyD0SideWithTrigJetMet"),
    triggers = triggersJetMet,
    cuts = copy.deepcopy(PreSelectionIsoTrkOnlyD0Side.cuts),
    )
PreSelectionIsoTrkOnlyD0SideWithTrigJetMet.cuts.insert(0,cutJetPt)
PreSelectionIsoTrkOnlyD0SideWithTrigJetMet.cuts.insert(0,cutMET)


PreSelIdMuonNoVeto = cms.PSet(
    name = cms.string("PreSelIdMuonNoVeto"),
#    triggers = triggersJetMet,
    cuts = cms.VPSet (
##         cutMET,
##         cutMETNoMu,
##         cutSecJetPt,
##         cutSecJetEta2p4,            
##         cutSecJetNoiseChgHad,
##         cutSecJetNoiseChgEM,
##         cutSecJetNoiseNeuHad,
##         cutSecJetNoiseNeuEM,
##         cutSubLeadingJetID,
##         cutJetJetDPhi,
        cutTrkMuonId, 
#       cutMET,
        cutTrkPt,
        cutTrkEta,
        cutTrkD0,
        cutTrkDZ,
        cutTrkNHits,
        cutTrkHitMissMid,
        cutTrkHitMissIn,
        cutTrkDeadEcalVeto,
        cutTrkCrackVeto,
        cutTrkRelIsoRp3,  
        cutTrkJetDeltaR,
        cutElecLooseIDVeto, 
        cutTauLooseHadronicVeto,  
        cutTrkWheel0GapVeto, 
        cutTrkEtaMuonPk, 
        cutMaxCalo10, 
##         cutTrkHitMissOut,
    )
)


PreSelCtrlNMiss = copy.deepcopy(PreSelection)
PreSelCtrlNMiss.name = "PreSelCtrlNMiss"
PreSelCtrlNMiss.cuts = cutsPreselCtrlNMiss 

PreSelCtrlNMissIdElec = copy.deepcopy(PreSelCtrlNMiss)
PreSelCtrlNMissIdElec.name = "PreSelCtrlNMissIdElec"
PreSelCtrlNMissIdElec.cuts.append(cutTrkElectronId) 

PreSelCtrlNMissIdMuon = copy.deepcopy(PreSelCtrlNMiss)
PreSelCtrlNMissIdMuon.name = "PreSelCtrlNMissIdMuon"
PreSelCtrlNMissIdMuon.cuts.append(cutTrkMuonId) 

PreSelCtrlNMissIdTau = copy.deepcopy(PreSelCtrlNMiss)
PreSelCtrlNMissIdTau.name = "PreSelCtrlNMissIdTau"
PreSelCtrlNMissIdTau.cuts.append(cutTrkTauId) 

PreSelCtrlNMissIdFake = copy.deepcopy(PreSelCtrlNMiss)
PreSelCtrlNMissIdFake.name = "PreSelCtrlNMissIdFake"
PreSelCtrlNMissIdFake.cuts.append(cutTrkNotGenMatched)  

PreSelCtrlNMissIdOther = copy.deepcopy(PreSelCtrlNMiss)
PreSelCtrlNMissIdOther.name = "PreSelCtrlNMissIdOther"
PreSelCtrlNMissIdOther.cuts = PreSelCtrlNMissIdOther.cuts + cutsTrkIdOther # Cannot append a VPSet

PreSelCtrlNMissElec = copy.deepcopy(PreSelCtrlNMiss)
PreSelCtrlNMissElec.name = "PreSelCtrlNMissElec"
for i in xrange(len(PreSelCtrlNMissElec.cuts) - 1, -1, -1):
    if PreSelCtrlNMissElec.cuts[i].cutString == cutElecLooseIDVeto.cutString:
        del PreSelCtrlNMissElec.cuts[i]

PreSelCtrlNMissMuon = copy.deepcopy(PreSelCtrlNMiss)
PreSelCtrlNMissMuon.name = "PreSelCtrlNMissMuon"
for i in xrange(len(PreSelCtrlNMissMuon.cuts) - 1, -1, -1):
    if PreSelCtrlNMissMuon.cuts[i].cutString == cutMuonLooseIDVeto.cutString or PreSelCtrlNMissMuon.cuts[i].cutString == cutSecMuonLooseIDVeto.cutString: 
        del PreSelCtrlNMissMuon.cuts[i]

PreSelCtrlNMissTau = copy.deepcopy(PreSelCtrlNMiss)
PreSelCtrlNMissTau.name = "PreSelCtrlNMissTau"
for i in xrange(len(PreSelCtrlNMissTau.cuts) - 1, -1, -1):
    if PreSelCtrlNMissTau.cuts[i].cutString == cutTauLooseHadronicVeto.cutString:
        del PreSelCtrlNMissTau.cuts[i]


PreSelCtrlEcalo = copy.deepcopy(PreSelection)
PreSelCtrlEcalo.name = "PreSelCtrlEcalo"
PreSelCtrlEcalo.cuts = cutsPreselCtrlEcalo 

PreSelCtrlEcaloIdElec = copy.deepcopy(PreSelCtrlEcalo)
PreSelCtrlEcaloIdElec.name = "PreSelCtrlEcaloIdElec"
PreSelCtrlEcaloIdElec.cuts.append(cutTrkElectronId) 

PreSelCtrlEcaloIdMuon = copy.deepcopy(PreSelCtrlEcalo)
PreSelCtrlEcaloIdMuon.name = "PreSelCtrlEcaloIdMuon"
PreSelCtrlEcaloIdMuon.cuts.append(cutTrkMuonId) 

PreSelCtrlEcaloIdTau = copy.deepcopy(PreSelCtrlEcalo)
PreSelCtrlEcaloIdTau.name = "PreSelCtrlEcaloIdTau"
PreSelCtrlEcaloIdTau.cuts.append(cutTrkTauId) 

PreSelCtrlEcaloIdFake = copy.deepcopy(PreSelCtrlEcalo)
PreSelCtrlEcaloIdFake.name = "PreSelCtrlEcaloIdFake"
PreSelCtrlEcaloIdFake.cuts.append(cutTrkNotGenMatched)  

PreSelCtrlEcaloIdOther = copy.deepcopy(PreSelCtrlEcalo)
PreSelCtrlEcaloIdOther.name = "PreSelCtrlEcaloIdOther"
PreSelCtrlEcaloIdOther.cuts = PreSelCtrlEcaloIdOther.cuts + cutsTrkIdOther # Cannot append a VPSet

PreSelCtrlEcaloElec = copy.deepcopy(PreSelCtrlEcalo)
PreSelCtrlEcaloElec.name = "PreSelCtrlEcaloElec"
for i in xrange(len(PreSelCtrlEcaloElec.cuts) - 1, -1, -1):
    if PreSelCtrlEcaloElec.cuts[i].cutString == cutElecLooseIDVeto.cutString:
        del PreSelCtrlEcaloElec.cuts[i]

PreSelCtrlEcaloMuon = copy.deepcopy(PreSelCtrlEcalo)
PreSelCtrlEcaloMuon.name = "PreSelCtrlEcaloMuon"
for i in xrange(len(PreSelCtrlEcaloMuon.cuts) - 1, -1, -1):
    if PreSelCtrlEcaloMuon.cuts[i].cutString == cutMuonLooseIDVeto.cutString or PreSelCtrlEcaloMuon.cuts[i].cutString == cutSecMuonLooseIDVeto.cutString: 
        del PreSelCtrlEcaloMuon.cuts[i]

PreSelCtrlEcaloTau = copy.deepcopy(PreSelCtrlEcalo)
PreSelCtrlEcaloTau.name = "PreSelCtrlEcaloTau"
for i in xrange(len(PreSelCtrlEcaloTau.cuts) - 1, -1, -1):
    if PreSelCtrlEcaloTau.cuts[i].cutString == cutTauLooseHadronicVeto.cutString:
        del PreSelCtrlEcaloTau.cuts[i]


PreSelIdElec = copy.deepcopy(PreSelection)
PreSelIdElec.name = "PreSelIdElec"
PreSelIdElec.cuts.append(cutTrkElectronId)

PreSelIdMuon = copy.deepcopy(PreSelection)
PreSelIdMuon.name = "PreSelIdMuon"
PreSelIdMuon.cuts.append(cutTrkMuonId)

PreSelIdTau = copy.deepcopy(PreSelection)
PreSelIdTau.name = "PreSelIdTau"
PreSelIdTau.cuts.append(cutTrkTauId)

PreSelIdFake = copy.deepcopy(PreSelection)
PreSelIdFake.name = "PreSelIdFake"
PreSelIdFake.cuts.append(cutTrkNotGenMatched)

PreSelIdOther = copy.deepcopy(PreSelection)
PreSelIdOther.name = "PreSelIdOther"
PreSelIdOther.cuts = PreSelIdOther.cuts + cutsTrkIdOther # Cannot append a VPSet 



FullSelIdElec = copy.deepcopy(FullSelection)
FullSelIdElec.name = "FullSelIdElec"
FullSelIdElec.cuts.append(cutTrkElectronId)

FullSelIdMuon = copy.deepcopy(FullSelection)
FullSelIdMuon.name = "FullSelIdMuon"
FullSelIdMuon.cuts.append(cutTrkMuonId)

FullSelIdTau = copy.deepcopy(FullSelection)
FullSelIdTau.name = "FullSelIdTau"
FullSelIdTau.cuts.append(cutTrkTauId)

FullSelIdFake = copy.deepcopy(FullSelection)
FullSelIdFake.name = "FullSelIdFake"
FullSelIdFake.cuts.append(cutTrkNotGenMatched)

FullSelIdOther = copy.deepcopy(FullSelection)
FullSelIdOther.name = "FullSelIdOther"
FullSelIdOther.cuts = FullSelIdOther.cuts + cutsTrkIdOther # Cannot append a VPSet 



PreSelIdMuonInvHits = cms.PSet(
    name = cms.string("PreSelIdMuonInvHits"),
    triggers = triggersJetMet,
    cuts = cms.VPSet (
        cutMET,
#        cutMETNoMu,
        cutSecJetPt,
        cutSecJetEta2p4,            
        cutSecJetNoiseChgHad,
        cutSecJetNoiseChgEM,
        cutSecJetNoiseNeuHad,
        cutSecJetNoiseNeuEM,
        cutSubLeadingJetID,
        cutJetJetDPhi,
#       cutTrkMuonId, 
#       cutTrkPt,
        cutTrkPt50,
        cutTrkEta,
#       cutTrkEtaBarrel,
        cutTrkD0,
        cutTrkDZ,
        cutTrkNHits,
        cutTrkHitMissMid,
        cutTrkHitMissIn,
        cutTrkDeadEcalVeto,
        cutTrkCrackVeto,
        cutTrkRelIsoRp3,  
        cutTrkJetDeltaR,
        cutElecLooseIDVeto, 
        cutTauLooseHadronicVeto,  
        cutMuonLooseIDVeto,
        cutSecMuonLooseIDVeto, 
        cutTrkWheel0GapVeto, 
        cutTrkEtaMuonPk, 
        cutMaxCalo10, 
        cutTrkHitMissOutInv,
    )
)

SimpleIdMuon = cms.PSet(
    name = cms.string("SimpleIdMuon"),
#    triggers = triggersJetMet,
    cuts = cms.VPSet (
        cutTrkMuonId, 
#        cutTrkPt,
        cutTrkPt50,
#       cutTrkPt75,
        cutTrkEta,
        cutMuonLooseIDVeto,
        cutSecMuonLooseIDVeto,
        )
    )


PreSelIdMuonNoMetJetNoVeto = cms.PSet(
    name = cms.string("PreSelIdMuonNoMetJetNoVeto"),
    triggers = triggersSingleMu, 
    cuts = cms.VPSet (
##         cutMET,
##         cutSecJetPt,
##         cutSecJetEta2p4,            
##         cutSecJetNoiseChgHad,
##         cutSecJetNoiseChgEM,
##         cutSecJetNoiseNeuHad,
##         cutSecJetNoiseNeuEM,
        cutSubLeadingJetID,
        cutJetJetDPhi,
        cutTrkMuonId, 
        cutTrkPt,
        cutTrkEta,
#       cutTrkEtaBarrel,
        cutTrkD0,
        cutTrkDZ,
        cutTrkNHits,
        cutTrkHitMissMid,
        cutTrkHitMissIn,
        cutTrkDeadEcalVeto,
        cutTrkCrackVeto,
        cutTrkRelIsoRp3,  
        cutTrkJetDeltaR,
        cutElecLooseIDVeto,
        cutTauLooseHadronicVeto,    
    )
)

PreSelIdMuonNoMetJet = copy.deepcopy(PreSelIdMuonNoMetJetNoVeto)  
PreSelIdMuonNoMetJet.name = "PreSelIdMuonNoMetJet"  
PreSelIdMuonNoMetJet.cuts.append(cutMuonLooseIDVeto)  
PreSelIdMuonNoMetJet.cuts.append(cutSecMuonLooseIDVeto)  



SigRegIdMuon = cms.PSet(
    name = cms.string("SigRegIdMuon"),
    triggers = triggersJetMet,
    cuts = cms.VPSet (
        cutTrkMuonId, 
        cutTrkPt,
        cutTrkEta,
        cutTrkD0,
        cutTrkDZ,
        cutTrkNHits,
        cutTrkHitMissMid,
        cutTrkHitMissIn,
        cutTrkDeadEcalVeto,
        cutTrkCrackVeto,
        cutTrkRelIsoRp3,  
        cutTrkJetDeltaR,
        cutElecLooseIDVeto,
        cutTauLooseHadronicVeto,    
        cutMET,
        cutSecJetPt,
        cutSecJetEta2p4,            
        cutSecJetNoiseChgHad,
        cutSecJetNoiseChgEM,
        cutSecJetNoiseNeuHad,
        cutSecJetNoiseNeuEM,
        cutSubLeadingJetID,
        cutJetJetDPhi,
        cutTrkHitMissOut,
        cutMaxCaloPUCorr,
##         cutMuonLooseIDVeto,
##         cutSecMuonLooseIDVeto,
    )
)


PreSelPMissInvVetoIdMuon = cms.PSet(
    name = cms.string("PreSelPMissInvVetoIdMuon"),
    triggers = triggersJetMet,
    cuts = cms.VPSet (
        cutMET,
        cutSecJetPt,
        cutSecJetEta2p4,            
        cutSecJetNoiseChgHad,
        cutSecJetNoiseChgEM,
        cutSecJetNoiseNeuHad,
        cutSecJetNoiseNeuEM,
        cutSubLeadingJetID,
        cutJetJetDPhi,
        cutTrkMuonId, 
        cutTrkPt,
        cutTrkEta,
        cutTrkD0,
        cutTrkDZ,
        cutTrkNHits,
        cutTrkHitMissMid,
        cutTrkHitMissIn,
        cutTrkDeadEcalVeto,
        cutTrkCrackVeto,
        cutTrkRelIsoRp3,  
        cutTrkJetDeltaR,
        cutElecLooseIDVeto,
        cutTauLooseHadronicVeto,    
        cutTrkHitMissOut,
        cutMaxCaloPUCorr,
        cutMuonLooseIDVetoInv,
    )
)

PreSelInvVetoIdMuon = cms.PSet(
    name = cms.string("PreSelInvVetoIdMuon"),
    triggers = triggersJetMet,
    cuts = copy.deepcopy(PreSelInvMuonVeto.cuts),
    )
PreSelInvVetoIdMuon.cuts.append(cutTrkMuonId)


PreSelectionPMissing = cms.PSet(
    name = cms.string("PreSelectionPMissing"),
    cuts = copy.deepcopy(PreSelection.cuts),
    )
PreSelectionPMissing.cuts.append(cutTrkHitMissOut)

PreSelNoTauVetoPMissing = cms.PSet(
    name = cms.string("PreSelNoTauVetoPMissing"),
    cuts = copy.deepcopy(PreSelNoTauVeto.cuts),
    )
PreSelNoTauVetoPMissing.cuts.append(cutTrkHitMissOut)


PreSelectionPMissingWithTrigJetMet = cms.PSet(
    name = cms.string("PreSelectionPMissingWithTrigJetMet"),
    triggers = triggersJetMet,
    cuts = copy.deepcopy(PreSelectionPMissing.cuts),
    )
PreSelectionPMissingWithTrigJetMet.cuts.insert(0,cutJetPt)
PreSelectionPMissingWithTrigJetMet.cuts.insert(0,cutMET)

PreSelectionPMissingBlindWithTrigJetMet = cms.PSet(
    name = cms.string("PreSelectionPMissingBlindWithTrigJetMet"),
    triggers = triggersJetMet,
    cuts = copy.deepcopy(PreSelectionPMissingWithTrigJetMet.cuts),
    )
PreSelectionPMissingBlindWithTrigJetMet.cuts.append(cutMaxCaloPUCorrBlind)



PreSelectionPSumPtLessThan = cms.PSet(
    name = cms.string("PreSelectionPSumPtLessThan"),
    cuts = copy.deepcopy(PreSelection.cuts),
    )
PreSelectionPSumPtLessThan.cuts.append(cutTrkSumPtLT)

PreSelectionPSumPtLessThanWithTrigJetMet = cms.PSet(
    name = cms.string("PreSelectionPSumPtLessThanWithTrigJetMet"),
    triggers = triggersJetMet,
    cuts = copy.deepcopy(PreSelectionPSumPtLessThan.cuts),
    )
PreSelectionPSumPtLessThanWithTrigJetMet.cuts.insert(0,cutJetPt)
PreSelectionPSumPtLessThanWithTrigJetMet.cuts.insert(0,cutMET)

PreSelectionPSumPtLessThanBlindWithTrigJetMet = cms.PSet(
    name = cms.string("PreSelectionPSumPtLessThanBlindWithTrigJetMet"),
    triggers = triggersJetMet,
    cuts = copy.deepcopy(PreSelectionPSumPtLessThanWithTrigJetMet.cuts),
    )
PreSelectionPSumPtLessThanBlindWithTrigJetMet.cuts.append(cutMaxCaloPUCorrBlind)



PreSelectionPSumPtGreaterThan = cms.PSet(
    name = cms.string("PreSelectionPSumPtGreaterThan"),
    cuts = copy.deepcopy(PreSelection.cuts),
    )
PreSelectionPSumPtGreaterThan.cuts.append(cutTrkSumPtGT)

PreSelectionPSumPtGreaterThanWithTrigJetMet = cms.PSet(
            name = cms.string("PreSelectionPSumPtGreaterThanWithTrigJetMet"),
            triggers = triggersJetMet,
            cuts = copy.deepcopy(PreSelectionPSumPtGreaterThan.cuts),
            )
PreSelectionPSumPtGreaterThanWithTrigJetMet.cuts.insert(0,cutJetPt)
PreSelectionPSumPtGreaterThanWithTrigJetMet.cuts.insert(0,cutMET)

PreSelectionPSumPtGreaterThanBlindWithTrigJetMet = cms.PSet(
    name = cms.string("PreSelectionPSumPtGreaterThanBlindWithTrigJetMet"),
    triggers = triggersJetMet,
    cuts = copy.deepcopy(PreSelectionPSumPtGreaterThanWithTrigJetMet.cuts),
    )
PreSelectionPSumPtGreaterThanBlindWithTrigJetMet.cuts.append(cutMaxCaloPUCorrBlind)



PreSelectionPMissingSumPtGreaterThan = cms.PSet(
        name = cms.string("PreSelectionPMissingSumPtGreaterThan"),
        cuts = copy.deepcopy(PreSelectionPMissing.cuts),
        )
PreSelectionPMissingSumPtGreaterThan.cuts.append(cutTrkSumPtGT)


PreSelectionPMissingSumPtGreaterThanWithTrigJetMet = cms.PSet(
        name = cms.string("PreSelectionPMissingSumGreaterThanWithTrigJetMet"),
            triggers = triggersJetMet,
            cuts = copy.deepcopy(PreSelectionPMissingSumPtGreaterThan.cuts),
            )
PreSelectionPMissingSumPtGreaterThanWithTrigJetMet.cuts.insert(0,cutJetPt)
PreSelectionPMissingSumPtGreaterThanWithTrigJetMet.cuts.insert(0,cutMET)

PreSelectionPMissingSumPtGreaterThanBlindWithTrigJetMet = cms.PSet(
    name = cms.string("PreSelectionPMissingSumGreaterThanBlindWithTrigJetMet"),
    triggers = triggersJetMet,
    cuts = copy.deepcopy(PreSelectionPMissingSumPtGreaterThanWithTrigJetMet.cuts),
    )
PreSelectionPMissingSumPtGreaterThanBlindWithTrigJetMet.cuts.append(cutMaxCaloPUCorrBlind)



PreSelectionPMissingSumPtLessThan = cms.PSet(
    name = cms.string("PreSelectionPMissingSumPtLessThan"),
    cuts = copy.deepcopy(PreSelectionPMissing.cuts),
    )
PreSelectionPMissingSumPtLessThan.cuts.append(cutTrkSumPtLT)

PreSelectionPMissingSumPtLessThanWithTrigJetMet = cms.PSet(
    name = cms.string("PreSelectionPMissingSumLessThanWithTrigJetMet"),
    triggers = triggersJetMet,
    cuts = copy.deepcopy(PreSelectionPMissingSumPtLessThan.cuts),
    )
PreSelectionPMissingSumPtLessThanWithTrigJetMet.cuts.insert(0,cutJetPt)
PreSelectionPMissingSumPtLessThanWithTrigJetMet.cuts.insert(0,cutMET)

PreSelectionPMissingSumPtLessThanBlindWithTrigJetMet = cms.PSet(
    name = cms.string("PreSelectionPMissingSumLessThanBlindWithTrigJetMet"),
    triggers = triggersJetMet,
    cuts = copy.deepcopy(PreSelectionPMissingSumPtLessThanWithTrigJetMet.cuts),
    )
PreSelectionPMissingSumPtLessThanBlindWithTrigJetMet.cuts.append(cutMaxCaloPUCorrBlind)



PreSelectionPMissingDzSide = cms.PSet(
    name = cms.string("PreSelectionPMissingDzSide"),
    cuts = copy.deepcopy(PreSelectionIsoTrkOnlyDzSide.cuts),
    )
PreSelectionPMissingDzSide.cuts.append(cutMuonVeto)
PreSelectionPMissingDzSide.cuts.append(cutElecVeto)
PreSelectionPMissingDzSide.cuts.append(cutTrkDeadEcalVeto)
PreSelectionPMissingDzSide.cuts.append(cutTrkCrackVeto)
PreSelectionPMissingDzSide.cuts.append(cutTrkHitMissOut)

PreSelectionPMissingD0Side = cms.PSet(
    name = cms.string("PreSelectionPMissingD0Side"),
    cuts = copy.deepcopy(PreSelectionIsoTrkOnlyD0Side.cuts),
    )
PreSelectionPMissingD0Side.cuts.append(cutMuonVeto)
PreSelectionPMissingD0Side.cuts.append(cutElecVeto)
PreSelectionPMissingD0Side.cuts.append(cutTrkDeadEcalVeto)
PreSelectionPMissingD0Side.cuts.append(cutTrkCrackVeto)
PreSelectionPMissingD0Side.cuts.append(cutTrkHitMissOut)


## Preselection (AOD)
PreSelectionNoHitCut = cms.PSet(
    name = cms.string("PreSelectionNoHitCut"),
    cuts = cms.VPSet (
       cutTrkPt,
       cutTrkEta,
       cutTrkD0,
       cutTrkDZ,
       cutTrkNHits,
       cutTrkIso,
       cutMuonVeto,
       cutElecVeto,
       cutTrkDeadEcalVeto,
       cutTrkCrackVeto,
       ),
    )
PreSelectionNoHitCutWithTrigJetMet = cms.PSet(
    name = cms.string("PreSelectionNoHitCutWithTrigJetMet"),
    triggers = triggersJetMet,
    cuts = copy.deepcopy(PreSelectionNoHitCut.cuts),
    )
PreSelectionNoHitCutWithTrigJetMet.cuts.insert(0,cutJetPt)
PreSelectionNoHitCutWithTrigJetMet.cuts.insert(0,cutMET)


PreSelectionIsoTrkOnlyNoHitCut = cms.PSet(
    name = cms.string("PreSelectionIsoTrkOnlyNoHitCut"),
    cuts = cms.VPSet (
       cutTrkPt,
       cutTrkEta,
       cutTrkD0,
       cutTrkDZ,
       cutTrkNHits,
       cutTrkIso,
       ),
    )

PreSelectionIsoTrkOnlyNoHitCutWithTrigJetMet = cms.PSet(
    name = cms.string("PreSelectionIsoTrkOnlyNoHitCutWithTrigJetMet"),
    triggers = triggersJetMet,
    cuts = copy.deepcopy(PreSelectionIsoTrkOnlyNoHitCut.cuts),
    )
PreSelectionIsoTrkOnlyNoHitCutWithTrigJetMet.cuts.insert(0,cutJetPt)
PreSelectionIsoTrkOnlyNoHitCutWithTrigJetMet.cuts.insert(0,cutMET)


PreSelectionMuonVetoOnlyNoHitCut = cms.PSet(
    name = cms.string("PreSelectionMuonVetoOnlyNoHitCut"),
    cuts = cms.VPSet (
       cutTrkPt,
       cutTrkEta,
       cutTrkD0,
       cutTrkDZ,
       cutTrkNHits,
       cutTrkIso,
       cutMuonVeto,
       ),
    )
PreSelectionMuonVetoOnlyNoHitCutWithTrigJetMet = cms.PSet(
    name = cms.string("PreSelectionMuonVetoOnlyNoHitCutWithTrigJetMet"),
    triggers = triggersJetMet,
    cuts = copy.deepcopy(PreSelectionMuonVetoOnlyNoHitCut.cuts),
    )
PreSelectionMuonVetoOnlyNoHitCutWithTrigJetMet.cuts.insert(0,cutJetPt)
PreSelectionMuonVetoOnlyNoHitCutWithTrigJetMet.cuts.insert(0,cutMET)



## Gen Matched Channels ##

## FullSelectionCharginoId = cms.PSet(
##     name = cms.string("FullSelectionCharginoId"),
##     cuts = copy.deepcopy(FullSelection.cuts),
##     )
FullSelectionCharginoId = copy.deepcopy(FullSelection) 
FullSelectionCharginoId.name = cms.string("FullSelectionCharginoId")
for i in range(0, len(FullSelectionCharginoId.cuts)):
    if FullSelectionCharginoId.cuts[i].cutString == cutTrkPt.cutString:
        idx = i
FullSelectionCharginoId.cuts.insert(idx, cutTrkCharginoId)

FullSelectionCharginoIdDeadEcalLast = copy.deepcopy(FullSelectionCharginoId) 
FullSelectionCharginoIdDeadEcalLast.name = cms.string("FullSelectionCharginoIdDeadEcalLast")  
for i in xrange(len(FullSelectionCharginoIdDeadEcalLast.cuts) - 1, -1, -1):
    if FullSelectionCharginoIdDeadEcalLast.cuts[i].cutString == cutTrkDeadEcalVeto.cutString:
        del FullSelectionCharginoIdDeadEcalLast.cuts[i]                
FullSelectionCharginoIdDeadEcalLast.cuts.append(cutTrkDeadEcalVeto)

FullSelectionCharginoIdNHitsLast = copy.deepcopy(FullSelectionCharginoId) 
FullSelectionCharginoIdNHitsLast.name = cms.string("FullSelectionCharginoIdNHitsLast")  
for i in xrange(len(FullSelectionCharginoIdNHitsLast.cuts) - 1, -1, -1):
    if FullSelectionCharginoIdNHitsLast.cuts[i].cutString == cutTrkNHits.cutString:
        del FullSelectionCharginoIdNHitsLast.cuts[i]                
FullSelectionCharginoIdNHitsLast.cuts.append(cutTrkNHits) 


PreSelectionCharginoId = cms.PSet(
    name = cms.string("PreSelectionCharginoId"),
    cuts = copy.deepcopy(PreSelection.cuts),
    )
PreSelectionCharginoId.cuts.append(cutTrkCharginoId)


PreSelectionElectronId = cms.PSet(
    name = cms.string("PreSelectionElectronId"),
    cuts = copy.deepcopy(PreSelection.cuts),
    )
PreSelectionElectronId.cuts.append(cutTrkElectronId)

PreSelMuonId = cms.PSet(
    name = cms.string("PreSelMuonId"),
    triggers = triggersJetMet,
    cuts = copy.deepcopy(PreSelection.cuts),
    )
PreSelMuonId.cuts.append(cutTrkMuonId)

PreSelectionElectronIdWithTrigJetMet = cms.PSet(
    triggers = triggersJetMet,
    name = cms.string("PreSelectionElectronIdWithTrigJetMet"),
    cuts = copy.deepcopy(PreSelectionWithTrigJetMet.cuts),
    )
PreSelectionElectronIdWithTrigJetMet.cuts.append(cutTrkElectronId)


PreSelectionPionId = cms.PSet(
    name = cms.string("PreSelectionPionId"),
    cuts = copy.deepcopy(PreSelection.cuts),
    )
PreSelectionPionId.cuts.append(cutTrkPionId)

PreSelectionPionIdWithTrigJetMet = cms.PSet(
    triggers = triggersJetMet,
    name = cms.string("PreSelectionPionIdWithTrigJetMet"),
    cuts = copy.deepcopy(PreSelectionWithTrigJetMet.cuts),
    )
PreSelectionPionIdWithTrigJetMet.cuts.append(cutTrkPionId)


PreSelectionNotGenMatched = cms.PSet(
    name = cms.string("PreSelectionNotGenMatched"),
    cuts = copy.deepcopy(PreSelection.cuts),
    )
PreSelectionNotGenMatched.cuts.append(cutTrkNotGenMatched)


PreSelectionPMissingElectronId = cms.PSet(
    name = cms.string("PreSelectionPMissingElectronId"),
    cuts = copy.deepcopy(PreSelectionPMissing.cuts),
    )
PreSelectionPMissingElectronId.cuts.append(cutTrkElectronId)


PreSelectionPMissingElectronIdWithTrigJetMet = cms.PSet(
    triggers = triggersJetMet,
    name = cms.string("PreSelectionPMissingElectronIdWithTrigJetMet"),
    cuts = copy.deepcopy(PreSelectionPMissingWithTrigJetMet.cuts),
    )
PreSelectionPMissingElectronIdWithTrigJetMet.cuts.append(cutTrkElectronId)


PreSelectionPMissingPionId = cms.PSet(
    name = cms.string("PreSelectionPMissingPionId"),
    cuts = copy.deepcopy(PreSelectionPMissing.cuts),
    )
PreSelectionPMissingPionId.cuts.append(cutTrkPionId)

PreSelectionPMissingPionIdWithTrigJetMet = cms.PSet(
    triggers = triggersJetMet,
    name = cms.string("PreSelectionPMissingPionIdWithTrigJetMet"),
    cuts = copy.deepcopy(PreSelectionPMissingWithTrigJetMet.cuts),
    )
PreSelectionPMissingPionIdWithTrigJetMet.cuts.append(cutTrkPionId)


PreSelectionPMissingNotGenMatched = cms.PSet(
    name = cms.string("PreSelectionPMissingNotGenMatched"),
    cuts = copy.deepcopy(PreSelectionPMissing.cuts),
    )
PreSelectionPMissingNotGenMatched.cuts.append(cutTrkNotGenMatched)


PreSelectionPMissingLtMesonId = cms.PSet(
    name = cms.string("PreSelectionPMissingLtMesonId"),
    cuts = copy.deepcopy(PreSelectionPMissing.cuts),
    )
PreSelectionPMissingLtMesonId.cuts.append(cutTrkLightMesonId)


PreSelectionPMissingKMesonId = cms.PSet(
    name = cms.string("PreSelectionPMissingKMesonId"),
    cuts = copy.deepcopy(PreSelectionPMissing.cuts),
    )
PreSelectionPMissingKMesonId.cuts.append(cutTrkKMesonId)


PreSelectionPMissingLtBaryonId = cms.PSet(
    name = cms.string("PreSelectionPMissingLtBaryonId"),
    cuts = copy.deepcopy(PreSelectionPMissing.cuts),
    )
PreSelectionPMissingLtBaryonId.cuts.append(cutTrkLightBaryonId)


PreSelectionPMissingKBaryonId = cms.PSet(
    name = cms.string("PreSelectionPMissingKBaryonId"),
    cuts = copy.deepcopy(PreSelectionPMissing.cuts),
    )
PreSelectionPMissingKBaryonId.cuts.append(cutTrkKBaryonId)


## Signal Region Channels ##

SigRegWithMaxCaloByPLoose = cms.PSet(
    name = cms.string("SigRegWithMaxCaloByPLoose"),
    cuts = copy.deepcopy(PreSelectionPMissing.cuts),
    )
SigRegWithMaxCaloByPLoose.cuts.append(cutMaxCaloByPLoose)


SigRegWithMaxCaloByPLooseWithTrigJetMet = cms.PSet(
    triggers = triggersJetMet,
    name = cms.string("SigRegWithMaxCaloByPLooseWithTrigJetMet"),
    cuts = copy.deepcopy(PreSelectionPMissingWithTrigJetMet.cuts),
    )
SigRegWithMaxCaloByPLooseWithTrigJetMet.cuts.append(cutMaxCaloByPLoose)


SigRegWithMaxCaloByP = cms.PSet(
    name = cms.string("SigRegWithMaxCaloByP"),
    cuts = copy.deepcopy(PreSelectionPMissing.cuts),
    )
SigRegWithMaxCaloByP.cuts.append(cutMaxCaloByP)


SigRegWithMaxCalo = cms.PSet(
    name = cms.string("SigRegWithMaxCalo"),
    cuts = copy.deepcopy(PreSelectionPMissing.cuts),
)
SigRegWithMaxCalo.cuts.append(cutMaxCaloTight)

PreSelWithMaxCalo = cms.PSet(
    name = cms.string("PreSelWithMaxCalo"),
    cuts = copy.deepcopy(PreSelection.cuts),
)
PreSelWithMaxCalo.cuts.append(cutMaxCaloTight) 
#PreSelWithMaxCalo.cuts.append(cutMaxMissOut)  # for data only


SigRegWithMaxCaloLoose = cms.PSet(
    name = cms.string("SigRegWithMaxCaloLoose"),
    cuts = copy.deepcopy(PreSelectionPMissing.cuts),
    )
SigRegWithMaxCaloLoose.cuts.append(cutMaxCaloLoose)


SigRegWithMaxCaloLooseWithTrigJetMet = cms.PSet(
    triggers = triggersJetMet,
    name = cms.string("SigRegWithMaxCaloLooseWithTrigJetMet"),
    cuts = copy.deepcopy(PreSelectionPMissingWithTrigJetMet.cuts),
    )
SigRegWithMaxCaloLooseWithTrigJetMet.cuts.append(cutMaxCaloLoose)


SigRegNominal = cms.PSet(
    name = cms.string("SigRegNominal"),
    cuts = copy.deepcopy(PreSelectionPMissing.cuts),
    )
SigRegNominal.cuts.append(cutMaxCalo10) 
SigRegNominal.cuts.append(cutTrkWheel0GapVeto) 
SigRegNominal.cuts.append(cutTrkEtaMuonPk)  

SigRegWithMaxCaloPUCorr = cms.PSet(
    name = cms.string("SigRegWithMaxCaloPUCorr"),
    cuts = copy.deepcopy(PreSelectionPMissing.cuts),
    )
SigRegWithMaxCaloPUCorr.cuts.append(cutMaxCalo10)

SigRegWithMaxCaloPUCorrNoiseCleaned = cms.PSet(
    triggers = triggersJetMet,
    name = cms.string("SigRegWithMaxCaloPUCorrNoiseCleaned"),
    cuts = copy.deepcopy(PreSelectionWithNoiseClean.cuts),
    )
SigRegWithMaxCaloPUCorrNoiseCleaned.cuts.append(cutTrkSumPtLT)
SigRegWithMaxCaloPUCorrNoiseCleaned.cuts.append(cutTrkHitMissOut)
SigRegWithMaxCaloPUCorrNoiseCleaned.cuts.append(cutMaxCaloPUCorr)

SigRegWithMaxCaloPUCorrAndSumPtLessThan = cms.PSet(
    name = cms.string("SigRegWithMaxCaloPUCorrAndSumPtLessThan"),
    cuts = copy.deepcopy(PreSelectionPMissing.cuts),
    )
SigRegWithMaxCaloPUCorrAndSumPtLessThan.cuts.append(cutTrkSumPtLT)
SigRegWithMaxCaloPUCorrAndSumPtLessThan.cuts.append(cutMaxCaloPUCorr)

SigRegWithMaxCaloPUCorrWithTrigJetMet = cms.PSet(
    triggers = triggersJetMet,
    name = cms.string("SigRegWithMaxCaloPUCorrWithTrigJetMet"),
    cuts = copy.deepcopy(PreSelectionPMissingWithTrigJetMet.cuts),
    )
SigRegWithMaxCaloPUCorrWithTrigJetMet.cuts.append(cutMaxCaloPUCorr)

SigRegWithMaxCaloPUCorrAndSumPtLessThanWithTrigJetMet = cms.PSet(
    triggers = triggersJetMet,
    name = cms.string("SigRegWithMaxCaloPUCorAndSumPtLessThanWithTrigJetMet"),
    cuts = copy.deepcopy(PreSelectionPMissingWithTrigJetMet.cuts),
    )
SigRegWithMaxCaloPUCorrAndSumPtLessThanWithTrigJetMet.cuts.append(cutTrkSumPtLT)
SigRegWithMaxCaloPUCorrAndSumPtLessThanWithTrigJetMet.cuts.append(cutMaxCaloPUCorr)


## Control Region Channels ##
CtrlReg = cms.PSet(
    name = cms.string("CtrlReg"),
    cuts = copy.deepcopy(PreSelection.cuts),
    )
CtrlReg.cuts.append(cutTrkHitMissOutCtrlReg)


CtrlRegWithTrigJetMet = cms.PSet(
    name = cms.string("CtrlRegWithTrigJetMet"),
    cuts = copy.deepcopy(PreSelectionWithTrigJetMet.cuts),
    )
CtrlRegWithTrigJetMet.cuts.append(cutTrkHitMissOutCtrlReg)


JetFirst = cms.PSet(
    name = cms.string("JetFirst"),
    triggers = triggersJetMet,
    cuts = cms.VPSet (
        cutJetPt,
        cutMET,
        )
    )

MetFirst = cms.PSet(
    name = cms.string("MetFirst"),
    triggers = triggersJetMet,
    cuts = cms.VPSet (
        cutMET,
        cutJetPt,
        )
    )

TrigTestTighterMet = cms.PSet(
    name = cms.string("TrigTestTighterMet"),
    triggers = triggersJetMet,
    cuts = cms.VPSet (
        cms.PSet (
            inputCollection = cms.string("mets"),
            cutString = cms.string("pt > 250"),
            numberRequired = cms.string(">= 1"),
            ),
        cutJetPt,
        )
    )

TrigTestTighterJet = cms.PSet(
    name = cms.string("TrigTestTighterJet"),
    triggers = triggersJetMet,
    cuts = cms.VPSet (
        cutMET,
        cms.PSet (
            inputCollection = cms.string("jets"),
            cutString = cms.string("pt > 180"),
            numberRequired = cms.string(">= 1"),
            ),
        )
    )


JetOnly = cms.PSet(
    name = cms.string("JetOnly"),
    triggers = triggersJetMet,
    cuts = cms.VPSet (
        cutMET,
        cutJetPt,
        cutJetEta,
        cutJetNoiseChgHad,
        cutJetNoiseNeuEM,
        cutJetNoiseNeuHad,
       ),
    )

JetOnlyNoClean = cms.PSet(
    name = cms.string("JetOnlyNoClean"),
    triggers = triggersJetMet,
    cuts = cms.VPSet (
        cutMET,
        cutJetPt,
        cutJetEta,
       ),
    )


# Monojet selection #  
MonoJet = cms.PSet(
    name = cms.string("MonoJet"),
    triggers = triggersJetMet,
    cuts = cms.VPSet (
#        cutMET200,
        cutMET,
        cutSecJetPt,
        cutSecJetEta2p4,            
        cutSecJetNoiseChgHad,
        cutSecJetNoiseChgEM,
        cutSecJetNoiseNeuHad,
        cutSecJetNoiseNeuEM,
#        cutJetPt,
#        cutJetEta2p4,
#        cutJetNoiseChgHad,
#        cutJetNoiseChgEM,
#        cutJetNoiseNeuEM,
#        cutJetNoiseChgEM,
#        cutLeadingJetID,
        cutSubLeadingJetID,
        cutNJets,
        cutJetJetDPhi,
        cutElecLooseIDVeto,
        cutMuonLooseIDVeto,
        cutTauLooseHadronicVeto,
        cutTrkPt,
        cutTrkEta,
        cutTrkD0,
        cutTrkDZ,
        cutTrkNHits,
        cutTrkHitMissMid,
        cutTrkHitMissIn,
#        cutTrkIso,
        cutTrkDeadEcalVeto,
        cutTrkCrackVeto,
#        cutSecJetNoiseChgHad,
#        cutSecJetNoiseChgEM,
#        cutSecJetNoiseNeuHad,
#        cutSecJetNoiseNeuEM,
#        cutSecJetPt,
#        cutSecJetEta2p4,
#        cutNJets,
#        cutJetJetDPhi,
#        cutMuonVeto,
#        cutElecVeto,
#        cutTauVeto,
       ),
    )

# Modified Monojet selection #  
MonoJetNoNJetVeto = cms.PSet(
    name = cms.string("MonoJetNoNJetVeto"),
    triggers = triggersJetMet,
    cuts = cms.VPSet (
        cutMET,
        cutSecJetPt,
        cutSecJetEta2p4,            
        cutSecJetNoiseChgHad,
        cutSecJetNoiseChgEM,
        cutSecJetNoiseNeuHad,
        cutSecJetNoiseNeuEM,
        cutSubLeadingJetID,
#        cutNJets,
        cutJetJetDPhi,
        cutElecLooseIDVeto,
        cutMuonLooseIDVeto,
        cutTauLooseHadronicVeto,
        cutTrkPt,
        cutTrkEta,
        cutTrkD0,
        cutTrkDZ,
        cutTrkNHits,
        cutTrkHitMissMid,
        cutTrkHitMissIn,
#        cutTrkIso,
        cutTrkDeadEcalVeto,
        cutTrkCrackVeto,
       ),
    )

# Modified Monojet selection #  
MonoJetNoSubjetCuts = cms.PSet(
    name = cms.string("MonoJetNoSubjetCuts"),  
    triggers = triggersJetMet,
    cuts = cms.VPSet (
        cutMET,
        cutSecJetPt,
        cutSecJetEta2p4,            
        cutSecJetNoiseChgHad,
        cutSecJetNoiseChgEM,
        cutSecJetNoiseNeuHad,
        cutSecJetNoiseNeuEM,
        cutSubLeadingJetID,
#        cutNJets,
#        cutJetJetDPhi,
        cutElecLooseIDVeto,
        cutMuonLooseIDVeto,
        cutTauLooseHadronicVeto,
        cutTrkPt,
        cutTrkEta,
        cutTrkD0,
        cutTrkDZ,
        cutTrkNHits,
        cutTrkHitMissMid,
        cutTrkHitMissIn,
#        cutTrkIso,
        cutTrkDeadEcalVeto,
        cutTrkCrackVeto,
       ),
    )


AtlasDisappTrk = cms.PSet(
    # Copy cuts from arXiv:1210.2852v1, JHEP 01 (2013) 131
    # and PRD 88, 112006 (2013)  
    name = cms.string("AtlasDisappTrk"),
    # Do not apply a trigger  
    cuts = cms.VPSet (
        cutEvtFilter,
        cutVtxGood, 
        cutSecJetEta2p8,
        cutSecJetNoiseChgHad,
        cutSecJetNoiseChgEM,
        cutSecJetNoiseNeuHad,
        cutSecJetNoiseNeuEM,
        cutElecVetoPt10, 
        cutMuonVetoPt10,
        cutSecMuonVetoPt10,
        cutSecJetPt90,
        cutMET90,
        cutMetDeltaPhiMin2Jets, 
        cutTrkPt15,
        # Missing:  highest-pt isolated track 
        cutTrkEtaAtlas,
        # Missing:  N_b-layer >= 1
        # Missing:  N_pixel >= 3
        # Missing:  N_SCT >= 2
        cutTrkNHits,
        cutTrkHitMissIn,
        cutTrkHitMissMid,
        cutTrkD0Atlas,
        cutTrkDZSinTheta,
        # Missing:  track chi2 prob > 10%  
        cutTrkChi2Norm1p6,
        #        cutTrkPtError,
        cutTrkRelIsoRp3Atlas, 
        cutTrkJetDeltaRAtlas,
        cutTrkDeadEcalVeto, 
        cutTrkHitMissOut,
        cutTrkPt75, 
       )  
    )

AtlasDisappTrkUptoMet = cms.PSet(
    name = cms.string("AtlasDisappTrkUptoMet"),
    cuts = copy.deepcopy(AtlasDisappTrk.cuts),
    )
# remove the cuts after the Met cut
for i in range(0, len(AtlasDisappTrkUptoMet.cuts)):  
    if AtlasDisappTrkUptoMet.cuts[i].cutString == cutMET90.cutString:
        idx = i
del AtlasDisappTrkUptoMet.cuts[idx+1:len(AtlasDisappTrkUptoMet.cuts)]  

AtlasDisappTrkIsoTrk = cms.PSet(
    name = cms.string("AtlasDisappTrkIsoTrk"),
    cuts = copy.deepcopy(AtlasDisappTrk.cuts),
    )
# remove the last two cuts 
del AtlasDisappTrkIsoTrk.cuts[len(AtlasDisappTrkIsoTrk.cuts)-1]
del AtlasDisappTrkIsoTrk.cuts[len(AtlasDisappTrkIsoTrk.cuts)-1]


AtlasDisappTrkIsoTrkMissOut3 = cms.PSet(
    name = cms.string("AtlasDisappTrkIsoTrkMissOut3"),
    cuts = copy.deepcopy(AtlasDisappTrkIsoTrk.cuts),
    )
AtlasDisappTrkIsoTrkMissOut3.cuts.append(cutTrkHitMissOut) 

AtlasDisappTrkIsoTrkMissOut6 = cms.PSet(
    name = cms.string("AtlasDisappTrkIsoTrkMissOut6"),
    cuts = copy.deepcopy(AtlasDisappTrkIsoTrk.cuts),
    )
AtlasDisappTrkIsoTrkMissOut6.cuts.append(cutTrkHitMissOut6) 

AtlasDisappTrkIsoTrkMissOut7 = cms.PSet(
    name = cms.string("AtlasDisappTrkIsoTrkMissOut7"),
    cuts = copy.deepcopy(AtlasDisappTrkIsoTrk.cuts),
    )
AtlasDisappTrkIsoTrkMissOut7.cuts.append(cutTrkHitMissOut7) 

AtlasDisappTrkIsoTrkMissOut8 = cms.PSet(
    name = cms.string("AtlasDisappTrkIsoTrkMissOut8"),
    cuts = copy.deepcopy(AtlasDisappTrkIsoTrk.cuts),
    )
AtlasDisappTrkIsoTrkMissOut8.cuts.append(cutTrkHitMissOut8) 

## AtlasDisappTrkIsoTrkDeadEcal = cms.PSet(
##     name = cms.string("AtlasDisappTrkIsoTrkDeadEcal"),
##     cuts = copy.deepcopy(AtlasDisappTrkIsoTrk.cuts),
##     )
## AtlasDisappTrkIsoTrkDeadEcal.cuts.append(cutTrkDeadEcalVeto)  

AtlasDisappTrkTrigMet = cms.PSet(
    name = cms.string("AtlasDisappTrkTrigMet"),
    triggers = triggersJetMet,
    cuts = copy.deepcopy(AtlasDisappTrk.cuts),
    )
AtlasDisappTrkTrigMet.cuts.append(cutMET)  

AtlasDisappTrkDeadEcal = cms.PSet(
    name = cms.string("AtlasDisappTrkDeadEcal"),
    cuts = copy.deepcopy(AtlasDisappTrk.cuts),
    )
AtlasDisappTrkDeadEcal.cuts.append(cutTrkDeadEcalVeto)  

AtlasDisappTrkDeadEcalMuonCuts = cms.PSet(
    name = cms.string("AtlasDisappTrkDeadEcalMuonCuts"),
    cuts = copy.deepcopy(AtlasDisappTrkDeadEcal.cuts),
    )
AtlasDisappTrkDeadEcalMuonCuts.cuts.append(cutSecMuonVetoPt10)
AtlasDisappTrkDeadEcalMuonCuts.cuts.append(cutTrkWheel0GapVeto)
AtlasDisappTrkDeadEcalMuonCuts.cuts.append(cutTrkEtaMuonPk)
AtlasDisappTrkDeadEcalMuonCuts.cuts.append(cutTrkBadCSCVeto)  

AtlasDisappTrkDeadEcalSecMuonVeto = cms.PSet(
    name = cms.string("AtlasDisappTrkDeadEcalSecMuonVeto"),
    cuts = copy.deepcopy(AtlasDisappTrkDeadEcal.cuts),
    )
AtlasDisappTrkDeadEcalSecMuonVeto.cuts.append(cutSecMuonVetoPt10)

AtlasDisappTrkDeadEcalSecMuonVetoEcalo = cms.PSet(
    name = cms.string("AtlasDisappTrkDeadEcalSecMuonVetoEcalo"),
    cuts = copy.deepcopy(AtlasDisappTrkDeadEcalSecMuonVeto.cuts),
    )
AtlasDisappTrkDeadEcalSecMuonVetoEcalo.cuts.append(cutMaxCalo10)

AtlasDisappTrkDeadEcalEtaVeto = cms.PSet(
    name = cms.string("AtlasDisappTrkDeadEcalEtaVeto"),
    cuts = copy.deepcopy(AtlasDisappTrkDeadEcal.cuts),
    )
AtlasDisappTrkDeadEcalEtaVeto.cuts.append(cutTrkEtaAtlasVeto)  

AtlasDisappTrkCharginoId = cms.PSet(
    name = cms.string("AtlasDisappTrkCharginoId"),
    cuts = copy.deepcopy(AtlasDisappTrk.cuts),
    )
AtlasDisappTrkCharginoId.cuts.insert(8,cutTrkCharginoId)  

AtlasDisappTrkCharginoIdTrigMet = cms.PSet(
    # add trigger and Met cut 
    name = cms.string("AtlasDisappTrkCharginoIdTrigMet"),
    triggers = triggersJetMet,
    cuts = copy.deepcopy(AtlasDisappTrk.cuts),
    )
AtlasDisappTrkCharginoIdTrigMet.cuts.append(cutMET)  





