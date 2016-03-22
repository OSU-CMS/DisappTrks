#ifndef EVENT_JET_VAR_PRODUCER
#define EVENT_JET_VAR_PRODUCER  

#include "OSUT3Analysis/AnaTools/interface/EventVariableProducer.h"
#include "TLorentzVector.h"
#include "DataFormats/Math/interface/deltaPhi.h"
#include "OSUT3Analysis/AnaTools/interface/DataFormat.h"
#include "OSUT3Analysis/AnaTools/interface/ValueLookupTree.h"
#include "OSUT3Analysis/AnaTools/interface/CommonUtils.h"
#include "DataFormats/VertexReco/interface/Vertex.h"



class EventJetVarProducer : public EventVariableProducer {
public:
  EventJetVarProducer (const edm::ParameterSet &);
  ~EventJetVarProducer ();
  
private:
  void AddVariables(const edm::Event &);
  edm::EDGetTokenT<vector<TYPE(jets)> > tokenJets_;
  edm::EDGetTokenT<vector<TYPE(electrons)> > tokenElectrons_;
  edm::EDGetTokenT<vector<TYPE(muons)> > tokenMuons_;
  edm::EDGetTokenT<vector<TYPE(mets)>  > tokenMets_;
  edm::EDGetTokenT<       TYPE(beamspots)>  tokenBeamspot_;
  edm::EDGetTokenT<vector<TYPE(primaryvertexs)>  > tokenVertices_;

  bool IsValidJet(const TYPE(jets) & jet, 
		  edm::Handle<vector<TYPE(electrons) > > & electrons,
		  edm::Handle<vector<TYPE(muons) > > & muons,
		  const reco::BeamSpot &beamspot, 
		  const reco::Vertex &vertex);   

  bool passesTightID (const pat::Electron &electron, 
		      const reco::BeamSpot &beamspot, 
		      const reco::Vertex &vertex  
		      // const edm::Handle<vector<reco::Conversion> > &conversions
		      ) const;  
    
};



EventJetVarProducer::EventJetVarProducer(const edm::ParameterSet &cfg) :
  EventVariableProducer(cfg)
{
  tokenJets_      = consumes<vector<TYPE(jets)> >      (collections_.getParameter<edm::InputTag> ("jets"));
  tokenElectrons_ = consumes<vector<TYPE(electrons)> > (collections_.getParameter<edm::InputTag> ("electrons"));
  tokenMuons_     = consumes<vector<TYPE(muons)> >     (collections_.getParameter<edm::InputTag> ("muons"));
  tokenMets_      = consumes<vector<TYPE(mets)> >      (collections_.getParameter<edm::InputTag> ("mets"));
  tokenBeamspot_  = consumes<reco::BeamSpot>           (collections_.getParameter<edm::InputTag> ("beamspots"));
  tokenVertices_  = consumes<vector<reco::Vertex> >    (collections_.getParameter<edm::InputTag> ("primaryvertexs"));  

}

EventJetVarProducer::~EventJetVarProducer() {}

bool
EventJetVarProducer::IsValidJet(const TYPE(jets) & jet, 
				edm::Handle<vector<TYPE(electrons) > > & electrons,
				edm::Handle<vector<TYPE(muons) > > & muons,
				const reco::BeamSpot &beamspot, 
				const reco::Vertex &vertex) {  

  // clog << "Checking valid jet" << endl;  
  if (!(jet.pt() > 30))         return false; 
  if (!(fabs(jet.eta()) < 4.5)) return false; 

  // Now check that the jet is not within DeltaR<0.15 of a tight electron or muon.  
  for (const auto &elec : *electrons) {
    if (elec.pt() > 20 &&
	passesTightID(elec, beamspot, vertex) && 
	fabs(deltaR(elec, jet)) < 0.15)
      return false; 
  }
  for (const auto &muon : *muons) {
    // cout << "Debug:  found muon with: "
    // 	 << " pt = " << muon.pt()
    // 	 << ", istight = " << muon.isTightMuon(vertex) 
    // 	 << ", deltaR(muon, jet) = " << deltaR(muon, jet) 
    // 	 << ", jet pt = " << jet.pt()
    // 	 << ", jet eta = " << jet.eta()  
    // 	 << endl;  
    if (muon.pt() > 20 &&
	muon.isTightMuon(vertex) &&
	fabs(deltaR(muon, jet)) < 0.15)  
      return false; 
  }

  return true;  
}


