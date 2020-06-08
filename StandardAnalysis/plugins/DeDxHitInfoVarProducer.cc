#include "DeDxHitInfoVarProducer.h"

DeDxHitInfoVarProducer::DeDxHitInfoVarProducer(const edm::ParameterSet &cfg) : 
EventVariableProducer(cfg)
{
  isoTrk2dedxHitInfoToken_ = consumes<reco::DeDxHitInfoAss>(edm::InputTag("isolatedTracks"));
  tracksToken_ = consumes<vector<osu::Track> >(collections_.getParameter<edm::InputTag>("tracks"));
}

void DeDxHitInfoVarProducer::AddVariables(const edm::Event &event, const edm::EventSetup &setup) {

  edm::Handle<vector<osu::Track> > tracks;
  if(!event.getByToken(tracksToken_, tracks) || !tracks.isValid()) return;

  edm::Handle<reco::DeDxHitInfoAss> isoTrk2dedxHitInfo;
  if(!event.getByToken(isoTrk2dedxHitInfoToken_, isoTrk2dedxHitInfo) || !isoTrk2dedxHitInfo.isValid()) return;

  // indexed [iTrack][iHit]
  vector<vector<float> > charge(tracks->size());
  vector<vector<bool> > isPixelHit(tracks->size());
  vector<vector<int> > pixelSize(tracks->size());
  vector<vector<int> > pixelSizeX(tracks->size());
  vector<vector<int> > pixelSizeY(tracks->size());

  /*
  edm::ESHandle<TrackerTopology> tTopoHandle;
  iSetup.get<TrackerTopologyRcd>().get(tTopoHandle);
  const TrackerTopology& tTopo = *tTopoHandle;
  */

  for(unsigned int itrk = 0; itrk < tracks->size(); itrk++) {
    if((*tracks)[itrk].dRToMatchedIsolatedTrack() < 0) continue; // INVALID_VALUE

    if(isoTrk2dedxHitInfo->contains((*tracks)[itrk].matchedIsolatedTrack().id())) {
      const reco::DeDxHitInfo * hitInfo = (*isoTrk2dedxHitInfo)[(*tracks)[itrk].matchedIsolatedTrack()].get();
      if(hitInfo == nullptr) {
        //edm::LogWarning ("disappTrks_DeDxHitInfoVarProducer") << "Encountered a null DeDxHitInfo object from a pat::IsolatedTrack? Skipping this track...";
        continue;
      }

      for(unsigned int iHit = 0; iHit < hitInfo->size(); iHit++) {
        bool isPixel = (hitInfo->pixelCluster(iHit) != nullptr);
        bool isStrip = (hitInfo->stripCluster(iHit) != nullptr);
	if(!isPixel && !isStrip) continue; // probably shouldn't happen
        if(isPixel && isStrip) continue;

        // shape selection for strips
        if(isStrip && !DeDxTools::shapeSelection(*(hitInfo->stripCluster(iHit)))) continue;
        float norm = isPixel ? 3.61e-06 : 3.61e-06 * 265;

        charge[itrk].push_back(norm * hitInfo->charge(iHit) / hitInfo->pathlength(iHit));
        isPixelHit[itrk].push_back(isPixel);

        pixelSize[itrk].push_back(isPixel ? hitInfo->pixelCluster(iHit)->size()   : -1);
        pixelSizeX[itrk].push_back(isPixel ? hitInfo->pixelCluster(iHit)->sizeX() : -1);
        pixelSizeY[itrk].push_back(isPixel ? hitInfo->pixelCluster(iHit)->sizeY() : -1);
      }
	} // if isoTrk in association map
  } // for tracks

  stringstream suffix;
  for(unsigned int itrk = 0; itrk < charge.size(); itrk++) {
    for(unsigned int iHit = 0; iHit < charge[itrk].size(); iHit++) {
      suffix.str("");
      suffix << "_" << itrk << "_" << iHit;
      (*eventvariables)["hitCharge" + suffix.str()] = charge[itrk][iHit];
      (*eventvariables)["hitIsPixel" + suffix.str()] = isPixelHit[itrk][iHit];

      (*eventvariables)["pixelSize"  + suffix.str()] = pixelSize[itrk][iHit];
      (*eventvariables)["pixelSizeX" + suffix.str()] = pixelSizeX[itrk][iHit];
      (*eventvariables)["pixelSizeY" + suffix.str()] = pixelSizeY[itrk][iHit];
    }
  }

}

#include "FWCore/Framework/interface/MakerMacros.h"
DEFINE_FWK_MODULE(DeDxHitInfoVarProducer);
