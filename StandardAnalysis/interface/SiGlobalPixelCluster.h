#ifndef DisappTrks_StandardAnalysis_SiGlobalPixelCluster_h
#define DisappTrks_StandardAnalysis_SiGlobalPixelCluster_h

#include "DataFormats/SiPixelCluster/interface/SiPixelCluster.h"
#include "Geometry/TrackerGeometryBuilder/interface/TrackerGeometry.h"
#include "DataFormats/DetId/interface/DetId.h"
#include "Geometry/CommonDetUnit/interface/GeomDet.h"
#include "DataFormats/GeometryVector/interface/LocalPoint.h"
#include "DataFormats/GeometryVector/interface/GlobalPoint.h"
#include "DataFormats/Common/interface/DetSetVector.h"
#include "DataFormats/Common/interface/DetSetVectorNew.h"
#include "DataFormats/Common/interface/Ref.h"
#include "DataFormats/Common/interface/DetSetRefVector.h"

using namespace std;

class SiGlobalPixelCluster : public SiPixelCluster
{
  private:
    double globalX_;
    double globalY_;
    double globalZ_;

  public:

    SiGlobalPixelCluster () :
      globalX_ (0.0),
      globalY_ (0.0),
      globalZ_ (0.0)
    {
    }

    SiGlobalPixelCluster (const SiPixelCluster &cluster, const uint32_t detId, const TrackerGeometry &theTracker) :
      SiPixelCluster (cluster)
    {
      DetId theDetUnitId (detId);
      const GeomDet *theDet = theTracker.idToDet (theDetUnitId);

      const Local2DPoint * const localPoint = new Local2DPoint (cluster.x (), cluster.y ());
      const GlobalPoint &globalPoint (theDet->surface ().toGlobal (*localPoint));
      globalX_ = globalPoint.x ();
      globalY_ = globalPoint.y ();
      globalZ_ = globalPoint.z ();
    }

    double globalX () const { return globalX_; };
    double globalY () const { return globalY_; };
    double globalZ () const { return globalZ_; };
};

typedef edm::DetSetVector<SiGlobalPixelCluster> SiGlobalPixelClusterCollection;
typedef edm::Ref<SiGlobalPixelClusterCollection, SiGlobalPixelCluster> SiGlobalPixelClusterRef;
typedef edm::DetSetRefVector<SiGlobalPixelCluster> SiGlobalPixelClusterRefVector;
typedef edm::RefProd<SiGlobalPixelClusterCollection> SiGlobalPixelClusterRefProd;

typedef edmNew::DetSetVector<SiGlobalPixelCluster> SiGlobalPixelClusterCollectionNew;
typedef edm::Ref<SiGlobalPixelClusterCollectionNew, SiGlobalPixelCluster> SiGlobalPixelClusterRefNew;

#endif
