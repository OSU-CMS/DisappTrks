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
#include "DataFormats/PatCandidates/interface/MET.h"
#include "DataFormats/PatCandidates/interface/Muon.h"
#include "DataFormats/PatCandidates/interface/TriggerObjectStandAlone.h"
#include "DataFormats/TrackReco/interface/Track.h"

#include "FWCore/Common/interface/TriggerNames.h"
#include "FWCore/Framework/interface/EDAnalyzer.h"
#include "FWCore/Framework/interface/Event.h"
#include "FWCore/Framework/interface/EventSetup.h"
#include "FWCore/ParameterSet/interface/ParameterSet.h"
#include "FWCore/ServiceRegistry/interface/Service.h"

#include "TH1D.h"
#include "TH2D.h"

using namespace std;

class TriggerEfficiency : public edm::EDAnalyzer
{
  public:
    TriggerEfficiency (const edm::ParameterSet &);
    ~TriggerEfficiency ();

    void analyze (const edm::Event &, const edm::EventSetup &);

  private:
    void logSpace (const unsigned, const double, const double, vector<double> &) const;
    void linSpace (const unsigned, const double, const double, vector<double> &) const;
    void fillHistograms (const vector<pat::MET> &, const vector<reco::CaloMET> &, const pat::TriggerObjectStandAlone &, const pat::TriggerObjectStandAlone &, const vector<pat::Muon> &, const string &, const string & = "NoTrigger") const;
    void fillHistograms (const vector<pat::MET> &, const vector<reco::CaloMET> &, const pat::TriggerObjectStandAlone &, const pat::TriggerObjectStandAlone &, const pat::Muon &, const string &, const string & = "NoTrigger") const;
    const pat::TriggerObjectStandAlone &getHLTMET (const edm::TriggerNames &, const vector<pat::TriggerObjectStandAlone> &, const string &) const;
    bool passesTriggerFilter (const edm::TriggerNames &, const vector<pat::TriggerObjectStandAlone> &, const string &) const;
    bool passesTrigger (const edm::TriggerNames &, const edm::TriggerResults &, const string &) const;
    bool genMatched (const pat::Muon &, const vector<reco::GenParticle> &, const int, const int, const double) const;

    edm::InputTag  mets_;
    edm::InputTag  caloMets_;
    edm::InputTag  muons_;
    edm::InputTag  electrons_;
    edm::InputTag  triggerBits_;
    edm::InputTag  triggerObjs_;
    edm::InputTag  vertices_;
    edm::InputTag  genParticles_;

    vector<vector<string> > metTriggersList_;
    vector<string> metTriggerNames_;

    edm::Service<TFileService> fs_;
    map<string, map<string, TH1D *> > oneDHists_;
    map<string, map<string, TH2D *> > twoDHists_;
};

#endif
