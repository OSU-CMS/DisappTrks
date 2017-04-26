#ifndef DEDX_ANALYZER

#define DEDX_ANALYZER

#include <map>
#include <string>

#include "TH1D.h"
#include "TH2D.h"

#include "CommonTools/UtilAlgos/interface/TFileService.h"

#include "DataFormats/Common/interface/ValueMap.h"
#include "DataFormats/EgammaCandidates/interface/GsfElectron.h"
#include "DataFormats/MuonReco/interface/Muon.h"
#include "DataFormats/TrackReco/interface/Track.h"
#include "DataFormats/TrackReco/interface/DeDxData.h"

#include "FWCore/Framework/interface/EDAnalyzer.h"
#include "FWCore/Framework/interface/Event.h"
#include "FWCore/Framework/interface/MakerMacros.h"
#include "FWCore/ParameterSet/interface/ParameterSet.h"
#include "FWCore/ServiceRegistry/interface/Service.h"
#include "FWCore/Utilities/interface/InputTag.h"

using namespace std;

struct SlimTrack {
  double pt;
  double eta;
  double phi;

  double p;
  double dEdx;

  SlimTrack (const reco::Track &track, const double meanDEdx) :
    pt (track.pt ()),
    eta (track.eta ()),
    phi (track.phi ()),
    p (track.p ()),
    dEdx (meanDEdx)
  {
  }
};

class DEdxAnalyzer : public edm::EDAnalyzer {
   public:
      explicit DEdxAnalyzer (const edm::ParameterSet &);
      ~DEdxAnalyzer ();

   private:
      void analyze (const edm::Event &, const edm::EventSetup &);

      edm::InputTag tracks_;
      edm::EDGetTokenT<vector<reco::Track> > tracksToken_;
      edm::InputTag electrons_;
      edm::EDGetTokenT<vector<reco::GsfElectron> > electronsToken_;
      edm::InputTag muons_;
      edm::EDGetTokenT<vector<reco::Muon> > muonsToken_;
      edm::InputTag dEdx_;
      edm::EDGetTokenT<edm::ValueMap<reco::DeDxData> > dEdxToken_;
      double minPt_;
      string vetoElectronsOrMuons_;

      edm::Service<TFileService> fs_;
      map<string, TH1D *> oneDHists_;
      map<string, TH2D *> twoDHists_;

      void logSpace (const unsigned, const double, const double, vector<double> &) const;
      bool isNearElectron (const reco::Track &, const vector<reco::GsfElectron> &) const;
      bool isNearMuon (const reco::Track &, const vector<reco::Muon> &) const;
};

#endif
