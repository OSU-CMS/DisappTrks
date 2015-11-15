import FWCore.ParameterSet.Config as cms
import copy


##############################
##### Constants          #####
##############################

mZPDG = 91.1876  # Z mass from http://pdglive.lbl.gov/DataBlock.action?node=S044M  


##############################
##### List of triggers   #####
##############################


triggersMet = cms.vstring(
        "HLT_MET75_IsoTrk50_v", # trigger designed for disappearing tracks
        "HLT_PFMETNoMu120_JetIdCleaned_PFMHTNoMu120_IDTight_v",  # monojet trigger in the data, unprescaled for all of 2015
        "HLT_PFMETNoMu120_NoiseCleaned_PFMHTNoMu120_IDTight_v",  # monojet trigger in the RunIISpring15DR74 MC samples

        #"HLT_PFMET120_PFMHT120_IDTight_v", # PFMET trigger in the data
        #"HLT_PFMET120_PFMHT120_IDLoose_v", # PFMET trigger in the RunIISpring15DR74 MC samples
        )

triggersSingleMu = cms.vstring(
    "HLT_IsoMu18_v",  # not available in bkgd MC
    "HLT_IsoMu20_v",  # yes available in bkgd MC
)

##########################
##### List of cuts   #####
##########################

##### List of valid input collections #####
# jets, muons, electrons, taus, photons, mets,
# events, tracks, primaryvertexs,
# genjets, mcparticles,
# bxlumis, superclusters 


##################################################
## primaryvertexs 
##################################################
cutGoodPV = cms.PSet (
    inputCollection = cms.vstring("primaryvertexs"),
    cutString = cms.string("isValid > 0 && ndof >= 4"),
    numberRequired = cms.string(">= 1")
)


##################################################
## mets
##################################################
cutMet = cms.PSet(
    inputCollection = cms.vstring("mets"),
    cutString = cms.string("pt > 100"),
    numberRequired = cms.string(">= 1"),
)


##################################################
## jets
##################################################
cutJetPt = cms.PSet(
    inputCollection = cms.vstring("jets"),
    cutString = cms.string("pt > 110"),
    numberRequired = cms.string(">= 1"),
) 
cutJetChgHad = cms.PSet(
    inputCollection = cms.vstring("jets"),
    cutString = cms.string("chargedHadronEnergyFraction > 0.2"),  
    numberRequired = cms.string(">= 1"),
) 
cutJetChgEm = cms.PSet(
    inputCollection = cms.vstring("jets"),
    cutString = cms.string("chargedEmEnergyFraction < 0.5"),  
    numberRequired = cms.string(">= 1"),
)  
cutJetNeuHad = cms.PSet(
    inputCollection = cms.vstring("jets"),
    cutString = cms.string("neutralHadronEnergyFraction < 0.7"),  
    numberRequired = cms.string(">= 1"),
) 
cutJetNeuEm = cms.PSet(
    inputCollection = cms.vstring("jets"),
    cutString = cms.string("neutralEmEnergyFraction < 0.7"),  
    numberRequired = cms.string(">= 1"),
) 


##################################################
## tracks
##################################################
cutTrkPt = cms.PSet(
    inputCollection = cms.vstring("tracks"),
    cutString = cms.string("pt > 50"),  
    numberRequired = cms.string(">= 1"),
) 
cutTrkEta = cms.PSet(
    inputCollection = cms.vstring("tracks"),
    cutString = cms.string("fabs ( eta ) < 2.1"),  
    numberRequired = cms.string(">= 1"),
) 
cutTrkEcalGapVeto = cms.PSet(  # BARREL-ENDCAP GAP VETO
    inputCollection = cms.vstring("tracks"),
    cutString = cms.string("fabs ( eta ) < 1.42 || fabs ( eta ) > 1.65"),  
    numberRequired = cms.string(">= 1"),
) 
cutTrkEtaMuonIneff1 = cms.PSet(        # TRACK ETA:  MUON INEFFICIENCY REGION 1
    inputCollection = cms.vstring("tracks"),
    cutString = cms.string("fabs ( eta ) < 0.15 || fabs ( eta ) > 0.35"),  
    numberRequired = cms.string(">= 1"),
) 
cutTrkEtaMuonIneff2 = cms.PSet(        # TRACK ETA:  MUON INEFFICIENCY REGION 2
    inputCollection = cms.vstring("tracks"),
    cutString = cms.string("fabs ( eta ) < 1.55 || fabs ( eta ) > 1.85"),  
    numberRequired = cms.string(">= 1"),
) 
# cutTrkEtaEcalCrackVeto = cms.PSet(  # TRACK ETA:  NOT IN ECAL CRACKS:  UPDATE CRACK BOUNDARIES
#     inputCollection = cms.vstring("tracks"),
#     cutString = cms.string("fabs ( eta ) "),  
#     numberRequired = cms.string(">= 1"),
# ) 
cutTrkNValidHits = cms.PSet( 
    inputCollection = cms.vstring("tracks"),
    cutString = cms.string("numberOfValidHits >= 7"),  
    numberRequired = cms.string(">= 1"),
) 
cutTrkNMissIn = cms.PSet(
    inputCollection = cms.vstring("tracks"),
    cutString = cms.string("missingInnerHits == 0"), 
    numberRequired = cms.string(">= 1"),
) 
cutTrkNMissMid = cms.PSet( 
    inputCollection = cms.vstring("tracks"),
    cutString = cms.string("missingMiddleHits == 0"), 
    numberRequired = cms.string(">= 1"),
) 
cutTrkIso = cms.PSet(
    inputCollection = cms.vstring("tracks"),
    cutString = cms.string(" ( trackIsoDRp3 / pt ) < 0.05"), 
    numberRequired = cms.string(">= 1"),
) 
cutTrkElecVeto = cms.PSet(
    inputCollection = cms.vstring("tracks"),
    cutString = cms.string("deltaRToClosestElectron > 0.15"), 
    numberRequired = cms.string(">= 1"),
) 
cutTrkMuonVeto = cms.PSet(
    inputCollection = cms.vstring("tracks"),
    cutString = cms.string("deltaRToClosestMuon > 0.15"), 
    numberRequired = cms.string(">= 1"),
) 
cutTrkTauVeto = cms.PSet(
    inputCollection = cms.vstring("tracks"),
    cutString = cms.string("deltaRToClosestTau > 0.15"), 
    numberRequired = cms.string(">= 1"),
) 
cutTrkEcalo = cms.PSet(
    inputCollection = cms.vstring("tracks"),
    cutString = cms.string("caloTotNoPUDRp5CentralCalo < 10"), 
    numberRequired = cms.string(">= 1"),
) 
cutTrkNMissOut = cms.PSet(
    inputCollection = cms.vstring("tracks"),
    cutString = cms.string("missingOuterHits >= 3"),  
    numberRequired = cms.string(">= 1"),
) 
cutTrkEcaloInv = cms.PSet(
    inputCollection = cms.vstring("tracks"),
    cutString = cms.string("caloTotNoPUDRp5CentralCalo > 10"), 
    numberRequired = cms.string(">= 1"),
) 
cutTrkNMissOutInv = cms.PSet(
    inputCollection = cms.vstring("tracks"),
    cutString = cms.string("missingOuterHits <= 2"),  
    numberRequired = cms.string(">= 1"),
) 


