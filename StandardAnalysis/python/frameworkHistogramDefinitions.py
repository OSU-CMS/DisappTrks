import FWCore.ParameterSet.Config as cms
import os
from OSUT3Analysis.Configuration.pdgIdBins import *
from OSUT3Analysis.Configuration.cutUtilities import *

###############################################
##### Hold over from framework change     #####
##### copy/pasted from old file
###############################################


###############################################
##### Set up the histograms to be plotted #####
###############################################


##############################################################################################

MuonHistograms = cms.PSet(
    inputCollection = cms.vstring("muons"),
    histograms = cms.VPSet (
        cms.PSet (
            name = cms.string("numMuons"),
            title = cms.string("Number of Selected Muons;# muons"),
            binsX = cms.untracked.vdouble(10, 0, 10),
            inputVariables = cms.vstring("number(muon)"),
        ),
        cms.PSet (
            name = cms.string("muonPt"),
            title = cms.string("Muon Transverse Momentum;Muon p_{T} [GeV]"),
            binsX = cms.untracked.vdouble(500, 0, 500),
            inputVariables = cms.vstring("pt"),
        ),
        cms.PSet (
            name = cms.string("muonLeadingPt"),
            title = cms.string("Muon Transverse Momentum;Muon p_{T} [GeV]"),
            binsX = cms.untracked.vdouble(500, 0, 500),
            indexX = cms.untracked.int32(0),
            inputVariables = cms.vstring("pt"),
        ),
        cms.PSet (
            name = cms.string("muonSubleadingPt"),
            title = cms.string("Muon Transverse Momentum;Muon p_{T} [GeV]"),
            binsX = cms.untracked.vdouble(500, 0, 500),
            indexX = cms.untracked.int32(1),
            inputVariables = cms.vstring("pt"),
        ),
        cms.PSet (
            name = cms.string("muonPt_ext"),
            title = cms.string("Muon Transverse Momentum;Muon p_{T} [GeV]"),
            binsX = cms.untracked.vdouble(300, 0, 3000),
            inputVariables = cms.vstring("pt"),
        ),
        cms.PSet (
            name = cms.string("muonEta"),
            title = cms.string("Muon Eta;Muon #eta"),
            binsX = cms.untracked.vdouble(80, -4, 4),
            inputVariables = cms.vstring("eta"),
        ),
        cms.PSet (
            name = cms.string("muonEtaPt"),
            title = cms.string("Muon Eta vs. Muon p_{T};Muon p_{T} [GeV];Muon #eta"),
            binsX = cms.untracked.vdouble(100, 0, 500),
            binsY = cms.untracked.vdouble(25, 0, 2.5),
            inputVariables = cms.vstring("pt","eta"),
        ),
        cms.PSet (
            name = cms.string("muonPhi"),
            title = cms.string("Muon Phi;Muon #phi"),
            binsX = cms.untracked.vdouble(64, -3.2, 3.2),
            inputVariables = cms.vstring("phi"),
        ),
        cms.PSet (
            name = cms.string("muonPVIndex"),
            title = cms.string("Muon PV Index;Muon PV Index"),
            binsX = cms.untracked.vdouble(10, 0, 10),
            inputVariables = cms.vstring("muonPVIndex"),
        ),
        cms.PSet (
            name = cms.string("muonCharge"),
            title = cms.string("Muon Charge;Muon charge"),
            binsX = cms.untracked.vdouble(3, -1.5, 1.5),
            inputVariables = cms.vstring("charge"),
        ),
        cms.PSet (
            name = cms.string("muonEtaPhi"),
            title = cms.string("Muon Eta vs. Muon Phi;Muon #phi;Muon #eta"),
            binsX = cms.untracked.vdouble(64, -3.2, 3.2),
            binsY = cms.untracked.vdouble(60, -3, 3),
            inputVariables = cms.vstring("phi","eta"),
        ),
        cms.PSet (
            name = cms.string("muonNumberOfMissingInnerHits"),
            title = cms.string("Muon Number of Missing Inner Hits;Muon number of missing inner silicon hits"),
            binsX = cms.untracked.vdouble(6, -0.5, 5.5),
            inputVariables = cms.vstring("missingInnerHits"),
        ),
        cms.PSet (
            name = cms.string("muonNumberOfMissingMiddleHits"),
            title = cms.string("Muon Number of Missing Middle Hits;Muon number of missing middle silicon hits"),
            binsX = cms.untracked.vdouble(6, -0.5, 5.5),
            inputVariables = cms.vstring("missingMiddleHits"),
        ),
        cms.PSet (
            name = cms.string("muonNumberOfMissingOuterHits"),
            title = cms.string("Muon Number of Missing Outer Hits;Muon number of missing outer silicon hits"),
            binsX = cms.untracked.vdouble(16, -0.5, 15.5),
            inputVariables = cms.vstring("missingOuterHits"),
        ),
        cms.PSet (
            name = cms.string("muonNumberOfValidHits"),
            title = cms.string("Muon Number of Valid Hits;Muon number of valid hits"),
            binsX = cms.untracked.vdouble(40, 0, 40),
            inputVariables = cms.vstring("numberOfValidHits"),
        ),
        cms.PSet (
            name = cms.string("muonNormalizedChi2"),
            title = cms.string("Muon Chi Squared;Muon #chi^{2}/ndf"),
            binsX = cms.untracked.vdouble(20, 0, 20),
            inputVariables = cms.vstring("globalTrack.normalizedChi2"),
        ),
        cms.PSet (
            name = cms.string("muonNumberOfMatchedStations"),
            title = cms.string("Muon Track Number of Matched Stations;Muon number of matched stations"),
            binsX = cms.untracked.vdouble(10, 0, 10),
            inputVariables = cms.vstring("numberOfMatchedStations"),
        ),
        cms.PSet (
            name = cms.string("muonNumberOfValidPixelHits"),
            title = cms.string("Muon Number of Valid Pixel Hits;Muon number of valid pixel hits"),
            binsX = cms.untracked.vdouble(30, 0, 30),
            inputVariables = cms.vstring("innerTrack.hitPattern_.numberOfValidPixelHits"),
        ),
        cms.PSet (
            name = cms.string("muonTrackerLayersWithMeasurement"),
            title = cms.string("Muon Number of Tracker Layer with Measurement;Muon tracker layers with measurement"),
            binsX = cms.untracked.vdouble(30, 0, 30),
            inputVariables = cms.vstring("innerTrack.hitPattern_.trackerLayersWithMeasurement"),
            ),
        cms.PSet (
            name = cms.string("muonIsGlobalMuon"),
            title = cms.string("Muon isGlobalMuon;Muon is global"),
            binsX = cms.untracked.vdouble(2, 0, 2),
            inputVariables = cms.vstring("isGlobalMuon"),
        ),
        cms.PSet (
            name = cms.string("muonIsPFMuon"),
            title = cms.string("Muon isPFMuon;Muon is PF"),
            binsX = cms.untracked.vdouble(2, 0, 2),
            inputVariables = cms.vstring("isPFMuon"),
        ),
        cms.PSet (
            name = cms.string("muonIsTightMuonWRTVtx"),
            title = cms.string("Muon isTightMuon;Muon passes tight ID"),
            binsX = cms.untracked.vdouble(2, 0, 2),
            inputVariables = cms.vstring("isTightMuonWRTVtx"),
        ),
        cms.PSet (
            name = cms.string("muonIsSoftMuonWRTVtx"),
            title = cms.string("Muon isSoftMuon;Muon passes soft ID"),
            binsX = cms.untracked.vdouble(2, 0, 2),
            inputVariables = cms.vstring("isSoftMuonWRTVtx"),
        ),
        cms.PSet (
            name = cms.string("muonPFdBetaIsolation"),
            title = cms.string("Muon PF-based #Delta#beta Isolation;Muon PF-based #Delta#beta isolation"),
            binsX = cms.untracked.vdouble(100, 0, 6.0),
            inputVariables = cms.vstring("(pfIsolationR04_.sumChargedHadronPt + max(0.0,pfIsolationR04_.sumNeutralHadronEt + pfIsolationR04_.sumPhotonEt - 0.5*pfIsolationR04_.sumPUPt))/pt"),
        ),
        cms.PSet (
            name = cms.string("muonPFdBetaIsolationCorr"),
            title = cms.string("Muon PF-based #Delta#beta Isolation Corrected;Muon PF-based #Delta#beta Isolation Corrected"),
            binsX = cms.untracked.vdouble(100, 0, 6.0),
            inputVariables = cms.vstring("pfdBetaIsoCorr"),
        ),
        cms.PSet (
            name = cms.string("muonPFdBetaIsolationDiff"),
            title = cms.string("Muon PF-based #Delta#beta Isolation Discrepancy;Muon PF-based Iso_{default} - Iso_{customized}"),
            binsX = cms.untracked.vdouble(100, -1, 1),
            inputVariables = cms.vstring("(pfIsolationR04_.sumChargedHadronPt + max(0.0,pfIsolationR04_.sumNeutralHadronEt + pfIsolationR04_.sumPhotonEt - 0.5*pfIsolationR04_.sumPUPt))/pt - pfdBetaIsoCorr"),
        ),

        #gen
        cms.PSet (
            name = cms.string("muonGenMatchPdgId"),
            title = cms.string(";|PDG ID| of generator particle matched to muon"),
            binsX = cms.untracked.vdouble(getPdgBins(["unmatched", "quarks", "leptons", "bosons"])),
            inputVariables = cms.vstring("abs (genMatchedParticle.noFlagsPdgId)"),
            ),
        cms.PSet (
            name = cms.string("muonGenMatchDeltaR"),
            title = cms.string(";#DeltaR between muon and generator particle matched to muon"),
            binsX = cms.untracked.vdouble(300,0,6),
            inputVariables = cms.vstring("genMatchedParticle.noFlagsDR"),
            ),
        cms.PSet (
            name = cms.string("muonGenMatchPt"),
            title = cms.string("Gen Muon Transverse Momentum;Gen muon p_{T} [GeV]"),
            binsX = cms.untracked.vdouble(100, 0, 500),
            inputVariables = cms.vstring("genMatchedParticle.noFlags.pt"),
        ),
        cms.PSet (
            name = cms.string("muonGenMatchPt_ext"),
            title = cms.string("Gen Muon Transverse Momentum;Gen muon p_{T} [GeV]"),
            binsX = cms.untracked.vdouble(300, 0, 3000),
            inputVariables = cms.vstring("genMatchedParticle.noFlags.pt"),
        ),
        cms.PSet (
            name = cms.string("muonGenMatchEta"),
            title = cms.string("Gen Muon Eta;Gen muon #eta"),
            binsX = cms.untracked.vdouble(80, -4, 4),
            inputVariables = cms.vstring("genMatchedParticle.noFlags.eta"),
        ),
        cms.PSet (
            name = cms.string("muonGenMatchPhi"),
            title = cms.string("Gen Muon Phi;Gen muon #phi"),
            binsX = cms.untracked.vdouble(64, -3.2, 3.2),
            inputVariables = cms.vstring("genMatchedParticle.noFlags.phi"),
        ),

        cms.PSet (
            name = cms.string("muonGenMatchOfSameTypePdgId"),
            title = cms.string(";|PDG ID| of generator particle matched to muon"),
            binsX = cms.untracked.vdouble(getPdgBins(["unmatched", "quarks", "leptons", "bosons"])),
            inputVariables = cms.vstring("abs (genMatchedParticleOfSameType.noFlagsPdgId)"),
            ),
        cms.PSet (
            name = cms.string("muonGenMatchOfSameTypeDeltaR"),
            title = cms.string(";#DeltaR between muon and generator particle matched to muon"),
            binsX = cms.untracked.vdouble(300,0,6),
            inputVariables = cms.vstring("genMatchedParticleOfSameType.noFlagsDR"),
            ),
        cms.PSet (
            name = cms.string("muonGenMatchOfSameTypePt"),
            title = cms.string("Gen Muon Transverse Momentum;Gen muon p_{T} [GeV]"),
            binsX = cms.untracked.vdouble(100, 0, 500),
            inputVariables = cms.vstring("genMatchedParticleOfSameType.noFlags.pt"),
        ),
        cms.PSet (
            name = cms.string("muonGenMatchOfSameTypePt_ext"),
            title = cms.string("Gen Muon Transverse Momentum;Gen muon p_{T} [GeV]"),
            binsX = cms.untracked.vdouble(300, 0, 3000),
            inputVariables = cms.vstring("genMatchedParticleOfSameType.noFlags.pt"),
        ),
        cms.PSet (
            name = cms.string("muonGenMatchOfSameTypeEta"),
            title = cms.string("Gen Muon Eta;Gen muon #eta"),
            binsX = cms.untracked.vdouble(80, -4, 4),
            inputVariables = cms.vstring("genMatchedParticleOfSameType.noFlags.eta"),
        ),
        cms.PSet (
            name = cms.string("muonGenMatchOfSameTypePhi"),
            title = cms.string("Gen Muon Phi;Gen muon #phi"),
            binsX = cms.untracked.vdouble(64, -3.2, 3.2),
            inputVariables = cms.vstring("genMatchedParticleOfSameType.noFlags.phi"),
        ),
    )
)

