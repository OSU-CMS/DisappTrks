#include "DisappTrks/StandardAnalysis/plugins/SiGlobalClusterProducer.h"

SiGlobalClusterProducer::SiGlobalClusterProducer (const edm::ParameterSet &cfg) :
  siPixelClusters_ (cfg.getParameter<edm::InputTag> ("siPixelClusters")),
  geomToken_(esConsumes<TrackerGeometry, TrackerDigiGeometryRecord>())
{
  siPixelClustersToken_ = consumes<edmNew::DetSetVector<SiPixelCluster> > (siPixelClusters_);
  produces<edmNew::DetSetVector<SiGlobalPixelCluster> > ("globalPixelClusters");
}

SiGlobalClusterProducer::~SiGlobalClusterProducer ()
{
}

void
SiGlobalClusterProducer::produce (edm::Event &event, const edm::EventSetup &setup)
{
  edm::Handle<edmNew::DetSetVector<SiPixelCluster> > siPixelClusters;
  event.getByToken (siPixelClustersToken_, siPixelClusters);

  globalPixelClusters_ = make_unique<edmNew::DetSetVector<SiGlobalPixelCluster> > ();

  // edm::ESHandle<TrackerGeometry> theTrackerGeometry;
  // setup.get<TrackerDigiGeometryRecord> ().get (theTrackerGeometry);
  edm::ESHandle<TrackerGeometry> theTrackerGeometry = setup.getHandle(geomToken_);
  const TrackerGeometry &theTracker (*theTrackerGeometry);

  for (edmNew::DetSetVector<SiPixelCluster>::const_iterator detSet = siPixelClusters->begin (); detSet != siPixelClusters->end (); detSet++)
    {
      uint32_t detId = detSet->detId ();
      edmNew::DetSetVector<SiGlobalPixelCluster>::FastFiller filler (*globalPixelClusters_, detId);
      for (edmNew::DetSet<SiPixelCluster>::const_iterator cluster = detSet->begin (); cluster != detSet->end (); cluster++)
        filler.push_back (SiGlobalPixelCluster (*cluster, detId, theTracker));
    }

  event.put (move (globalPixelClusters_), "globalPixelClusters");
}

#include "FWCore/Framework/interface/MakerMacros.h"
DEFINE_FWK_MODULE(SiGlobalClusterProducer);