##################################################
## muons
##################################################
cutMuonPt20 = cms.PSet (
    inputCollection = cms.vstring("muons"),
    cutString = cms.string("pt > 20"),
    numberRequired = cms.string(">= 1"),
    )
cutMuonEta21 = cms.PSet (
    inputCollection = cms.vstring("muons"),
    cutString = cms.string("fabs(eta) < 2.1"),
    numberRequired = cms.string(">= 1"),
    )
cutMuonTightID = cms.PSet (  # Recommended by https://twiki.cern.ch/twiki/bin/view/CMS/SWGuideMuonIdRun2#Muon_Isolation
    inputCollection = cms.vstring("muons"),
    cutString = cms.string("isTightMuonWRTVtx > 0"),
    numberRequired = cms.string(">= 1"),
    )
cutMuonPFIso = cms.PSet (  # Get this from Bing 
    inputCollection = cms.vstring("muons"),
    cutString = cms.string("relPFdBetaIso < 0.12"),
    numberRequired = cms.string(">= 1"),
    )
cutMuonPairPt20 = cms.PSet (
    inputCollection = cms.vstring("muons"),
    cutString = cms.string("pt > 20"),
    numberRequired = cms.string("== 2"),
    )
cutMuonPairEta21 = cms.PSet (
    inputCollection = cms.vstring("muons"),
    cutString = cms.string("fabs(eta) < 2.1"),
    numberRequired = cms.string("== 2"),
    )
cutMuonPairTightID = cms.PSet (  
    inputCollection = cms.vstring("muons"),
    cutString = cms.string("isTightMuonWRTVtx > 0"),
    numberRequired = cms.string("== 2"),
    )


##################################################
## muon-muon pairs
##################################################
cutMuMuChargeProduct = cms.PSet(
    inputCollection = cms.vstring("muons", "muons"),  
    cutString = cms.string("muon.charge * muon.charge < 0"),  
    numberRequired = cms.string(">= 1"),
    )
cutMuMuInvMassZLo = cms.PSet(
    inputCollection = cms.vstring("muons", "muons"),  
    cutString = cms.string("invMass ( muon , muon ) > " + str(mZPDG) + " - 10"),  
    numberRequired = cms.string(">= 1"),
    )
cutMuMuInvMassZHi = cms.PSet(
    inputCollection = cms.vstring("muons", "muons"),  
    cutString = cms.string("invMass ( muon , muon ) < " + str(mZPDG) + " + 10"),  
    numberRequired = cms.string(">= 1"),
    )


##################################################
## muon-track pairs
##################################################
cutMuTrkDeltaR = cms.PSet(
    inputCollection = cms.vstring("muons", "tracks"),  
    cutString = cms.string("deltaR ( muon , track ) > 0.15"),
    numberRequired = cms.string(">= 1"),
    )
cutMuTrkInvMass80To100 = cms.PSet(
    inputCollection = cms.vstring("muons", "tracks"),  
    cutString = cms.string("invMass ( muon , track ) > 80 && invMass ( muon , track ) < 100"), 
    numberRequired = cms.string(">= 1"),
    )


##################################################
## Functions for adding, removing cuts  
##################################################
def addCuts(cutVPset, cutsToAdd):
    for cut in cutsToAdd:
        cutVPset.append(cut)  
        
def removeCuts(cutVPset, cutsToRemove):
    for i in xrange(len(cutVPset) - 1, -1, -1):  # iterate backwards to avoid error 
        for cut in cutsToRemove: 
            if cutVPset[i].cutString == cut.cutString:  
                del cutVPset[i]





