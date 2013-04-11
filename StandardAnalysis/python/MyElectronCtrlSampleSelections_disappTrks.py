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
triggersSingleElec = cms.vstring(
     # Choose triggers by going to http://j2eeps.cern.ch/cms-project-confdb-hltdev/browser/
     # Select online/2012/8e33/v2.1.
     # Take all the single electron triggers than are unprescaled and do not have extra strange requirements.
##      "HLT_Ele24_WP80_CentralPFJet35_CentralPFJet25_PFMET20_v",
##      "HLT_Ele24_WP80_CentralPFJet35_CentralPFJet25_v",
##      "HLT_Ele24_WP80_PFJet30_PFJet25_Deta3_CentralPFJet30_v",
##      "HLT_Ele24_WP80_PFJet30_PFJet25_Deta3_v",
##      "HLT_Ele25_CaloIdVT_CaloIsoT_TrkIdT_TrkIsoT_CentralPFNoPUJet30_BTagIPIter_v",
##      "HLT_Ele27_WP80_CentralPFJet80_v",
##      "HLT_Ele27_WP80_PFMET_MT50_v",
##     "HLT_Ele27_WP80_WCandPt80_v",
     "HLT_Ele27_WP80_v",
     )


ZtoEE = cms.PSet(
     name = cms.string("ZtoEE"),
     triggers = copy.deepcopy(triggersSingleElec), 
     cuts = cms.VPSet(
     cms.PSet(
         inputCollection = cms.string("electrons"),
         cutString = cms.string("pt > 20"),
         numberRequired = cms.string(">= 2"),
         alias = cms.string("electron pt > 20 GeV")
         ),
     cms.PSet(
         inputCollection= cms.string("electrons"),
         cutString = cms.string("fabs(eta) < 2.1"),
         numberRequired = cms.string(">= 2"),
         alias =cms.string("$|\eta|$ < 2.1")
        ),
     cms.PSet(
         inputCollection= cms.string("electrons"),
         cutString = cms.string("fabs(correctedD0Vertex) < 0.01"),
         numberRequired = cms.string(">= 2"),
         alias =cms.string("$|d_{0}|$ < 0.05 cm")
         ),
     cms.PSet(
         inputCollection= cms.string("electrons"),
         cutString = cms.string("fabs(correctedDZ) < 0.01"),
         numberRequired = cms.string(">= 2"),
         alias =cms.string("$|d_{z}|$ < 0.05 cm")
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
         alias = cms.string("Muons = 0")
         ),
     cms.PSet (
         inputCollection = cms.string("electron-electron pairs"),
         cutString = cms.string("invMass > 40 & invMass < 160"),
         numberRequired = cms.string(">= 1"),
         alias = cms.string("40 < InvMass(e+e) < 160")
         ),
     )
     )


