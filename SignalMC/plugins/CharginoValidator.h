#ifndef CHARGINO_VALIDATOR

#define CHARGINO_VALIDATOR

#include <map>
#include <string>

#include "TH1D.h"
#include "TH2D.h"
#include "TVector3.h"
#include "TLorentzVector.h"

#include "CommonTools/UtilAlgos/interface/TFileService.h"

#include "DataFormats/TrackReco/interface/Track.h"
#include "DataFormats/HepMCCandidate/interface/GenParticle.h"
#include "DataFormats/Math/interface/deltaR.h"
#include "DataFormats/METReco/interface/GenMET.h"
#include "DataFormats/METReco/interface/GenMETCollection.h"

#include "FWCore/Framework/interface/EDAnalyzer.h"
#include "FWCore/Framework/interface/Event.h"
#include "FWCore/Framework/interface/MakerMacros.h"
#include "FWCore/ParameterSet/interface/ParameterSet.h"
#include "FWCore/ServiceRegistry/interface/Service.h"
#include "SimDataFormats/PileupSummaryInfo/interface/PileupSummaryInfo.h"
#include "FWCore/Utilities/interface/InputTag.h"

using namespace std;

class CharginoValidator : public edm::EDAnalyzer {
   public:
      explicit CharginoValidator (const edm::ParameterSet &);
      ~CharginoValidator ();

   private:
      void analyze (const edm::Event &, const edm::EventSetup &);

      edm::InputTag tracks_;
      edm::InputTag genParticles_;
      edm::InputTag pileupInfo_;
      edm::InputTag genMets_;

      edm::EDGetTokenT<vector<reco::Track> > tracksToken_;
      edm::EDGetTokenT<vector<reco::GenParticle> > genParticlesToken_;
      edm::EDGetTokenT<edm::View<PileupSummaryInfo> > pileupInfoToken_;
      edm::EDGetTokenT<reco::GenMETCollection> genMetsToken_;

      bool cutPythia8Flag_;

      edm::Service<TFileService> fs_;
      map<string, TH1D *> oneDHists_;
      map<string, TH2D *> twoDHists_;

      void getEndVertex (const reco::GenParticle &, TVector3 &) const;
      const reco::Track * getMatchedTrack (const reco::GenParticle &, const edm::Handle<vector<reco::Track> > &) const;
};

#endif
