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
#include "DisappTrks/CandidateTrackProducer/interface/CandidateTrack.h"
#include "DisappTrks/CandidateTrackProducer/plugins/CandidateTrackProducer.h"

#include "MagneticField/Engine/interface/MagneticField.h"
#include "MagneticField/Records/interface/IdealMagneticFieldRecord.h"


#include "DataFormats/Math/interface/deltaR.h"
#include "Geometry/CaloGeometry/interface/CaloSubdetectorGeometry.h"
#include "Geometry/CaloGeometry/interface/CaloCellGeometry.h"

#include "CommonTools/UtilAlgos/interface/TFileService.h"
#include "DataFormats/PatCandidates/interface/IsolatedTrack.h"


using namespace std;
   
//
// constructors and destructor
//
CandidateTrackProducer::CandidateTrackProducer (const edm::ParameterSet& iConfig) :
  tracksTag_    (iConfig.getParameter<edm::InputTag> ("tracks")),
  electronsTag_ (iConfig.getParameter<edm::InputTag> ("electrons")),
  muonsTag_     (iConfig.getParameter<edm::InputTag> ("muons")),
  tausTag_      (iConfig.getParameter<edm::InputTag> ("taus")),
  beamspotTag_      (iConfig.getParameter<edm::InputTag> ("beamspot")),
  verticesTag_      (iConfig.getParameter<edm::InputTag> ("vertices")),
  conversionsTag_   (iConfig.getParameter<edm::InputTag> ("conversions")),
  rhoTag_           (iConfig.getParameter<edm::InputTag> ("rhoTag")),
  rhoCaloTag_       (iConfig.getParameter<edm::InputTag> ("rhoCaloTag")),
  rhoCentralCaloTag_(iConfig.getParameter<edm::InputTag> ("rhoCentralCaloTag")),
  EBRecHitsTag_     (iConfig.getParameter<edm::InputTag> ("EBRecHits")),
  EERecHitsTag_     (iConfig.getParameter<edm::InputTag> ("EERecHits")),
  HBHERecHitsTag_   (iConfig.getParameter<edm::InputTag> ("HBHERecHits")),
  PackedCandidateCollectionTag_ (iConfig.getParameter<edm::InputTag> ("packedPFCandidates")),
  LostTracksCollectionTag_      (iConfig.getParameter<edm::InputTag> ("lostTracksCollection")),
  IsolatedTracksTag_            (iConfig.getParameter<edm::InputTag> ("isolatedTracksCollection")),
  generalTracksTag_             (iConfig.getParameter<edm::InputTag> ("tracks")),
  gt2pcTag_                     (iConfig.getParameter<edm::InputTag> ("packedPFCandidates")),
  gt2ltTag_                     (iConfig.getParameter<edm::InputTag> ("lostTracksCollection")),
  gt2itTag_                     (iConfig.getParameter<edm::InputTag> ("isolatedTracksCollection")),

  candMinPt_        (iConfig.getParameter<double> ("candMinPt"))
{
  produces<vector<CandidateTrack> > ();

  tracksToken_          =  consumes<vector<reco::Track> >       (tracksTag_);
  electronsToken_       =  consumes<vector<pat::Electron> >     (electronsTag_);
  muonsToken_           =  consumes<vector<pat::Muon> >         (muonsTag_);
  tausToken_            =  consumes<vector<pat::Tau> >          (tausTag_);
  beamspotToken_        =  consumes<reco::BeamSpot>             (beamspotTag_);
  verticesToken_        =  consumes<vector<reco::Vertex> >      (verticesTag_);
  conversionsToken_     =  consumes<vector<reco::Conversion> >  (conversionsTag_);
  rhoToken_             =  consumes<double>                     (rhoTag_);
  rhoCaloToken_         =  consumes<double>                     (rhoCaloTag_);
  rhoCentralCaloToken_  =  consumes<double>                     (rhoCentralCaloTag_);
  EBRecHitsToken_       =  consumes<EBRecHitCollection>         (EBRecHitsTag_);
  EERecHitsToken_       =  consumes<EERecHitCollection>         (EERecHitsTag_);
  HBHERecHitsToken_     =  consumes<HBHERecHitCollection>       (HBHERecHitsTag_);
  PackedCandidateCollectionToken_ = consumes<pat::PackedCandidateCollection> (PackedCandidateCollectionTag_);
  LostTracksCollectionToken_      = consumes<pat::PackedCandidateCollection> (LostTracksCollectionTag_);
  IsolatedTracksToken_            = consumes<vector<pat::IsolatedTrack>> (IsolatedTracksTag_);
  generalTracksToken_             = consumes<reco::TrackCollection> (generalTracksTag_);
  gt2pc_                          = consumes<edm::Association<pat::PackedCandidateCollection> > (gt2pcTag_);
  gt2lt_                          = consumes<edm::Association<pat::PackedCandidateCollection> > (gt2ltTag_);
  gt2it_                          = consumes<edm::Association<vector<pat::IsolatedTrack> > >    (gt2itTag_);

}