void
EventJetVarProducer::AddVariables (const edm::Event &event) {

  edm::Handle<vector<TYPE(jets)> > jets;
  if (!event.getByToken (tokenJets_, jets)) {
    clog << "ERROR:  Could not find jets collection." << endl; 
    return;
  } 

  edm::Handle<vector<TYPE(electrons)> > electrons;
  if (!event.getByToken (tokenElectrons_, electrons)) {
    clog << "ERROR:  Could not find electrons collection." << endl; 
    return;
  } 

  edm::Handle<vector<TYPE(muons)> > muons;
  if (!event.getByToken (tokenMuons_, muons)) {
    clog << "ERROR:  Could not find muons collection." << endl; 
    return;
  } 

  edm::Handle<vector<TYPE(mets)> > mets;
  if (!event.getByToken (tokenMets_, mets)) {
    clog << "ERROR:  Could not find mets collection." << endl; 
    return;
  } 

  edm::Handle<reco::BeamSpot> beamspot;
  if (!event.getByToken (tokenBeamspot_, beamspot)) {
    clog << "ERROR:  Could not find beamspot collection." << endl; 
    return;
  }

  edm::Handle<vector<reco::Vertex> > vertices;
  if (!event.getByToken (tokenVertices_, vertices)) { 
    clog << "ERROR:  Could not find primary vertex collection." << endl; 
    return;
  }

  reco::Vertex vertex; 
  // if (vertices->size()) {
  //   vertex = vertices->at(0);
  // } else {
  //   clog << "ERROR:  Primary vertex collection is empty.  Please fix." << endl;
  //   exit(0);  
  // }

  if (!vertices->size()) {
    clog << "ERROR:  Primary vertex collection is empty.  Please fix." << endl;
    exit(0);  
  }
  
  int nJets = 0; 
  double dijetMaxDeltaPhi         = -999.;  // default is large negative value
  double deltaPhiMetJetLeading    =  999.;  // default is large positive value
  double deltaPhiMetJetSubleading =  999.; 
  double ptJetLeading    = -999;
  double ptJetSubleading = -999;
  int idx1 = -1;
  for (const auto &jet1 : *jets) {
    idx1++;  
    if (!(IsValidJet(jet1, electrons, muons, *beamspot, vertices->at(0)))) continue;  
    int idx2 = -1; 
    if (jet1.pt() > ptJetSubleading) {
      double dPhi = fabs(deltaPhi(jet1, mets->at(0)));  
      if (jet1.pt() > ptJetLeading) { 
	ptJetSubleading = ptJetLeading; 
	deltaPhiMetJetSubleading = deltaPhiMetJetLeading;
	ptJetLeading = jet1.pt();
	deltaPhiMetJetLeading = dPhi;
      } else {
	ptJetSubleading = jet1.pt();  
	deltaPhiMetJetSubleading = dPhi;  
      }		
    } 
    for (const auto &jet2 : *jets) {
      idx2++;  
      if (idx2 <= idx1)              continue;  // Avoid double-counting.  
      if (!(IsValidJet(jet2, electrons, muons, *beamspot, vertices->at(0)))) continue;  
      double dPhi = fabs(deltaPhi(jet1.phi(), jet2.phi()));  
      if (dPhi > dijetMaxDeltaPhi) {
	dijetMaxDeltaPhi = dPhi; 
      }  
    }
    nJets++;  
  }

  (*eventvariables)["nJets"]            = nJets;
  (*eventvariables)["dijetMaxDeltaPhi"] = dijetMaxDeltaPhi; 
  (*eventvariables)["deltaPhiMetJetLeading"]     = deltaPhiMetJetLeading;
  (*eventvariables)["deltaPhiMetJetSubleading"]  = deltaPhiMetJetSubleading;

}


// This function copied from CandidateTrackProducer/src/CandidateTrack.cc.
// Eventually switch to that version.
// But for now conversions are not available in skims, so remove that criterion.  
bool
EventJetVarProducer::passesTightID (const pat::Electron &electron, 
				    const reco::BeamSpot &beamspot, 
				    const reco::Vertex &vertex  
				    // const edm::Handle<vector<reco::Conversion> > &conversions
				    ) const
{
  if (fabs (electron.superCluster ()->eta ()) <= 1.479)
    {
      return (electron.full5x5_sigmaIetaIeta ()                                                              <   0.0101
           && fabs (electron.deltaEtaSuperClusterTrackAtVtx ())                                              <   0.00926
           && fabs (electron.deltaPhiSuperClusterTrackAtVtx ())                                              <   0.0336
           && electron.hadronicOverEm ()                                                                     <   0.0597
           && fabs (1.0 / electron.ecalEnergy () - electron.eSuperClusterOverP () / electron.ecalEnergy ())  <   0.012
           && fabs (electron.gsfTrack ()->dxy (vertex.position ()))                                          <   0.0111
           && fabs (electron.gsfTrack ()->dz (vertex.position ()))                                           <   0.0466
           && electron.gsfTrack ()->hitPattern ().numberOfHits (reco::HitPattern::MISSING_INNER_HITS)        <=  2
           // && !ConversionTools::hasMatchedConversion (electron, conversions, beamspot.position ()));
	      ); 
    }
  else if (fabs (electron.superCluster ()->eta ()) < 2.5)
    {
      return (electron.full5x5_sigmaIetaIeta ()                                                              <   0.0279
           && fabs (electron.deltaEtaSuperClusterTrackAtVtx ())                                              <   0.00724
           && fabs (electron.deltaPhiSuperClusterTrackAtVtx ())                                              <   0.0918
           && electron.hadronicOverEm ()                                                                     <   0.0615
           && fabs (1.0 / electron.ecalEnergy () - electron.eSuperClusterOverP () / electron.ecalEnergy ())  <   0.00999
           && fabs (electron.gsfTrack ()->dxy (vertex.position ()))                                          <   0.0351
           && fabs (electron.gsfTrack ()->dz (vertex.position ()))                                           <   0.417
           && electron.gsfTrack ()->hitPattern ().numberOfHits (reco::HitPattern::MISSING_INNER_HITS)        <=  1
           // && !ConversionTools::hasMatchedConversion (electron, conversions, beamspot.position ()));
	      );  
    }
  return false;
}


#include "FWCore/Framework/interface/MakerMacros.h"
DEFINE_FWK_MODULE(EventJetVarProducer);


#endif