if os.environ["CMSSW_VERSION"].startswith ("CMSSW_7_6_") or os.environ["CMSSW_VERSION"].startswith ("CMSSW_8_0_"):
    MuonHistograms.histograms.append(
        cms.PSet (
            name = cms.string("muonGenMatchMotherPdgId"),
            title = cms.string(";|PDG ID| of mother of gen muon"),
            binsX = cms.untracked.vdouble(getPdgBins(["unmatched", "quarks", "leptons", "bosons"])),
            inputVariables = cms.vstring("abs(genMatchedParticle.noFlags.mother_.pdgId)"),
        ),
        )
elif os.environ["CMSSW_VERSION"].startswith ("CMSSW_9_4_") or os.environ["CMSSW_VERSION"].startswith ("CMSSW_10_2_"):
    MuonHistograms.histograms.append(
        cms.PSet (
            name = cms.string("muonGenMatchMotherPdgId"),
            title = cms.string(";|PDG ID| of mother of gen muon"),
            binsX = cms.untracked.vdouble(getPdgBins(["unmatched", "quarks", "leptons", "bosons"])),
            inputVariables = cms.vstring("abs(genMatchedParticle.noFlags.motherRef.pdgId)"),
        ),
        )

##############################################################################################

MuonIPHistograms = cms.PSet(
    inputCollection = cms.vstring("muons","beamspots"),
    histograms = cms.VPSet (
        cms.PSet (
            name = cms.string("muonD0Beamspot"),
            title = cms.string("Muon d_{0} wrt Beamspot;Muon d_{0} [cm]"),
            binsX = cms.untracked.vdouble(100, -0.02, 0.02),
            inputVariables = cms.vstring("(-(muon.vx - beamspot.x0)*muon.py + (muon.vy - beamspot.y0)*muon.px)/muon.pt"),
        ),
        cms.PSet (
            name = cms.string("muonAbsD0Beamspot"),
            title = cms.string("Muon |d_{0}| wrt Beamspot;Muon |d_{0}| [cm]"),
            binsX = cms.untracked.vdouble(100, 0.0, 0.02),
            inputVariables = cms.vstring("abs(-(muon.vx - beamspot.x0)*muon.py + (muon.vy - beamspot.y0)*muon.px)/muon.pt"),
        ),
        cms.PSet (
            name = cms.string("muonD0SigBeamspot"),
            title = cms.string("Muon d_{0}/#sigma(d_{0}) wrt Beamspot;d_{0}/#sigma(d_{0})"),
            binsX = cms.untracked.vdouble(100, -20, 20),
            inputVariables = cms.vstring("((-(muon.vx - beamspot.x0)*muon.py + (muon.vy - beamspot.y0)*muon.px)/muon.pt)/hypot(muon.innerTrack.d0Error, hypot(beamspot.x0Error, beamspot.y0Error))"),
        ),
        cms.PSet (
            name = cms.string("muonAbsD0SigBeamspot"),
            title = cms.string("Muon |d_{0}/#sigma(d_{0})| wrt Beamspot;|d_{0}/#sigma(d_{0})|"),
            binsX = cms.untracked.vdouble(100, 0.0, 20),
            inputVariables = cms.vstring("abs(((-(muon.vx - beamspot.x0)*muon.py + (muon.vy - beamspot.y0)*muon.px)/muon.pt)/hypot(muon.innerTrack.d0Error, hypot(beamspot.x0Error, beamspot.y0Error)))"),
        ),
        cms.PSet (
            name = cms.string("muonDz"),
            title = cms.string("Muon d_{z} wrt Beamspot;Muon d_{z} [cm]"),
            binsX = cms.untracked.vdouble(200, -20, 20),
            inputVariables = cms.vstring("(muon.vz - beamspot.z0) - ((muon.vx - beamspot.x0)*muon.px + (muon.vy - beamspot.y0)*muon.py)/muon.pt*(muon.pz/muon.pt)"),
        ),
        cms.PSet (
            name = cms.string("muonAbsDz"),
            title = cms.string("Muon |d_{z}| wrt Beamspot;Muon |d_{z}| [cm]"),
            binsX = cms.untracked.vdouble(200, 0, 20),
            inputVariables = cms.vstring("abs((muon.vz - beamspot.z0) - ((muon.vx - beamspot.x0)*muon.px + (muon.vy - beamspot.y0)*muon.py)/muon.pt*(muon.pz/muon.pt))"),
        ),
        cms.PSet (
            name = cms.string("muonDbetaIsolationVsMuonIp"),
            title = cms.string("Muon Isolation vs Ip;Muon Ip d_{xy} [cm];Muon #Delta#beta Isolation"),
            binsX = cms.untracked.vdouble(500, 0, 0.5),
            binsY = cms.untracked.vdouble(600, 0, 6.0),
            inputVariables = cms.vstring("abs(-(muon.vx - beamspot.x0)*muon.py + (muon.vy - beamspot.y0)*muon.px)/muon.pt","(muon.pfIsolationR04_.sumChargedHadronPt + max(0.0,muon.pfIsolationR04_.sumNeutralHadronEt + muon.pfIsolationR04_.sumPhotonEt - 0.5*muon.pfIsolationR04_.sumPUPt))/muon.pt"),
        ),
    )
)

##############################################################################################

DiMuonHistograms = cms.PSet(
    inputCollection = cms.vstring("muons", "muons"),
    histograms = cms.VPSet (
        cms.PSet (
            name = cms.string("diMuonPt"),
            title = cms.string("Di-muon Tranverse Momentum;p_{T} [GeV]"),
            binsX = cms.untracked.vdouble(100, 0, 500),
            inputVariables = cms.vstring("pT (muon, muon)"),
        ),
        cms.PSet (
            name = cms.string("diMuonInvMass"),
            title = cms.string("Di-muon Invariant Mass;M_{#mu#mu} [GeV]"),
            binsX = cms.untracked.vdouble(100, 0, 500),
            inputVariables = cms.vstring("invMass (muon, muon)"),
        ),
        cms.PSet (
            name = cms.string("diMuonInvMassZmassWindow"),
            title = cms.string("Di-muon Invariant Mass;M_{#mu#mu} [GeV]"),
            binsX = cms.untracked.vdouble(100, 50, 150),
            inputVariables = cms.vstring("invMass (muon, muon)"),
        ),
        cms.PSet (
            name = cms.string("diMuonChargeProduct"),
            title = cms.string("Di-muon Charge Product;charge_{#mu}_{1}*charge_{#mu}_{2}"),
            binsX = cms.untracked.vdouble(3, -1.5, 1.5),
            inputVariables = cms.vstring("muon.charge * muon.charge"),
        ),
        cms.PSet (
            name = cms.string("diMuonDeltaPhi"),
            title = cms.string("Di-muon Phi Difference;|#Delta(#phi)|"),
            binsX = cms.untracked.vdouble(32, 0, 3.2),
            inputVariables = cms.vstring("abs ( deltaPhi (muon, muon) )"),
        ),
        cms.PSet (
            name = cms.string("diMuonDeltaEta"),
            title = cms.string("Di-muon Eta Difference;|#Delta(#eta)|"),
            binsX = cms.untracked.vdouble(60, 0, 6),
            inputVariables = cms.vstring("abs (muon.eta - muon.eta)"),
        ),
        cms.PSet (
            name = cms.string("diMuonDeltaR"),
            title = cms.string("Di-muon #DeltaR;#DeltaR"),
            binsX = cms.untracked.vdouble(60, 0, 6),
            inputVariables = cms.vstring("deltaR (muon, muon)"),
        ),
        cms.PSet (
            name = cms.string("diMuonCosAlpha"),
            title = cms.string("Di-muon cos(#alpha);cos(#alpha)"),
            binsX = cms.untracked.vdouble(100, -1, 1),
            inputVariables = cms.vstring("cosAlpha (muon, muon)"),
        ),
    )
)

##############################################################################################