CandidateTrackProducer::~CandidateTrackProducer ()
{
}

//
// member functions
//

// ------------ method called to produce the data  ------------
bool
CandidateTrackProducer::filter (edm::Event& iEvent, const edm::EventSetup& iSetup)
{
  edm::Handle<vector<reco::Track> > tracks;
  iEvent.getByToken (tracksToken_, tracks );
  edm::Handle<vector<pat::Electron> > electrons;
  iEvent.getByToken (electronsToken_, electrons );
  edm::Handle<vector<pat::Muon> > muons;
  iEvent.getByToken (muonsToken_, muons );
  edm::Handle<vector<pat::Tau> > taus;
  iEvent.getByToken (tausToken_, taus );
  edm::Handle<reco::BeamSpot> beamspot;
  iEvent.getByToken (beamspotToken_, beamspot );
  edm::Handle<vector<reco::Vertex> > vertices;
  iEvent.getByToken (verticesToken_, vertices );
  edm::Handle<vector<reco::Conversion> > conversions;
  iEvent.getByToken (conversionsToken_, conversions );
  edm::Handle<double> rhoHandle;
  iEvent.getByToken (rhoToken_, rhoHandle );
  edm::Handle<double> rhoCaloHandle;
  iEvent.getByToken (rhoCaloToken_, rhoCaloHandle );
  edm::Handle<double> rhoCentralCaloHandle;
  iEvent.getByToken (rhoCentralCaloToken_, rhoCentralCaloHandle );

  edm::ESHandle<MagneticField> magneticField;
  iSetup.get<IdealMagneticFieldRecord>().get(magneticField);

  iSetup.get<CaloGeometryRecord>().get(caloGeometry_);
  if (!caloGeometry_.isValid())
    throw cms::Exception("FatalError") << "Unable to find CaloGeometryRecord in event!\n";

  edm::Handle<EBRecHitCollection> EBRecHits;
  iEvent.getByToken(EBRecHitsToken_, EBRecHits);
  if (!EBRecHits.isValid()) throw cms::Exception("FatalError") << "Unable to find EBRecHitCollection in the event!\n";
  edm::Handle<EERecHitCollection> EERecHits;
  iEvent.getByToken(EERecHitsToken_, EERecHits);
  if (!EERecHits.isValid()) throw cms::Exception("FatalError") << "Unable to find EERecHitCollection in the event!\n";
  edm::Handle<HBHERecHitCollection> HBHERecHits;
  iEvent.getByToken(HBHERecHitsToken_, HBHERecHits);
  if (!HBHERecHits.isValid()) throw cms::Exception("FatalError") << "Unable to find HBHERecHitCollection in the event!\n";

  edm::Handle<pat::PackedCandidateCollection> PackedCandidates;
  iEvent.getByToken(PackedCandidateCollectionToken_, PackedCandidates);
  if (!PackedCandidates.isValid()) throw cms::Exception("FatalError") << "Unable to find PackedCandidateCollection in the event!\n";

  edm::Handle<pat::PackedCandidateCollection> LostTracks;
  iEvent.getByToken(LostTracksCollectionToken_, LostTracks);
  if (!LostTracks.isValid()) throw cms::Exception("FatalError") << "Unable to find LostTracks in the event!\n";

  edm::Handle<vector<pat::IsolatedTrack> > IsolatedTracks;
  iEvent.getByToken (IsolatedTracksToken_, IsolatedTracks );
  if (!IsolatedTracks.isValid()) throw cms::Exception("FatalError") << "Unable to find IsolatedTracks in the event!\n";
  const vector<pat::IsolatedTrack> *IsolatedTracksVector = IsolatedTracks.product();

  // generalTracks collection
  edm::Handle<reco::TrackCollection> gt_h;
  iEvent.getByToken( generalTracksToken_, gt_h );
  const reco::TrackCollection *generalTracks = gt_h.product();

  // generalTracks-->packedPFCandidate association
  edm::Handle<edm::Association<pat::PackedCandidateCollection> > gt2pc;
  iEvent.getByToken(gt2pc_, gt2pc);

  // generalTracks-->lostTracks association
  edm::Handle<edm::Association<pat::PackedCandidateCollection> > gt2lt;
  iEvent.getByToken(gt2lt_, gt2lt);

  // generalTracks-->isolatedTracks association
  edm::Handle<edm::Association<vector<pat::IsolatedTrack> > >    gt2it;
  iEvent.getByToken(gt2it_, gt2it);



  unique_ptr<vector<CandidateTrack> > candTracks (new vector<CandidateTrack> ());
  for (const auto &track : *tracks) {
    if (track.pt () < candMinPt_)
      continue;

    CandidateTrack candTrack(track, *tracks, *electrons, *muons, *taus, *beamspot, *vertices, conversions, *PackedCandidates, *LostTracks, *IsolatedTracks, *gt_h, *gt2pc, *gt2lt);
    candTrack.set_rhoPUCorr(*rhoHandle);
    candTrack.set_rhoPUCorrCalo(*rhoCaloHandle);
    candTrack.set_rhoPUCorrCentralCalo(*rhoCentralCaloHandle);

    const CaloEnergy &caloE_0p5 = calculateCaloE(candTrack, *EBRecHits, *EERecHits, *HBHERecHits, 0.5);
    candTrack.set_caloNewEMDRp5 (caloE_0p5.eEM);
    candTrack.set_caloNewHadDRp5 (caloE_0p5.eHad);

    const CaloEnergy &caloE_0p3 = calculateCaloE(candTrack, *EBRecHits, *EERecHits, *HBHERecHits, 0.3);
    candTrack.set_caloNewEMDRp3 (caloE_0p3.eEM);
    candTrack.set_caloNewHadDRp3 (caloE_0p3.eHad);

    candTracks->push_back (candTrack);
    if (track.pt() > 55) {
    //cout << "Equivalently printing for every CANDtrack from within CTProducer";
    //cout << "\tCandidate w/ pt=" << track.pt() << ", eta=" << track.eta() << ", phi=" << track.phi() << endl;
    //cout << "----" << generalTracks->size() << " tracks in this event" << endl;
    

    int counterPFcand  = 0;
    int counterLostTrk = 0;
    int counterIsoTrk  = 0;
    int counterProblem = 0;
    double isolationPF            = 0.0;
    double isolationPFLost        = 0.0;
    double isolationPFLostIso     = 0.0;
    double isolationAllGen        = 0.0;
   
    //bool printed = false;
    for(unsigned int igt=0; igt<generalTracks->size(); igt++){
      //cout << ".";

      const reco::Track &gentk = (*gt_h)[igt];
      reco::TrackRef tkref = reco::TrackRef(gt_h, igt);
      pat::PackedCandidateRef pcref              = (*gt2pc)[tkref];
      pat::PackedCandidateRef ltref              = (*gt2lt)[tkref];
      //edm::Ref<vector<pat::IsolatedTrack>> itref = (*gt2it)[tkref];
      const pat::PackedCandidate & pfCand        = *(pcref.get());
      const pat::PackedCandidate & lostTrack     = *(ltref.get());
      //const pat::IsolatedTrack   & isoTrack      = *(itref.get());

      bool isInPackedCands    = (pcref.isNonnull() && pcref.id()==PackedCandidates.id() && pfCand.charge()!=0);
      bool isInLostTracks     = (ltref.isNonnull() && ltref.id()==LostTracks.id());
      bool isInIsolatedTracks = false;//!(gentk.pt() < 5); //if it's less than 5 it for sure is not an isolatedTrack
      bool isNotPFnorLostTracks = !isInPackedCands && !isInLostTracks;

      if (isNotPFnorLostTracks) { //match to isolatedTracks using dR
        int numIsoTrks = 0;//cout << "attempting to match " << IsolatedTracksVector->size() << endl;
	for (unsigned int iit=0; iit<IsolatedTracksVector->size(); iit++){
          const pat::IsolatedTrack &ITit = (*IsolatedTracks)[iit];
          numIsoTrks++;
	  double dR2 = deltaR (gentk.eta(), gentk.phi(), ITit.eta(), ITit.phi());
          if (dR2 < 0.0001) {
            cout << "matching IsolatedTrack found! (pt=" << ITit.pt() << ", genTrack pt=" << gentk.pt() << ")" << endl;
            isInIsolatedTracks = true;
          }
        }
	//if (!printed) cout << "attempted to match to " << numIsoTrks << endl;
	//printed = true;
      }

      //if (isNotPFnorLostTracks && isInIsolatedTracks) cout << "found a generalTrack without a pfCandidate OR a lostTrack (pt=" << gentk.pt() << ")" << endl;
      //if (isNotPFnorLostTracks && !isInIsolatedTracks) cout << "PROBLEM: (pt=" << gentk.pt() << ") not in pfCand or lostTracks or isolatedTracks" << endl;

      //counters
      //if (isInPackedCands)         counterPFcand++;
      //else if (isInLostTracks)     counterLostTrk++;
      //else if (isInIsolatedTracks) counterIsoTrk++;
      //else                         counterProblem++;
 
      double dR0 = deltaR (track, gentk);  //for tracks in the cone
      if(dR0 < 0.3 && dR0 > 0.00001){ //kick out tracks that are very close (don't match self)
     
        //counters
        if (isInPackedCands)         counterPFcand++;
        else if (isInLostTracks)     counterLostTrk++;
        else if (isInIsolatedTracks) counterIsoTrk++;
        else			     counterProblem++;  

        if (isInPackedCands) isolationPF += gentk.pt();
        if (isInPackedCands || isInLostTracks) isolationPFLost += gentk.pt();
        if (isInPackedCands || isInLostTracks || isInIsolatedTracks) isolationPFLostIso += gentk.pt();
        isolationAllGen += gentk.pt();
      }

    }
    //cout << "PFCands:" << counterPFcand << "\tLostTrks:" << counterLostTrk << "\tIsolatedTrks:" << counterIsoTrk << "\tProblems:" << counterProblem << endl;
    //cout << "Isolation using PFCands     =" << isolationPF << endl;
    //cout << "Isolation using PF+Lost     =" << isolationPFLost << endl;
    //cout << "Isolation using PF+Lost+Iso =" << isolationPFLostIso << endl;
    //cout << "Isolation using AllGenTracks=" << isolationAllGen << endl;
    double addedByGenTrk = isolationAllGen - isolationPFLostIso;
    if (addedByGenTrk > 0.01) cout << "Isolation added by GeneralTracks = " << addedByGenTrk << endl;
    //cout << endl;
    }
  }

  // save the vector
  iEvent.put (std::move (candTracks));

  return true;
}

