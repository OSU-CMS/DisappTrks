#ifndef TRIGGER_WEIGHT_PRODUCER
#define TRIGGER_WEIGHT_PRODUCER

#include "OSUT3Analysis/AnaTools/interface/EventVariableProducer.h"

#include "TFile.h"
#include "TGraphAsymmErrors.h"
#include "TVector2.h"
#include "TString.h"

class TriggerWeightProducer : public EventVariableProducer
{
public:
  TriggerWeightProducer(const edm::ParameterSet &);
  ~TriggerWeightProducer() {};

private:
  edm::EDGetTokenT<vector<TYPE(mets)> > metsToken_;
  edm::EDGetTokenT<vector<TYPE(muons)> > muonsToken_;
  edm::EDGetTokenT<vector<TYPE(tracks)> > tracksToken_;
  edm::EDGetTokenT<vector<reco::Vertex> > vertexToken_;
  edm::EDGetTokenT<vector<reco::GenParticle> > genParticlesToken_;
  edm::EDGetTokenT<vector<TYPE(hardInteractionMcparticles)> > mcparticlesToken_;

  string efficiencyFile_;
  string dataset_;
  string target_;

  void FindEfficiency(TGraphAsymmErrors *, double, double &, double &, double &);
  const TVector2 getPFMETNoMu(const vector<TYPE(mets)> &, const vector<TYPE(muons)> &) const;
  const double getLeadTrackPt(const vector<TYPE(tracks)> &, const vector<reco::GenParticle> &, const reco::Vertex &) const;

  bool isGoodTrack(const TYPE(tracks) &, const reco::Vertex &) const;
  bool isGoodTrack(const TYPE(tracks) &, const reco::Vertex &, const vector<reco::GenParticle> &) const;
  bool genMatched(const TYPE(tracks) &, const vector<reco::GenParticle> &, const int, const int, const double) const;

  void AddVariables(const edm::Event &);
};

TriggerWeightProducer::TriggerWeightProducer(const edm::ParameterSet &cfg) :
  EventVariableProducer(cfg),
  efficiencyFile_ (cfg.getParameter<string> ("efficiencyFile")),
  dataset_        (cfg.getParameter<string> ("dataset")),
  target_         (cfg.getParameter<string> ("target"))
{
  metsToken_         = consumes<vector<TYPE(mets)> >        (collections_.getParameter<edm::InputTag> ("mets"));
  muonsToken_        = consumes<vector<TYPE(muons)> >       (collections_.getParameter<edm::InputTag> ("muons"));
  tracksToken_       = consumes<vector<TYPE(tracks)> >      (collections_.getParameter<edm::InputTag> ("tracks"));
  vertexToken_       = consumes<vector<reco::Vertex> >      (collections_.getParameter<edm::InputTag> ("primaryvertexs"));
  mcparticlesToken_  = consumes<vector<TYPE(hardInteractionMcparticles)> > (collections_.getParameter<edm::InputTag> ("hardInteractionMcparticles"));
}