ElectronHistograms = cms.PSet(
    inputCollection = cms.vstring("electrons"),
    histograms = cms.VPSet (
        cms.PSet (
            name = cms.string("numElectrons"),
            title = cms.string("Number of Selected Electrons;# electrons"),
            binsX = cms.untracked.vdouble(10, 0, 10),
            inputVariables = cms.vstring("number(electron)"),
        ),
        cms.PSet (
            name = cms.string("electronPt"),
            title = cms.string("Electron Transverse Momentum;Electron p_{T} [GeV]"),
            binsX = cms.untracked.vdouble(500, 0, 500),
            inputVariables = cms.vstring("pt"),
        ),
        cms.PSet (
            name = cms.string("electronLeadingPt"),
            title = cms.string("Electron Transverse Momentum;Electron p_{T} [GeV]"),
            binsX = cms.untracked.vdouble(500, 0, 500),
            indexX = cms.untracked.int32(0),
            inputVariables = cms.vstring("pt"),
        ),
        cms.PSet (
            name = cms.string("electronSubleadingPt"),
            title = cms.string("Electron Transverse Momentum;Electron p_{T} [GeV]"),
            binsX = cms.untracked.vdouble(500, 0, 500),
            indexX = cms.untracked.int32(1),
            inputVariables = cms.vstring("pt"),
        ),
        cms.PSet (
            name = cms.string("electronPt_ext"),
            title = cms.string("Electron Transverse Momentum;Electron p_{T} [GeV]"),
            binsX = cms.untracked.vdouble(300, 0, 3000),
            inputVariables = cms.vstring("pt"),
        ),
        cms.PSet (
            name = cms.string("electronEta"),
            title = cms.string("Electron Eta;Electron #eta"),
            binsX = cms.untracked.vdouble(60, -3, 3),
            inputVariables = cms.vstring("eta"),
        ),
        cms.PSet (
            name = cms.string("electronEtaPt"),
            title = cms.string("Electron Eta vs. Electron p_{T};Electron p_{T} [GeV];Electron #eta"),
            binsX = cms.untracked.vdouble(100, 0, 500),
            binsY = cms.untracked.vdouble(25, 0, 2.5),
            inputVariables = cms.vstring("pt","eta"),
        ),
        cms.PSet (
            name = cms.string("electronPhi"),
            title = cms.string("Electron Phi;Electron #phi"),
            binsX = cms.untracked.vdouble(64, -3.2, 3.2),
            inputVariables = cms.vstring("phi"),
        ),
        cms.PSet (
            name = cms.string("electronPVIndex"),
            title = cms.string("Electron PV Index;Electron PV Index"),
            binsX = cms.untracked.vdouble(10, 0, 10),
            inputVariables = cms.vstring("electronPVIndex"),
        ),
        cms.PSet (
            name = cms.string("electronCharge"),
            title = cms.string("Electron Charge;Electron charge"),
            binsX = cms.untracked.vdouble(3, -1.5, 1.5),
            inputVariables = cms.vstring("charge"),
        ),
        cms.PSet (
            name = cms.string("electronEtaPhi"),
            title = cms.string("Electron Eta vs. Electron Phi;Electron #phi;Electron #eta"),
            binsX = cms.untracked.vdouble(64, -3.2, 3.2),
            binsY = cms.untracked.vdouble(60, -3, 3),
            inputVariables = cms.vstring("phi","eta"),
        ),
        cms.PSet (
            name = cms.string("electronNumberOfMissingInnerHits"),
            title = cms.string("Electron Number of Missing Inner Hits;Electron number of missing inner hits"),
            binsX = cms.untracked.vdouble(6, -0.5, 5.5),
            inputVariables = cms.vstring("missingInnerHits"),
        ),
        cms.PSet (
            name = cms.string("electronNumberOfMissingMiddleHits"),
            title = cms.string("Electron Number of Missing Middle Hits;Electron number of missing middle silicon hits"),
            binsX = cms.untracked.vdouble(6, -0.5, 5.5),
            inputVariables = cms.vstring("missingMiddleHits"),
        ),
        cms.PSet (
            name = cms.string("electronNumberOfMissingOuterHits"),
            title = cms.string("Electron Number of Missing Outer Hits;Electron number of missing outer hits"),
            binsX = cms.untracked.vdouble(16, -0.5, 15.5),
            inputVariables = cms.vstring("missingOuterHits"),
        ),
        cms.PSet (
            name = cms.string("electronDeltaEtaSuperClusterTrackAtVtx"),
            title = cms.string("Electron deltaEtaSuperClusterTrackAtVtx;#Delta#eta(SC, track) at vertex"),
            binsX = cms.untracked.vdouble(100, 0, 0.01),
            inputVariables = cms.vstring("abs(deltaEtaSuperClusterTrackAtVtx)"),
        ),
        # N.B.: below causes a ProductNotFound of 'reco::CaloCluster' when run over skims (ahart + bfrancis)
        #cms.PSet (
        #    name = cms.string("electronDeltaEtaSeedClusterTrackAtVtx"),
        #    title = cms.string("Electron deltaEtaSeedClusterTrackAtVtx;#Delta#eta(seed, track) at vertex"),
        #    binsX = cms.untracked.vdouble(100, 0, 0.01),
        #    inputVariables = cms.vstring("abs(deltaEtaSuperClusterTrackAtVtx - superCluster.eta + superCluster.seed_.eta)"),
        #),
        cms.PSet (
            name = cms.string("electronDeltaPhiSuperClusterTrackAtVtx"),
            title = cms.string("Electron deltaPhiSuperClusterTrackAtVtx;#Delta#phi(SC, track) at vertex"),
            binsX = cms.untracked.vdouble(100, 0, 0.1),
            inputVariables = cms.vstring("abs(deltaPhiSuperClusterTrackAtVtx)"),
        ),
        cms.PSet (
            name = cms.string("electronFull5x5_sigmaIetaIeta"),
            title = cms.string("Electron full5x5_sigmaIetaIeta;#sigmai#etai#eta"),
            binsX = cms.untracked.vdouble(100, 0, 0.1),
            inputVariables = cms.vstring("full5x5_sigmaIetaIeta"),
        ),
        cms.PSet (
            name = cms.string("electronHadronicOverEm"),
            title = cms.string("Electron H/E;H/E"),
            binsX = cms.untracked.vdouble(100, 0, 0.5),
            inputVariables = cms.vstring("hadronicOverEm"),
        ),
        cms.PSet (
            name = cms.string("electronOoEmooP"),
            title = cms.string("Electron 1/E - 1/p;1/E - 1/p [GeV^{-1}]"),
            binsX = cms.untracked.vdouble(100, 0, 0.5),
            inputVariables = cms.vstring("abs(1/ecalEnergy - eSuperClusterOverP/ecalEnergy)"),
        ),
        cms.PSet (
            name = cms.string("electronVtxFitConversion"),
            title = cms.string("Electron Pass Conversion Veto;Pass Conversion Veto"),
            binsX = cms.untracked.vdouble(2, 0, 2),
            inputVariables = cms.vstring("passConversionVeto"),
        ),

#        cms.PSet (
#            name = cms.string("electronTkNormChi2"),
#            title = cms.string("Electron Track NormChi2;#chi^{2}"),
#            binsX = cms.untracked.vdouble(50, 0, 50),
#            inputVariables = cms.vstring("gsfTrack.normalizedChi2"),
#        ),
#        cms.PSet (
#            name = cms.string("electronTkValidHits"),
#            title = cms.string("Electron Track Number of Valid Hits;# Hits"),
#            binsX = cms.untracked.vdouble(20, 0, 20),
#            inputVariables = cms.vstring("gsfTrack.numberOfValidHits"),
#        ),
        cms.PSet (
            name = cms.string("electronPFrhoIsolation"),
            title = cms.string("Electron PF-based #rho-corrected Isolation;Electron rel. iso."),
            binsX = cms.untracked.vdouble(100, 0, 6),
            inputVariables = cms.vstring("(pfIso_.sumChargedHadronPt + max(0.0,pfIso_.sumNeutralHadronEt + pfIso_.sumPhotonEt - rho*AEff))/pt"),
        ),
        cms.PSet (
            name = cms.string("electronPFrhoIsolationCorr"),
            title = cms.string("Electron PF-based #rho-corrected Isolation Corrected;Electron #rho-corrected Isolation Corrected"),
            binsX = cms.untracked.vdouble(100, 0, 6.0),
            inputVariables = cms.vstring("pfdRhoIsoCorr"),
        ),
        cms.PSet (
            name = cms.string("electronPFrhoIsolationDiff"),
            title = cms.string("Electron PF-based #rho-corrected Isolation Discrepancy;Electron PF-based Iso_{default} - Iso_{customized}"),
            binsX = cms.untracked.vdouble(100, -1, 1),
            inputVariables = cms.vstring("(pfIso_.sumChargedHadronPt + max(0.0,pfIso_.sumNeutralHadronEt + pfIso_.sumPhotonEt - rho*AEff))/pt - pfdRhoIsoCorr"),
        ),
#        cms.PSet (
#            name = cms.string("electronFbrem"),
#            title = cms.string("Electron Brem. Energy Fraction;electron fbrem"),
#            binsX = cms.untracked.vdouble(100, 0, 2),
#            inputVariables = cms.vstring("fbrem"),
#        ),
#        cms.PSet (
#            name = cms.string("electronNumberOfLostHits"),
#            title = cms.string("Electon Number of Lost Hits;# lost hits"),
#            binsX = cms.untracked.vdouble(10, 0, 10),
#            inputVariables = cms.vstring("gsfTrack.numberOfLostHits"),
#        ),

        #gen
        cms.PSet (
            name = cms.string("electronGenMatchPdgId"),
            title = cms.string(";|PDG ID| of generator particle matched to electron"),
            binsX = cms.untracked.vdouble(getPdgBins(["unmatched", "quarks", "leptons", "bosons"])),
            inputVariables = cms.vstring("abs (genMatchedParticle.noFlagsPdgId)"),
            ),
        cms.PSet (
            name = cms.string("electronGenMatchDeltaR"),
            title = cms.string(";#DeltaR between electron and generator particle matched to electron"),
            binsX = cms.untracked.vdouble(300,0,6),
            inputVariables = cms.vstring("genMatchedParticle.noFlagsDR"),
        ),
        cms.PSet (
            name = cms.string("electronGenMatchPt"),
            title = cms.string("Gen Electron Transverse Momentum;Gen electron p_{T} [GeV]"),
            binsX = cms.untracked.vdouble(100, 0, 500),
            inputVariables = cms.vstring("genMatchedParticle.noFlags.pt"),
        ),
        cms.PSet (
            name = cms.string("electronGenMatchPt_ext"),
            title = cms.string("Gen Electron Transverse Momentum;Gen electron p_{T} [GeV]"),
            binsX = cms.untracked.vdouble(300, 0, 3000),
            inputVariables = cms.vstring("genMatchedParticle.noFlags.pt"),
        ),
        cms.PSet (
            name = cms.string("electronGenMatchEta"),
            title = cms.string("Gen Electron Eta;Gen electron #eta"),
            binsX = cms.untracked.vdouble(80, -4, 4),
            inputVariables = cms.vstring("genMatchedParticle.noFlags.eta"),
        ),
        cms.PSet (
            name = cms.string("electronGenMatchPhi"),
            title = cms.string("Gen Electron Phi;Gen electron #phi"),
            binsX = cms.untracked.vdouble(64, -3.2, 3.2),
            inputVariables = cms.vstring("genMatchedParticle.noFlags.phi"),
        ),

        cms.PSet (
            name = cms.string("electronGenMatchOfSameTypePdgId"),
            title = cms.string(";|PDG ID| of generator particle matched to electron"),
            binsX = cms.untracked.vdouble(getPdgBins(["unmatched", "quarks", "leptons", "bosons"])),
            inputVariables = cms.vstring("abs (genMatchedParticleOfSameType.noFlagsPdgId)"),
            ),
        cms.PSet (
            name = cms.string("electronGenMatchOfSameTypeDeltaR"),
            title = cms.string(";#DeltaR between electron and generator particle matched to electron"),
            binsX = cms.untracked.vdouble(300,0,6),
            inputVariables = cms.vstring("genMatchedParticleOfSameType.noFlagsDR"),
        ),
        cms.PSet (
            name = cms.string("electronGenMatchOfSameTypePt"),
            title = cms.string("Gen Electron Transverse Momentum;Gen electron p_{T} [GeV]"),
            binsX = cms.untracked.vdouble(100, 0, 500),
            inputVariables = cms.vstring("genMatchedParticleOfSameType.noFlags.pt"),
        ),
        cms.PSet (
            name = cms.string("electronGenMatchOfSameTypePt_ext"),
            title = cms.string("Gen Electron Transverse Momentum;Gen electron p_{T} [GeV]"),
            binsX = cms.untracked.vdouble(300, 0, 3000),
            inputVariables = cms.vstring("genMatchedParticleOfSameType.noFlags.pt"),
        ),
        cms.PSet (
            name = cms.string("electronGenMatchOfSameTypeEta"),
            title = cms.string("Gen Electron Eta;Gen electron #eta"),
            binsX = cms.untracked.vdouble(80, -4, 4),
            inputVariables = cms.vstring("genMatchedParticleOfSameType.noFlags.eta"),
        ),
        cms.PSet (
            name = cms.string("electronGenMatchOfSameTypePhi"),
            title = cms.string("Gen Electron Phi;Gen electron #phi"),
            binsX = cms.untracked.vdouble(64, -3.2, 3.2),
            inputVariables = cms.vstring("genMatchedParticleOfSameType.noFlags.phi"),
        ),
    )
)

if os.environ["CMSSW_VERSION"].startswith ("CMSSW_7_6_") or os.environ["CMSSW_VERSION"].startswith ("CMSSW_8_0_"):
    ElectronHistograms.histograms.append(
        cms.PSet (
            name = cms.string("electronGenMatchMotherPdgId"),
            title = cms.string(";|PDG ID| of mother of gen electron"),
            binsX = cms.untracked.vdouble(getPdgBins(["unmatched", "quarks", "leptons", "bosons"])),
            inputVariables = cms.vstring("abs(genMatchedParticle.noFlags.mother_.pdgId)"),
        ),
        )
elif os.environ["CMSSW_VERSION"].startswith ("CMSSW_9_4_") or os.environ["CMSSW_VERSION"].startswith ("CMSSW_10_2_"):
    ElectronHistograms.histograms.append(
        cms.PSet (
            name = cms.string("electronGenMatchMotherPdgId"),
            title = cms.string(";|PDG ID| of mother of gen electron"),
            binsX = cms.untracked.vdouble(getPdgBins(["unmatched", "quarks", "leptons", "bosons"])),
            inputVariables = cms.vstring("abs(genMatchedParticle.noFlags.motherRef.pdgId)"),
        ),
        )

##############################################################################################

