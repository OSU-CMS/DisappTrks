#include "DisappTrks/StandardAnalysis/interface/SiGlobalPixelCluster.h"

template void edmNew::DetSet<SiGlobalPixelCluster>::set(edmNew::DetSetVector<SiGlobalPixelCluster> const&, edmNew::dstvdetails::DetSetVectorTrans::Item const&, bool);
template SiGlobalPixelCluster const * edmNew::DetSet<SiGlobalPixelCluster>::data() const;
template void edmNew::DetSetVector<SiGlobalPixelCluster>::update(edmNew::dstvdetails::DetSetVectorTrans::Item const&) const;
