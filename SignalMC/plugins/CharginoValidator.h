#ifndef CHARGINO_VALIDATOR

#define CHARGINO_VALIDATOR

#include <map>
#include <string>

#include "TH1D.h"
#include "TH2D.h"
#include "TLorentzVector.h"
#include "TVector3.h"

#include "FWCore/Framework/interface/Frameworkfwd.h"
#include "FWCore/Framework/interface/stream/EDAnalyzer.h"

#include "DataFormats/TrackReco/interface/Track.h"
#include "DataFormats/HepMCCandidate/interface/GenParticle.h"
#include "DataFormats/Math/interface/deltaR.h"
#include "DataFormats/METReco/interface/GenMET.h"
#include "DataFormats/METReco/interface/GenMETCollection.h"
#include "DataFormats/METReco/interface/PFMET.h"
#include "DataFormats/METReco/interface/PFMETCollection.h"
#include "DataFormats/MuonReco/interface/Muon.h"
#include "CommonTools/UtilAlgos/interface/TFileService.h"
#include "FWCore/Framework/interface/Event.h"
#include "FWCore/Framework/interface/MakerMacros.h"
#include "FWCore/ParameterSet/interface/ParameterSet.h"
#include "FWCore/ServiceRegistry/interface/Service.h"
#include "FWCore/Utilities/interface/InputTag.h"

using namespace std;

class CharginoValidator : public edm::stream::EDAnalyzer<> {
   public:
      explicit CharginoValidator (const edm::ParameterSet &);
      ~CharginoValidator ();

   private:
      void analyze (const edm::Event &, const edm::EventSetup &);

      edm::InputTag genParticles_;
      edm::InputTag genMets_;
      edm::InputTag tracks_;
      edm::InputTag pfmet_;
      edm::InputTag muonsCol_;
      edm::EDGetTokenT<vector<reco::PFMET> > pfmetToken_;
      edm::EDGetTokenT<vector<reco::Track> > tracksToken_;
      edm::EDGetTokenT<vector<reco::GenParticle> > genParticlesToken_;
      edm::EDGetTokenT<reco::GenMETCollection> genMetsToken_;
      edm::EDGetTokenT<vector<reco::Muon> > muonsToken_;

      bool cutPythia8Flag_;

      edm::Service<TFileService> fs_;
      map<string, TH1D *> oneDHists_;
      map<string, TH2D *> twoDHists_;

      void getEndVertex (const reco::GenParticle &, TVector3 &) const;
      const reco::Track * getMatchedTrack (const reco::GenParticle &, const edm::Handle<vector<reco::Track> > &) const;
      unsigned getMatchedTrackNumber (const reco::GenParticle &, const edm::Handle<vector<reco::Track> > &) const;
      const reco::Muon * getMatchedMuon (const reco::GenParticle &, const edm::Handle<vector<reco::Muon> > &) const;
      void logSpace (const unsigned, const double, const double, vector<double> &) const;
};

#endif