void TriggerWeightProducer::AddVariables(const edm::Event &event) {

  edm::Handle<vector<TYPE(mets)> > mets;
  if(!event.getByToken(metsToken_, mets)) {
    clog << "TriggerWeightProducer: could not find mets collection." << endl;
    return;
  }

  edm::Handle<vector<TYPE(muons)> > muons;
  if(!event.getByToken(muonsToken_, muons)) {
    clog << "TriggerWeightProducer: could not find muons collection." << endl;
    return;
  }

  edm::Handle<vector<TYPE(tracks)> > tracks;
  if(!event.getByToken(tracksToken_, tracks)) {
    clog << "TriggerWeightProducer: could not find tracks collection." << endl;
    return;
  }

  edm::Handle<vector<reco::Vertex> > vertices;
  if(!event.getByToken(vertexToken_, vertices)) {
    clog << "TriggerWeightProducer: could not find primaryvertexs collection." << endl;
    return;
  }
  const reco::Vertex &pv = vertices->at(0);

  edm::Handle<vector<reco::GenParticle> > genParticles;
  if(!event.getByToken(mcparticlesToken_, genParticles)) {
    clog << "TriggerWeightProducer: could not find hardInteractionMcparticles collection." << endl;
    return;
  }

  if(event.isRealData()) {

    (*eventvariables)["metLegWeight"] = 1;
    (*eventvariables)["metLegWeightMCUp"] = 1;
    (*eventvariables)["metLegWeightMCDown"] = 1;
    (*eventvariables)["metLegWeightDataUp"] = 1;
    (*eventvariables)["metLegWeightDataDown"] = 1;

    (*eventvariables)["trackLegWeight"] = 1;
    (*eventvariables)["trackLegWeightMCUp"] = 1;
    (*eventvariables)["trackLegWeightMCDown"] = 1;
    (*eventvariables)["trackLegWeightDataUp"] = 1;
    (*eventvariables)["trackLegWeightDataDown"] = 1;

    return;
  }

  const TVector2 metNoMu = getPFMETNoMu(*mets, *muons);
  double metNoMuPt = metNoMu.Mod();

  const double leadTrackPt = getLeadTrackPt(*tracks, *genParticles, pv);

  TFile * fin = TFile::Open(efficiencyFile_.c_str());
  if(!fin || fin->IsZombie()) {
    clog << "ERROR [TriggerWeightProducer]: Could not find file: " << efficiencyFile_
         << "; would cause a seg fault." << endl;
    exit(1);
  }

  TGraphAsymmErrors * metLegNumerator     = (TGraphAsymmErrors*)fin->Get((TString)dataset_ + "/metLeg");
  TGraphAsymmErrors * metLegDenominator   = (TGraphAsymmErrors*)fin->Get((TString)target_ + "/metLeg");
  TGraphAsymmErrors * trackLegNumerator   = (TGraphAsymmErrors*)fin->Get((TString)dataset_ + "/trackLeg");
  TGraphAsymmErrors * trackLegDenominator = (TGraphAsymmErrors*)fin->Get((TString)target_ + "/trackLeg");

  if(!metLegNumerator || !metLegDenominator || !trackLegNumerator || !trackLegDenominator) {
    clog << "ERROR [TriggerWeightProducer]: Could not find all efficiency graphs: " << endl
         << "\t" << dataset_ << "/metLeg (/trackLeg), " << endl
         << "\t" << target_ << "/metLeg (/trackLeg)" << endl
         << "Would cause a seg fault." << endl;
    exit(1);
  }

  double numerator, numeratorUp, numeratorDown;
  double denominator, denominatorUp, denominatorDown;

  // met leg

  FindEfficiency(metLegNumerator, metNoMuPt, numerator, numeratorUp, numeratorDown);
  FindEfficiency(metLegDenominator, metNoMuPt, denominator, denominatorUp, denominatorDown);

  double metWeight = (denominator > 0) ? numerator / denominator : 0.;
  double metWeightMCUp = (denominatorUp > 0) ? numerator / denominatorUp : 0.;
  double metWeightMCDown = (denominatorDown > 0) ? numerator / denominatorDown : 0.;
  double metWeightDataUp = (denominator > 0) ? numeratorUp / denominator : 0.;
  double metWeightDataDown = (denominator > 0) ? numeratorDown / denominator : 0.;

  // track leg

  FindEfficiency(trackLegNumerator, leadTrackPt, numerator, numeratorUp, numeratorDown);
  FindEfficiency(trackLegDenominator, leadTrackPt, denominator, denominatorUp, denominatorDown);

  double trackWeight = (denominator > 0) ? numerator / denominator : 0.;
  double trackWeightMCUp = (denominatorUp > 0) ? numerator / denominatorUp : 0.;
  double trackWeightMCDown = (denominatorDown > 0) ? numerator / denominatorDown : 0.;
  double trackWeightDataUp = (denominator > 0) ? numeratorUp / denominator : 0.;
  double trackWeightDataDown = (denominator > 0) ? numeratorDown / denominator : 0.;

  // store variables

  (*eventvariables)["metLegWeight"] = metWeight;
  (*eventvariables)["metLegWeightMCUp"] = metWeightMCUp;
  (*eventvariables)["metLegWeightMCDown"] = metWeightMCDown;
  (*eventvariables)["metLegWeightDataUp"] = metWeightDataUp;
  (*eventvariables)["metLegWeightDataDown"] = metWeightDataDown;

  (*eventvariables)["trackLegWeight"] = trackWeight;
  (*eventvariables)["trackLegWeightMCUp"] = trackWeightMCUp;
  (*eventvariables)["trackLegWeightMCDown"] = trackWeightMCDown;
  (*eventvariables)["trackLegWeightDataUp"] = trackWeightDataUp;
  (*eventvariables)["trackLegWeightDataDown"] = trackWeightDataDown;

  delete metLegNumerator;
  delete metLegDenominator;
  delete trackLegNumerator;
  delete trackLegDenominator;

}

