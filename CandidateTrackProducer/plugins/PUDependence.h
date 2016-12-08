#ifndef PU_DEPENDENCE
#define PU_DEPENDENCE

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
#include "FWCore/Framework/interface/EDAnalyzer.h"
#include "FWCore/Framework/interface/Event.h"
#include "FWCore/Framework/interface/EventSetup.h"
#include "FWCore/ParameterSet/interface/ParameterSet.h"
#include "FWCore/ServiceRegistry/interface/Service.h"

#include "TH1D.h"
#include "TH2D.h"
#include "TVector2.h"

using namespace std;

class PUDependence : public edm::EDAnalyzer
{
  public:
    PUDependence (const edm::ParameterSet &);
    ~PUDependence ();

    void analyze (const edm::Event &, const edm::EventSetup &);

  private:
    void logSpace (const unsigned, const double, const double, vector<double> &) const;
    void linSpace (const unsigned, const double, const double, vector<double> &) const;
    template<class T> bool genMatched (const T &, const vector<reco::GenParticle> &, const int, const int, const double) const;

    edm::InputTag  tracks_;
    edm::InputTag  vertices_;
    edm::InputTag  genParticles_;

    edm::Service<TFileService> fs_;
    map<string, TH1D *> oneDHists_;
    map<string, TH2D *> twoDHists_;
};

#endif