ElectronIPHistograms = cms.PSet(
    inputCollection = cms.vstring("electrons","beamspots"),
    histograms = cms.VPSet (
        cms.PSet (
            name = cms.string("electronD0Beamspot"),
            title = cms.string("Electron d_{0} wrt Beamspot;Electron d_{0} [cm]"),
            binsX = cms.untracked.vdouble(100, -0.02, 0.02),
            inputVariables = cms.vstring("(-(electron.vx - beamspot.x0)*electron.py + (electron.vy - beamspot.y0)*electron.px)/electron.pt"),
        ),
        cms.PSet (
            name = cms.string("electronAbsD0Beamspot"),
            title = cms.string("Electron |d_{0}| wrt Beamspot;Electron |d_{0}| [cm]"),
            binsX = cms.untracked.vdouble(100, 0.0, 0.02),
            inputVariables = cms.vstring("abs(-(electron.vx - beamspot.x0)*electron.py + (electron.vy - beamspot.y0)*electron.px)/electron.pt"),
        ),
        cms.PSet (
            name = cms.string("electronD0SigBeamspot"),
            title = cms.string("Electron d_{0}/#sigma(d_{0}) wrt Beamspot;d_{0}/#sigma(d_{0})"),
            binsX = cms.untracked.vdouble(100, -20, 20),
            inputVariables = cms.vstring("((-(electron.vx - beamspot.x0)*electron.py + (electron.vy - beamspot.y0)*electron.px)/electron.pt)/hypot(electron.gsfTrack.d0Error, hypot(beamspot.x0Error, beamspot.y0Error))"),
        ),
        cms.PSet (
            name = cms.string("electronAbsD0SigBeamspot"),
            title = cms.string("Electron |d_{0}/#sigma(d_{0})| wrt Beamspot;|d_{0}/#sigma(d_{0})|"),
            binsX = cms.untracked.vdouble(100, 0.0, 20),
            inputVariables = cms.vstring("abs(((-(electron.vx - beamspot.x0)*electron.py + (electron.vy - beamspot.y0)*electron.px)/electron.pt)/hypot(electron.gsfTrack.d0Error, hypot(beamspot.x0Error, beamspot.y0Error)))"),
        ),
        cms.PSet (
            name = cms.string("electronDz"),
            title = cms.string("Electron d_{z} wrt Beamspot;Electron d_{z} [cm]"),
            binsX = cms.untracked.vdouble(200, -20, 20),
            inputVariables = cms.vstring("(electron.vz - beamspot.z0) - ((electron.vx - beamspot.x0)*electron.px + (electron.vy - beamspot.y0)*electron.py)/electron.pt*(electron.pz/electron.pt)"),
        ),
        cms.PSet (
            name = cms.string("electronAbsDz"),
            title = cms.string("Electron |d_{z}| wrt Beamspot;Electron |d_{z}| [cm]"),
            binsX = cms.untracked.vdouble(200, 0, 20),
            inputVariables = cms.vstring("abs((electron.vz - beamspot.z0) - ((electron.vx - beamspot.x0)*electron.px + (electron.vy - beamspot.y0)*electron.py)/electron.pt*(electron.pz/electron.pt))"),
        ),
        cms.PSet (
            name = cms.string("electronDbetaIsolationVsElectronIp"),
            title = cms.string("Electron Isolation vs Ip;Electron Ip d_{xy} [cm];Electron #Delta#beta Isolation"),
            binsX = cms.untracked.vdouble(500, 0, 0.5),
            binsY = cms.untracked.vdouble(300, 0, 3.0),
            inputVariables = cms.vstring("abs(-(electron.vx - beamspot.x0)*electron.py + (electron.vy - beamspot.y0)*electron.px)/electron.pt","(electron.pfIso_.sumChargedHadronPt + max(0.0,electron.pfIso_.sumNeutralHadronEt + electron.pfIso_.sumPhotonEt - electron.rho*electron.AEff))/electron.pt"),
        ),
    )
)

##############################################################################################

DiElectronHistograms = cms.PSet(
    inputCollection = cms.vstring("electrons", "electrons"),
    histograms = cms.VPSet (
        cms.PSet (
            name = cms.string("diElectronPt"),
            title = cms.string("Di-electron Tranverse Momentum;p_{T} [GeV]"),
            binsX = cms.untracked.vdouble(100, 0, 500),
            inputVariables = cms.vstring("pT (electron, electron)"),
        ),
        cms.PSet (
            name = cms.string("diElectronInvMass"),
            title = cms.string("Di-electron Invariant Mass;M_{ee} [GeV]"),
            binsX = cms.untracked.vdouble(100, 0, 500),
            inputVariables = cms.vstring("invMass(electron, electron)"),
        ),
        cms.PSet (
            name = cms.string("diElectronChargeProduct"),
            title = cms.string("Di-electron Charge Product;charge_{e}_{1}*charge_{e}_{2}"),
            binsX = cms.untracked.vdouble(3, -1.5, 1.5),
            inputVariables = cms.vstring("electron.charge * electron.charge"),
        ),
        cms.PSet (
            name = cms.string("diElectronDeltaPhi"),
            title = cms.string("Di-electron Phi Difference;|#Delta(#phi)|"),
            binsX = cms.untracked.vdouble(32, 0, 3.2),
            inputVariables = cms.vstring("abs(deltaPhi(electron, electron))"),
        ),
        cms.PSet (
            name = cms.string("diElectronDeltaEta"),
            title = cms.string("Di-electron Eta Difference;|#Delta(#eta)|"),
            binsX = cms.untracked.vdouble(60, 0, 6),
            inputVariables = cms.vstring("abs(electron.eta - electron.eta)"),
        ),
        cms.PSet (
            name = cms.string("diElectronDeltaR"),
            title = cms.string("Di-electron #DeltaR;#DeltaR"),
            binsX = cms.untracked.vdouble(60, 0, 6),
            inputVariables = cms.vstring("deltaR(electron, electron)"),
        ),
        cms.PSet (
            name = cms.string("diElectronDeltaZ"),
            title = cms.string("Di-electron #DeltaZ;#DeltaZ"),
            binsX = cms.untracked.vdouble(200, 0, 20),
            inputVariables = cms.vstring("abs(electron.vz - electron.vz)"),
        ),
   )
)

##############################################################################################

ElectronMuonHistograms = cms.PSet(
    inputCollection = cms.vstring("electrons","muons"),
    histograms = cms.VPSet (
        cms.PSet (
            name = cms.string("electronPtMuonPt"),
            title = cms.string("Electron Momentum vs Muon Momentum;Muon p_{T} [GeV];Electron p_{T} [GeV]"),
            binsX = cms.untracked.vdouble(100,0,500),
            binsY = cms.untracked.vdouble(100,0,500),
            inputVariables = cms.vstring("muon.pt","electron.pt"),
        ),
        cms.PSet (
            name = cms.string("electronEtaMuonEta"),
            title = cms.string("Electron Eta vs Muon Eta;Muon #eta;Electron #eta"),
            binsX = cms.untracked.vdouble(25,0,2.5),
            binsY = cms.untracked.vdouble(25,0,2.5),
            inputVariables = cms.vstring("abs(muon.eta)","abs(electron.eta)"),
        ),
        cms.PSet (
            name = cms.string("electronMuonPt"),
            title = cms.string("Momentum of Electron-Muon System;electron-muon p_{T} [GeV];"),
            binsX = cms.untracked.vdouble(100,0,500),
            inputVariables = cms.vstring("pT(electron, muon)"),
        ),
        cms.PSet (
            name = cms.string("electronMuonInvMass"),
            title = cms.string("Electron-muon Invariant Mass;M_{e#mu} [GeV]"),
            binsX = cms.untracked.vdouble(100, 0, 500),
            inputVariables = cms.vstring("invMass(electron, muon)"),
        ),
        cms.PSet (
            name = cms.string("electronMuonChargeProduct"),
            title = cms.string("Electron-muon Charge Product;charge_{e}*charge_{#mu}"),
            binsX = cms.untracked.vdouble(3, -1.5, 1.5),
            inputVariables = cms.vstring("electron.charge * muon.charge"),
        ),
        cms.PSet (
            name = cms.string("electronMuonDeltaPhi"),
            title = cms.string("Electron-muon Phi Difference;|#Delta(#phi)|"),
            binsX = cms.untracked.vdouble(32, 0, 3.2),
            inputVariables = cms.vstring("abs(deltaPhi(electron, muon))"),
        ),
        cms.PSet (
            name = cms.string("electronMuonDeltaEta"),
            title = cms.string("Electron-muon Eta Difference;|#Delta(#eta)|"),
            binsX = cms.untracked.vdouble(60, 0, 6),
            inputVariables = cms.vstring("abs(electron.eta - muon.eta)"),
        ),
        cms.PSet (
            name = cms.string("electronMuonDeltaR"),
            title = cms.string("Electron-muon #DeltaR;#DeltaR"),
            binsX = cms.untracked.vdouble(60, 0, 6),
            inputVariables = cms.vstring("deltaR(electron, muon)"),
        ),
        cms.PSet (
            name = cms.string("electronMuonDeltaZ"),
            title = cms.string("Electron-muon #DeltaZ;#DeltaZ [cm]"),
            binsX = cms.untracked.vdouble(100, -20, 20),
            inputVariables = cms.vstring("electron.vz - muon.vz"),
        ),
        cms.PSet (
            name = cms.string("electronRhoIsoVsMuonDbetaIso"),
            title = cms.string("Electron #rho-corrected Isolation vs. Muon #Delta#beta-corrected Isolation;Muon rel. iso.;Electron rel. iso."),
            binsX = cms.untracked.vdouble(300, 0, 3),
            binsY = cms.untracked.vdouble(300, 0, 3),
            inputVariables = cms.vstring("(muon.pfIsolationR04_.sumChargedHadronPt + max(0.0,muon.pfIsolationR04_.sumNeutralHadronEt + muon.pfIsolationR04_.sumPhotonEt - 0.5*muon.pfIsolationR04_.sumPUPt))/muon.pt","(electron.pfIso_.sumChargedHadronPt + max(0.0,electron.pfIso_.sumNeutralHadronEt + electron.pfIso_.sumPhotonEt - electron.rho*electron.AEff))/electron.pt"),
        ),
    )
)

##############################################################################################

ElectronMuonIPHistograms = cms.PSet(
    inputCollection = cms.vstring("electrons","muons","beamspots"),
    histograms = cms.VPSet (
        cms.PSet (
            name = cms.string("electronD0vsMuonD0Beamspot"),
            title = cms.string("Electron d_{0} wrt Beamspot vs. Muon d_{0} wrt Beamspot;Muon d_{0} [cm];Electron d_{0} [cm]"),
            binsX = cms.untracked.vdouble(100, -0.02, 0.02),
            binsY = cms.untracked.vdouble(100, -0.02, 0.02),
            inputVariables = cms.vstring("(-(muon.vx - beamspot.x0)*muon.py + (muon.vy - beamspot.y0)*muon.px)/muon.pt","(-(electron.vx - beamspot.x0)*electron.py + (electron.vy - beamspot.y0)*electron.px)/electron.pt"),
        ),
        cms.PSet (
            name = cms.string("electronAbsD0BeamspotVsMuonAbsD0Beamspot"),
            title = cms.string("Electron |d_{0}| wrt Beamspot vs. Muon |d_{0}| wrt Beamspot;Muon |d_{0}| [cm];Electron |d_{0}| [cm]"),
            binsX = cms.untracked.vdouble(100, 0, 0.02),
            binsY = cms.untracked.vdouble(100, 0, 0.02),
            inputVariables = cms.vstring("abs((-(muon.vx - beamspot.x0)*muon.py + (muon.vy - beamspot.y0)*muon.px)/muon.pt)","abs((-(electron.vx - beamspot.x0)*electron.py + (electron.vy - beamspot.y0)*electron.px)/electron.pt)"),
        ),
    )
)


##############################################################################################

ElectronMetHistograms = cms.PSet(
    inputCollection = cms.vstring("electrons","mets"),
    histograms = cms.VPSet (
        cms.PSet (
            name = cms.string("electronMetMT"),
            title = cms.string("Transverse Mass of Electron-E_{T}^{miss} System;m_{T}(e,E_{T}^{miss}) [GeV]"),
            binsX = cms.untracked.vdouble(100, 0, 200),
            inputVariables = cms.vstring("sqrt(2 * met.pt * electron.pt * (1.0 - cos(deltaPhi(electron,met))))"),
        ),
    )
)

##############################################################################################

MuonMetHistograms = cms.PSet(
    inputCollection = cms.vstring("muons","mets"),
    histograms = cms.VPSet (
        cms.PSet (
            name = cms.string("muonMetMT"),
            title = cms.string("Transverse Mass of Muon-E_{T}^{miss} System;m_{T}(#mu,E_{T}^{miss}) [GeV]"),
            binsX = cms.untracked.vdouble(100, 0, 200),
            inputVariables = cms.vstring("sqrt(2 * met.pt * muon.pt * (1.0 - cos(deltaPhi(muon,met))))"),
        ),
    )
)

##############################################################################################

