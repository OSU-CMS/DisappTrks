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


// system include files
#include <memory>

// user include files
#include "FWCore/Framework/interface/Frameworkfwd.h"
#include "FWCore/Framework/interface/EDProducer.h"

#include "FWCore/Framework/interface/Event.h"
#include "FWCore/Framework/interface/MakerMacros.h"

#include "FWCore/ParameterSet/interface/ParameterSet.h"

#include "DataFormats/TrackReco/interface/TrackFwd.h"
#include "DataFormats/TrackReco/interface/Track.h"
#include "DataFormats/TrackReco/interface/TrackExtra.h"

#include "FWCore/MessageLogger/interface/MessageLogger.h"
#include "FWCore/Utilities/interface/InputTag.h"

//
// class declaration
//

class CandidateTrackProducer : public edm::EDProducer {
   public:
      explicit CandidateTrackProducer(const edm::ParameterSet&);
      ~CandidateTrackProducer();

      static void fillDescriptions(edm::ConfigurationDescriptions& descriptions);

   private:
      virtual void beginJob() override;
      virtual void produce(edm::Event&, const edm::EventSetup&) override;
      virtual void endJob() override;
      
      //virtual void beginRun(edm::Run const&, edm::EventSetup const&) override;
      //virtual void endRun(edm::Run const&, edm::EventSetup const&) override;
      //virtual void beginLuminosityBlock(edm::LuminosityBlock const&, edm::EventSetup const&) override;
      //virtual void endLuminosityBlock(edm::LuminosityBlock const&, edm::EventSetup const&) override;

      // ----------member data ---------------------------
       edm::InputTag tracksTag_; 
};

//
// constants, enums and typedefs
//

       // define container that will be booked into event
//       typedef std::vector<reco::Particle> MyParticleCollection;

//
// static data member definitions
//

//
// constructors and destructor
//
CandidateTrackProducer::CandidateTrackProducer(const edm::ParameterSet& iConfig)
 :
   tracksTag_( iConfig.getParameter<edm::InputTag>( "tracks" ))
{

  produces<std::vector<reco::Track> >("candidateDisappearingTracks");

}


CandidateTrackProducer::~CandidateTrackProducer()
{
 
   // do anything here that needs to be done at desctruction time
   // (e.g. close files, deallocate resources etc.)

}


//
// member functions
//

// ------------ method called to produce the data  ------------
void
CandidateTrackProducer::produce(edm::Event& iEvent, const edm::EventSetup& iSetup)
{
  using namespace edm;
  using namespace reco;
  using namespace std;
/* This is an event example
   //Read 'ExampleData' from the Event
   Handle<ExampleData> pIn;
   iEvent.getByLabel("example",pIn);

   //Use the ExampleData to create an ExampleData2 which 
   // is put into the Event
   std::unique_ptr<ExampleData2> pOut(new ExampleData2(*pIn));
   iEvent.put(std::move(pOut));
*/

/* this is an EventSetup example
   //Read SetupData from the SetupRecord in the EventSetup
   ESHandle<SetupData> pSetup;
   iSetup.get<SetupRecord>().get(pSetup);
*/
 
  Handle<TrackCollection> tracks;
  iEvent.getByLabel( tracksTag_, tracks );
    
    
  // create a new collection of Particle objects
  // unique_ptr<MyParticleCollection> newParticles( new MyParticleCollection );
  std::auto_ptr<std::vector<reco::Track> > candTracks(new std::vector<reco::Track>());
  candTracks->reserve(tracks->size());

 
    // // if the number of electrons or muons is 4 (or 2 and 2), costruct a new particle
    // if( muons->size() == 4 || electrons->size() == 4 || ( muons->size() == 2 && electrons->size() == 2 ) ) {
       
    //    // sums of momenta and charges will be calculated
    //    Particle::LorentzVector totalP4( 0, 0, 0, 0 );
    //    Particle::Charge charge( 0 );
       
    //    // loop over muons, sum over p4s and charges. Later same for electrons
    //    for( MuonCollection::const_iterator muon = muons->begin(); muon != muons->end(); ++muon ) {
    //       totalP4 += muon->p4();
    //       charge += muon->charge();
    //    }
       
    //    for( PixelMatchGsfElectronCollection::const_iterator electron = electrons->begin(); electron != electrons->end(); ++electron ) {
    //       totalP4 += electron->p4(); 
    //       charge += electron->charge(); 
    //    }
       
    //    // create a particle with momentum and charge from muons and electrons
    //    Particle h;
    //    h.setP4(totalP4);
    //    h.setCharge(charge);
 
    //    // fill the particles into the vector
    //    newParticles->push_back( h );      
    // }
    
    // save the vector
    iEvent.put( candTracks, "candidateDisappearingTracks" );
}

// ------------ method called once each job just before starting event loop  ------------
void 
CandidateTrackProducer::beginJob()
{
}

// ------------ method called once each job just after ending the event loop  ------------
void 
CandidateTrackProducer::endJob() {
}

// ------------ method called when starting to processes a run  ------------
/*
void
CandidateTrackProducer::beginRun(edm::Run const&, edm::EventSetup const&)
{
}
*/
 
// ------------ method called when ending the processing of a run  ------------
/*
void
CandidateTrackProducer::endRun(edm::Run const&, edm::EventSetup const&)
{
}
*/
 
// ------------ method called when starting to processes a luminosity block  ------------
/*
void
CandidateTrackProducer::beginLuminosityBlock(edm::LuminosityBlock const&, edm::EventSetup const&)
{
}
*/
 
// ------------ method called when ending the processing of a luminosity block  ------------
/*
void
CandidateTrackProducer::endLuminosityBlock(edm::LuminosityBlock const&, edm::EventSetup const&)
{
}
*/
 
// ------------ method fills 'descriptions' with the allowed parameters for the module  ------------
void
CandidateTrackProducer::fillDescriptions(edm::ConfigurationDescriptions& descriptions) {
  //The following says we do not know what parameters are allowed so do no validation
  // Please change this to state exactly what you do use, even if it is no parameters
  edm::ParameterSetDescription desc;
  desc.setUnknown();
  descriptions.addDefault(desc);
  
  //Specify that only 'muons' and 'electrons' are allowed
  //To use, remove the default given above and uncomment below
  //ParameterSetDescription desc;
  //desc.add<edm::InputTag>("muons","muons");
  //desc.add<edm::InputTag>("electrons","pixelMatchGsfElectrons");
  //descriptions.addDefault(desc);
}

//define this as a plug-in
DEFINE_FWK_MODULE(CandidateTrackProducer);
