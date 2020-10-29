#include "FWCore/Common/interface/TriggerNames.h"
#include "FWCore/Framework/interface/EDFilter.h"
#include "FWCore/Framework/interface/Run.h"
#include "FWCore/Framework/interface/Event.h"
#include "FWCore/Framework/interface/MakerMacros.h"
#include "FWCore/ParameterSet/interface/ParameterSet.h"
#include "FWCore/Utilities/interface/InputTag.h"

#include "DataFormats/Common/interface/TriggerResults.h"
#include "DataFormats/PatCandidates/interface/MET.h"
#include "DataFormats/PatCandidates/interface/Electron.h"
#include "DataFormats/PatCandidates/interface/Muon.h"
#include "DataFormats/PatCandidates/interface/PackedCandidate.h"
#include "DataFormats/VertexReco/interface/Vertex.h"

#include "RecoEgamma/EgammaTools/interface/ConversionTools.h"

using namespace std;

enum Flavor {ELECTRON, MUON};

template<Flavor T>
class ZToLLFilter : public edm::EDFilter {
   public:
      ZToLLFilter (const edm::ParameterSet &);
      ~ZToLLFilter ();

      bool filter (edm::Event &, const edm::EventSetup &);

   private:
      bool passesTrigger(const edm::Event &, const edm::TriggerResults &) const;
      void selectLeptons(const edm::Event &,
                         const reco::Vertex &,
                         const vector<pat::Electron> &, const vector<pat::Muon> &,
                         vector<pat::Electron> &, vector<pat::Muon> &);

      bool filterDecision(const vector<pat::Electron>, const vector<pat::Muon>) const;

      edm::InputTag triggers_;
      edm::InputTag vertices_;
      edm::InputTag electrons_;
      edm::InputTag muons_;

      vector<string> triggerNames_;
      string dataTakingPeriod_;

      bool is2017_;

      edm::EDGetTokenT<edm::TriggerResults>                   triggersToken_;
      edm::EDGetTokenT<vector<reco::Vertex> >                 verticesToken_;
      edm::EDGetTokenT<vector<pat::Electron> >                electronsToken_;
      edm::EDGetTokenT<vector<pat::Muon> >                    muonsToken_;
};