JetHistograms = cms.PSet(
    inputCollection = cms.vstring("jets"),
    histograms = cms.VPSet (
        cms.PSet (
            name = cms.string("numJets"),
            title = cms.string("Number of Selected Jets;# jets"),
            binsX = cms.untracked.vdouble(10, 0, 10),
            inputVariables = cms.vstring("number(jet)"),
        ),
        cms.PSet (
            name = cms.string("jetPt"),
            title = cms.string("Jet Transverse Momentum;jet p_{T} [GeV]"),
            binsX = cms.untracked.vdouble(100, 0, 500),
            inputVariables = cms.vstring("pt"),
        ),
        cms.PSet (
            name = cms.string("jetEta"),
            title = cms.string("Jet Eta;jet #eta"),
            binsX = cms.untracked.vdouble(60, -3, 3),
            inputVariables = cms.vstring("eta"),
        ),
        cms.PSet (
            name = cms.string("jetPhi"),
            title = cms.string("Jet Phi;jet #phi"),
            binsX = cms.untracked.vdouble(64, -3.2, 3.2),
            inputVariables = cms.vstring("phi"),
        ),
        cms.PSet (
            name = cms.string("jetCharge"),
            title = cms.string("Jet Charge;jet charge"),
            binsX = cms.untracked.vdouble(41, -20.5, 20.5),
            inputVariables = cms.vstring("charge"),
        ),
        cms.PSet (
            name = cms.string("jetMass"),
            title = cms.string("Jet Mass;jet mass [GeV]"),
            binsX = cms.untracked.vdouble(100, 0, 200),
            inputVariables = cms.vstring("mass"),
        ),
        cms.PSet (
            name = cms.string("jetEtaPhi"),
            title = cms.string("Jet Eta vs. Jet Phi;jet #phi;jet #eta"),
            binsX = cms.untracked.vdouble(64, -3.2, 3.2),
            binsY = cms.untracked.vdouble(60, -3, 3),
            inputVariables = cms.vstring("phi","eta"),
        ),
        cms.PSet (
            name = cms.string("jetChargedHadronEnergyFraction"),
            title = cms.string("Jet Charged Hadron Fraction;jet charged hadron energy fraction"),
            binsX = cms.untracked.vdouble(101, 0.0, 1.0 + (1.0 / 100.0)),
            inputVariables = cms.vstring("chargedHadronEnergyFraction"),
        ),
        cms.PSet (
            name = cms.string("jetNeutralHadronEnergyFraction"),
            title = cms.string("Jet Neutral Hadron Fraction;jet neutral hadron energy fraction"),
            binsX = cms.untracked.vdouble(101, 0.0, 1.0 + (1.0 / 100.0)),
            inputVariables = cms.vstring("neutralHadronEnergyFraction"),
        ),
        cms.PSet (
            name = cms.string("jetNeutralEMEnergyFraction"),
            title = cms.string("Jet Neutral EM Fraction;jet neutral EM energy fraction"),
            binsX = cms.untracked.vdouble(101, 0.0, 1.0 + (1.0 / 100.0)),
            inputVariables = cms.vstring("neutralEmEnergyFraction"),
        ),
        cms.PSet (
            name = cms.string("jetChargedEMEnergyFraction"),
            title = cms.string("Jet Charged EM Fraction;jet charged EM energy fraction"),
            binsX = cms.untracked.vdouble(101, 0.0, 1.0 + (1.0 / 100.0)),
            inputVariables = cms.vstring("chargedEmEnergyFraction"),
        ),
        cms.PSet (
            name = cms.string("jetCSV"),
            title = cms.string("Jet Combined Secondary Vertex B-tagging Discriminant"),
            binsX = cms.untracked.vdouble(100, 0, 1),
            inputVariables = cms.vstring("pfCombinedInclusiveSecondaryVertexV2BJetTags"),
        ),
        cms.PSet (
            name = cms.string("jetPileUpId"),
            title = cms.string("Jet PileUp Id"),
            binsX = cms.untracked.vdouble(200, -1, 1),
            inputVariables = cms.vstring("pileupJetId"),
        ),
    )
)

#####################################################################################

BjetHistograms = cms.PSet(
    inputCollection = cms.vstring("bjets"),
    histograms = cms.VPSet (
        cms.PSet (
            name = cms.string("numBjets"),
            title = cms.string("Number of Selected Bjets;# bjets"),
            binsX = cms.untracked.vdouble(10, 0, 10),
            inputVariables = cms.vstring("number(bjet)"),
        ),
        cms.PSet (
            name = cms.string("bjetPt"),
            title = cms.string("Bjet Transverse Momentum;bjet p_{T} [GeV]"),
            binsX = cms.untracked.vdouble(100, 0, 500),
            inputVariables = cms.vstring("pt"),
        ),
        cms.PSet (
            name = cms.string("bjetEta"),
            title = cms.string("Bjet Eta;bjet #eta"),
            binsX = cms.untracked.vdouble(60, -3, 3),
            inputVariables = cms.vstring("eta"),
        ),
        cms.PSet (
            name = cms.string("bjetPhi"),
            title = cms.string("Bjet Phi;bjet #phi"),
            binsX = cms.untracked.vdouble(64, -3.2, 3.2),
            inputVariables = cms.vstring("phi"),
        ),
        cms.PSet (
            name = cms.string("bjetCharge"),
            title = cms.string("Bjet Charge;bjet charge"),
            binsX = cms.untracked.vdouble(41, -20.5, 20.5),
            inputVariables = cms.vstring("charge"),
        ),
        cms.PSet (
            name = cms.string("bjetEtaPhi"),
            title = cms.string("Bjet Eta vs. Bjet Phi;bjet #phi;bjet #eta"),
            binsX = cms.untracked.vdouble(64, -3.2, 3.2),
            binsY = cms.untracked.vdouble(60, -3, 3),
            inputVariables = cms.vstring("phi","eta"),
        ),
        cms.PSet (
            name = cms.string("bjetChargedHadronEnergyFraction"),
            title = cms.string("Bjet Charged Hadron Fraction;bjet charged hadron energy fraction"),
            binsX = cms.untracked.vdouble(101, 0.0, 1.0 + (1.0 / 100.0)),
            inputVariables = cms.vstring("chargedHadronEnergyFraction"),
        ),
        cms.PSet (
            name = cms.string("bjetNeutralHadronEnergyFraction"),
            title = cms.string("Bjet Neutral Hadron Fraction;bjet neutral hadron energy fraction"),
            binsX = cms.untracked.vdouble(101, 0.0, 1.0 + (1.0 / 100.0)),
            inputVariables = cms.vstring("neutralHadronEnergyFraction"),
        ),
        cms.PSet (
            name = cms.string("bjetNeutralEMEnergyFraction"),
            title = cms.string("Bjet Neutral EM Fraction;bjet neutral EM energy fraction"),
            binsX = cms.untracked.vdouble(101, 0.0, 1.0 + (1.0 / 100.0)),
            inputVariables = cms.vstring("neutralEmEnergyFraction"),
        ),
        cms.PSet (
            name = cms.string("bjetChargedEMEnergyFraction"),
            title = cms.string("Bjet Charged EM Fraction;bjet charged EM energy fraction"),
            binsX = cms.untracked.vdouble(101, 0.0, 1.0 + (1.0 / 100.0)),
            inputVariables = cms.vstring("chargedEmEnergyFraction"),
        ),
        cms.PSet (
            name = cms.string("bjetCSV"),
            title = cms.string("Bjet Combined Secondary Vertex B-tagging Discriminant"),
            binsX = cms.untracked.vdouble(100, 0, 1),
            inputVariables = cms.vstring("pfCombinedInclusiveSecondaryVertexV2BJetTags"),
        ),
        cms.PSet (
            name = cms.string("bjetPileUpId"),
            title = cms.string("BJet PileUp Id"),
            binsX = cms.untracked.vdouble(200, -1, 1),
            inputVariables = cms.vstring("pileupJetId"),
        ),
    )
)

#####################################################################################

JetIsoHistograms = cms.PSet(
    inputCollection = cms.vstring("jets"),
    histograms = cms.VPSet (
        cms.PSet (
            name = cms.string("jetChargedHadronEnergy"),
            title = cms.string("Charged Hadron Energy Deposited Within the Jet;E [GeV]"),
            binsX = cms.untracked.vdouble(100, 0, 500),
            inputVariables = cms.vstring("chargedHadronEnergy"),
        ),
        cms.PSet (
            name = cms.string("jetNeutralHadronEnergy"),
            title = cms.string("Neutral Hadron Energy Deposited Within the Jet;E [GeV]"),
            binsX = cms.untracked.vdouble(100, 0, 500),
            inputVariables = cms.vstring("neutralHadronEnergy"),
        ),
        cms.PSet (
            name = cms.string("jetChargedEmEnergy"),
            title = cms.string("Charged Em Energy Deposited Near the Jet;E [GeV]"),
            binsX = cms.untracked.vdouble(100, 0, 500),
            inputVariables = cms.vstring("chargedEmEnergy"),
        ),
        cms.PSet (
            name = cms.string("jetNeutralEmEnergy"),
            title = cms.string("Neutral Em Energy Deposited Near the Jet;E [GeV]"),
            binsX = cms.untracked.vdouble(100, 0, 500),
            inputVariables = cms.vstring("neutralEmEnergy"),
        ),
    )
)

##########################################################################################

JetBjetHistograms = cms.PSet(
    inputCollection = cms.vstring("jets","bjets"),
    histograms = cms.VPSet (
        cms.PSet (
            name = cms.string("jetBjetInvMass"),
            title = cms.string("Jet-bjet Invariant Mass;M(jet,bjet) [GeV]"),
            binsX = cms.untracked.vdouble(100, 0, 500),
            inputVariables = cms.vstring("invMass(jet,bjet)"),
        ),
        cms.PSet (
            name = cms.string("jetBjetDeltaPhi"),
            title = cms.string("Jet-bjet Phi Difference;|#Delta#phi(jet,bjet)|"),
            binsX = cms.untracked.vdouble(32, 0, 3.2),
            inputVariables = cms.vstring("abs(deltaPhi(jet,bjet))"),
        ),
        cms.PSet (
            name = cms.string("jetBjetDeltaEta"),
            title = cms.string("Jet-bjet Eta Difference;|#Delta#eta(jet,bjet)|"),
            binsX = cms.untracked.vdouble(60, 0, 6),
            inputVariables = cms.vstring("abs(jet.eta - bjet.eta)"),
        ),
        cms.PSet (
            name = cms.string("jetBjetDeltaR"),
            title = cms.string("Jet-bjet #DeltaR;#DeltaR(jet,bjet)"),
            binsX = cms.untracked.vdouble(60, 0, 6),
            inputVariables = cms.vstring("deltaR(jet,bjet)"),
        ),
        cms.PSet (
            name = cms.string("jetBjetDeltaZ"),
            title = cms.string("Jet-bjet Z Difference;|#Deltaz(jet,bjet)| [cm]"),
            binsX = cms.untracked.vdouble(100, 0, 20),
            inputVariables = cms.vstring("abs(jet.vz - bjet.vz)"),
        ),
        cms.PSet (
            name = cms.string("jetBjetDeltaRvsjetBjetDeltaEta"),
            title = cms.string("Jet-bjet #DeltaR vs #Delta#eta;|#Delta#eta(jet,bjet)|;#DeltaR(jet,bjet)"),
            binsX = cms.untracked.vdouble(60, 0, 6),
            binsY = cms.untracked.vdouble(60, 0 ,6),
            inputVariables = cms.vstring("abs(jet.eta - bjet.eta)","deltaR(jet,bjet)"),
        ),
        cms.PSet (
            name = cms.string("jetBjetDeltaRvsjetBjetDeltaPhi"),
            title = cms.string("Jet-bjet #DeltaR vs #Delta#phi;|#Delta#phi(jet,bjet)|;#DeltaR(jet,bjet)"),
            binsX = cms.untracked.vdouble(32, 0, 3.2),
            binsY = cms.untracked.vdouble(60, 0, 6),
            inputVariables = cms.vstring("abs(deltaPhi(jet,bjet))","deltaR(jet,bjet)"),
        ),
        cms.PSet (
            name = cms.string("jetEtavsBjetEta"),
            title = cms.string("Jet Eta.vs Bjet Eta;Bjet #eta;Jet #eta"),
            binsX = cms.untracked.vdouble(120, -6, 6),
            binsY = cms.untracked.vdouble(120, -6 ,6),
            inputVariables = cms.vstring("bjet.eta","jet.eta"),
        ),
        cms.PSet (
            name = cms.string("jetPhivsBjetPhi"),
            title = cms.string("Jet Phi.vs Bjet Phi;Bjet #phi;Jet #phi"),
            binsX = cms.untracked.vdouble(64, -3.2, 3.2),
            binsY = cms.untracked.vdouble(64, -3.2 ,3.2),
            inputVariables = cms.vstring("bjet.phi","jet.phi"),
        ),
    )
)

