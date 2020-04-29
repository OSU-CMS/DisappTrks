#include "DisappTrks/IsoTrkDevelopment/plugins/IsoTrkAnalyzerProducer.h"
#include "DataFormats/PatCandidates/interface/IsolatedTrack.h"
#include "DataFormats/Math/interface/deltaR.h"
#include "DataFormats/Math/interface/LorentzVector.h"

#include "TLorentzVector.h"
#include "TMath.h"
#include "TString.h"

#define M_Z (91.1876)
#define CHARGINO (1000024)
#define isMC (false)

template<class T, class... Args>
IsoTrkAnalyzerProducer<T, Args...>::IsoTrkAnalyzerProducer (const edm::ParameterSet &cfg) :
  EventVariableProducer(cfg)
{
  tokenProbes_ = consumes<vector<T> > (collections_.getParameter<edm::InputTag> (tagCollectionParameter ()));
  if(isMC){
    genParticlesToken_ = consumes<vector<reco::GenParticle> > (collections_.getParameter<edm::InputTag> ("hardInteractionMcparticles"));
    pileupInfoToken_   = consumes<edm::View<PileupSummaryInfo>>(collections_.getParameter<edm::InputTag>("pileupinfos"));
  }

  TH1::SetDefaultSumw2();

  
  oneDHists_["nPU"] = fs_->make<TH1D>("nPU", ";trueNumInteractions", 100, 0, 100);

  // Object-by-object CutFlow
  vector<TString> cuts_IsoTrk = {"total","dxy < 0.05","dz < 1.0", "pt > 45GeV", "looseTrack", "tightTrack", "HighPurityTrack", "low NoPU energy deposit < 10 GeV"};
  vector<TString> cuts_Chargino = {"total","isChargino","dxy < 0.05","dz < 1.0", "pt > 45GeV", "looseTrack", "tightTrack", "HighPurityTrack", "low NoPU energy deposit < 10 GeV"};
  oneDHists_["cutflow_IsoTrk"] = fs_->make<TH1D>("cutflow_IsoTrk","", cuts_IsoTrk.size(), 0, cuts_IsoTrk.size());
  oneDHists_["cutflow_InclusiveIsoTrk"] = fs_->make<TH1D>("cutflow_InclusiveIsoTrk","", cuts_IsoTrk.size(), 0, cuts_IsoTrk.size());
  oneDHists_["cutflow_PreviousIsoTrk"] = fs_->make<TH1D>("cutflow_PreviousIsoTrk","", cuts_IsoTrk.size(), 0, cuts_IsoTrk.size());
  oneDHists_["cutflow_Chargino"] = fs_->make<TH1D>("cutflow_Chargino","", cuts_Chargino.size(), 0, cuts_Chargino.size());
  
  for (std::vector<TString>::iterator iCut = cuts_IsoTrk.begin() ; iCut != cuts_IsoTrk.end(); ++iCut){
    int ibin = iCut - cuts_IsoTrk.begin();
    oneDHists_.at("cutflow_IsoTrk")->GetXaxis()->SetBinLabel(ibin+1, *iCut);
    oneDHists_.at("cutflow_InclusiveIsoTrk")->GetXaxis()->SetBinLabel(ibin+1, *iCut);
    oneDHists_.at("cutflow_PreviousIsoTrk")->GetXaxis()->SetBinLabel(ibin+1, *iCut);
  }
  for (std::vector<TString>::iterator iCut = cuts_Chargino.begin() ; iCut != cuts_Chargino.end(); ++iCut){
    int ibin = iCut - cuts_Chargino.begin();
    oneDHists_.at("cutflow_Chargino")->GetXaxis()->SetBinLabel(ibin+1, *iCut);
  }
  // IsoTrk-matched Chargino
  oneDHists_["nCharginos"] = fs_->make<TH1D>("nCharginos", ";number of charginos", 5, -0.5, 4.5);
  oneDHists_["genCharge"] = fs_->make<TH1D>("genCharge", ";generator chargino charge", 3, -1.5, 1.5);
  oneDHists_["genMass"] = fs_->make<TH1D>("genMass", ";generator chargino mass [GeV]", 1000, -0.5, 999.5);
  oneDHists_["genPt"] = fs_->make<TH1D>("genPt", ";generator chargino p_{T} [GeV]", 500, 0.0, 1000.0);
  oneDHists_["genPhi"] = fs_->make<TH1D>("genPhi", ";generator chargino #phi", 100, -3.2, 3.2);
  oneDHists_["genEta"] = fs_->make<TH1D>("genEta", ";generator chargino #eta", 100, -5.0, 5.0);
  oneDHists_["genP"] = fs_->make<TH1D>("genP", ";generator chargino p [GeV]", 500, 0.0, 1000.0);
  oneDHists_["genBeta"] = fs_->make<TH1D>("genBeta", ";generator chargino #beta", 500, 0.0, 1.0);
  oneDHists_["genGamma"] = fs_->make<TH1D>("genGamma", ";generator chargino #gamma", 500, 0.0, 100.0);
  oneDHists_["genBetaGamma"] = fs_->make<TH1D>("genBetaGamma", ";generator chargino #beta#gamma", 500, 0.0, 100.0);
  oneDHists_["genBetaGammaM"] = fs_->make<TH1D>("genBetaGammaM", ";generator chargino #beta#gammam [GeV]", 500, 0.0, 1000.0);

  oneDHists_["genDecayLength_10"] = fs_->make<TH1D>("genDecayLength_10", ";generator chargino decay length [cm]", 1000, 0.0, 10.0);
  oneDHists_["genDecayLength_100"] = fs_->make<TH1D>("genDecayLength_100", ";generator chargino decay length [cm]", 1000, 0.0, 100.0);
  oneDHists_["genDecayLength_1000"] = fs_->make<TH1D>("genDecayLength_1000", ";generator chargino decay length [cm]", 1000, 0.0, 1000.0);
  oneDHists_["genDecayLength_10000"] = fs_->make<TH1D>("genDecayLength_10000", ";generator chargino decay length [cm]", 1000, 0.0, 10000.0);
  oneDHists_["genDecayLength_100000"] = fs_->make<TH1D>("genDecayLength_100000", ";generator chargino decay length [cm]", 1000, 0.0, 100000.0);

  oneDHists_["genCTau_10"] = fs_->make<TH1D>("genCTau_10", ";generator chargino c#tau [cm]", 1000, 0.0, 10.0);
  oneDHists_["genCTau_100"] = fs_->make<TH1D>("genCTau_100", ";generator chargino c#tau [cm]", 1000, 0.0, 100.0);
  oneDHists_["genCTau_1000"] = fs_->make<TH1D>("genCTau_1000", ";generator chargino c#tau [cm]", 1000, 0.0, 1000.0);
  oneDHists_["genCTau_10000"] = fs_->make<TH1D>("genCTau_10000", ";generator chargino c#tau [cm]", 1000, 0.0, 10000.0);
  oneDHists_["genCTau_100000"] = fs_->make<TH1D>("genCTau_100000", ";generator chargino c#tau [cm]", 1000, 0.0, 100000.0);

  // Chargino-matched IsolatedTrack
  oneDHists_["charge"] = fs_->make<TH1D>("charge", ";track charge", 3, -1.5, 1.5);
  oneDHists_["pt"] = fs_->make<TH1D>("pt", ";track p_{T} [GeV]", 500, 0.0, 1000.0);
  oneDHists_["phi"] = fs_->make<TH1D>("phi", ";track #phi", 100, -3.2, 3.2);
  oneDHists_["eta"] = fs_->make<TH1D>("eta", ";track #eta", 100, -5.0, 5.0);

  oneDHists_["dxy"] = fs_->make<TH1D>("dxy",";track d_{xy}", 100, -5.0, 5.0 );
  oneDHists_["dz"]  = fs_->make<TH1D>("dz",";track d_{z}", 100, -5.0, 5.0 );

  oneDHists_["numberOfValidHits"] = fs_->make<TH1D>("numberOfValidHits", ";track number of valid hits", 100, -0.5, 99.5);
  oneDHists_["numberOfMissingInnerHits"] = fs_->make<TH1D>("numberOfMissingInnerHits", ";track number of missing inner hits", 20, -0.5, 19.5);
  oneDHists_["numberOfMissingMiddleHits"] = fs_->make<TH1D>("numberOfMissingMiddleHits", ";track number of missing middle hits", 20, -0.5, 19.5);
  oneDHists_["numberOfMissingOuterHits"] = fs_->make<TH1D>("numberOfMissingOuterHits", ";track number of missing outer hits", 20, -0.5, 19.5);

  oneDHists_["assocCaloDR05"] = fs_->make<TH1D>("assocCaloDR05", ";associatedCalo (dR<05) [GeV]", 200, -0.5, 99.5);
  oneDHists_["assocEMCaloDR05"] = fs_->make<TH1D>("assocEMCaloDR05", ";associatedCalo (dR<05) [GeV]", 200, -0.5, 99.5);
  oneDHists_["assocHadCaloDR05"] = fs_->make<TH1D>("assocHadCaloDR05", ";associatedCalo (dR<05) [GeV]", 200, -0.5, 99.5);

  oneDHists_["assocCaloDR05NoPU"] = fs_->make<TH1D>("assocCaloDR05NoPU", ";associatedCalo (dR<05) [GeV]", 200, -0.5, 99.5);
  oneDHists_["assocEMCaloDR05NoPU"] = fs_->make<TH1D>("assocEMCaloDR05NoPU", ";associatedCalo (dR<05) [GeV]", 200, -0.5, 99.5);
  oneDHists_["assocHadCaloDR05NoPU"] = fs_->make<TH1D>("assocHadCaloDR05NoPU", ";associatedCalo (dR<05) [GeV]", 200, -0.5, 99.5);

  oneDHists_["assocCaloDR05NoPUCalo"] = fs_->make<TH1D>("assocCaloDR05NoPUCalo", ";associatedCalo (dR<05) [GeV]", 200, -0.5, 99.5);
  oneDHists_["assocEMCaloDR05NoPUCalo"] = fs_->make<TH1D>("assocEMCaloDR05NoPUCalo", ";associatedCalo (dR<05) [GeV]", 200, -0.5, 99.5);
  oneDHists_["assocHadCaloDR05NoPUCalo"] = fs_->make<TH1D>("assocHadCaloDR05NoPUCalo", ";associatedCalo (dR<05) [GeV]", 200, -0.5, 99.5);

  oneDHists_["assocCaloDR05NoPUCentralCalo"] = fs_->make<TH1D>("assocCaloDR05NoPUCentralCalo", ";associatedCalo (dR<05) [GeV]", 200, -0.5, 99.5);
  oneDHists_["assocEMCaloDR05NoPUCentralCalo"] = fs_->make<TH1D>("assocEMCaloDR05NoPUCentralCalo", ";associatedCalo (dR<05) [GeV]", 200, -0.5, 99.5);
  oneDHists_["assocHadCaloDR05NoPUCentralCalo"] = fs_->make<TH1D>("assocHadCaloDR05NoPUCentralCalo", ";associatedCalo (dR<05) [GeV]", 200, -0.5, 99.5);

  twoDHists_["chargeVsPU"] = fs_->make<TH2D>("chargeVsPU", ";trueNumInteractions;track charge", 100, 0, 100, 3, -1.5, 1.5);
  twoDHists_["ptVsPU"] = fs_->make<TH2D>("ptVsPU", ";trueNumInteractions;track p_{T} [GeV]", 100, 0, 100, 500, 0.0, 1000.0);
  twoDHists_["etaVsPU"] = fs_->make<TH2D>("etaVsPU", ";trueNumInteractions;track #eta", 100, 0, 100, 100, -5.0, 5.0);

  twoDHists_["numberOfValidHits"] = fs_->make<TH2D>("numberOfValidHitsVsPU", ";trueNumInteractions;track number of valid hits", 100, 0, 100, 100, -0.5, 99.5);
  twoDHists_["numberOfMissingInnerHits"] = fs_->make<TH2D>("numberOfMissingInnerHitsVsPU", ";trueNumInteractions;track number of missing inner hits", 100, 0, 100, 20, -0.5, 19.5);
  twoDHists_["numberOfMissingMiddleHits"] = fs_->make<TH2D>("numberOfMissingMiddleHitsVsPU", ";trueNumInteractions;track number of missing middle hits", 100, 0, 100, 20, -0.5, 19.5);
  twoDHists_["numberOfMissingOuterHits"] = fs_->make<TH2D>("numberOfMissingOuterHitsVsPU", ";trueNumInteractions;track number of missing outer hits", 100, 0, 100, 20, -0.5, 19.5);
  twoDHists_["assocCalNoPUVsMissingOuterHits"] = fs_->make<TH2D>("assocCaloDR05NoPUVsMissingOuterHits",";assocCaloDR05NoPU [GeV]; track number of missing outer hits",200, -0.5, 99.5, 20, -0.5, 19.5);

}