ZtoETrack = cms.PSet(
    name = cms.string("ZtoETrack"),
#    triggers = copy.deepcopy(triggersSingleElec),
    cuts = cms.VPSet(
    cms.PSet(
        inputCollection = cms.string("electrons"),
        cutString = cms.string("pt > 20"),
        numberRequired = cms.string(">= 1"),
        alias = cms.string("(e) pt > 20 GeV")
        ),
    cms.PSet(
        inputCollection= cms.string("electrons"),
        cutString = cms.string("fabs(eta) < 2.1"),
        numberRequired = cms.string(">= 1"),
        alias =cms.string("(e) $|\eta|$ < 2.1")
        ),
    cms.PSet(
        inputCollection= cms.string("electrons"),
        cutString = cms.string("fabs(correctedD0Vertex) < 0.01"),
        numberRequired = cms.string(">= 1"),
        alias =cms.string("(e) $|d_{0}|$ < 0.01 cm")
        ),
    cms.PSet(
        inputCollection= cms.string("electrons"),
        cutString = cms.string("fabs(correctedDZ) < 0.01"),
        numberRequired = cms.string(">= 1"),
        alias =cms.string("(e) $|d_{z}|$ < 0.01 cm")
        ),
    cms.PSet(
        inputCollection= cms.string("electrons"),
        cutString = cms.string("mvaNonTrigV0 > 0.9"),
        numberRequired = cms.string(">= 1"),
        alias =cms.string("(e) mvaNonTrigV0 > 0.9")
        ),
    cms.PSet(
        inputCollection= cms.string("electrons"),
        cutString = cms.string("relPFrhoIso < 0.1"),
        numberRequired = cms.string(">= 1"),
        alias =cms.string("(e) Electron Iso  < 0.1")
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
        alias = cms.string("(t) pt > 20 GeV")
        ),
    cms.PSet(
        inputCollection= cms.string("tracks"),
        cutString = cms.string("fabs(eta) < 2.1"),
        numberRequired = cms.string(">= 1"),
        alias =cms.string("(t) $|\eta|$ < 2.1")
        ),
    cms.PSet(
        inputCollection= cms.string("tracks"),
        cutString = cms.string("fabs(d0wrtPV) < 0.01"),
        numberRequired = cms.string(">= 1"),
        alias =cms.string("(t) $|d_{0}|$ < 0.01 cm")
        ),
    cms.PSet(
        inputCollection = cms.string("tracks"),
        cutString = cms.string("pt > 20"),
        numberRequired = cms.string(">= 1"),
        alias = cms.string("(t) pt > 20 GeV")
        ),
    cms.PSet(
        inputCollection= cms.string("tracks"),
        cutString = cms.string("fabs(eta) < 2.1"),
        numberRequired = cms.string(">= 1"),
        alias =cms.string("(t) $|\eta|$ < 2.1")
        ),
    cms.PSet(
        inputCollection= cms.string("tracks"),
        cutString = cms.string("fabs(d0wrtPV) < 0.01"),
        numberRequired = cms.string(">= 1"),
        alias =cms.string("(t) $|d_{0}|$ < 0.01 cm")
        ),
    cms.PSet(
        inputCollection= cms.string("tracks"),
        cutString = cms.string("fabs(dZwrtPV) < 0.01"),
        numberRequired = cms.string(">= 1"),
        alias =cms.string("(t) $|d_{z}|$ < 0.01 cm")
        ),
    cms.PSet(
        inputCollection= cms.string("tracks"),
        cutString = cms.string("numValidHits > 4"),
        numberRequired = cms.string(">= 1"),
        alias =cms.string("(t) Valid Hits > 4")
        ),
    ##         cms.PSet (
    ##             inputCollection = cms.string("tracks"),
    ##             cutString = cms.string("nHitsMissingMiddle == 0"),
    ##             numberRequired = cms.string(">= 1"),
    ##             alias = cms.string("Missing Middle Hits = 0")
    ##             ),
    ##         cms.PSet (
    ##             inputCollection = cms.string("tracks"),
    ##             cutString = cms.string("nHitsMissingInner == 0"),
    ##             numberRequired = cms.string(">= 1"),
    ##             alias = cms.string("Missing Inner Hits = 0")
    ##            ),
    cms.PSet (
        inputCollection = cms.string("tracks"),
        cutString = cms.string("isIso == 1"),
        numberRequired = cms.string(">= 1"),
        alias = cms.string("Track Isolation")
        ),

    cms.PSet (
        inputCollection = cms.string("electron-track pairs"),
        cutString = cms.string("deltaR > 0.15"),
        numberRequired = cms.string(">= 1"),
        alias = cms.string("deltaRETrack > 0.15")
        ),

    cms.PSet(
        inputCollection= cms.string("muons"),
        cutString = cms.string("pt > -1"),
        numberRequired = cms.string("= 0"),
        alias =cms.string("Muons = 0")
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
    numberRequired = cms.string(">= 1"),
    alias = cms.string("40 < InvMass(e+t) < 160")
    )

ZtoETrackPreSel.cuts.append(cutETrackInvMass)

ZtoETrackFullPreSel = cms.PSet(
    name = cms.string("ZtoETrackFullPreSel"),
    triggers = copy.deepcopy(triggersSingleElec), 
    cuts = copy.deepcopy(ZtoETrack.cuts)
    )

ElectronVetoOneMax =   cms.PSet (
        inputCollection = cms.string("electrons"),
        cutString = cms.string("pt > -1"),
        numberRequired = cms.string("<= 1"),  # Require no more than one electron in event (since one elec is already selected).  
        alias = cms.string("Electrons = 1")
        )

ElectronVetoAll =   cms.PSet (
        inputCollection = cms.string("electrons"),
        cutString = cms.string("pt > -1"),
        numberRequired = cms.string("= 0"),  # Require no electron in event.  
        alias = cms.string("Electrons = 0")
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