##########################################################################################
##########################################################################################

MuonJetHistograms = cms.PSet(
    inputCollection = cms.vstring("muons","jets","beamspots"),
    histograms = cms.VPSet (
        cms.PSet (
            name = cms.string("muonAbsIPvsJetCSV"),
            title = cms.string("Muon Abs IP vs Jet CSV;Jet CSV"),
            binsX = cms.untracked.vdouble(100, 0, 1),
            binsY = cms.untracked.vdouble(500, 0, 0.5),
            inputVariables = cms.vstring("jet.pfCombinedInclusiveSecondaryVertexV2BJetTags","abs((-(muon.vx - beamspot.x0)*muon.py + (muon.vy - beamspot.y0)*muon.px)/muon.pt)",),
        ),
        cms.PSet (
            name = cms.string("muonJetInvMass"),
            title = cms.string("Muon-jet Invariant Mass;M(#mu,jet) [GeV]"),
            binsX = cms.untracked.vdouble(100, 0, 500),
            inputVariables = cms.vstring("invMass(muon,jet)"),
        ),
        cms.PSet (
            name = cms.string("muonJetDeltaPt"),
            title = cms.string("Muon-jet p_{T} Difference;|#Deltap_{T}(#mu,jet)|"),
            binsX = cms.untracked.vdouble(100, 0, 100),
            inputVariables = cms.vstring("abs(muon.pt - jet.pt)"),
        ),
        cms.PSet (
            name = cms.string("muonJetDeltaPhi"),
            title = cms.string("Muon-jet Phi Difference;|#Delta#phi(#mu,jet)|"),
            binsX = cms.untracked.vdouble(32, 0, 3.2),
            inputVariables = cms.vstring("abs(deltaPhi(muon,jet))"),
        ),
        cms.PSet (
            name = cms.string("muonJetDeltaEta"),
            title = cms.string("Muon-jet Eta Difference;|#Delta#eta(#mu,jet)|"),
            binsX = cms.untracked.vdouble(60, 0, 6),
            inputVariables = cms.vstring("abs(muon.eta - jet.eta)"),
        ),
        cms.PSet (
            name = cms.string("muonJetDeltaR"),
            title = cms.string("Muon-jet #DeltaR;#DeltaR(#mu,jet)"),
            binsX = cms.untracked.vdouble(60, 0, 6),
            inputVariables = cms.vstring("deltaR(muon,jet)"),
        ),
        cms.PSet (
            name = cms.string("muonJetDeltaZ"),
            title = cms.string("Muon-jet Z Difference;|#Deltaz(#mu,jet)| [cm]"),
            binsX = cms.untracked.vdouble(100, 0, 20),
            inputVariables = cms.vstring("abs(muon.vz - jet.vz)"),
        ),
        cms.PSet (
            name = cms.string("muonJetDeltaRvsmuonJetDeltaEta"),
            title = cms.string("Muon-jet #DeltaR vs #Delta#eta;|#Delta#eta(#mu,jet)|;#DeltaR(#mu,jet)"),
            binsX = cms.untracked.vdouble(60, 0, 6),
            binsY = cms.untracked.vdouble(60, 0 ,6),
            inputVariables = cms.vstring("abs(muon.eta - jet.eta)","deltaR(muon,jet)"),
        ),
        cms.PSet (
            name = cms.string("muonJetDeltaRvsmuonJetDeltaPhi"),
            title = cms.string("Muon-jet #DeltaR vs #Delta#phi;|#Delta#phi(#mu,jet)|;#DeltaR(#mu,jet)"),
            binsX = cms.untracked.vdouble(32, 0, 3.2),
            binsY = cms.untracked.vdouble(60, 0, 6),
            inputVariables = cms.vstring("abs(deltaPhi(muon,jet))","deltaR(muon,jet)"),
        ),
        cms.PSet (
            name = cms.string("muonEtavsJetEta"),
            title = cms.string("Muon Eta.vs Jet Eta;Jet #eta;Muon #eta"),
            binsX = cms.untracked.vdouble(120, -6, 6),
            binsY = cms.untracked.vdouble(120, -6 ,6),
            inputVariables = cms.vstring("jet.eta","muon.eta"),
        ),
        cms.PSet (
            name = cms.string("muonPhivsJetPhi"),
            title = cms.string("Muon Phi.vs Jet Phi;Jet #phi;Muon #phi"),
            binsX = cms.untracked.vdouble(64, -3.2, 3.2),
            binsY = cms.untracked.vdouble(64, -3.2 ,3.2),
            inputVariables = cms.vstring("jet.phi","muon.phi"),
        ),
    )
)

##########################################################################################
##########################################################################################

ElectronJetHistograms = cms.PSet(
    inputCollection = cms.vstring("electrons","jets","beamspots"),
    histograms = cms.VPSet (
        cms.PSet (
            name = cms.string("electronAbsIPvsJetCSV"),
            title = cms.string("Electron Abs IP vs Jet CSV;Jet CSV"),
            binsX = cms.untracked.vdouble(100, 0, 1),
            binsY = cms.untracked.vdouble(500, 0, 0.5),
            inputVariables = cms.vstring("jet.pfCombinedInclusiveSecondaryVertexV2BJetTags","abs((-(electron.vx - beamspot.x0)*electron.py + (electron.vy - beamspot.y0)*electron.px)/electron.pt)",),
        ),
        cms.PSet (
            name = cms.string("electronJetInvMass"),
            title = cms.string("Electron-jet Invariant Mass;M(e,jet) [GeV]"),
            binsX = cms.untracked.vdouble(100, 0, 500),
            inputVariables = cms.vstring("invMass(electron,jet)"),
        ),
        cms.PSet (
            name = cms.string("electronJetDeltaPt"),
            title = cms.string("Electron-jet p_{T} Difference;|#Deltap_{T}(e,jet)|"),
            binsX = cms.untracked.vdouble(100, 0, 100),
            inputVariables = cms.vstring("abs(electron.pt - jet.pt)"),
        ),
        cms.PSet (
            name = cms.string("electronJetDeltaPhi"),
            title = cms.string("Electron-jet Phi Difference;|#Delta#phi(e,jet)|"),
            binsX = cms.untracked.vdouble(32, 0, 3.2),
            inputVariables = cms.vstring("abs(deltaPhi(electron,jet))"),
        ),
        cms.PSet (
            name = cms.string("electronJetDeltaEta"),
            title = cms.string("Electron-jet Eta Difference;|#Delta#eta(e,jet)|"),
            binsX = cms.untracked.vdouble(60, 0, 6),
            inputVariables = cms.vstring("abs(electron.eta - jet.eta)"),
        ),
        cms.PSet (
            name = cms.string("electronJetDeltaR"),
            title = cms.string("Electron-jet #DeltaR;#DeltaR(e,jet)"),
            binsX = cms.untracked.vdouble(60, 0, 6),
            inputVariables = cms.vstring("deltaR(electron,jet)"),
        ),
        cms.PSet (
            name = cms.string("electronJetDeltaZ"),
            title = cms.string("Electron-jet Z Difference;|#Deltaz(e,jet)| [cm]"),
            binsX = cms.untracked.vdouble(100, 0, 20),
            inputVariables = cms.vstring("abs(electron.vz - jet.vz)"),
        ),
        cms.PSet (
            name = cms.string("electronJetDeltaRvselectronJetDeltaEta"),
            title = cms.string("Electron-jet #DeltaR vs #Delta#eta;|#Delta#eta(e,jet)|;#DeltaR(e,jet)"),
            binsX = cms.untracked.vdouble(60, 0, 6),
            binsY = cms.untracked.vdouble(60, 0 ,6),
            inputVariables = cms.vstring("abs(electron.eta - jet.eta)","deltaR(electron,jet)"),
        ),
        cms.PSet (
            name = cms.string("electronJetDeltaRvselectronJetDeltaPhi"),
            title = cms.string("Electron-jet #DeltaR vs #Delta#phi;|#Delta#phi(e,jet)|;#DeltaR(e,jet)"),
            binsX = cms.untracked.vdouble(32, 0, 3.2),
            binsY = cms.untracked.vdouble(60, 0, 6),
            inputVariables = cms.vstring("abs(deltaPhi(electron,jet))","deltaR(electron,jet)"),
        ),
        cms.PSet (
            name = cms.string("electronEtavsJetEta"),
            title = cms.string("Electron Eta.vs Jet Eta;Jet #eta;Electron #eta"),
            binsX = cms.untracked.vdouble(120, -6, 6),
            binsY = cms.untracked.vdouble(120, -6 ,6),
            inputVariables = cms.vstring("jet.eta","electron.eta"),
        ),
        cms.PSet (
            name = cms.string("electronPhivsJetPhi"),
            title = cms.string("Electron Phi.vs Jet Phi;Jet #phi;Electron #phi"),
            binsX = cms.untracked.vdouble(64, -3.2, 3.2),
            binsY = cms.untracked.vdouble(64, -3.2 ,3.2),
            inputVariables = cms.vstring("jet.phi","electron.phi"),
        ),
    )
)

##########################################################################################

MuonBjetHistograms = cms.PSet(
    inputCollection = cms.vstring("muons","bjets","beamspots"),
    histograms = cms.VPSet (
        cms.PSet (
            name = cms.string("muonAbsIPvsBjetCSV"),
            title = cms.string("Muon Abs IP vs Bjet CSV;Bjet CSV"),
            binsX = cms.untracked.vdouble(100, 0, 1),
            binsY = cms.untracked.vdouble(500, 0, 0.5),
            inputVariables = cms.vstring("bjet.pfCombinedInclusiveSecondaryVertexV2BJetTags","abs((-(muon.vx - beamspot.x0)*muon.py + (muon.vy - beamspot.y0)*muon.px)/muon.pt)",),
        ),
        cms.PSet (
            name = cms.string("muonBjetInvMass"),
            title = cms.string("Muon-bjet Invariant Mass;M(#mu,bjet) [GeV]"),
            binsX = cms.untracked.vdouble(100, 0, 500),
            inputVariables = cms.vstring("invMass(muon,bjet)"),
        ),
        cms.PSet (
            name = cms.string("muonJetDeltaPt"),
            title = cms.string("Muon-jet p_{T} Difference;|#Deltap_{T}(#mu,bjet)|"),
            binsX = cms.untracked.vdouble(100, 0, 100),
            inputVariables = cms.vstring("abs(muon.pt - bjet.pt)"),
        ),
        cms.PSet (
            name = cms.string("muonBjetDeltaPhi"),
            title = cms.string("Muon-bjet Phi Difference;|#Delta#phi(#mu,bjet)|"),
            binsX = cms.untracked.vdouble(32, 0, 3.2),
            inputVariables = cms.vstring("abs(deltaPhi(muon,bjet))"),
        ),
        cms.PSet (
            name = cms.string("muonBjetDeltaEta"),
            title = cms.string("Muon-bjet Eta Difference;|#Delta#eta(#mu,bjet)|"),
            binsX = cms.untracked.vdouble(60, 0, 6),
            inputVariables = cms.vstring("abs(muon.eta - bjet.eta)"),
        ),
        cms.PSet (
            name = cms.string("muonBjetDeltaR"),
            title = cms.string("Muon-bjet #DeltaR;#DeltaR(#mu,bjet)"),
            binsX = cms.untracked.vdouble(60, 0, 6),
            inputVariables = cms.vstring("deltaR(muon,bjet)"),
        ),
        cms.PSet (
            name = cms.string("muonBjetDeltaZ"),
            title = cms.string("Muon-bjet Z Difference;|#Deltaz(#mu,bjet)| [cm]"),
            binsX = cms.untracked.vdouble(100, 0, 20),
            inputVariables = cms.vstring("abs(muon.vz - bjet.vz)"),
        ),
        cms.PSet (
            name = cms.string("muonBjetDeltaRvsmuonBjetDeltaEta"),
            title = cms.string("Muon-bjet #DeltaR vs #Delta#eta;|#Delta#eta(#mu,bjet)|;#DeltaR(#mu,bjet)"),
            binsX = cms.untracked.vdouble(60, 0, 6),
            binsY = cms.untracked.vdouble(60, 0 ,6),
            inputVariables = cms.vstring("abs(muon.eta - bjet.eta)","deltaR(muon,bjet)"),
        ),
        cms.PSet (
            name = cms.string("muonBjetDeltaRvsmuonBjetDeltaPhi"),
            title = cms.string("Muon-bjet #DeltaR vs #Delta#phi;|#Delta#phi(#mu,bjet)|;#DeltaR(#mu,bjet)"),
            binsX = cms.untracked.vdouble(32, 0, 3.2),
            binsY = cms.untracked.vdouble(60, 0, 6),
            inputVariables = cms.vstring("abs(deltaPhi(muon,bjet))","deltaR(muon,bjet)"),
        ),
        cms.PSet (
            name = cms.string("muonEtavsBjetEta"),
            title = cms.string("Muon Eta.vs Bjet Eta;Bjet #eta;Muon #eta"),
            binsX = cms.untracked.vdouble(120, -6, 6),
            binsY = cms.untracked.vdouble(120, -6 ,6),
            inputVariables = cms.vstring("bjet.eta","muon.eta"),
        ),
        cms.PSet (
            name = cms.string("muonPhivsBjetPhi"),
            title = cms.string("Muon Phi.vs Bjet Phi;Bjet #phi;Muon #phi"),
            binsX = cms.untracked.vdouble(64, -3.2, 3.2),
            binsY = cms.untracked.vdouble(64, -3.2 ,3.2),
            inputVariables = cms.vstring("bjet.phi","muon.phi"),
        ),
    )
)