void TriggerWeightProducer::FindEfficiency(TGraphAsymmErrors * graph, double value,
                                           double& efficiency, double& efficiencyUp, double& efficiencyDown) {

  // If the x-axis value is out of bounds, use the boundary efficiency
  double xmin, ymin, xmax, ymax;
  graph->ComputeRange(xmin, ymin, xmax, ymax);
  if(value < xmin) value = xmin + 1.e-6;
  if(value > xmax) value = xmax - 1.e-6;

  double x, y;

  for(int i = 0; i < graph->GetN(); i++) {
    graph->GetPoint(i, x, y);
    if(graph->GetErrorX(i) > fabs(value - x)) {
      efficiency = y;
      efficiencyUp = y + graph->GetErrorYhigh(i);
      efficiencyDown = y - graph->GetErrorYlow(i);
      return;
    }
  }

  // If you didn't find the graph bin (shouldn't be possible?), return zeros

  efficiency = 0;
  efficiencyUp = 0;
  efficiencyDown = 0;

  return;
}

const TVector2 TriggerWeightProducer::getPFMETNoMu(const vector<TYPE(mets)> &mets, const vector<TYPE(muons)> &muons) const {
  TVector2 metNoMu(0, 0);
  for(const auto &met : mets) {
    metNoMu += TVector2(met.px(), met.py());
    for(const auto &muon : muons) {
      if(muon.isLooseMuon()) metNoMu += TVector2(muon.px(), muon.py());
    }
  }

  return metNoMu;
}

const double TriggerWeightProducer::getLeadTrackPt(const vector<TYPE(tracks)> &tracks,
                                                   const vector<reco::GenParticle> &genParticles,
                                                   const reco::Vertex &pv) const {

  vector<const TYPE(tracks)*> selectedTracks;
  for(const auto &track : tracks) {
      if(isGoodTrack(track, pv, genParticles)) selectedTracks.push_back(&track);
  }

  sort(selectedTracks.begin(),
       selectedTracks.end(),
       [](const TYPE(tracks) *a, const TYPE(tracks) *b) -> bool { return (a->pt() > b->pt()); });

  return selectedTracks.size() ? selectedTracks.at(0)->pt() : -1.0;
}

bool TriggerWeightProducer::isGoodTrack(const TYPE(tracks) &track,
                                        const reco::Vertex &pv,
                                        const vector<reco::GenParticle> &genParticles) const {

  return (isGoodTrack(track, pv) &&
          (genParticles.size() == 0 || genMatched(track, genParticles, 1000024, 3, 0.1)));

}

bool TriggerWeightProducer::isGoodTrack(const TYPE(tracks) &track,
                                        const reco::Vertex &pv) const {
  if(fabs(track.eta()) < 2.5 &&
     track.normalizedChi2() < 10.0 &&
     fabs(track.dxy(pv.position())) < 0.2 &&
     fabs(track.dz(pv.position())) < 0.5 &&
     track.hitPattern().numberOfValidPixelHits() >= 1 &&
     track.hitPattern().trackerLayersWithMeasurement() >= 6 &&
     track.hitPattern().trackerLayersWithoutMeasurement(reco::HitPattern::MISSING_INNER_HITS) == 0 &&
     track.hitPattern().trackerLayersWithoutMeasurement(reco::HitPattern::TRACK_HITS) == 0 &&
     track.trackIsoNoPUDRp3() / track.pt() < 0.01) {
       return true;
     }

     return false;
}

bool TriggerWeightProducer::genMatched(const TYPE(tracks) &track,
                                       const vector<reco::GenParticle> &genParticles,
                                       const int pdgId,
                                       const int status,
                                       const double maxDeltaR) const {
  for(const auto &genParticle : genParticles) {
      if(abs(genParticle.pdgId()) != abs (pdgId)) continue;
      if(genParticle.status() != status) break;
      if(deltaR(track, genParticle) > maxDeltaR) continue;
      return true;
    }
  return false;
}


#include "FWCore/Framework/interface/MakerMacros.h"
DEFINE_FWK_MODULE(TriggerWeightProducer);

#endif
