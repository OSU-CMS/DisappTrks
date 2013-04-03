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

# Selection of control samples

triggersSingleElec = cms.vstring()

## # FIXME:  Need to figure out why no events seem to pass these triggers.  
## triggersSingleElec = cms.vstring(
##     # Choose triggers by going to http://j2eeps.cern.ch/cms-project-confdb-hltdev/browser/
##     # Select online/2012/8e33/v2.1.
##     # Take all the single electron triggers than are unprescaled and do not have extra strange requirements.
##     "HLT_Ele24_WP80_CentralPFJet35_CentralPFJet25_PFMET20_v1",
##     "HLT_Ele24_WP80_CentralPFJet35_CentralPFJet25_v1",
##     "HLT_Ele24_WP80_PFJet30_PFJet25_Deta3_CentralPFJet30_v1",
##     "HLT_Ele24_WP80_PFJet30_PFJet25_Deta3_v1",
##     "HLT_Ele25_CaloIdVT_CaloIsoT_TrkIdT_TrkIsoT_CentralPFNoPUJet30_BTagIPIter_v9",
##     "HLT_Ele27_WP80_CentralPFJet80_v9",
##     "HLT_Ele27_WP80_PFMET_MT50_v7",
##     "HLT_Ele27_WP80_WCandPt80_v9",
##     "HLT_Ele27_WP80_v11",
##     )



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
        cutString = cms.string("numberOfValidMuonHits > 0"),
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


ZtoMuTau = cms.PSet(
    name = cms.string("ZtoMuTau"),
    cuts = cms.VPSet (
    cms.PSet (
        inputCollection = cms.string("taus"),
        cutString = cms.string("abs(eta) < 2.5"),
        numberRequired = cms.string(">= 1")
        ),
    cms.PSet (
        inputCollection = cms.string("taus"),
        cutString = cms.string("pt > 25"),
        numberRequired = cms.string(">= 1")
        ),
    cms.PSet (
        inputCollection = cms.string("muons"),
        cutString = cms.string("abs(eta) < 2.5"),
        numberRequired = cms.string(">= 1")
        ),
    cms.PSet (
        inputCollection = cms.string("muons"),
        cutString = cms.string("pt > 25"),
        numberRequired = cms.string(">= 1")
        ),
    cms.PSet (
        inputCollection = cms.string("muons"),
        cutString = cms.string("numberOfValidMuonHits > 0"),
        numberRequired = cms.string(">= 1")
        ),
    cms.PSet (
        inputCollection = cms.string("muons"),
        cutString = cms.string("relPFdBetaIso < 0.12"),
        numberRequired = cms.string(">= 1")
        ),
    cms.PSet (
        inputCollection = cms.string("muon-tau pairs"),
        cutString = cms.string("invMass > 40 & invMass < 160"),
       numberRequired = cms.string(">= 1")
        ),
    
    )
    )




