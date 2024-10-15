#include "FWCore/Common/interface/TriggerNames.h"
#include "FWCore/Framework/interface/stream/EDFilter.h"
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
#include "DisappTrks/CandidateTrackProducer/interface/CandidateTrack.h"


#if CMSSW_VERSION_CODE >= CMSSW_VERSION(11,2,0)
#include "CommonTools/Egamma/interface/ConversionTools.h"
#else
#include "RecoEgamma/EgammaTools/interface/ConversionTools.h"
#endif

using namespace std;

class TrainingPreselectionSkim : public edm::stream::EDFilter<> {
   public:
      TrainingPreselectionSkim (const edm::ParameterSet &);
      ~TrainingPreselectionSkim ();

      bool filter (edm::Event &, const edm::EventSetup &);

   private:
     
      string dataTakingPeriod_;
      edm::InputTag tracks_;

      bool is2017_;
      
      edm::EDGetTokenT<vector<reco::Track> > tracksToken_;

};
