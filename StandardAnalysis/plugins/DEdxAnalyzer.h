#ifndef DEDX_ANALYZER

#define DEDX_ANALYZER

#include <map>
#include <string>

#include "TH1D.h"
#include "TH2D.h"

#include "CommonTools/UtilAlgos/interface/TFileService.h"

#include "DataFormats/Common/interface/ValueMap.h"
#include "DataFormats/TrackReco/interface/Track.h"
#include "DataFormats/TrackReco/interface/DeDxData.h"

#include "FWCore/Framework/interface/EDAnalyzer.h"
#include "FWCore/Framework/interface/Event.h"
#include "FWCore/Framework/interface/MakerMacros.h"
#include "FWCore/ParameterSet/interface/ParameterSet.h"
#include "FWCore/ServiceRegistry/interface/Service.h"
#include "FWCore/Utilities/interface/InputTag.h"

using namespace std;

class DEdxAnalyzer : public edm::EDAnalyzer {
   public:
      explicit DEdxAnalyzer (const edm::ParameterSet &);
      ~DEdxAnalyzer ();

   private:
      void analyze (const edm::Event &, const edm::EventSetup &);

      edm::InputTag tracks_;
      edm::EDGetTokenT<vector<reco::Track> > tracksToken_;
      edm::InputTag dEdx_;
      edm::EDGetTokenT<edm::ValueMap<reco::DeDxData> > dEdxToken_;

      edm::Service<TFileService> fs_;
      map<string, TH1D *> oneDHists_;
      map<string, TH2D *> twoDHists_;

      void logSpace (const unsigned, const double, const double, vector<double> &) const;
};

#endif