##########################################################################
ElectronBjetHistograms = cms.PSet(
    inputCollection = cms.vstring("electrons","bjets","beamspots"),
    histograms = cms.VPSet (
        cms.PSet (
            name = cms.string("electronAbsIPvsBjetCSV"),
            title = cms.string("Electron Abs IP vs Bjet CSV;Bjet CSV"),
            binsX = cms.untracked.vdouble(100, 0, 1),
            binsY = cms.untracked.vdouble(500, 0, 0.5),
            inputVariables = cms.vstring("bjet.pfCombinedInclusiveSecondaryVertexV2BJetTags","abs((-(electron.vx - beamspot.x0)*electron.py + (electron.vy - beamspot.y0)*electron.px)/electron.pt)",),
        ),
        cms.PSet (
            name = cms.string("electronBjetInvMass"),
            title = cms.string("Electron-bjet Invariant Mass;M(#mu,bjet) [GeV]"),
            binsX = cms.untracked.vdouble(100, 0, 500),
            inputVariables = cms.vstring("invMass(electron,bjet)"),
        ),
        cms.PSet (
            name = cms.string("electronBjetDeltaPt"),
            title = cms.string("Electron-bjet p_{T} Difference;|#Deltap_{T}(e,bjet)|"),
            binsX = cms.untracked.vdouble(100, 0, 100),
            inputVariables = cms.vstring("abs(electron.pt - bjet.pt)"),
        ),
        cms.PSet (
            name = cms.string("electronBjetDeltaPhi"),
            title = cms.string("Electron-bjet Phi Difference;|#Delta#phi(#mu,bjet)|"),
            binsX = cms.untracked.vdouble(32, 0, 3.2),
            inputVariables = cms.vstring("abs(deltaPhi(electron,bjet))"),
        ),
        cms.PSet (
            name = cms.string("electronBjetDeltaEta"),
            title = cms.string("Electron-bjet Eta Difference;|#Delta#eta(#mu,bjet)|"),
            binsX = cms.untracked.vdouble(60, 0, 6),
            inputVariables = cms.vstring("abs(electron.eta - bjet.eta)"),
        ),
        cms.PSet (
            name = cms.string("electronBjetDeltaR"),
            title = cms.string("Electron-bjet #DeltaR;#DeltaR(#mu,bjet)"),
            binsX = cms.untracked.vdouble(60, 0, 6),
            inputVariables = cms.vstring("deltaR(electron,bjet)"),
        ),
        cms.PSet (
            name = cms.string("electronBjetDeltaZ"),
            title = cms.string("Electron-bjet Z Difference;|#Deltaz(#mu,bjet)| [cm]"),
            binsX = cms.untracked.vdouble(100, 0, 20),
            inputVariables = cms.vstring("abs(electron.vz - bjet.vz)"),
        ),
        cms.PSet (
            name = cms.string("electronBjetDeltaRvselectronBjetDeltaEta"),
            title = cms.string("Electron-bjet #DeltaR vs #Delta#eta;|#Delta#eta(#mu,bjet)|;#DeltaR(#mu,bjet)"),
            binsX = cms.untracked.vdouble(60, 0, 6),
            binsY = cms.untracked.vdouble(60, 0 ,6),
            inputVariables = cms.vstring("abs(electron.eta - bjet.eta)","deltaR(electron,bjet)"),
        ),
        cms.PSet (
            name = cms.string("electronBjetDeltaRvselectronBjetDeltaPhi"),
            title = cms.string("Electron-bjet #DeltaR vs #Delta#phi;|#Delta#phi(#mu,bjet)|;#DeltaR(#mu,bjet)"),
            binsX = cms.untracked.vdouble(32, 0, 3.2),
            binsY = cms.untracked.vdouble(60, 0, 6),
            inputVariables = cms.vstring("abs(deltaPhi(electron,bjet))","deltaR(electron,bjet)"),
        ),
        cms.PSet (
            name = cms.string("electronEtavsBjetEta"),
            title = cms.string("Electron Eta.vs Bjet Eta;Bjet #eta;Electron #eta"),
            binsX = cms.untracked.vdouble(120, -6, 6),
            binsY = cms.untracked.vdouble(120, -6 ,6),
            inputVariables = cms.vstring("bjet.eta","electron.eta"),
        ),
        cms.PSet (
            name = cms.string("electronPhivsBjetPhi"),
            title = cms.string("Electron Phi.vs Bjet Phi;Bjet #phi;Electron #phi"),
            binsX = cms.untracked.vdouble(64, -3.2, 3.2),
            binsY = cms.untracked.vdouble(64, -3.2 ,3.2),
            inputVariables = cms.vstring("bjet.phi","electron.phi"),
        ),
    )
)

##########################################################################
PhotonHistograms = cms.PSet(
    inputCollection = cms.vstring("photons"),
    histograms = cms.VPSet (
        cms.PSet (
            name = cms.string("photonPt"),
            title = cms.string("Photon Transverse Momentum;p_{T} [GeV]"),
            binsX = cms.untracked.vdouble(100, 0, 500),
            inputVariables = cms.vstring("pt"),
        ),
        cms.PSet (
            name = cms.string("photonEta"),
            title = cms.string("Photon Eta;#eta"),
            binsX = cms.untracked.vdouble(60, -3, 3),
            inputVariables = cms.vstring("eta"),
        ),
        cms.PSet (
            name = cms.string("photonPhi"),
            title = cms.string("Photon Phi;#phi"),
            binsX = cms.untracked.vdouble(64, -3.2, 3.2),
            inputVariables = cms.vstring("phi"),
        ),
        cms.PSet (
            name = cms.string("photonEtaPhi"),
            title = cms.string("Photon Eta vs. Photon Phi;#phi;#eta"),
            binsX = cms.untracked.vdouble(64, -3.2, 3.2),
            binsY = cms.untracked.vdouble(60, -3, 3),
            inputVariables = cms.vstring("phi","eta"),
        ),
        cms.PSet (
            name = cms.string("photonGenMatchPdgId"),
            title = cms.string(";|PDG ID| of generator particle matched to photon"),
            binsX = cms.untracked.vdouble(600, 0, 600),
            inputVariables = cms.vstring("abs (genMatchedParticle.noFlagsPdgId)"),
            ),
        cms.PSet (
            name = cms.string("photonGenMatchPt"),
            title = cms.string("Gen Photon Transverse Momentum;Gen photon p_{T} [GeV]"),
            binsX = cms.untracked.vdouble(100, 0, 500),
            inputVariables = cms.vstring("genMatchedParticle.noFlags.pt"),
        ),
        cms.PSet (
            name = cms.string("photonGenMatchEta"),
            title = cms.string("Gen Photon Eta;Gen photon #eta"),
            binsX = cms.untracked.vdouble(80, -4, 4),
            inputVariables = cms.vstring("genMatchedParticle.noFlags.eta"),
        ),
        cms.PSet (
            name = cms.string("photonGenMatchPhi"),
            title = cms.string("Gen Photon Phi;Gen photon #phi"),
            binsX = cms.untracked.vdouble(64, -3.2, 3.2),
            inputVariables = cms.vstring("genMatchedParticle.noFlags.phi"),
        ),
    )
)
if os.environ["CMSSW_VERSION"].startswith ("CMSSW_7_6_") or os.environ["CMSSW_VERSION"].startswith ("CMSSW_8_0_"):
    PhotonHistograms.histograms.append(
        cms.PSet (
            name = cms.string("photonGenMatchMotherPdgId"),
            title = cms.string(";|PDG ID| of mother of gen photon"),
            binsX = cms.untracked.vdouble(getPdgBins(["unmatched", "quarks", "leptons", "bosons"])),
            inputVariables = cms.vstring("abs(genMatchedParticle.noFlags.mother_.pdgId)"),
        ),
        )
elif os.environ["CMSSW_VERSION"].startswith ("CMSSW_9_4_") or os.environ["CMSSW_VERSION"].startswith ("CMSSW_10_2_"):
    PhotonHistograms.histograms.append(
        cms.PSet (
            name = cms.string("photonGenMatchMotherPdgId"),
            title = cms.string(";|PDG ID| of mother of gen photon"),
            binsX = cms.untracked.vdouble(getPdgBins(["unmatched", "quarks", "leptons", "bosons"])),
            inputVariables = cms.vstring("abs(genMatchedParticle.noFlags.motherRef.pdgId)"),
        ),
        )



##############################################################################################

MetHistograms = cms.PSet(
    inputCollection = cms.vstring("mets"),
    histograms = cms.VPSet (
        cms.PSet (
            name = cms.string("metPt"),
            title = cms.string("Missing E_{T};E_{T}^{miss} [GeV]"),
            binsX = cms.untracked.vdouble(100, 0, 500),
            inputVariables = cms.vstring("pt"),
        ),
        cms.PSet (
            name = cms.string("metPhi"),
            title = cms.string("Phi of Missing E_{T};#phi(E_{T}^{miss})"),
            binsX = cms.untracked.vdouble(64, -3.2, 3.2),
            inputVariables = cms.vstring("phi"),
        ),
    )
)

##############################################################################################

