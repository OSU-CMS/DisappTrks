// -*- C++ -*-
//
// Package:    DisappTrks/CandidateTrackProducer
// Class:      CandidateTrackProducer
//
/**\class CandidateTrackProducer CandidateTrackProducer.cc DisappTrks/CandidateTrackProducer/plugins/CandidateTrackProducer.cc

 Description: Calculates quantities of interest for candidate disappearing tracks.

 Implementation:
   Run this producer with AOD as input, to produce MiniAOD output.


*/
//
// Original Author:  Wells Wulsin
//         Created:  Thu, 17 Sep 2015 09:33:32 GMT
//
//

// user include files
#include "FWCore/Framework/interface/EDProducer.h"

#include "FWCore/Framework/interface/Event.h"
#include "FWCore/Framework/interface/MakerMacros.h"

#include "FWCore/ParameterSet/interface/ParameterSet.h"

#include "FWCore/Utilities/interface/InputTag.h"

using namespace std;

//
// class declaration
//

class CandidateTrackProducer : public edm::EDProducer {
   public:
      explicit CandidateTrackProducer (const edm::ParameterSet&);
      ~CandidateTrackProducer ();

   private:
      virtual void produce (edm::Event&, const edm::EventSetup&) override;

      // ----------member data ---------------------------
       edm::InputTag tracksTag_;
       edm::InputTag electronsTag_;
       edm::InputTag muonsTag_;
       edm::InputTag tausTag_;
};
