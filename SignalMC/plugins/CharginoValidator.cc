#include "DisappTrks/SignalMC/plugins/CharginoValidator.h"

CharginoValidator::CharginoValidator(const edm::ParameterSet &cfg) :
  genParticles_     (cfg.getParameter<edm::InputTag>("genParticles")),
  genMets_          (cfg.getParameter<edm::InputTag>("genMets")),
  tracks_           (cfg.getParameter<edm::InputTag>("tracks")),
  pfmet_            (cfg.getParameter<edm::InputTag>("pfmet")),
  muonsCol_         (cfg.getParameter<edm::InputTag>("muonsCol")),
  cutPythia8Flag_   (cfg.getUntrackedParameter<bool>("cutPythia8Flag", false))
{
  TH1::SetDefaultSumw2();
  vector<double> bins;
  logSpace (100, 0.0, 3.0, bins);

  vector<double> bins2;
  logSpace (62, 0.0, 2.5, bins2);
  bins2.push_back(10000.0);

  oneDHists_["nCharginos"] = fs_->make<TH1D>("nCharginos", ";number of charginos", 5, -0.5, 4.5);
  oneDHists_["genCharge"] = fs_->make<TH1D>("genCharge", ";generator chargino charge", 3, -1.5, 1.5);
  oneDHists_["genMass"] = fs_->make<TH1D>("genMass", ";generator chargino mass [GeV]", 1000, -0.5, 999.5);
  oneDHists_["genPt"] = fs_->make<TH1D>("genPt", ";generator chargino p_{T} [GeV]", 100, 0.0, 2000.0);
  oneDHists_["genPhi"] = fs_->make<TH1D>("genPhi", ";generator chargino #phi", 50, -3.2, 3.2);
  oneDHists_["genEta"] = fs_->make<TH1D>("genEta", ";generator chargino #eta", 50, -5.0, 5.0);
  oneDHists_["genEtaCut"] = fs_->make<TH1D>("genEtaCut", ";pt cut generator chargino #eta", 50, -5.0, 5.0);
  oneDHists_["genP"] = fs_->make<TH1D>("genP", ";generator chargino p [GeV]", 500, 0.0, 2000.0);
  oneDHists_["genBeta"] = fs_->make<TH1D>("genBeta", ";generator chargino #beta", 500, 0.0, 1.0);
  oneDHists_["genGamma"] = fs_->make<TH1D>("genGamma", ";generator chargino #gamma", 500, 0.0, 100.0);
  oneDHists_["genBetaGamma"] = fs_->make<TH1D>("genBetaGamma", ";generator chargino #beta#gamma", 500, 0.0, 100.0);
  oneDHists_["genBetaGammaM"] = fs_->make<TH1D>("genBetaGammaM", ";generator chargino #beta#gammam [GeV]", 500, 0.0, 1000.0);

  oneDHists_["genPtPion"] = fs_->make<TH1D>("genPtPion", ";generator pion p_{T} [GeV]", 22, 0.0, 2.0);
  oneDHists_["genPPion"] = fs_->make<TH1D>("genPPion", ";generator pion p [GeV]", 20, 0.0, 2.0);

  oneDHists_["genMet"] = fs_->make<TH1D>("genMet", ";generator MET [GeV]", 100, 0.0, 2000.0);
  oneDHists_["pfMet"] = fs_->make<TH1D>("pfMet", ";reco (PF) MET [GeV]", 100, 0.0, 2000.0);
  oneDHists_["FSumPt"] = fs_->make<TH1D>("FSumPt", ";p_{T}(F#bar{F}) [GeV]", 100, 0, 2000);
  oneDHists_["ewkinoSumPtLog"] = fs_->make<TH1D> ("ewkinoSumPtLog", ";p_{T}(#chi^{#pm}#chi^{#pm}/#chi^{#pm}#chi^{0}) [GeV]", bins.size () - 1, bins.data ());
  oneDHists_["ewkinoSumPtLogDiffbin"] = fs_->make<TH1D> ("ewkinoSumPtLogDiffbin", ";p_{T}(#chi^{#pm}#chi^{#pm}/#chi^{#pm}#chi^{0}) [GeV]", bins2.size () - 1, bins2.data ());

  oneDHists_["ZPtLog"] = fs_->make<TH1D> ("ZPtLog", ";p_{T}(Z) [GeV]", bins.size () - 1, bins.data ());
  oneDHists_["ZPt"] = fs_->make<TH1D> ("ZPt", ";p_{T}(Z) [GeV]", 50, 0, 250);
  oneDHists_["ZMass"] = fs_->make<TH1D> ("ZMass", ";mass(Z) [GeV]", 100, 0, 200);

  const Int_t NBINS = 35;
  Double_t edges[NBINS + 1] = {0.0, 20.0, 40.0, 60.0, 80.0, 100.0, 120.0, 140.0, 160.0, 180.0, 200.0, 220.0, 240.0, 260.0, 280.0, 300.0, 320.0, 340.0, 360.0, 380.0, 400.0, 420.0, 440.0, 460.0, 480.0, 500.0, 600.0, 700.0, 800.0, 900.0, 1000.0, 1200.0, 1400.0, 1600.0, 1800.0, 2000.0};
  oneDHists_["FSumPtDiffbin"] = fs_->make<TH1D>("FSumPtDiffbin", ";p_{T}(F#bar{F}) [GeV]", 35, edges);

  oneDHists_["DMSumPt"] = fs_->make<TH1D>("DMSumPt", ";p_{T}(ss) [GeV]", 100, 0, 2000);
  oneDHists_["InvisibleSumPt"] = fs_->make<TH1D>("InvisibleSumPt", ";p_{T}(Invisible) [GeV]", 100, 0, 2000);
  oneDHists_["InvisibleSumPt_without1000023"] = fs_->make<TH1D>("InvisibleSumPt_without1000023", ";p_{T}(Invisible - 1000023) [GeV]", 100, 0, 2000);

  oneDHists_["genDecayLength_10"] = fs_->make<TH1D>("genDecayLength_10", ";generator chargino decay length [cm]", 200, 0.0, 10.0);
  oneDHists_["genDecayLength_100"] = fs_->make<TH1D>("genDecayLength_100", ";generator chargino decay length [cm]", 200, 0.0, 100.0);
  oneDHists_["genDecayLength_1000"] = fs_->make<TH1D>("genDecayLength_1000", ";generator chargino decay length [cm]", 200, 0.0, 1000.0);
  oneDHists_["genDecayLength_10000"] = fs_->make<TH1D>("genDecayLength_10000", ";generator chargino decay length [cm]", 200, 0.0, 10000.0);
  oneDHists_["genDecayLength_100000"] = fs_->make<TH1D>("genDecayLength_100000", ";generator chargino decay length [cm]", 200, 0.0, 100000.0);

  oneDHists_["genCTau_10"] = fs_->make<TH1D>("genCTau_10", ";generator chargino c#tau [cm]", 200, 0.0, 10.0);
  oneDHists_["genCTau_100"] = fs_->make<TH1D>("genCTau_100", ";generator chargino c#tau [cm]", 200, 0.0, 100.0);
  oneDHists_["genCTau_1000"] = fs_->make<TH1D>("genCTau_1000", ";generator chargino c#tau [cm]", 200, 0.0, 1000.0);
  oneDHists_["genCTau_10000"] = fs_->make<TH1D>("genCTau_10000", ";generator chargino c#tau [cm]", 200, 0.0, 10000.0);
  oneDHists_["genCTau_100000"] = fs_->make<TH1D>("genCTau_100000", ";generator chargino c#tau [cm]", 200, 0.0, 100000.0);

  oneDHists_["matchedTrack"] = fs_->make<TH1D>("matchedTrack", ";matched track found", 2, -0.5, 1.5);
  oneDHists_["charge"] = fs_->make<TH1D>("charge", ";track charge", 3, -1.5, 1.5);
  oneDHists_["pt"] = fs_->make<TH1D>("pt", ";track p_{T} [GeV]", 100, 0.0, 1000.0);
  oneDHists_["phi"] = fs_->make<TH1D>("phi", ";track #phi", 50, -3.2, 3.2);
  oneDHists_["eta"] = fs_->make<TH1D>("eta", ";track #eta", 50, -5.0, 5.0);

  oneDHists_["allTracksCharge"] = fs_->make<TH1D>("allTracksCharge", ";all track charge", 3, -1.5, 1.5);
  oneDHists_["allTracksPt"] = fs_->make<TH1D>("allTracksPt", ";all track p_{T} [GeV]", 100, 0.0, 1000.0);
  oneDHists_["allTracksPhi"] = fs_->make<TH1D>("allTracksPhi", ";all track #phi", 50, -3.2, 3.2);
  oneDHists_["allTracksEta"] = fs_->make<TH1D>("allTracksEta", ";all track #eta", 50, -5.0, 5.0);

  oneDHists_["ptCutTracksCharge"] = fs_->make<TH1D>("ptCutTracksCharge", ";p_{T} > 50 GeV track charge", 3, -1.5, 1.5);
  oneDHists_["ptCutTracksPt"] = fs_->make<TH1D>("ptCutTracksPt", ";p_{T} > 50 GeV track p_{T} [GeV]", 100, 0.0, 1000.0);
  oneDHists_["ptCutTracksPhi"] = fs_->make<TH1D>("ptCutTracksPhi", ";p_{T} > 50 GeV track #phi", 50, -3.2, 3.2);
  oneDHists_["ptCutTracksEta"] = fs_->make<TH1D>("ptCutTracksEta", ";p_{T} > 50 GeV track #eta", 50, -5.0, 5.0);

  oneDHists_["numberOfValidHits"] = fs_->make<TH1D>("numberOfValidHits", ";track number of valid hits", 100, -0.5, 99.5);
  oneDHists_["numberOfMissingInnerHits"] = fs_->make<TH1D>("numberOfMissingInnerHits", ";track number of missing inner layers", 20, -0.5, 19.5);
  oneDHists_["numberOfMissingMiddleHits"] = fs_->make<TH1D>("numberOfMissingMiddleHits", ";track number of missing middle layers", 20, -0.5, 19.5);
  oneDHists_["numberOfMissingOuterHits"] = fs_->make<TH1D>("numberOfMissingOuterHits", ";track number of missing outer layers", 20, -0.5, 19.5);
  oneDHists_["numberOfValidLayers"] = fs_->make<TH1D>("numberOfValidLayers", ";track number of valid layers", 21, -0.5, 20.5);

  oneDHists_["smallCtauNumberOfValidHits"] = fs_->make<TH1D>("smallCtauNumberOfValidHits", ";small c#tau track number of valid hits", 100, -0.5, 99.5);
  oneDHists_["smallCtauNumberOfMissingInnerHits"] = fs_->make<TH1D>("smallCtauNumberOfMissingInnerHits", ";small c#tau track number of missing inner layers", 20, -0.5, 19.5);
  oneDHists_["smallCtauNumberOfMissingMiddleHits"] = fs_->make<TH1D>("smallCtauNumberOfMissingMiddleHits", ";small c#tau track number of missing middle layers", 20, -0.5, 19.5);
  oneDHists_["smallCtauNumberOfMissingOuterHits"] = fs_->make<TH1D>("smallCtauNumberOfMissingOuterHits", ";small c#tau track number of missing outer layers", 20, -0.5, 19.5);

  oneDHists_["largeCtauTracksCharge"] = fs_->make<TH1D>("largeCtauTracksCharge", ";large c#tau track charge", 3, -1.5, 1.5);
  oneDHists_["largeCtauTracksPt"] = fs_->make<TH1D>("largeCtauTracksPt", ";large c#tau track p_{T} [GeV]", 100, 0.0, 1000.0);
  oneDHists_["largeCtauTracksPhi"] = fs_->make<TH1D>("largeCtauTracksPhi", ";large c#tau track #phi", 50, -3.2, 3.2);
  oneDHists_["largeCtauTracksEta"] = fs_->make<TH1D>("largeCtauTracksEta", ";large c#tau track #eta", 50, -5.0, 5.0);
  oneDHists_["largeCtauNumberOfValidHits"] = fs_->make<TH1D>("largeCtauNumberOfValidHits", ";large c#tau track number of valid hits", 100, -0.5, 99.5);
  oneDHists_["largeCtauNumberOfMissingInnerHits"] = fs_->make<TH1D>("largeCtauNumberOfMissingInnerHits", ";large c#tau track number of missing inner layers", 20, -0.5, 19.5);
  oneDHists_["largeCtauNumberOfMissingMiddleHits"] = fs_->make<TH1D>("largeCtauNumberOfMissingMiddleHits", ";large c#tau track number of missing middle layers", 20, -0.5, 19.5);
  oneDHists_["largeCtauNumberOfMissingOuterHits"] = fs_->make<TH1D>("largeCtauNumberOfMissingOuterHits", ";large c#tau track number of missing outer layers", 20, -0.5, 19.5);

  oneDHists_["largeMissOutTracksCharge"] = fs_->make<TH1D>("largeMissOutTracksCharge", ";large c#tau track charge", 3, -1.5, 1.5);
  oneDHists_["largeMissOutTracksPt"] = fs_->make<TH1D>("largeMissOutTracksPt", ";large c#tau track p_{T} [GeV]", 100, 0.0, 1000.0);
  oneDHists_["largeMissOutTracksPhi"] = fs_->make<TH1D>("largeMissOutTracksPhi", ";large c#tau track #phi", 50, -3.2, 3.2);
  oneDHists_["largeMissOutTracksEta"] = fs_->make<TH1D>("largeMissOutTracksEta", ";large c#tau track #eta", 50, -5.0, 5.0);

  oneDHists_["chargeClosest"] = fs_->make<TH1D>("chargeClosest", ";track charge", 3, -1.5, 1.5);
  oneDHists_["ptClosest"] = fs_->make<TH1D>("ptClosest", ";track p_{T} [GeV]", 100, 0.0, 1000.0);
  oneDHists_["phiClosest"] = fs_->make<TH1D>("phiClosest", ";track #phi", 50, -3.2, 3.2);
  oneDHists_["etaClosest"] = fs_->make<TH1D>("etaClosest", ";track #eta", 50, -5.0, 5.0);

  oneDHists_["chargeCTauCut"] = fs_->make<TH1D>("chargeCTauCut", ";track charge", 3, -1.5, 1.5);
  oneDHists_["ptCTauCut"] = fs_->make<TH1D>("ptCTauCut", ";track p_{T} [GeV]", 100, 0.0, 1000.0);
  oneDHists_["phiCTauCut"] = fs_->make<TH1D>("phiCTauCut", ";track #phi", 50, -3.2, 3.2);
  oneDHists_["etaCTauCut"] = fs_->make<TH1D>("etaCTauCut", ";track #eta", 50, -5.0, 5.0);

  oneDHists_["numberOfValidHitsClosest"] = fs_->make<TH1D>("numberOfValidHitsClosest", ";track number of valid hits", 100, -0.5, 99.5);
  oneDHists_["numberOfMissingInnerHitsClosest"] = fs_->make<TH1D>("numberOfMissingInnerHitsClosest", ";track number of missing inner layers", 20, -0.5, 19.5);
  oneDHists_["numberOfMissingMiddleHitsClosest"] = fs_->make<TH1D>("numberOfMissingMiddleHitsClosest", ";track number of missing middle layers", 20, -0.5, 19.5);
  oneDHists_["numberOfMissingOuterHitsClosest"] = fs_->make<TH1D>("numberOfMissingOuterHitsClosest", ";track number of missing outer layers", 20, -0.5, 19.5);

  oneDHists_["matchedMuon"] = fs_->make<TH1D>("matchedMuon", ";matched track found", 2, -0.5, 1.5);
  oneDHists_["chargeMuon"] = fs_->make<TH1D>("chargeMuon", ";track charge", 3, -1.5, 1.5);
  oneDHists_["ptMuon"] = fs_->make<TH1D>("ptMuon", ";track p_{T} [GeV]", 100, 0.0, 1000.0);
  oneDHists_["phiMuon"] = fs_->make<TH1D>("phiMuon", ";track #phi", 50, -3.2, 3.2);
  oneDHists_["etaMuon"] = fs_->make<TH1D>("etaMuon", ";track #eta", 50, -5.0, 5.0);

  oneDHists_["numberOfValidHitsBarrel"] = fs_->make<TH1D>("numberOfValidHitsBarrel", ";track number of valid hits in barrel", 36, -0.5, 35.5);
  oneDHists_["numberOfValidHitsEndcap"] = fs_->make<TH1D>("numberOfValidHitsEndcap", ";track number of valid hits in endcap", 36, -0.5, 35.5);

  twoDHists_["numberOfValidHitsVsnumberOfMissingInnerHits"] = fs_->make<TH2D>("numberOfValidHitsVsnumberOfMissingInnerHits", ";track number of valid hits;track number of missing inner layers", 36, -0.5, 35.5, 20, -0.5, 19.5);
  twoDHists_["numberOfValidHitsVsnumberOfMissingMiddleHits"] = fs_->make<TH2D>("numberOfValidHitsVsnumberOfMissingMiddleHits", ";track number of valid hits;track number of missing middle layers", 36, -0.5, 35.5, 20, -0.5, 19.5);
  twoDHists_["numberOfValidHitsVsnumberOfMissingOuterHits"] = fs_->make<TH2D>("numberOfValidHitsVsnumberOfMissingOuterHits", ";track number of valid hits;track number of missing outer layers", 36, -0.5, 35.5, 20, -0.5, 19.5);

  twoDHists_["trackChargeVsCharginoCTau"] = fs_->make<TH2D>("trackChargeVsCharginoCTau", ";matched track charge;gen chargino c#tau [cm]", 3, -1.5, 1.5, 30, 0.0, 30000.0);
  twoDHists_["trackPtVsCharginoCTau"] = fs_->make<TH2D>("trackPtVsCharginoCTau", ";matched track p_{T} [GeV];gen chargino c#tau [cm]", 100, 0.0, 1000.0, 30, 0.0, 30000.0);
  twoDHists_["trackEtaVsCharginoCTau"] = fs_->make<TH2D>("trackEtaVsCharginoCTau", ";matched track #eta;gen chargino c#tau [cm]", 50, -5.0, 5.0, 30, 0.0, 30000.0);
  twoDHists_["trackPhiVsCharginoCTau"] = fs_->make<TH2D>("trackPhiVsCharginoCTau", ";matched track #phi;gen chargino c#tau [cm]", 50, -3.2, 3.2, 30, 0.0, 30000.0);
  twoDHists_["trackEtaVsCharginoDecayLength"] = fs_->make<TH2D>("trackEtaVsCharginoDecayLength", ";matched track #eta;gen chargino decay length [cm]", 50, -5.0, 5.0, 30, 0.0, 30000.0);
  twoDHists_["charginoEtaVsCharginoCTau"] = fs_->make<TH2D>("charginoEtaVsCharginoCTau", ";generated chargino #eta;gen chargino c#tau [cm]", 50, -5.0, 5.0, 30, 0.0, 30000.0);
  twoDHists_["charginoEtaVsCharginoT"] = fs_->make<TH2D>("charginoEtaVsCharginoT", ";generated chargino #eta;gen chargino t [ns]", 50, -5.0, 5.0, 50, 0.0, 150000.0);
  twoDHists_["trackEtaVsCharginoT"] = fs_->make<TH2D>("trackEtaVsCharginoT", ";track #eta;gen chargino t [ns]", 50, -5.0, 5.0, 50, 0.0, 150000.0);
  twoDHists_["charginoEtaVsCharginoTau"] = fs_->make<TH2D>("charginoEtaVsCharginoTau", ";generated chargino #eta;gen chargino #tau [ns]", 50, -5.0, 5.0, 50, 0.0, 150000.0);
  twoDHists_["trackEtaVsCharginoTau"] = fs_->make<TH2D>("trackEtaVsCharginoTau", ";track #eta;gen chargino #tau [ns]", 50, -5.0, 5.0, 50, 0.0, 150000.0);

  twoDHists_["largeMissOutTrackChargeVsCharginoCTau"] = fs_->make<TH2D>("largeMissOutTrackChargeVsCharginoCTau", ";missOut cut matched track charge;gen chargino c#tau [cm]", 3, -1.5, 1.5, 30, 0.0, 30000.0);
  twoDHists_["largeMissOutTrackPtVsCharginoCTau"] = fs_->make<TH2D>("largeMissOutTrackPtVsCharginoCTau", ";missOut cut matched track p_{T} [GeV];gen chargino c#tau [cm]", 100, 0.0, 1000.0, 30, 0.0, 30000.0);
  twoDHists_["largeMissOutTrackEtaVsCharginoCTau"] = fs_->make<TH2D>("largeMissOutTrackEtaVsCharginoCTau", ";missOut cut matched track #eta;gen chargino c#tau [cm]", 50, -5.0, 5.0, 30, 0.0, 30000.0);
  twoDHists_["largeMissOutTrackPhiVsCharginoCTau"] = fs_->make<TH2D>("largeMissOutTrackPhiVsCharginoCTau", ";missOut cut matched track #phi;gen chargino c#tau [cm]", 50, -3.2, 3.2, 30, 0.0, 30000.0);
  twoDHists_["largeMissOutTrackEtaVsCharginoDecayLength"] = fs_->make<TH2D>("largeMissOutTrackEtaVsCharginoDecayLength", ";missOut cut matched track #eta;gen chargino decay length [cm]", 50, -5.0, 5.0, 30, 0.0, 30000.0);
  twoDHists_["largeMissOutTrackEtaVsCharginoT"] = fs_->make<TH2D>("largeMissOutTrackEtaVsCharginoT", ";missOut cut track #eta;gen chargino t [ns]", 50, -5.0, 5.0, 50, 0.0, 150000.0);
  twoDHists_["largeMissOutTrackEtaVsCharginoTau"] = fs_->make<TH2D>("largeMissOutTrackEtaVsCharginoTau", ";missOut cut track #eta;gen chargino #tau [ns]", 50, -5.0, 5.0, 50, 0.0, 150000.0);

  oneDHists_["charginoEta1000"] = fs_->make<TH1D>("charginoEta1000", ";chargino #eta (c#tau < 1000 cm)", 50, -5.0, 5.0);
  oneDHists_["charginoEta2000"] = fs_->make<TH1D>("charginoEta2000", ";chargino #eta (1000 cm < c#tau < 2000 cm)", 50, -5.0, 5.0);
  oneDHists_["charginoEta3000"] = fs_->make<TH1D>("charginoEta3000", ";chargino #eta (2000 cm < c#tau < 3000 cm)", 50, -5.0, 5.0);
  oneDHists_["charginoEta4000"] = fs_->make<TH1D>("charginoEta4000", ";chargino #eta (3000 cm < c#tau < 4000 cm)", 50, -5.0, 5.0);
  oneDHists_["charginoEta5000"] = fs_->make<TH1D>("charginoEta5000", ";chargino #eta (4000 cm < c#tau < 5000 cm)", 50, -5.0, 5.0);
  oneDHists_["charginoEta6000"] = fs_->make<TH1D>("charginoEta6000", ";chargino #eta (5000 cm < c#tau < 6000 cm)", 50, -5.0, 5.0);
  oneDHists_["charginoEta7000"] = fs_->make<TH1D>("charginoEta7000", ";chargino #eta (6000 cm < c#tau < 7000 cm)", 50, -5.0, 5.0);
  oneDHists_["charginoEta8000"] = fs_->make<TH1D>("charginoEta8000", ";chargino #eta (7000 cm < c#tau < 8000 cm)", 50, -5.0, 5.0);
  oneDHists_["charginoEta9000"] = fs_->make<TH1D>("charginoEta9000", ";chargino #eta (8000 cm < c#tau < 9000 cm)", 50, -5.0, 5.0);
  oneDHists_["charginoEta10000"] = fs_->make<TH1D>("charginoEta10000", ";chargino #eta (9000 cm < c#tau)", 50, -5.0, 5.0);

  oneDHists_["eta1000"] = fs_->make<TH1D>("eta1000", ";track #eta (c#tau < 1000 cm)", 50, -5.0, 5.0);
  oneDHists_["eta2000"] = fs_->make<TH1D>("eta2000", ";track #eta (1000 cm < c#tau < 2000 cm)", 50, -5.0, 5.0);
  oneDHists_["eta3000"] = fs_->make<TH1D>("eta3000", ";track #eta (2000 cm < c#tau < 3000 cm)", 50, -5.0, 5.0);
  oneDHists_["eta4000"] = fs_->make<TH1D>("eta4000", ";track #eta (3000 cm < c#tau < 4000 cm)", 50, -5.0, 5.0);
  oneDHists_["eta5000"] = fs_->make<TH1D>("eta5000", ";track #eta (4000 cm < c#tau < 5000 cm)", 50, -5.0, 5.0);
  oneDHists_["eta6000"] = fs_->make<TH1D>("eta6000", ";track #eta (5000 cm < c#tau < 6000 cm)", 50, -5.0, 5.0);
  oneDHists_["eta7000"] = fs_->make<TH1D>("eta7000", ";track #eta (6000 cm < c#tau < 7000 cm)", 50, -5.0, 5.0);
  oneDHists_["eta8000"] = fs_->make<TH1D>("eta8000", ";track #eta (7000 cm < c#tau < 8000 cm)", 50, -5.0, 5.0);
  oneDHists_["eta9000"] = fs_->make<TH1D>("eta9000", ";track #eta (8000 cm < c#tau < 9000 cm)", 50, -5.0, 5.0);
  oneDHists_["eta10000"] = fs_->make<TH1D>("eta10000", ";track #eta (9000 cm < c#tau)", 50, -5.0, 5.0);

  tracksToken_         = consumes<vector<reco::Track> >          (tracks_);
  pfmetToken_         = consumes<vector<reco::PFMET> >          (pfmet_);
  genParticlesToken_   = consumes<vector<reco::GenParticle> >    (genParticles_);
  genMetsToken_        = consumes<reco::GenMETCollection>        (genMets_);
  muonsToken_         = consumes<vector<reco::Muon> >          (muonsCol_);
}

