#ifndef DisappTrks_StandardAnalysis_classes_h
#define DisappTrks_StandardAnalysis_classes_h
#include "DisappTrks/StandardAnalysis/interface/SiGlobalPixelCluster.h"
#include "DataFormats/Common/interface/RefProd.h"
#include "DataFormats/Common/interface/Wrapper.h"
#include "DataFormats/Common/interface/ContainerMask.h"

namespace DisappTrks_StandardAnalysis {
  struct dictionary {
    std::vector<SiGlobalPixelCluster> v1;
    edm::DetSet<SiGlobalPixelCluster> ds1;
    std::vector<edm::DetSet<SiGlobalPixelCluster> > vds1;
    SiGlobalPixelClusterCollection c1;
    SiGlobalPixelClusterCollectionNew c1_new;
    edm::Wrapper<SiGlobalPixelClusterCollection> w1;
    edm::Wrapper<SiGlobalPixelClusterCollectionNew> w1_new;
    SiGlobalPixelClusterRef r1;
    SiGlobalPixelClusterRefNew r1_new;
    SiGlobalPixelClusterRefVector rv1;
    SiGlobalPixelClusterRefProd rp1;
    edm::Ref<edm::DetSetVector<SiGlobalPixelCluster>,edm::DetSet<SiGlobalPixelCluster>,edm::refhelper::FindDetSetForDetSetVector<SiGlobalPixelCluster,edm::DetSetVector<SiGlobalPixelCluster> > > boguscrap;

    std::vector<edm::Ref<edmNew::DetSetVector<SiGlobalPixelCluster>,SiGlobalPixelCluster,edmNew::DetSetVector<SiGlobalPixelCluster>::FindForDetSetVector> > dsvr_v;
    edmNew::DetSetVector<edm::Ref<edmNew::DetSetVector<SiGlobalPixelCluster>,SiGlobalPixelCluster,edmNew::DetSetVector<SiGlobalPixelCluster>::FindForDetSetVector> > dsvr;
    edm::Wrapper<edmNew::DetSetVector<edm::Ref<edmNew::DetSetVector<SiGlobalPixelCluster>,SiGlobalPixelCluster,edmNew::DetSetVector<SiGlobalPixelCluster>::FindForDetSetVector> > > dsvr_w;

    edm::ContainerMask<SiGlobalPixelClusterCollectionNew> cm1;
    edm::Wrapper<edm::ContainerMask<SiGlobalPixelClusterCollectionNew> > w_cm1;
  };
}

#endif
