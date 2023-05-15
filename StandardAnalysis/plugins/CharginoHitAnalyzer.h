#ifndef CHARGINO_HIT_ANALYZER

#define CHARGINO_HIT_ANALYZER

#include <map>
#include <string>
#include <limits>

#include "TH1D.h"
#include "TH2D.h"

#include "CommonTools/UtilAlgos/interface/TFileService.h"

#include "DataFormats/GsfTrackReco/interface/GsfTrack.h"
#include "DataFormats/TrackReco/interface/Track.h"
#include "DataFormats/HepMCCandidate/interface/GenParticle.h"
#include "DataFormats/Math/interface/deltaR.h"

#include "FWCore/Framework/interface/stream/EDAnalyzer.h"
#include "FWCore/Framework/interface/Event.h"
#include "FWCore/Framework/interface/MakerMacros.h"
#include "FWCore/ParameterSet/interface/ParameterSet.h"
#include "FWCore/ServiceRegistry/interface/Service.h"
#include "FWCore/Utilities/interface/InputTag.h"

using namespace std;

class CharginoHitAnalyzer : public edm::stream::EDAnalyzer<> {
   public:
      explicit CharginoHitAnalyzer (const edm::ParameterSet &);
      ~CharginoHitAnalyzer ();

   private:
      void analyze (const edm::Event &, const edm::EventSetup &);

      edm::InputTag tracks_;
      edm::EDGetTokenT<vector<reco::Track> > tracksToken_;
      edm::InputTag gsfTracks_;
      edm::EDGetTokenT<vector<reco::GsfTrack> > gsfTracksToken_;
      edm::InputTag genParticles_;
      edm::EDGetTokenT<vector<reco::GenParticle> > genParticlesToken_;

      edm::Service<TFileService> fs_;
      map<string, TH1D *> oneDHists_;
      map<string, TH2D *> twoDHists_;

      void logSpace (const unsigned, const double, const double, vector<double> &) const;
      double getCTau (const reco::GenParticle &, double &) const;
      void getFinalPosition (const reco::Candidate &, const int, bool, math::XYZPoint &) const;
      int getExpectedNumberOfHits (const double) const;
      template<class T> const T * const getTrack (const reco::GenParticle &, const vector<T> &, double &) const;
      template<class T> void fillHistograms (const T &, const string &);
      template<class T0, class T1> void fillHistograms (const T0 &, const T1 &, const string &);
};

#endif