ZtoEE = cms.PSet(
    name = cms.string("ZtoEE"),
    triggers = triggersSingleElec, 
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

ZtoEEPreSel = cms.PSet(
     name = cms.string("ZtoEEPreSel"),
     triggers = triggersSingleElec, 
     cuts = cms.VPSet(
     cms.PSet(
         inputCollection = cms.string("electrons"),
         cutString = cms.string("pt > 20"),
         numberRequired = cms.string(">= 2"),
         alias = cms.string("electron pT > 20 GeV")
         ),
     cms.PSet(
         inputCollection= cms.string("electrons"),
         cutString = cms.string("fabs(eta) < 2.1"),
         numberRequired = cms.string(">= 2"),
         alias =cms.string("|eta| < 2.1")
        ),
     cms.PSet(
         inputCollection= cms.string("electrons"),
         cutString = cms.string("fabs(correctedD0Vertex) < 0.01"),
         numberRequired = cms.string(">= 2"),
         alias =cms.string("|d0| < 0.05 cm")
         ),
     cms.PSet(
         inputCollection= cms.string("electrons"),
         cutString = cms.string("fabs(correctedDZ) < 0.01"),
         numberRequired = cms.string(">= 2"),
         alias =cms.string("|dZ| < 0.05 cm")
         ),
     cms.PSet(
         inputCollection= cms.string("electrons"),
         cutString = cms.string("tkNumValidHits > 4"),
         numberRequired = cms.string(">= 2"),
         alias =cms.string("Valid Hits > 4")
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
     )
     )

ZtoETrack = cms.PSet(
    name = cms.string("ZtoETrack"),
    triggers = copy.deepcopy(triggersSingleElec), 
    cuts = cms.VPSet(
        cms.PSet(
            inputCollection = cms.string("electrons"),
            cutString = cms.string("pt > 20"),
            numberRequired = cms.string(">= 1"),
            alias = cms.string("(e) pT > 20 GeV")
            ),
        cms.PSet(
            inputCollection= cms.string("electrons"),
            cutString = cms.string("fabs(eta) < 2.1"),
            numberRequired = cms.string(">= 1"),
            alias =cms.string("(e) |eta| < 2.1")
            ),
        cms.PSet(
            inputCollection= cms.string("electrons"),
            cutString = cms.string("fabs(correctedD0Vertex) < 0.01"),
            numberRequired = cms.string(">= 1"),
            alias =cms.string("(e) |d0| < 0.01 cm")
            ),
        cms.PSet(
            inputCollection= cms.string("electrons"),
            cutString = cms.string("fabs(correctedDZ) < 0.01"),
            numberRequired = cms.string(">= 1"),
            alias =cms.string("(e) |dZ| < 0.01 cm")
            ),
        cms.PSet(
             inputCollection= cms.string("electrons"),
             cutString = cms.string("tkNumValidHits > 4"),
             numberRequired = cms.string(">= 1"),
             alias =cms.string("(e) Valid Hits > 4")
             ),
        cms.PSet(
             inputCollection = cms.string("tracks"),
             cutString = cms.string("pt > 20"),
             numberRequired = cms.string(">= 1"),
             alias = cms.string("(t) pT > 20 GeV")
             ),
        cms.PSet(
             inputCollection= cms.string("tracks"),
             cutString = cms.string("fabs(eta) < 2.1"),
             numberRequired = cms.string(">= 1"),
             alias =cms.string("(t) |eta| < 2.1")
             ),
        cms.PSet(
             inputCollection= cms.string("tracks"),
             cutString = cms.string("fabs(d0wrtPV) < 0.01"),
             numberRequired = cms.string(">= 1"),
             alias =cms.string("(t) |d0| < 0.01 cm")
             ),
        cms.PSet(
             inputCollection= cms.string("tracks"),
             cutString = cms.string("fabs(dZwrtPV) < 0.01"),
             numberRequired = cms.string(">= 1"),
             alias =cms.string("(t) |dZ| < 0.01 cm")
             ),
         cms.PSet(
             inputCollection= cms.string("tracks"),
             cutString = cms.string("numValidHits > 4"),
             numberRequired = cms.string(">= 1"),
             alias =cms.string("(t) Valid Hits > 4")
             ),
        cms.PSet (
            inputCollection = cms.string("tracks"),
            cutString = cms.string("nHitsMissingMiddle == 0"),
            numberRequired = cms.string(">= 1"),
            alias = cms.string("Missing Middle Hits = 0")
            ),
        cms.PSet (
            inputCollection = cms.string("tracks"),
            cutString = cms.string("nHitsMissingInner == 0"),
            numberRequired = cms.string(">= 1"),
            alias = cms.string("Missing Inner Hits = 0")
            ),
        cms.PSet (
            inputCollection = cms.string("tracks"),
            cutString = cms.string("isIso == 1"),
            numberRequired = cms.string(">= 1"),
            alias = cms.string("Track Isolation")
            ),
        
         cms.PSet(
             inputCollection= cms.string("muons"),
             cutString = cms.string("pt > -1"),
             numberRequired = cms.string("= 0"),
             alias =cms.string("Muon Veto")
             ),
          
         )
         )

ZtoETrackPreSel = cms.PSet(
    name = cms.string("ZtoETrackPreSel"),
    triggers = copy.deepcopy(triggersSingleElec), 
    cuts = copy.deepcopy(ZtoETrack.cuts)
    )

cutETrackInvMass = cms.PSet(
    inputCollection = cms.string("electron-track pairs"),
    cutString = cms.string("invMass > 40 & invMass < 160"),
    numberRequired = cms.string(">= 1")
    )
ZtoETrackPreSel.cuts.append(cutETrackInvMass)

ZtoETrackFullPreSel = cms.PSet(
    name = cms.string("ZtoETrackFullPreSel"),
    triggers = triggersSingleElec, 
    cuts = copy.deepcopy(ZtoETrack.cuts)
    )

ElectronVetoOneMax =   cms.PSet (
        inputCollection = cms.string("electrons"),
        cutString = cms.string("pt > -1"),
        numberRequired = cms.string("<= 1"),  # Require no more than one electron in event (since one elec is already selected).  
        alias = cms.string("Electron Veto")
        )

ElectronVetoAll =   cms.PSet (
        inputCollection = cms.string("electrons"),
        cutString = cms.string("pt > -1"),
        numberRequired = cms.string("= 0"),  # Require no electron in event.  
        alias = cms.string("Electron Veto")
        )

deadEcalVeto =  cms.PSet (
        inputCollection = cms.string("tracks"),
        cutString = cms.string("isMatchedDeadEcal == 0"),
        numberRequired = cms.string(">= 1"),
        alias = cms.string("deadEcal Veto")
        )

crackVeto =    cms.PSet (
        inputCollection = cms.string("tracks"),
        cutString = cms.string("fabs(eta) < 1.42 | fabs(eta) > 1.65"),
        numberRequired = cms.string(">= 1"),
        alias = cms.string("Crack Veto")
        )   
 
ZtoETrackFullPreSel.cuts.append(ElectronVetoOneMax)  
ZtoETrackFullPreSel.cuts.append(deadEcalVeto)  
ZtoETrackFullPreSel.cuts.append(crackVeto)
ZtoETrackFullPreSel.cuts.append(cutETrackInvMass)


#####For Pions#####
ZtoTauTau = cms.PSet(
    name = cms.string("ZtoTauTau"),
    cuts = cms.VPSet (
    cms.PSet (
        inputCollection = cms.string("taus"),
        cutString = cms.string("pt > 20"),
        numberRequired = cms.string(">= 2"),
        alias = cms.string("pT > 20 GeV")
                            ),
    cms.PSet (
        inputCollection = cms.string("taus"),
        cutString = cms.string("fabs(eta) < 2.1"),
        numberRequired = cms.string(">= 2"),
        alias = cms.string("|eta| < 2.1")
        ),
    cms.PSet (
        inputCollection = cms.string("tau-tau pairs"),
        cutString = cms.string("invMass > 40 & invMass < 160"),
        numberRequired = cms.string(">= 1")
        ),
    )  # end cuts = cms.VPSet (
    ) # end ZtoEE = cms.PSet(         

ZtoMuTrack = cms.PSet(
    name = cms.string("ZtoMuTrack"),
    cuts = cms.VPSet(
    cms.PSet(
        inputCollection = cms.string("muons"),
        cutString = cms.string("pt > 20"),
        numberRequired = cms.string(">= 1"),
        alias = cms.string("(m) pT > 20 GeV")
        ),
    
    cms.PSet(
        inputCollection= cms.string("muons"),
        cutString = cms.string("fabs(eta) < 2.1"),
        numberRequired = cms.string(">= 1"),
        alias =cms.string("(m) |eta| < 2.1")
        ),
    cms.PSet(
        inputCollection= cms.string("muons"),
        cutString = cms.string("fabs(correctedD0Vertex) < 0.01"),
        numberRequired = cms.string(">= 1"),
        alias =cms.string("(m) |d0| < 0.01 cm")
        ),
    
    cms.PSet(
        inputCollection= cms.string("muons"),
        cutString = cms.string("fabs(correctedDZ) < 0.01"),
        numberRequired = cms.string(">= 1"),
        alias =cms.string("(m) |dZ| < 0.01 cm")
        ),
    cms.PSet (
        inputCollection = cms.string("muons"),
        cutString = cms.string("numberOfValidMuonHits > 0"),
        numberRequired = cms.string(">= 1"),
        alias = cms.string("Muon Stations > 0")
        ),
    cms.PSet (
        inputCollection = cms.string("muons"),
        cutString = cms.string("relPFdBetaIso < 0.12"),
        numberRequired = cms.string(">= 1")
        ),
    cms.PSet(
        inputCollection= cms.string("muons"),
        cutString = cms.string("tkNumValidHits > 4"),
        numberRequired = cms.string(">= 1"),
        alias =cms.string("(m) Valid Hits > 4")
        ),
    cms.PSet(
        inputCollection = cms.string("tracks"),
        cutString = cms.string("pt > 20"),
        numberRequired = cms.string(">= 1"),
        alias = cms.string("(t) pT > 20 GeV")
        ),
    cms.PSet(
        inputCollection= cms.string("tracks"),
        cutString = cms.string("fabs(eta) < 2.1"),
        numberRequired = cms.string(">= 1"),
        alias =cms.string("(t) |eta| < 2.1")
        ),
    cms.PSet(
        inputCollection= cms.string("tracks"),
        cutString = cms.string("fabs(d0wrtPV) < 0.01"),
        numberRequired = cms.string(">= 1"),
        alias =cms.string("(t) |d0| < 0.01 cm")
        ),
    cms.PSet(
        inputCollection= cms.string("tracks"),
        cutString = cms.string("fabs(dZwrtPV) < 0.01"),
        numberRequired = cms.string(">= 1"),
        alias =cms.string("(t) |dZ| < 0.01 cm")
        ),
    cms.PSet(
         inputCollection= cms.string("tracks"),
         cutString = cms.string("numValidHits > 4"),
         numberRequired = cms.string(">= 1"),
         alias =cms.string("(t) Valid Hits > 4")
         ),
    cms.PSet (
        inputCollection = cms.string("tracks"),
        cutString = cms.string("nHitsMissingMiddle == 0"),
        numberRequired = cms.string(">= 1"),
        alias = cms.string("Missing Middle Hits = 0")
        ),
    cms.PSet (
        inputCollection = cms.string("tracks"),
        cutString = cms.string("nHitsMissingInner == 0"),
        numberRequired = cms.string(">= 1"),
        alias = cms.string("Missing Inner Hits = 0")
        ),
    cms.PSet (
        inputCollection = cms.string("tracks"),
        cutString = cms.string("isIso == 1"),
        numberRequired = cms.string(">= 1"),
        alias = cms.string("Track Isolation")
        ),
    )
    )

ZtoMuTrackPreSel = cms.PSet(
    name = cms.string("ZtoMuTrackPreSel"),
    cuts = copy.deepcopy(ZtoMuTrack.cuts)
    )
cutMuTrackInvMass = cms.PSet(
    inputCollection = cms.string("muon-track pairs"),
    cutString = cms.string("invMass > 40 & invMass < 160"),
    numberRequired = cms.string(">= 1")
    )
ZtoMuTrackPreSel.cuts.append(cutMuTrackInvMass)

ZtoMuTrackFullPreSel = cms.PSet(
    name = cms.string("ZtoMuTrackFullPreSel"),
    cuts = copy.deepcopy(ZtoMuTrack.cuts)
    )
ZtoMuTrackFullPreSel.cuts.append(ElectronVetoAll)
ZtoMuTrackFullPreSel.cuts.append(deadEcalVeto)
ZtoMuTrackFullPreSel.cuts.append(crackVeto)
ZtoMuTrackFullPreSel.cuts.append(cutMuTrackInvMass)
