#ifndef PARTICLE_GUN_VAR_PRODUCER
#define PARTICLE_GUN_VAR_PRODUCER

#include <sstream>
#include <map>
#include <string>

#include "TH1D.h"
#include "TH2D.h"
#include "TVector3.h"
#include "TLorentzVector.h"

#include "DataFormats/Math/interface/deltaPhi.h"
#include "DataFormats/Math/interface/deltaR.h"
#include "DataFormats/HepMCCandidate/interface/GenParticle.h"
#include "FWCore/ServiceRegistry/interface/Service.h"
#include "CommonTools/UtilAlgos/interface/TFileService.h"
#include "FWCore/Framework/interface/MakerMacros.h"

#include "OSUT3Analysis/AnaTools/interface/EventVariableProducer.h"
#include "OSUT3Analysis/AnaTools/interface/DataFormat.h"
#include "OSUT3Analysis/AnaTools/interface/CommonUtils.h"
#include "OSUT3Analysis/Collections/interface/Electron.h"
#include "OSUT3Analysis/Collections/interface/Muon.h"
#include "OSUT3Analysis/Collections/interface/Tau.h"
#include "OSUT3Analysis/Collections/interface/DisappearingTrack.h"
#include "OSUT3Analysis/Collections/interface/GenMatchable.h"

template<class T, class... Args> class IsoTrkAnalyzerProducer : public EventVariableProducer
{
  public:
    IsoTrkAnalyzerProducer (const edm::ParameterSet &);
    ~IsoTrkAnalyzerProducer ();

  private:
    void AddVariables(const edm::Event &);
    edm::EDGetTokenT<vector<T> > tokenProbes_;
    edm::EDGetTokenT<vector<reco::GenParticle> > genParticlesToken_;
    edm::EDGetTokenT<edm::View<PileupSummaryInfo> > pileupInfoToken_;

    const string tagCollectionParameter () const;
    bool genProbeMatched (const osu::Track &probe, const reco::GenParticle &genParticle) const;
    void getEndVertex (const reco::GenParticle &, TVector3 &) const;

    edm::Service<TFileService> fs_;
    map<string, TH1D *> oneDHists_;
    map<string, TH2D *> twoDHists_;
};

typedef IsoTrkAnalyzerProducer<osu::Track, reco::GenParticle> GenMatchedTrackProducer;
#endif
