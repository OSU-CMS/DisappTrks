#include "DisappTrks/StandardAnalysis/plugins/SlimmedSiClusterProducer.h"

SlimmedSiClusterProducer::SlimmedSiClusterProducer (const edm::ParameterSet &cfg) :
  siPixelClusters_   (cfg.getParameter<edm::InputTag> ("siPixelClusters")),
  tracks_            (cfg.getParameter<edm::InputTag> ("tracks")),
  minTrackPt_        (cfg.getParameter<double>        ("minTrackPt")),
  requiredNumLayers_ (cfg.getParameter<int>           ("requiredNumLayers")),
  maxDR_             (cfg.getParameter<double>        ("maxDR")),
  geomToken_(esConsumes<TrackerGeometry, TrackerDigiGeometryRecord>())
{
  siPixelClustersToken_ = consumes<edmNew::DetSetVector<SiPixelCluster> > (siPixelClusters_);
  tracksToken_ = consumes<vector<reco::Track> > (tracks_);

  produces<edmNew::DetSetVector<SiPixelCluster> > ("slimmedPixelClusters");
}

SlimmedSiClusterProducer::~SlimmedSiClusterProducer ()
{
}

void
SlimmedSiClusterProducer::produce (edm::Event &event, const edm::EventSetup &setup)
{
  edm::Handle<edmNew::DetSetVector<SiPixelCluster> > siPixelClusters;
  event.getByToken (siPixelClustersToken_, siPixelClusters);

  edm::Handle<vector<reco::Track> > tracks;
  event.getByToken (tracksToken_, tracks);

  slimmedPixelClusters_ = make_unique<edmNew::DetSetVector<SiPixelCluster> > ();

  // edm::ESHandle<TrackerGeometry> theTrackerGeometry;
  // setup.get<TrackerDigiGeometryRecord> ().get (theTrackerGeometry);
  edm::ESHandle<TrackerGeometry> theTrackerGeometry = setup.getHandle(geomToken_);
  const TrackerGeometry &theTracker (*theTrackerGeometry);

  for (edmNew::DetSetVector<SiPixelCluster>::const_iterator detSet = siPixelClusters->begin(); detSet != siPixelClusters->end(); detSet++) {
    
    uint32_t detId = detSet->detId();
    edmNew::DetSetVector<SiPixelCluster>::FastFiller filler (*slimmedPixelClusters_, detId);
    
    for (edmNew::DetSet<SiPixelCluster>::const_iterator cluster = detSet->begin(); cluster != detSet->end(); cluster++) {
      
      DetId theDetUnitId(detId);
      const GeomDet * theDet = theTracker.idToDet(theDetUnitId);

      const Local2DPoint * const localPoint = new Local2DPoint(cluster->x(), cluster->y());
      const GlobalPoint &globalPoint(theDet->surface().toGlobal(*localPoint));
      
      math::XYZVector idPositionRoot(globalPoint.x(), globalPoint.y(), globalPoint.z());

      bool keepThisCluster = false;
      for(const auto &track : *tracks) {
        if(track.pt() < minTrackPt_) continue;
        if(requiredNumLayers_ > 0 && track.hitPattern().trackerLayersWithMeasurement() != requiredNumLayers_) continue;
        if(deltaR(track, idPositionRoot) < maxDR_) {
          keepThisCluster = true;
          break;
        }
      }

      if(keepThisCluster) {
        filler.push_back(SiPixelCluster(*cluster));
      }
    }
  }

  event.put (move (slimmedPixelClusters_), "slimmedPixelClusters");
}

#include "FWCore/Framework/interface/MakerMacros.h"
DEFINE_FWK_MODULE(SlimmedSiClusterProducer);
