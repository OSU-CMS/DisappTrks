#ifndef DisappTrks_StandardAnalysis_SlimmedSiClusterProducer_h
#define DisappTrks_StandardAnalysis_SlimmedSiClusterProducer_h

#include <utility>
#include <memory>
#include <iostream>

#include "FWCore/Framework/interface/stream/EDProducer.h"
#include "FWCore/Framework/interface/Event.h"
#include "FWCore/Framework/interface/EventSetup.h"
#include "FWCore/ParameterSet/interface/ParameterSet.h"
#include "FWCore/Framework/interface/ESHandle.h"

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
#include "DataFormats/TrackReco/interface/Track.h"
#include "DataFormats/Math/interface/deltaR.h"

#include "Geometry/Records/interface/TrackerDigiGeometryRecord.h"

using namespace std;

class SlimmedSiClusterProducer : public edm::stream::EDProducer<>
{
  public:
    SlimmedSiClusterProducer (const edm::ParameterSet &);
    ~SlimmedSiClusterProducer ();

    void produce (edm::Event &, const edm::EventSetup &);

  private:
    edm::InputTag siPixelClusters_;
    edm::InputTag tracks_;
    double minTrackPt_;
    int requiredNumLayers_;
    double maxDR_;

    edm::EDGetTokenT<edmNew::DetSetVector<SiPixelCluster> > siPixelClustersToken_;
    edm::EDGetTokenT<vector<reco::Track> > tracksToken_;
    const edm::ESGetToken<TrackerGeometry, TrackerDigiGeometryRecord> geomToken_;

    unique_ptr<edmNew::DetSetVector<SiPixelCluster> >  slimmedPixelClusters_;
};

#endif
