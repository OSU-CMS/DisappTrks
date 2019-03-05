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


using namespace std;

//
// constructors and destructor
//
CandidateTrackProducer::CandidateTrackProducer (const edm::ParameterSet& iConfig) :
  tracksTag_    (iConfig.getParameter<edm::InputTag> ("tracks")),
  rhoTag_           (iConfig.getParameter<edm::InputTag> ("rhoTag")),
  rhoCaloTag_       (iConfig.getParameter<edm::InputTag> ("rhoCaloTag")),
  rhoCentralCaloTag_(iConfig.getParameter<edm::InputTag> ("rhoCentralCaloTag")),
  EBRecHitsTag_     (iConfig.getParameter<edm::InputTag> ("EBRecHits")),
  EERecHitsTag_     (iConfig.getParameter<edm::InputTag> ("EERecHits")),
  HBHERecHitsTag_   (iConfig.getParameter<edm::InputTag> ("HBHERecHits")),
  gt2dedxPixelTag_  (iConfig.getParameter<edm::InputTag> ("dEdxDataPixel")),
  gt2dedxStripTag_  (iConfig.getParameter<edm::InputTag> ("dEdxDataStrip")),
  candMinPt_        (iConfig.getParameter<double> ("candMinPt"))
{
  produces<vector<CandidateTrack> > ();

  tracksToken_          = consumes<vector<reco::Track> >          (tracksTag_);
  rhoToken_             = consumes<double>                        (rhoTag_);
  rhoCaloToken_         = consumes<double>                        (rhoCaloTag_);
  rhoCentralCaloToken_  = consumes<double>                        (rhoCentralCaloTag_);
  EBRecHitsToken_       = consumes<EBRecHitCollection>            (EBRecHitsTag_);
  EERecHitsToken_       = consumes<EERecHitCollection>            (EERecHitsTag_);
  HBHERecHitsToken_     = consumes<HBHERecHitCollection>          (HBHERecHitsTag_);
  gt2dedxPixelToken_    = consumes<edm::ValueMap<reco::DeDxData> > (gt2dedxPixelTag_);
  gt2dedxStripToken_    = consumes<edm::ValueMap<reco::DeDxData> > (gt2dedxStripTag_);
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

  // associate generalTracks with their DeDx data (estimator for pixel dE/dx)
  edm::Handle<edm::ValueMap<reco::DeDxData> > gt2dedxPixel;
  iEvent.getByToken(gt2dedxPixelToken_, gt2dedxPixel);
  if (!gt2dedxPixel.isValid()) throw cms::Exception("FatalError") << "Unable to find DeDxData ValueMap for pixels in the event!\n";

  // associate generalTracks with their DeDx data (estimator for strip dE/dx)
  edm::Handle<edm::ValueMap<reco::DeDxData> > gt2dedxStrip;
  iEvent.getByToken(gt2dedxStripToken_, gt2dedxStrip);
  if (!gt2dedxStrip.isValid()) throw cms::Exception("FatalError") << "Unable to find DeDxData ValueMap for strips in the event!\n";
  
  unique_ptr<vector<CandidateTrack> > candTracks (new vector<CandidateTrack> ());
  unsigned int iTrack = -1;
  for (const auto &track : *tracks) {
    iTrack++;

    if (track.pt () < candMinPt_) continue;

    CandidateTrack candTrack(track, *tracks);
    candTrack.set_rhoPUCorr(*rhoHandle);
    candTrack.set_rhoPUCorrCalo(*rhoCaloHandle);
    candTrack.set_rhoPUCorrCentralCalo(*rhoCentralCaloHandle);

    const CaloEnergy &caloE_0p5 = calculateCaloE(candTrack, *EBRecHits, *EERecHits, *HBHERecHits, 0.5);
    candTrack.set_caloNewEMDRp5 (caloE_0p5.eEM);
    candTrack.set_caloNewHadDRp5 (caloE_0p5.eHad);

    const CaloEnergy &caloE_0p3 = calculateCaloE(candTrack, *EBRecHits, *EERecHits, *HBHERecHits, 0.3);
    candTrack.set_caloNewEMDRp3 (caloE_0p3.eEM);
    candTrack.set_caloNewHadDRp3 (caloE_0p3.eHad);

    const CaloEnergy &caloE_0p2 = calculateCaloE(candTrack, *EBRecHits, *EERecHits, *HBHERecHits, 0.2);
    candTrack.set_caloNewEMDRp2 (caloE_0p2.eEM);
    candTrack.set_caloNewHadDRp2 (caloE_0p2.eHad);

    const CaloEnergy &caloE_0p1 = calculateCaloE(candTrack, *EBRecHits, *EERecHits, *HBHERecHits, 0.1);
    candTrack.set_caloNewEMDRp1 (caloE_0p1.eEM);
    candTrack.set_caloNewHadDRp1 (caloE_0p1.eHad);

    reco::TrackRef tkref = reco::TrackRef(tracks, iTrack);

    if(gt2dedxPixel->contains(tkref.id())) {
      candTrack.set_dEdx_pixel((*gt2dedxPixel)[tkref].dEdx(), 
                               (*gt2dedxPixel)[tkref].dEdxError(),
                               (*gt2dedxPixel)[tkref].numberOfSaturatedMeasurements(),
                               (*gt2dedxPixel)[tkref].numberOfMeasurements());
    }
    else {
      candTrack.set_dEdx_pixel(-1, -1, 0, 0);
    }

    if(gt2dedxStrip->contains(tkref.id())) {
      candTrack.set_dEdx_strip((*gt2dedxStrip)[tkref].dEdx(), 
                               (*gt2dedxStrip)[tkref].dEdxError(),
                               (*gt2dedxStrip)[tkref].numberOfSaturatedMeasurements(),
                               (*gt2dedxStrip)[tkref].numberOfMeasurements());
    }
    else {
      candTrack.set_dEdx_strip(-1, -1, 0, 0);
    }

    candTracks->push_back (candTrack);
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