TrackHistograms = cms.PSet(
     inputCollection = cms.vstring("tracks"),
     histograms = cms.VPSet (
        cms.PSet (
            name = cms.string("trackPt"),
            title = cms.string("Track Transverse Momentum;track p_{T} [GeV]"),
            binsX = cms.untracked.vdouble(100, 10, 510),
            inputVariables = cms.vstring("pt"),
        ),
        cms.PSet (
             name = cms.string("trackEta"),
             title = cms.string("Track Eta;track #eta"),
             binsX = cms.untracked.vdouble(60, -3, 3),
             inputVariables = cms.vstring("eta"),
        ),
        cms.PSet (
             name = cms.string("trackEtaMag"),
             title = cms.string("Track Eta;track |#eta|"),
             binsX = cms.untracked.vdouble(30, 0, 3),
             inputVariables = cms.vstring("fabs(eta)"),
        ),
        cms.PSet (
             name = cms.string("trackPhi"),
             title = cms.string("Track Phi;track #phi"),
             binsX = cms.untracked.vdouble(64, -3.2, 3.2),
             inputVariables = cms.vstring("phi"),
        ),
        cms.PSet (
            name = cms.string("trackEtaVsPhi"),
            title = cms.string("#eta vs #phi;track #eta;track #phi"),
            binsX = cms.untracked.vdouble(60, -3, 3),
            binsY = cms.untracked.vdouble(64, -3.2, 3.2),
            inputVariables = cms.vstring("eta", "phi"),
        ),
        cms.PSet (
            name = cms.string("trackd0"),
            title = cms.string("Track d_{0};track d_{0} [cm]"),
            binsX = cms.untracked.vdouble(100, -0.5, 0.5),
            inputVariables = cms.vstring("dxy"),
        ),
        cms.PSet (
            name = cms.string("trackd0Mag"),
            title = cms.string("Track d_{0};track |d_{0}| [cm]"),
            binsX = cms.untracked.vdouble(50, 0.0, 0.5),
            inputVariables = cms.vstring("fabs(dxy)"),
        ),
        cms.PSet (
            name = cms.string("trackdz"),
            title = cms.string("Track d_{z};track d_{z} [cm]"),
            binsX = cms.untracked.vdouble(60, -30, 30),
            inputVariables = cms.vstring("dz"),
        ),
        cms.PSet (
            name = cms.string("trackdzMag"),
            title = cms.string("Track d_{z};track |d_{z}| [cm]"),
            binsX = cms.untracked.vdouble(30, 0, 30),
            inputVariables = cms.vstring("fabs(dz)"),
        ),
        cms.PSet (
            name = cms.string("trackNumValidPixelHits"),
            title = cms.string("Track Number of Valid Pixel Hits;number of valid pixel hits"),
            binsX = cms.untracked.vdouble(10, -0.5, 9.5),
            inputVariables = cms.vstring("hitPattern_.numberOfValidPixelHits"),
        ),
        cms.PSet (
            name = cms.string("trackNumValidHits"),
            title = cms.string("Track Number of Valid Hits;number of valid hits"),
            binsX = cms.untracked.vdouble(100, -0.5, 99.5),
            inputVariables = cms.vstring("hitPattern_.numberOfValidHits"),
        ),
        cms.PSet (
            name = cms.string("trackNumLayersWithMeasurement"),
            title = cms.string("Track Number of Layers with Measurement;number of layers with measurement"),
            binsX = cms.untracked.vdouble(20, -0.5, 19.5),
            inputVariables = cms.vstring("hitPattern_.trackerLayersWithMeasurement"),
        ),
        cms.PSet (
            name = cms.string("trackChi2"),
            title = cms.string("Track Reduced Chi2;track #chi^{2}/ndf"),
            binsX = cms.untracked.vdouble(50, 0, 10),
            inputVariables = cms.vstring("normalizedChi2"),
        ),
        cms.PSet (
            name = cms.string("trackCharge"),
            title = cms.string("Track Charge;track charge"),
            binsX = cms.untracked.vdouble(3, -1.5, 1.5),
            inputVariables = cms.vstring("charge"),
        ),
        cms.PSet (
            name = cms.string("noFlagsPdgId"),
            title = cms.string(";|PDG ID| of generator particle matched to track"),
            binsX = cms.untracked.vdouble(getPdgBins(["unmatched", "quarks", "leptons", "bosons"])),
            inputVariables = cms.vstring("abs (genMatchedParticle.noFlagsPdgId)"),
            ),
        cms.PSet (
            name = cms.string("genMatchedPromptFinalStateIsMatched"),
            title = cms.string(";track is matched to generator particle"),
            binsX = cms.untracked.vdouble(2.0, -0.5, 1.5),
            inputVariables = cms.vstring("genMatchedParticle.promptFinalState.isNonnull"),
        ),
        cms.PSet (
            name = cms.string("genMatchedPromptFinalStatePdgId"),
            title = cms.string(";|PDG ID| of matched generator particle"),
            binsX = cms.untracked.vdouble(getPdgBins(["quarks", "leptons", "bosons", "hadrons"])),
            inputVariables = cms.vstring("abs (genMatchedParticle.promptFinalState.pdgId)"),
        ),
        cms.PSet (
            name = cms.string("genMatchedPromptFinalStatePdgIdNoHadrons"),
            title = cms.string(";|PDG ID| of matched generator particle"),
            binsX = cms.untracked.vdouble(getPdgBins(["quarks", "leptons", "bosons"])),
            inputVariables = cms.vstring("abs (genMatchedParticle.promptFinalState.pdgId)"),
        ),
        cms.PSet (
            name = cms.string("genMatchedDirectPromptTauDecayProductFinalStateIsMatched"),
            title = cms.string(";track is matched to generator #tau decay product"),
            binsX = cms.untracked.vdouble(2.0, -0.5, 1.5),
            inputVariables = cms.vstring("genMatchedParticle.directPromptTauDecayProductFinalState.isNonnull"),
        ),
        cms.PSet (
            name = cms.string("genMatchedDirectPromptTauDecayProductFinalStatePdgId"),
            title = cms.string(";|PDG ID| of matched generator #tau decay product"),
            binsX = cms.untracked.vdouble(getPdgBins(["quarks", "leptons", "bosons", "hadrons"])),
            inputVariables = cms.vstring("abs (genMatchedParticle.directPromptTauDecayProductFinalState.pdgId)"),
        ),
        cms.PSet (
            name = cms.string("genMatchedDirectPromptTauDecayProductFinalStatePdgIdNoHadrons"),
            title = cms.string(";|PDG ID| of matched generator #tau decay product"),
            binsX = cms.untracked.vdouble(getPdgBins(["quarks", "leptons", "bosons"])),
            inputVariables = cms.vstring("abs (genMatchedParticle.directPromptTauDecayProductFinalState.pdgId)"),
        ),
        cms.PSet (
            name = cms.string("DeepSetsElectronScore"),
            title = cms.string(";Deep Sets Electron Score"),
            binsX = cms.untracked.vdouble(50.0, 0.0, 1.0),
            inputVariables = cms.vstring("deepSetsElectronScore"),
        ),
        cms.PSet (
            name = cms.string("fakeTrackScore"),
            title = cms.string(";Fake Track NN Score"),
            binsX = cms.untracked.vdouble(50.0, 0.0, 1.0),
            inputVariables = cms.vstring("fakeTrackScore"),
        )
    )
)

##############################################################################################

TrackBeamspotHistograms = cms.PSet(
     inputCollection = cms.vstring("tracks", "beamspots"),
     histograms = cms.VPSet (
        cms.PSet (
            name = cms.string("trackd0"),
            title = cms.string("Track d_{0};track d_{0} [cm]"),
            binsX = cms.untracked.vdouble(100, -0.5, 0.5),
            inputVariables = cms.vstring(trackD0WRTBeamspot),
        ),
        cms.PSet (
            name = cms.string("trackd0Mag"),
            title = cms.string("Track d_{0};track |d_{0}| [cm]"),
            binsX = cms.untracked.vdouble(50, 0, 0.5),
            inputVariables = cms.vstring("fabs ( " + trackD0WRTBeamspot + " )"),
        ),
        cms.PSet (
            name = cms.string("trackdz"),
            title = cms.string("Track d_{z};track d_{z} [cm]"),
            binsX = cms.untracked.vdouble(60, -30, 30),
            inputVariables = cms.vstring("(track.vz - beamspot.z0) - ((track.vx - beamspot.x0) * track.px + (track.vy - beamspot.y0) * track.py) / track.pt * (track.pz / track.pt)"),
        ),
        cms.PSet (
            name = cms.string("trackdzMag"),
            title = cms.string("Track d_{z};track |d_{z}| [cm]"),
            binsX = cms.untracked.vdouble(30, 0, 30),
            inputVariables = cms.vstring("fabs((track.vz - beamspot.z0) - ((track.vx - beamspot.x0) * track.px + (track.vy - beamspot.y0) * track.py) / track.pt * (track.pz / track.pt))"),
        ),
    )
)


##############################################################################################

TrackEventVarHistograms = cms.PSet(
    # To produce these histograms, include in your PSet:
    # variableProducers.append("PrimaryVtxVarProducer")
     inputCollection = cms.vstring("tracks", "eventvariables"),
     histograms = cms.VPSet (
        cms.PSet (
            name = cms.string("trackd0WRTPV"),
            title = cms.string("Track d_{0} wrt leading PV;track d_{0} [cm]"),
            binsX = cms.untracked.vdouble(100, -0.5, 0.5),
            inputVariables = cms.vstring('track.dxy'),
        ),
        cms.PSet (
            name = cms.string("trackd0WRTPV_Zoom"),
            title = cms.string("Track d_{0} wrt leading PV;track d_{0} [cm]"),
            binsX = cms.untracked.vdouble(100, -0.1, 0.1),
            inputVariables = cms.vstring('track.dxy'),
        ),
        cms.PSet (
            name = cms.string("trackd0WRTPVMag"),
            title = cms.string("Track d_{0} wrt leading PV;track |d_{0}| [cm]"),
            binsX = cms.untracked.vdouble(50, 0, 0.5),
            inputVariables = cms.vstring("fabs ( " + 'track.dxy' + " )"),
        ),
        cms.PSet (
            name = cms.string("trackdzWRTPV"),
            title = cms.string("Track d_{z} wrt leading PV;track d_{z} [cm]"),
            binsX = cms.untracked.vdouble(100, -10, 10),
            inputVariables = cms.vstring('track.dz'),
        ),
        cms.PSet (
            name = cms.string("trackdzWRTPV_Zoom"),
            title = cms.string("Track d_{z} wrt leading PV;track d_{z} [cm]"),
            binsX = cms.untracked.vdouble(100, -2, 2),
            inputVariables = cms.vstring('track.dz'),
        ),
        cms.PSet (
            name = cms.string("trackdzWRTPVMag"),
            title = cms.string("Track d_{z} wrt leading PV;track |d_{z}| [cm]"),
            binsX = cms.untracked.vdouble(100, 0, 10),
            inputVariables = cms.vstring("fabs( " + 'track.dz' + " )" ),
        ),
    )
)
##############################################################################################

TrackMCParticleHistograms = cms.PSet(
    inputCollection = cms.vstring("track-mcparticle pairs"),
    histograms = cms.VPSet (
        cms.PSet (
            name = cms.string("TrackMCPartDeltaEta"),
            title = cms.string("Track-MCParticle Eta Difference;|#Delta(#eta)|"),
            binsX = cms.untracked.vdouble(100, 0, 10),
            inputVariables = cms.vstring("deltaEta"),
            ),
        cms.PSet (
            name = cms.string("TrackMCPartDeltaPhi"),
            title = cms.string("Track-MCParticle Phi Difference;|#Delta(#phi)|"),
            binsX = cms.untracked.vdouble(32, 0, 3.2),
            inputVariables = cms.vstring("deltaPhi"),
            ),
        cms.PSet (
            name = cms.string("TrackMCPartDeltaR"),
            title = cms.string("Track-MCParticle #DeltaR;#DeltaR"),
            binsX = cms.untracked.vdouble(100, 0, 10),
            inputVariables = cms.vstring("deltaR"),
            ),
        cms.PSet (
            name = cms.string("TrackMCPartDeltaRZoom"),
            title = cms.string("Track-MCParticle #DeltaR;#DeltaR"),
            binsX = cms.untracked.vdouble(100, 0, 1),
            inputVariables = cms.vstring("deltaR"),
            ),
        cms.PSet (
            name = cms.string("TrackMCPart3DAngle"),
            title = cms.string("Track-MCParticle 3D Angle;3D angle"),
            binsX = cms.untracked.vdouble(100, 0, 4),
            inputVariables = cms.vstring("threeDAngle"),
            ),
        )
    )

##############################################################################################

EventVariablePVHistograms = cms.PSet(
    # EventVariable quantities associated with primary vertices
    # To produce these variables, include in your PSet:
    # variableProducers.append("PrimaryVtxVarProducer")
    inputCollection = cms.vstring("eventvariables"),
    histograms = cms.VPSet (
        cms.PSet (
            name = cms.string("numPVReco"),
            title = cms.string(";Number of Primary Vertices"),
            binsX = cms.untracked.vdouble(50, 0.0, 50.0),
            inputVariables = cms.vstring("numPVReco"),
        ),
        cms.PSet (
            name = cms.string("leadingPV_x"),
            title = cms.string(";X Position of Leading Primary Vertex"),
            binsX = cms.untracked.vdouble(50, -1.0, 1.0),
            inputVariables = cms.vstring("leadingPV_x"),
        ),
        cms.PSet (
            name = cms.string("leadingPV_y"),
            title = cms.string(";Y Position of Leading Primary Vertex"),
            binsX = cms.untracked.vdouble(50, -1.0, 1.0),
            inputVariables = cms.vstring("leadingPV_y"),
        ),
        cms.PSet (
            name = cms.string("leadingPV_z"),
            title = cms.string(";Z Position of Leading Primary Vertex"),
            binsX = cms.untracked.vdouble(50, -20.0, 20.0),
            inputVariables = cms.vstring("leadingPV_z"),
        ),
    )
)

##############################################################################################