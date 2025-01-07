#ifndef DisappTrks_StandardAnalysis_SiGlobalClusterProducer_h
#define DisappTrks_StandardAnalysis_SiGlobalClusterProducer_h

#include <utility>
#include <memory>
#include <iostream>

#include "FWCore/Framework/interface/stream/EDProducer.h"
#include "FWCore/Framework/interface/Event.h"
#include "FWCore/Framework/interface/EventSetup.h"
#include "FWCore/ParameterSet/interface/ParameterSet.h"
#include "FWCore/Framework/interface/ESHandle.h"

#include "Geometry/Records/interface/TrackerDigiGeometryRecord.h"

#include "DisappTrks/StandardAnalysis/interface/SiGlobalPixelCluster.h"

using namespace std;

class SiGlobalClusterProducer : public edm::stream::EDProducer<>
{
  public:
    SiGlobalClusterProducer (const edm::ParameterSet &);
    ~SiGlobalClusterProducer ();

    void produce (edm::Event &, const edm::EventSetup &);

  private:
    edm::InputTag siPixelClusters_;
    edm::EDGetTokenT<edmNew::DetSetVector<SiPixelCluster> > siPixelClustersToken_;
    const edm::ESGetToken<TrackerGeometry, TrackerDigiGeometryRecord> geomToken_;
    unique_ptr<edmNew::DetSetVector<SiGlobalPixelCluster> >  globalPixelClusters_;
};

#endif