template<class T, class... Args>
IsoTrkAnalyzerProducer<T, Args...>::~IsoTrkAnalyzerProducer ()
{
}

template<class T, class... Args> void
IsoTrkAnalyzerProducer<T, Args...>::AddVariables (const edm::Event &event )
{
  edm::Handle<vector<T> > probes;
  event.getByToken (tokenProbes_, probes);

  edm::Handle<vector<reco::GenParticle> > genParticles;
  edm::Handle<edm::View<PileupSummaryInfo>> pileupInfos;
  if (isMC){
    event.getByToken (genParticlesToken_, genParticles);
    event.getByToken(pileupInfoToken_, pileupInfos);
  }

  //std::cout << "probes isValid: " << probes.isValid () << std::endl;
  //std::cout << "genParticles isValid: " << genParticles.isValid () << std::endl;
  //std::cout << "pileupInfos isValid: " << pileupInfos.isValid () << std::endl;
  if ( !probes.isValid () && !genParticles.isValid() )
    return;

  int nCharginoMatchedIsoTrk = 0;
  int nGenChargino = 0;

  vector<math::XYZTLorentzVector> matchedProbeLorentzVectors;
  vector<math::XYZTLorentzVector> genLorentzVectors;

  vector<PileupSummaryInfo>::const_iterator iterPU;
  double truePV = -1;
  if(isMC){
    for(edm::View<PileupSummaryInfo>::const_iterator iterPU = pileupInfos->begin(); iterPU != pileupInfos->end(); iterPU++) {
          if(iterPU->getBunchCrossing() == 0) truePV = iterPU->getTrueNumInteractions();
    }
    oneDHists_.at("nPU")->Fill(truePV);
  }


  // Find Chargino matched IsolatedTrack
  for (const auto &probe : *probes){
        
    vector<bool> cutResult_IsoTrk = {true,abs(probe.dxy()) < 0.05, abs(probe.dz()) < 1.0, probe.pt() > 45.0, probe.isLooseTrack(), probe.isTightTrack(), probe.isHighPurityTrack(),probe.assocCaloDR05() - probe.rhoPUCorr() * TMath::Pi()*0.5*0.5 < 10.0 };
    vector<bool> cutResult_susySoftDisTrk= vector<bool>(cutResult_IsoTrk.size(), ( probe.pt() > 10. && (probe.pt() > 15. || probe.hitPattern().pixelLayersWithMeasurement() == probe.hitPattern().trackerLayersWithMeasurement())  && abs(probe.dxy()) < 0.02 && abs(probe.dz()) < 0.1 && (probe.miniPFIsolation().chargedHadronIso()/probe.pt() < 0.2) && !(probe.pfLepOverlap()) && probe.pfNeutralSum()/probe.pt() < 0.2 ));
    vector<bool> cutResult_HighPtTrack = vector<bool>(cutResult_IsoTrk.size(),( probe.pt() > 50 &&  probe.isHighPurityTrack() &&  abs(probe.dxy()) < 0.5 && abs(probe.dz()) < 0.5 &&  (probe.miniPFIsolation().chargedHadronIso()/probe.pt() < 1.0 || probe.pt() > 100) ));
    vector<bool> cutResult_InclusiveIsoTrk;
    vector<bool> cutResult_PreviousIsoTrk;

    for(std::vector<bool>::iterator itr = cutResult_IsoTrk.begin(); itr != cutResult_IsoTrk.end(); ++itr ){
      int ibin = itr-cutResult_IsoTrk.begin();
      cutResult_InclusiveIsoTrk.push_back( cutResult_IsoTrk.at(ibin) || cutResult_susySoftDisTrk.at(ibin) || cutResult_HighPtTrack.at(ibin));
      cutResult_PreviousIsoTrk.push_back( cutResult_susySoftDisTrk.at(ibin) || cutResult_HighPtTrack.at(ibin));
    }
    for(std::vector<bool>::iterator itr = cutResult_IsoTrk.begin(); itr != cutResult_IsoTrk.end() && *itr != false; ++itr ){
      oneDHists_.at("cutflow_IsoTrk")->Fill(itr-cutResult_IsoTrk.begin()+0.5);
    }
    for(std::vector<bool>::iterator itr = cutResult_InclusiveIsoTrk.begin(); itr != cutResult_InclusiveIsoTrk.end() && *itr != false; ++itr ){
      oneDHists_.at("cutflow_InclusiveIsoTrk")->Fill(itr-cutResult_InclusiveIsoTrk.begin()+0.5);
    }
    for(std::vector<bool>::iterator itr = cutResult_PreviousIsoTrk.begin(); itr != cutResult_PreviousIsoTrk.end() && *itr != false; ++itr ){
      oneDHists_.at("cutflow_PreviousIsoTrk")->Fill(itr-cutResult_PreviousIsoTrk.begin()+0.5);
    }


    // Fill chargino-matched IsolatedTrack
    oneDHists_.at("charge")->Fill(probe.charge());
    oneDHists_.at("pt")->Fill(probe.pt());
    oneDHists_.at("phi")->Fill(probe.phi());
    oneDHists_.at("eta")->Fill(probe.eta());

    oneDHists_.at("dxy")->Fill(probe.dxy());
    oneDHists_.at("dz")->Fill(probe.dz());

    oneDHists_.at("numberOfValidHits")->Fill(probe.hitPattern().numberOfValidHits());
    oneDHists_.at("numberOfMissingInnerHits")->Fill(probe.hitPattern().trackerLayersWithoutMeasurement(reco::HitPattern::MISSING_INNER_HITS));
    oneDHists_.at("numberOfMissingMiddleHits")->Fill(probe.hitPattern().trackerLayersWithoutMeasurement(reco::HitPattern::TRACK_HITS));
    oneDHists_.at("numberOfMissingOuterHits")->Fill(probe.hitPattern().trackerLayersWithoutMeasurement(reco::HitPattern::MISSING_OUTER_HITS));

    oneDHists_.at("assocCaloDR05")->Fill(probe.assocCaloDR05());
    oneDHists_.at("assocEMCaloDR05")->Fill(probe.assocEMCaloDR05());
    oneDHists_.at("assocHadCaloDR05")->Fill(probe.assocHadCaloDR05());

    oneDHists_.at("assocCaloDR05NoPU")->Fill(probe.assocCaloDR05() - probe.rhoPUCorr() * TMath::Pi()*0.5*0.5);
    oneDHists_.at("assocEMCaloDR05NoPU")->Fill(probe.assocEMCaloDR05() - probe.rhoPUCorr() * TMath::Pi()*0.5*0.5);
    oneDHists_.at("assocHadCaloDR05NoPU")->Fill(probe.assocHadCaloDR05() - probe.rhoPUCorr() * TMath::Pi()*0.5*0.5);

    oneDHists_.at("assocCaloDR05NoPUCalo")->Fill(probe.assocCaloDR05() - probe.rhoPUCorrCalo() * TMath::Pi()*0.5*0.5);
    oneDHists_.at("assocEMCaloDR05NoPUCalo")->Fill(probe.assocEMCaloDR05() - probe.rhoPUCorrCalo() * TMath::Pi()*0.5*0.5);
    oneDHists_.at("assocHadCaloDR05NoPUCalo")->Fill(probe.assocHadCaloDR05() - probe.rhoPUCorrCalo() * TMath::Pi()*0.5*0.5);


    oneDHists_.at("assocCaloDR05NoPUCentralCalo")->Fill(probe.assocCaloDR05() - probe.rhoPUCorrCentralCalo() * TMath::Pi()*0.5*0.5);
    oneDHists_.at("assocEMCaloDR05NoPUCentralCalo")->Fill(probe.assocEMCaloDR05() - probe.rhoPUCorrCentralCalo() * TMath::Pi()*0.5*0.5);
    oneDHists_.at("assocHadCaloDR05NoPUCentralCalo")->Fill(probe.assocHadCaloDR05() - probe.rhoPUCorrCentralCalo() * TMath::Pi()*0.5*0.5);


    twoDHists_["numberOfValidHits"]->Fill(truePV, probe.hitPattern().numberOfValidHits());
    twoDHists_["numberOfMissingInnerHits"]->Fill(truePV, probe.hitPattern().trackerLayersWithoutMeasurement(reco::HitPattern::MISSING_INNER_HITS));
    twoDHists_["numberOfMissingMiddleHits"]->Fill(truePV, probe.hitPattern().trackerLayersWithoutMeasurement(reco::HitPattern::TRACK_HITS));
    twoDHists_["numberOfMissingOuterHits"]->Fill(truePV, probe.hitPattern().trackerLayersWithoutMeasurement(reco::HitPattern::MISSING_OUTER_HITS));
    if (isMC){
      twoDHists_["chargeVsPU"]->Fill(truePV, probe.charge());
      twoDHists_["ptVsPU"]->Fill(truePV, probe.pt());
      twoDHists_["etaVsPU"]->Fill(truePV, probe.eta());
      twoDHists_["assocCalNoPUVsMissingOuterHits"]->Fill(probe.assocCaloDR05() - probe.rhoPUCorr() * TMath::Pi()*0.5*0.5,probe.hitPattern().trackerLayersWithoutMeasurement(reco::HitPattern::MISSING_OUTER_HITS));
    }

    if (isMC){
      for (const auto &genParticle : *genParticles){
        if(abs(genParticle.pdgId()) == CHARGINO && genProbeMatched(probe,genParticle)){
       // if(genProbeMatched(probe,genParticle)){
          matchedProbeLorentzVectors.push_back(probe.p4());
          nCharginoMatchedIsoTrk++;
        
          vector<bool> cutResult_Chargino = {true, genParticle.pdgId() == CHARGINO, abs(probe.dxy()) < 0.05, abs(probe.dz()) < 1.0, probe.pt() > 45.0, probe.isLooseTrack(), probe.isTightTrack(), probe.isHighPurityTrack(),probe.assocCaloDR05() - probe.rhoPUCorr() * TMath::Pi()*0.5*0.5 < 10.0 };
          for(std::vector<bool>::iterator itr = cutResult_Chargino.begin(); itr != cutResult_Chargino.end() && *itr != false; ++itr ){
            oneDHists_.at("cutflow_Chargino")->Fill(itr-cutResult_Chargino.begin()+0.5);
          }

          // Fill track-matched Chargino
          TVector3 x(genParticle.vx(), genParticle.vy(), genParticle.vz()),
               y(0.0, 0.0, 0.0);

          double boost = 1.0 /(genParticle.p4().Beta(), genParticle.p4().Gamma());
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
  
          oneDHists_.at("genDecayLength_10")->Fill((x - y).Mag());
          oneDHists_.at("genDecayLength_100")->Fill((x - y).Mag());
          oneDHists_.at("genDecayLength_1000")->Fill((x - y).Mag());
          oneDHists_.at("genDecayLength_10000")->Fill((x - y).Mag());
          oneDHists_.at("genDecayLength_100000")->Fill((x - y).Mag());
  
          oneDHists_.at("genCTau_10")->Fill((x - y).Mag() * boost);
          oneDHists_.at("genCTau_100")->Fill((x - y).Mag() * boost);
          oneDHists_.at("genCTau_1000")->Fill((x - y).Mag() * boost);
          oneDHists_.at("genCTau_10000")->Fill((x - y).Mag() * boost);
          oneDHists_.at("genCTau_100000")->Fill((x - y).Mag() * boost);

          break;
        }
      }
    }
  }
  if(isMC){
    for (const auto &genParticle : *genParticles)
      {
        if (abs(genParticle.pdgId()) == CHARGINO && genParticle.status() == 23 ){
          genLorentzVectors.push_back(genParticle.p4());
          nGenChargino++;
        }
      }
  }
  // End of truth particles

  oneDHists_.at("nCharginos")->Fill(nGenChargino);
  //std::cout << "nCharginoMatchedIsoTrk :" << nCharginoMatchedIsoTrk << "   nGenChargino: " << nGenChargino << std::endl;  
  // Store probe/genParticle associated variables
  (*eventvariables)["nCharginoMatchedIsoTrk"] = nCharginoMatchedIsoTrk;
  (*eventvariables)["nGenChargino"]           = nGenChargino; 
  (*eventvariables)["MatchedProbeLeadingPt"]         = matchedProbeLorentzVectors.size() > 0 ? matchedProbeLorentzVectors.at(0).Pt() : -1.0;
  (*eventvariables)["GenCharginoLeadingPt"]   = genLorentzVectors.size() > 0 ? genLorentzVectors.at(0).Pt() : -1.0;
}