const CaloEnergy
CandidateTrackProducer::calculateCaloE (const CandidateTrack &candTrack, const EBRecHitCollection &EBRecHits, const EERecHitCollection &EERecHits, const HBHERecHitCollection &HBHERecHits, const double dR) const
{
  double eEM = 0;
  for (const auto &hit : EBRecHits) {
    if (insideCone(candTrack, hit.detid(), dR)) {
      eEM += hit.energy();
    }
  }
  for (const auto &hit : EERecHits) {
    if (insideCone(candTrack, hit.detid(), dR)) {
      eEM += hit.energy();
    }
  }

  double eHad = 0;
  for (const auto &hit : HBHERecHits)
    if (insideCone(candTrack, hit.detid(), dR))
      eHad += hit.energy();

  return {eEM, eHad};
}


bool CandidateTrackProducer::insideCone(const CandidateTrack& candTrack, const DetId& id, const double dR) const
{
   const GlobalPoint &idPosition = getPosition(id);
   if (idPosition.mag()<0.01) return false;

   math::XYZVector idPositionRoot( idPosition.x(), idPosition.y(), idPosition.z() );
   return deltaR(candTrack, idPositionRoot) < dR;
}

const GlobalPoint CandidateTrackProducer::getPosition( const DetId& id) const
{
   if ( ! caloGeometry_.isValid() ||
        ! caloGeometry_->getSubdetectorGeometry(id) ||
        ! caloGeometry_->getSubdetectorGeometry(id)->getGeometry(id) ) {
      throw cms::Exception("FatalError") << "Failed to access geometry for DetId: " << id.rawId();
      return GlobalPoint(0,0,0);
   }
   return caloGeometry_->getSubdetectorGeometry(id)->getGeometry(id)->getPosition();
}


//define this as a plug-in
DEFINE_FWK_MODULE (CandidateTrackProducer);
