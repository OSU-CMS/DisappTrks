#ifndef TRIGGER_EFFICIENCY
#define TRIGGER_EFFICIENCY

#include <string>
#include <map>
#include <vector>

#include "CommonTools/UtilAlgos/interface/TFileService.h"

#include "DataFormats/Common/interface/Handle.h"
#include "DataFormats/Common/interface/TriggerResults.h"
#include "DataFormats/HepMCCandidate/interface/GenParticle.h"
#include "DataFormats/METReco/interface/CaloMET.h"
#include "DataFormats/PatCandidates/interface/Jet.h"
#include "DataFormats/PatCandidates/interface/MET.h"
#include "DataFormats/PatCandidates/interface/Muon.h"
#include "DataFormats/PatCandidates/interface/TriggerObjectStandAlone.h"
#include "DataFormats/TrackReco/interface/Track.h"

#include "FWCore/Common/interface/TriggerNames.h"
#include "FWCore/Framework/interface/stream/EDFilter.h"
#include "FWCore/Framework/interface/Event.h"
#include "FWCore/Framework/interface/EventSetup.h"
#include "FWCore/ParameterSet/interface/ParameterSet.h"
#include "FWCore/ServiceRegistry/interface/Service.h"

#include "TH1D.h"
#include "TH2D.h"
#include "TVector2.h"

using namespace std;

template<class T>
class TriggerEfficiency : public edm::stream::EDFilter<>
{
  public:
    TriggerEfficiency (const edm::ParameterSet &);
    ~TriggerEfficiency ();

    bool filter (edm::Event &, const edm::EventSetup &);

  private:
    void logSpace (const unsigned, const double, const double, vector<double> &) const;
    void linSpace (const unsigned, const double, const double, vector<double> &) const;
    const TVector2 * const getPFMETNoMu (const vector<pat::MET> &, const vector<pat::Muon> &) const;
    void fillHistograms (const vector<pat::MET> &, const TVector2 &, const pat::TriggerObjectStandAlone &, const pat::TriggerObjectStandAlone &, const T &, const string &, const string & = "NoTrigger") const;
    void fillHistograms (const vector<pat::MET> &, const TVector2 &, const pat::TriggerObjectStandAlone &, const pat::TriggerObjectStandAlone &, const vector<T> &, const string &, const string & = "NoTrigger") const;
    void fillTrackHistograms (const T &track, const vector<pat::MET> &, const TVector2 &, const string &channel, const string &trigger) const;
    const pat::TriggerObjectStandAlone &getHLTObj (const edm::TriggerNames &, const vector<pat::TriggerObjectStandAlone> &, const string &) const;
    bool passesTriggerFilter (const edm::TriggerNames &, const vector<pat::TriggerObjectStandAlone> &, const string &) const;
    bool passesTrigger (const edm::TriggerNames &, const edm::TriggerResults &, const string &) const;
    double trackIsolation (const reco::Track &, const vector<reco::Track> &, const double, const double) const;
    bool genMatched (const T &, const vector<reco::GenParticle> &, const int, const int, const double) const;
    bool hasGoodMuon (const vector<pat::Muon> &, const reco::Vertex &) const;
    bool isGoodTrack (const T &, const reco::Vertex &, const vector<T> &, const vector<reco::GenParticle> &) const;
    bool isGoodTrack (const T &, const reco::Vertex &, const vector<T> &) const;

    bool isMC_;
    bool matchToHLTTrack_;

    edm::InputTag  metsTag_;
    edm::InputTag  muonsTag_;
    edm::InputTag  tracksTag_;
    edm::InputTag  triggerBitsTag_;
    edm::InputTag  triggerObjsTag_;
    edm::InputTag  verticesTag_;
    edm::InputTag  genParticlesTag_;
    edm::InputTag  jetsTag_;

    edm::EDGetTokenT<vector<pat::MET> > metsToken_;
    edm::EDGetTokenT<vector<pat::Muon> > muonsToken_;
    edm::EDGetTokenT<vector<T> > tracksToken_;
    edm::EDGetTokenT<edm::TriggerResults> triggerBitsToken_;
    edm::EDGetTokenT<vector<pat::TriggerObjectStandAlone> > triggerObjsToken_;
    edm::EDGetTokenT<vector<reco::Vertex> > verticesToken_;
    edm::EDGetTokenT<vector<reco::GenParticle> > genParticlesToken_;
    edm::EDGetTokenT<vector<pat::Jet> > jetsToken_;

    vector<vector<string> > metTriggersList_;
    vector<string> metTriggerNames_;

    edm::Service<TFileService> fs_;
    map<string, map<string, TH1D *> > oneDHists_;
    map<string, map<string, TH2D *> > twoDHists_;
};

#endif