template<> const string
IsoTrkAnalyzerProducer<osu::Track,reco::GenParticle>::tagCollectionParameter () const
{
  return "tracks";
}

template<class T, class... Args> bool
IsoTrkAnalyzerProducer< T, Args...>::genProbeMatched (const osu::Track &probe, const reco::GenParticle &genParticle) const
{
  double dR = deltaR(probe, genParticle);
  if (dR < 0.01) { return true; }
  return false;
}

/*
template<class T, class... Args> bool
IsoTrkAnalyzerProducer<T, Args...>::passesVeto (const osu::Track &probe) const
{
  return false;
}
*/

/*template<> bool
IsoTrkAnalyzerProducer<osu::Track, osu::Electron>::passesVeto (const osu::Track &probe) const
{
#if DATA_FORMAT == MINI_AOD_2017
  bool passes = probe.deltaRToClosestPFElectron () > 0.15
             && (probe.matchedCaloJetEmEnergy() + probe.matchedCaloJetHadEnergy()) < 10.0
             && probe.hitAndTOBDrop_bestTrackMissingOuterHits () >= 3.0;
#else
  bool passes = probe.deltaRToClosestElectron () > 0.15
             && probe.caloNewNoPUDRp5CentralCalo () < 10.0
             && probe.hitAndTOBDrop_bestTrackMissingOuterHits () >= 3.0;
#endif

  return passes;
}
*/

template<class T, class... Args> void
IsoTrkAnalyzerProducer< T, Args...>::getEndVertex(const reco::GenParticle &genParticle, TVector3 &y) const
{
  if(!genParticle.numberOfDaughters())
    y.SetXYZ(99999.0, 99999.0, 99999.0);
  else
    for(const auto &daughter : genParticle)
      {
        if(abs(daughter.pdgId()) != 1000022)
          continue;

        y.SetXYZ(daughter.vx(), daughter.vy(), daughter.vz());
        break;
      }
}


#include "FWCore/Framework/interface/MakerMacros.h"
DEFINE_FWK_MODULE(GenMatchedTrackProducer);