CharginoValidator::~CharginoValidator()
{
}

void
CharginoValidator::analyze(const edm::Event &event, const edm::EventSetup &setup)
{

  edm::Handle<vector<reco::Track> > tracks;
  event.getByToken(tracksToken_, tracks);

  edm::Handle<vector<reco::PFMET> > pfmet;
  event.getByToken(pfmetToken_, pfmet);

  edm::Handle<vector<reco::GenParticle> > genParticles;
  event.getByToken(genParticlesToken_, genParticles);

  edm::Handle<reco::GenMETCollection> genMets;
  event.getByToken(genMetsToken_, genMets);

  edm::Handle<vector<reco::Muon> > muons;
  event.getByToken(muonsToken_, muons);

  oneDHists_.at("genMet")->Fill(genMets->front().pt());
  oneDHists_.at("pfMet")->Fill(pfmet->front().pt());

  double genPtCut = 30.0;

  for(const auto &track : *tracks) {
    oneDHists_.at("allTracksCharge")->Fill(track.charge());
    oneDHists_.at("allTracksPt")->Fill(track.pt());
    oneDHists_.at("allTracksPhi")->Fill(track.phi());
    oneDHists_.at("allTracksEta")->Fill(track.eta());
    if(track.pt() < genPtCut) continue;
    oneDHists_.at("ptCutTracksCharge")->Fill(track.charge());
    oneDHists_.at("ptCutTracksPt")->Fill(track.pt());
    oneDHists_.at("ptCutTracksPhi")->Fill(track.phi());
    oneDHists_.at("ptCutTracksEta")->Fill(track.eta());
  }

  unsigned nCharginos = 0;
  unsigned nTracks = 0;
  TLorentzVector l(0.0, 0.0, 0.0, 0.0);
  TLorentzVector l2(0.0, 0.0, 0.0, 0.0);
  for(const auto &genParticle : *genParticles)
    {

      if(abs(genParticle.pdgId()) != 1000024) continue; // Uncomment for charginos
      if(genParticle.numberOfDaughters() == 1) continue; // Uncomment for charginos
      //if(abs(genParticle.pdgId()) != 13) continue; // Uncomment for muons
      //if(abs(genParticle.status()) != 1) continue; // Uncomment for muons
//      bool isNeutralino2 = false;
//      for(unsigned int i = 0; i < genParticle.numberOfDaughters(); ++i){
//          if(abs(genParticle.daughter(i)->pdgId())==1000022) isNeutralino2 = true;
//      }
//      if(isNeutralino2 == false) continue;
      //if(abs(genParticle.status()) == 1) cout << genParticle.pdgId() << "\t" << genParticle.status() << endl;

      nCharginos++;

      TVector3 x(genParticle.vx(), genParticle.vy(), genParticle.vz()),
               y(0.0, 0.0, 0.0);
      double boost = 1.0 /(genParticle.p4().Beta() * genParticle.p4().Gamma());
      getEndVertex(genParticle, y);

      oneDHists_.at("genCharge")->Fill(genParticle.charge());
      oneDHists_.at("genMass")->Fill(genParticle.mass());
      oneDHists_.at("genPt")->Fill(genParticle.pt());
      oneDHists_.at("genPhi")->Fill(genParticle.phi());
      oneDHists_.at("genEta")->Fill(genParticle.eta());
      oneDHists_.at("genP")->Fill(genParticle.p());
      oneDHists_.at("genBeta")->Fill(genParticle.p4().Beta());
      oneDHists_.at("genGamma")->Fill(genParticle.p4().Gamma());
      oneDHists_.at("genBetaGamma")->Fill(genParticle.p4().Beta() * genParticle.p4().Gamma());
      oneDHists_.at("genBetaGammaM")->Fill(genParticle.p4().Beta() * genParticle.p4().Gamma() * genParticle.mass());

      if(genParticle.pt() > genPtCut) oneDHists_.at("genEtaCut")->Fill(genParticle.eta());

      oneDHists_.at("genDecayLength_10")->Fill((x - y).Mag());
      oneDHists_.at("genDecayLength_100")->Fill((x - y).Mag());
      oneDHists_.at("genDecayLength_1000")->Fill((x - y).Mag());
      oneDHists_.at("genDecayLength_10000")->Fill((x - y).Mag());
      oneDHists_.at("genDecayLength_100000")->Fill((x - y).Mag());

      double t = (x - y).Mag() / (genParticle.p4().Beta() * 299792458.0 * 0.000000001);
      double tau = ((x - y).Mag() * boost) / (299792458.0 * 0.000000001);

      oneDHists_.at("genCTau_10")->Fill((x - y).Mag() * boost);
      oneDHists_.at("genCTau_100")->Fill((x - y).Mag() * boost);
      oneDHists_.at("genCTau_1000")->Fill((x - y).Mag() * boost);
      oneDHists_.at("genCTau_10000")->Fill((x - y).Mag() * boost);
      oneDHists_.at("genCTau_100000")->Fill((x - y).Mag() * boost);

      if(((x - y).Mag() * boost) < 1000.0) oneDHists_.at("charginoEta1000")->Fill(genParticle.eta());
      if(((x - y).Mag() * boost) > 1000.0 && ((x - y).Mag() * boost) < 2000.0) oneDHists_.at("charginoEta2000")->Fill(genParticle.eta());
      if(((x - y).Mag() * boost) > 2000.0 && ((x - y).Mag() * boost) < 3000.0) oneDHists_.at("charginoEta3000")->Fill(genParticle.eta());
      if(((x - y).Mag() * boost) > 3000.0 && ((x - y).Mag() * boost) < 4000.0) oneDHists_.at("charginoEta4000")->Fill(genParticle.eta());
      if(((x - y).Mag() * boost) > 4000.0 && ((x - y).Mag() * boost) < 5000.0) oneDHists_.at("charginoEta5000")->Fill(genParticle.eta());
      if(((x - y).Mag() * boost) > 5000.0 && ((x - y).Mag() * boost) < 6000.0) oneDHists_.at("charginoEta6000")->Fill(genParticle.eta());
      if(((x - y).Mag() * boost) > 6000.0 && ((x - y).Mag() * boost) < 7000.0) oneDHists_.at("charginoEta7000")->Fill(genParticle.eta());
      if(((x - y).Mag() * boost) > 7000.0 && ((x - y).Mag() * boost) < 8000.0) oneDHists_.at("charginoEta8000")->Fill(genParticle.eta());
      if(((x - y).Mag() * boost) > 8000.0 && ((x - y).Mag() * boost) < 9000.0) oneDHists_.at("charginoEta9000")->Fill(genParticle.eta());
      if(((x - y).Mag() * boost) > 9000.0) oneDHists_.at("charginoEta10000")->Fill(genParticle.eta());

      twoDHists_.at("charginoEtaVsCharginoCTau")->Fill(genParticle.eta(),((x - y).Mag() * boost));
      twoDHists_.at("charginoEtaVsCharginoT")->Fill(genParticle.eta(),t);
      twoDHists_.at("charginoEtaVsCharginoTau")->Fill(genParticle.eta(),tau);

      if(genParticle.pt() < 10.0)
        {
          oneDHists_.at("matchedTrack")->Fill(-1.0);
          continue;
        }

  // Start comment here with / * to remove tracks ####################################################################

      const reco::Track *track = getMatchedTrack(genParticle, tracks);
      nTracks = getMatchedTrackNumber(genParticle, tracks);

      if(track)
      {
  
        const double deltaphi = deltaPhi(genParticle.phi(),track->phi());
        const double deltaeta = genParticle.eta() - track->eta();
        const double dR = sqrt(pow(deltaphi,2)+pow(deltaeta,2));
  
        if(dR < 0.1)
        {
  
          oneDHists_.at("matchedTrack")->Fill(1.0);
          oneDHists_.at("charge")->Fill(track->charge());
          oneDHists_.at("pt")->Fill(track->pt());
          oneDHists_.at("phi")->Fill(track->phi());
          oneDHists_.at("eta")->Fill(track->eta());

          twoDHists_.at("trackChargeVsCharginoCTau")->Fill(track->charge(),((x - y).Mag() * boost));
          twoDHists_.at("trackPtVsCharginoCTau")->Fill(track->pt(),((x - y).Mag() * boost));
          twoDHists_.at("trackPhiVsCharginoCTau")->Fill(track->phi(),((x - y).Mag() * boost));
          twoDHists_.at("trackEtaVsCharginoCTau")->Fill(track->eta(),((x - y).Mag() * boost));
          twoDHists_.at("trackEtaVsCharginoDecayLength")->Fill(track->eta(),((x - y).Mag())); 
          twoDHists_.at("trackEtaVsCharginoT")->Fill(track->eta(),t);
          twoDHists_.at("trackEtaVsCharginoTau")->Fill(track->eta(),tau);

          oneDHists_.at("numberOfValidHits")->Fill(track->numberOfValidHits());
          oneDHists_.at("numberOfMissingInnerHits")->Fill(track->hitPattern().trackerLayersWithoutMeasurement(reco::HitPattern::MISSING_INNER_HITS));
          oneDHists_.at("numberOfMissingMiddleHits")->Fill(track->hitPattern().trackerLayersWithoutMeasurement(reco::HitPattern::TRACK_HITS));
          oneDHists_.at("numberOfMissingOuterHits")->Fill(track->hitPattern().trackerLayersWithoutMeasurement(reco::HitPattern::MISSING_OUTER_HITS));
  
          twoDHists_.at("numberOfValidHitsVsnumberOfMissingInnerHits")->Fill(track->numberOfValidHits(),track->hitPattern().trackerLayersWithoutMeasurement(reco::HitPattern::MISSING_INNER_HITS));
          twoDHists_.at("numberOfValidHitsVsnumberOfMissingMiddleHits")->Fill(track->numberOfValidHits(),track->hitPattern().trackerLayersWithoutMeasurement(reco::HitPattern::TRACK_HITS));
          twoDHists_.at("numberOfValidHitsVsnumberOfMissingOuterHits")->Fill(track->numberOfValidHits(),track->hitPattern().trackerLayersWithoutMeasurement(reco::HitPattern::MISSING_OUTER_HITS));
  
          if(abs(track->eta())<1.0) {oneDHists_.at("numberOfValidHitsBarrel")->Fill(track->numberOfValidHits());}
          else {oneDHists_.at("numberOfValidHitsEndcap")->Fill(track->numberOfValidHits());}
 
          if(((x - y).Mag() * boost) < 1000.0) oneDHists_.at("eta1000")->Fill(track->eta());
          if(((x - y).Mag() * boost) > 1000.0 && ((x - y).Mag() * boost) < 2000.0) oneDHists_.at("eta2000")->Fill(track->eta());
          if(((x - y).Mag() * boost) > 2000.0 && ((x - y).Mag() * boost) < 3000.0) oneDHists_.at("eta3000")->Fill(track->eta());
          if(((x - y).Mag() * boost) > 3000.0 && ((x - y).Mag() * boost) < 4000.0) oneDHists_.at("eta4000")->Fill(track->eta());
          if(((x - y).Mag() * boost) > 4000.0 && ((x - y).Mag() * boost) < 5000.0) oneDHists_.at("eta5000")->Fill(track->eta());
          if(((x - y).Mag() * boost) > 5000.0 && ((x - y).Mag() * boost) < 6000.0) oneDHists_.at("eta6000")->Fill(track->eta());
          if(((x - y).Mag() * boost) > 6000.0 && ((x - y).Mag() * boost) < 7000.0) oneDHists_.at("eta7000")->Fill(track->eta());
          if(((x - y).Mag() * boost) > 7000.0 && ((x - y).Mag() * boost) < 8000.0) oneDHists_.at("eta8000")->Fill(track->eta());
          if(((x - y).Mag() * boost) > 8000.0 && ((x - y).Mag() * boost) < 9000.0) oneDHists_.at("eta9000")->Fill(track->eta());
          if(((x - y).Mag() * boost) > 9000.0) oneDHists_.at("eta10000")->Fill(track->eta());

          if(((x - y).Mag() * boost) < 4000.0)
          {

            oneDHists_.at("smallCtauNumberOfValidHits")->Fill(track->numberOfValidHits());
            oneDHists_.at("smallCtauNumberOfMissingInnerHits")->Fill(track->hitPattern().trackerLayersWithoutMeasurement(reco::HitPattern::MISSING_INNER_HITS));
            oneDHists_.at("smallCtauNumberOfMissingMiddleHits")->Fill(track->hitPattern().trackerLayersWithoutMeasurement(reco::HitPattern::TRACK_HITS));
            oneDHists_.at("smallCtauNumberOfMissingOuterHits")->Fill(track->hitPattern().trackerLayersWithoutMeasurement(reco::HitPattern::MISSING_OUTER_HITS));

          }

          if(((x - y).Mag() * boost) > 4000.0)
          {

            oneDHists_.at("largeCtauTracksCharge")->Fill(track->charge());
            oneDHists_.at("largeCtauTracksPt")->Fill(track->pt());
            oneDHists_.at("largeCtauTracksPhi")->Fill(track->phi());
            oneDHists_.at("largeCtauTracksEta")->Fill(track->eta());

            oneDHists_.at("largeCtauNumberOfValidHits")->Fill(track->numberOfValidHits());
            oneDHists_.at("largeCtauNumberOfMissingInnerHits")->Fill(track->hitPattern().trackerLayersWithoutMeasurement(reco::HitPattern::MISSING_INNER_HITS));
            oneDHists_.at("largeCtauNumberOfMissingMiddleHits")->Fill(track->hitPattern().trackerLayersWithoutMeasurement(reco::HitPattern::TRACK_HITS));
            oneDHists_.at("largeCtauNumberOfMissingOuterHits")->Fill(track->hitPattern().trackerLayersWithoutMeasurement(reco::HitPattern::MISSING_OUTER_HITS));

          }

          if(track->hitPattern().trackerLayersWithoutMeasurement(reco::HitPattern::MISSING_OUTER_HITS) > 2){

            oneDHists_.at("largeMissOutTracksCharge")->Fill(track->charge());
            oneDHists_.at("largeMissOutTracksPt")->Fill(track->pt());
            oneDHists_.at("largeMissOutTracksPhi")->Fill(track->phi());
            oneDHists_.at("largeMissOutTracksEta")->Fill(track->eta());

            twoDHists_.at("largeMissOutTrackChargeVsCharginoCTau")->Fill(track->charge(),((x - y).Mag() * boost));
            twoDHists_.at("largeMissOutTrackPtVsCharginoCTau")->Fill(track->pt(),((x - y).Mag() * boost));
            twoDHists_.at("largeMissOutTrackPhiVsCharginoCTau")->Fill(track->phi(),((x - y).Mag() * boost));
            twoDHists_.at("largeMissOutTrackEtaVsCharginoCTau")->Fill(track->eta(),((x - y).Mag() * boost));
            twoDHists_.at("largeMissOutTrackEtaVsCharginoDecayLength")->Fill(track->eta(),((x - y).Mag()));
            twoDHists_.at("largeMissOutTrackEtaVsCharginoT")->Fill(track->eta(),t);
            twoDHists_.at("largeMissOutTrackEtaVsCharginoTau")->Fill(track->eta(),tau);

          }

          if(((x - y).Mag() * boost) < 2000.0)
          {

            oneDHists_.at("chargeCTauCut")->Fill(track->charge());
            oneDHists_.at("ptCTauCut")->Fill(track->pt());
            oneDHists_.at("phiCTauCut")->Fill(track->phi());
            oneDHists_.at("etaCTauCut")->Fill(track->eta());

          }
 
        }
  
        else {
  
          oneDHists_.at("matchedTrack")->Fill(0.0);
  
          oneDHists_.at("chargeClosest")->Fill(track->charge());
          oneDHists_.at("ptClosest")->Fill(track->pt());
          oneDHists_.at("phiClosest")->Fill(track->phi());
          oneDHists_.at("etaClosest")->Fill(track->eta());
  
          oneDHists_.at("numberOfValidHitsClosest")->Fill(track->numberOfValidHits());
          oneDHists_.at("numberOfMissingInnerHitsClosest")->Fill(track->hitPattern().trackerLayersWithoutMeasurement(reco::HitPattern::MISSING_INNER_HITS));
          oneDHists_.at("numberOfMissingMiddleHitsClosest")->Fill(track->hitPattern().trackerLayersWithoutMeasurement(reco::HitPattern::TRACK_HITS));
          oneDHists_.at("numberOfMissingOuterHitsClosest")->Fill(track->hitPattern().trackerLayersWithoutMeasurement(reco::HitPattern::MISSING_OUTER_HITS));
  
        }
  
      }
      else {
        oneDHists_.at("matchedTrack")->Fill(0.0);
  
      }

      const reco::Muon *muon = getMatchedMuon(genParticle, muons);

      if(muon)
      {

        if(muon->isTrackerMuon()){
          reco::Track m = *(muon->innerTrack());

          oneDHists_.at("matchedMuon")->Fill(1.0);
          oneDHists_.at("chargeMuon")->Fill(m.charge());
          oneDHists_.at("ptMuon")->Fill(m.pt());
          oneDHists_.at("phiMuon")->Fill(m.phi());
          oneDHists_.at("etaMuon")->Fill(m.eta());

        }

      }
      else {
        oneDHists_.at("matchedMuon")->Fill(0.0);

      }

    } // End comment here with * / to remove tracks ###########################################################3
  oneDHists_.at("nCharginos")->Fill(nCharginos);
  std::cout << nTracks << std::endl;
  if(!nCharginos)
    clog << "[" << event.id() << "] No charginos found!" << endl;

  if(l.Pt()!=0.0 and l.M()!=0.0){
    oneDHists_.at("ZPtLog")->Fill(l.Pt());
    oneDHists_.at("ZPt")->Fill(l.Pt());
    oneDHists_.at("ZMass")->Fill(l.M());
  }

  if(l2.Pt()!=0.0 and l2.M()!=0.0){
    oneDHists_.at("ZPtLog")->Fill(l2.Pt());
    oneDHists_.at("ZPt")->Fill(l2.Pt());
    oneDHists_.at("ZMass")->Fill(l2.M());
  }

  TLorentzVector p(0.0, 0.0, 0.0, 0.0);
  TLorentzVector p2(0.0, 0.0, 0.0, 0.0);
  unsigned nEwkinos = 0;
  unsigned nDMs = 0;
  for(const auto &genParticle : *genParticles) {
    int pdgId = abs(genParticle.pdgId());
    unsigned status = genParticle.status();

    if(pdgId != 1000022 && pdgId != 1000024 && pdgId != 1000023) continue;

    if(cutPythia8Flag_) {
      if(pdgId == 1000022 && status != 1) continue;
      if(pdgId == 1000023 && status != 1) continue;
      if(pdgId == 1000024 && status != 62) continue;
    }
    else {
      if(status != 1) continue;
    }

    if(nEwkinos==2) continue;
    p += TLorentzVector(genParticle.px(), genParticle.py(), genParticle.pz(), genParticle.energy());
    nEwkinos++;
  }

  for(const auto &genParticle : *genParticles) {
    int pdgId = abs(genParticle.pdgId());
    unsigned status = abs(genParticle.status());

    if(pdgId != 1000022 && pdgId != 1000023) continue;

    if(cutPythia8Flag_) {
      if(pdgId == 1000022 && status != 1) continue;
      if(pdgId == 1000023 && status != 1) continue;
    }
    else {
      if(status != 1) continue;
    }

    p2 += TLorentzVector(genParticle.px(), genParticle.py(), genParticle.pz(), genParticle.energy());
    nDMs++;
  }

  if(nEwkinos == 2) {oneDHists_.at("FSumPt")->Fill(p.Pt()); oneDHists_.at("FSumPtDiffbin")->Fill(p.Pt()); oneDHists_.at("ewkinoSumPtLog")->Fill(p.Pt()); oneDHists_.at("ewkinoSumPtLogDiffbin")->Fill(p.Pt());}
  if(nDMs == 2) oneDHists_.at("DMSumPt")->Fill(p2.Pt());

  for(const auto &genParticle : *genParticles) {
    if(abs(genParticle.pdgId()) != 211) continue;
    if(abs(genParticle.mother()->pdgId()) != 1000024) continue;

    oneDHists_.at("genPtPion")->Fill(genParticle.pt());
    oneDHists_.at("genPPion")->Fill(genParticle.p());
  }

  TLorentzVector p3(0.0, 0.0, 0.0, 0.0);

  for(const auto &genParticle : *genParticles) {
    if(abs(genParticle.pdgId()) != 1000022 && abs(genParticle.pdgId()) != 1000023 && abs(genParticle.pdgId()) != 12 && abs(genParticle.pdgId()) != 14 && abs(genParticle.pdgId()) != 16) continue;
    int pdgId = abs(genParticle.pdgId());
    unsigned status = abs(genParticle.status());
    if(pdgId == 1000022 && status != 1) continue;
    if(pdgId == 1000023 && status != 1) continue;
    if(pdgId == 12 && status != 1) continue;
    if(pdgId == 14 && status != 1) continue;
    if(pdgId == 16 && status != 1) continue;
    p3 += TLorentzVector(genParticle.px(), genParticle.py(), genParticle.pz(), genParticle.energy()); 
  }

  oneDHists_.at("InvisibleSumPt")->Fill(p3.Pt());

  TLorentzVector p4(0.0, 0.0, 0.0, 0.0);

  for(const auto &genParticle : *genParticles) {
    if(abs(genParticle.pdgId()) != 1000022 && abs(genParticle.pdgId()) != 12 && abs(genParticle.pdgId()) != 14 && abs(genParticle.pdgId()) != 16) continue;
    int pdgId = abs(genParticle.pdgId());
    unsigned status = abs(genParticle.status());
    if(pdgId == 1000022 && status != 1) continue;
    if(pdgId == 12 && status != 1) continue;
    if(pdgId == 14 && status != 1) continue;
    if(pdgId == 16 && status != 1) continue;
    p4 += TLorentzVector(genParticle.px(), genParticle.py(), genParticle.pz(), genParticle.energy());
  }

  oneDHists_.at("InvisibleSumPt_without1000023")->Fill(p4.Pt());

}

