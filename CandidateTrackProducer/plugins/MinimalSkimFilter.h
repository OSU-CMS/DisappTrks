#include "FWCore/Common/interface/TriggerNames.h"
#include "FWCore/Framework/interface/one/EDFilter.h"
#include "FWCore/Framework/interface/Run.h"
#include "FWCore/Framework/interface/Event.h"
#include "FWCore/Framework/interface/MakerMacros.h"
#include "FWCore/ParameterSet/interface/ParameterSet.h"
#include "FWCore/Utilities/interface/InputTag.h"

#include "DataFormats/BeamSpot/interface/BeamSpot.h"
#include "DataFormats/Common/interface/TriggerResults.h"
#include "DataFormats/PatCandidates/interface/MET.h"
#include "DataFormats/PatCandidates/interface/Electron.h"
#include "DataFormats/PatCandidates/interface/Muon.h"
#include "DataFormats/PatCandidates/interface/Tau.h"
#include "DataFormats/VertexReco/interface/Vertex.h"

#include "RecoEgamma/EgammaTools/interface/ConversionTools.h"

#include "DisappTrks/CandidateTrackProducer/interface/CutResult.h"

using namespace std;

enum MinimalSkim {MET, ELECTRON, MUON, TAU};

template<MinimalSkim T>
class MinimalSkimFilter : public edm::one::EDFilter<edm::EndRunProducer> {
   public:
      MinimalSkimFilter (const edm::ParameterSet &);
      ~MinimalSkimFilter ();

      bool filter (edm::Event &, const edm::EventSetup &);
      void endRunProduce (edm::Run &, const edm::EventSetup &);

   private:
      bool passesTightID_noIsolation_2015 (const pat::Electron &, const reco::BeamSpot &, const reco::Vertex &, const edm::Handle<vector<reco::Conversion> > &) const;
      bool passesTightID_noIsolation_2016 (const pat::Electron &, const reco::BeamSpot &, const reco::Vertex &, const edm::Handle<vector<reco::Conversion> > &) const;
      double effectiveArea_2015 (const pat::Electron &) const;
      double effectiveArea_2016 (const pat::Electron &) const;
      bool passesTrigger (const edm::Event &, const edm::TriggerResults &) const;
      void initializeCutResults ();
      bool filterDecision (const edm::Event &event, const edm::TriggerResults &, const reco::BeamSpot &, const reco::Vertex &, const pat::MET &, const vector<pat::Electron> &, const edm::Handle<vector<reco::Conversion> > &, const vector<pat::Muon> &, const vector<pat::Tau> &, const double) const;

      edm::InputTag triggers_;
      edm::InputTag beamspot_;
      edm::InputTag vertices_;
      edm::InputTag met_;
      edm::InputTag electrons_;
      edm::InputTag conversions_;
      edm::InputTag muons_;
      edm::InputTag taus_;
      edm::InputTag rho_;
      vector<string> triggerNames_;

      edm::EDGetTokenT<edm::TriggerResults>        triggersToken_;
      edm::EDGetTokenT<reco::BeamSpot>             beamspotToken_;
      edm::EDGetTokenT<vector<reco::Vertex> >      verticesToken_;
      edm::EDGetTokenT<vector<pat::MET> >          metToken_;
      edm::EDGetTokenT<vector<pat::Electron> >     electronsToken_;
      edm::EDGetTokenT<vector<reco::Conversion> >  conversionsToken_;
      edm::EDGetTokenT<vector<pat::Muon> >         muonsToken_;
      edm::EDGetTokenT<vector<pat::Tau> >          tausToken_;
      edm::EDGetTokenT<double>                     rhoToken_;

      unique_ptr<CutResults> cutResults_;
};