void
CharginoValidator::getEndVertex(const reco::GenParticle &genParticle, TVector3 &y) const
{
  if(!genParticle.numberOfDaughters())
    y.SetXYZ(99999.0, 99999.0, 99999.0);
  else
    for(const auto &daughter : genParticle)
      {
        if(abs(daughter.pdgId()) != 1000022 and abs(daughter.pdgId()) != 1000023)
          continue;

        y.SetXYZ(daughter.vx(), daughter.vy(), daughter.vz());
        break;
      }
}

const reco::Track *
CharginoValidator::getMatchedTrack(const reco::GenParticle &genParticle, const edm::Handle<vector<reco::Track> > &tracks) const
{
  const reco::Track *matchedTrack = NULL;
  double minDR = -1.0;
  int i = -1;
  for(const auto &track : *tracks) {
    i++;
    if(track.pt() < 10.0) continue;
    const double dR = deltaR(genParticle, track);
    if(dR > 0.1) continue;
    if(!matchedTrack || dR < minDR) {
      matchedTrack = &(tracks->at(i));
      minDR = dR;
    }
  }

  return matchedTrack;
}

unsigned
CharginoValidator::getMatchedTrackNumber(const reco::GenParticle &genParticle, const edm::Handle<vector<reco::Track> > &tracks) const
{
  unsigned i = 0;
  for(const auto &track : *tracks) {
    const double dR = deltaR(genParticle, track);
    if(dR > 0.05) continue;
    i++;
  }

  return i;
}

const reco::Muon *
CharginoValidator::getMatchedMuon(const reco::GenParticle &genParticle, const edm::Handle<vector<reco::Muon> > &muons) const
{
  const reco::Muon *matchedMuon = NULL;
  double minDR = -1.0;
  int i = -1;
  for(const auto &muon : *muons) {
    i++;
    if(muon.isTrackerMuon()){
      reco::Track m = *(muon.innerTrack());
      if(m.pt() < 10.0) continue;
      const double dR = deltaR(genParticle, m);
      if(dR > 0.1) continue;
      if(!matchedMuon || dR < minDR) {
        matchedMuon = &(muons->at(i));
        minDR = dR;
      }
    }
  }

  return matchedMuon;
}

void
CharginoValidator::logSpace (const unsigned n, const double a, const double b, vector<double> &bins) const
{
  double step = (b - a) / ((double) n);

  bins.clear ();
  for (double i = a; i < b + 0.5 * step; i += step)
    bins.push_back (pow (10.0, i));
}

DEFINE_FWK_MODULE(CharginoValidator);
