#ifndef CANDIDATETRACK_H
#define CANDIDATETRACK_H

#include "DataFormats/BeamSpot/interface/BeamSpot.h"

#include "DataFormats/EgammaCandidates/interface/Conversion.h"

#include "DataFormats/PatCandidates/interface/Electron.h"
#include "DataFormats/PatCandidates/interface/Muon.h"
#include "DataFormats/PatCandidates/interface/Tau.h"

#include "DataFormats/TrackReco/interface/Track.h"

#include "DataFormats/VertexReco/interface/Vertex.h"

#define MAX_DR (99.0)

using namespace std;

class CandidateTrack : public reco::Track
{
  public:
    CandidateTrack ();
    CandidateTrack (const reco::Track &);
    CandidateTrack (const reco::Track &, const vector<reco::Track> &, const vector<pat::Electron> &, const vector<pat::Muon> &, const vector<pat::Tau> &, const reco::BeamSpot &, const vector<reco::Vertex> &, const edm::Handle<vector<reco::Conversion> > &);
    ~CandidateTrack ();


    enum RhoType { All, Calo, CentralCalo };

    const float caloNewEMDRp5 () const;   // New calculation that uses all rec hits in DR<0.5 cone.
    const float caloNewHadDRp5 () const;  // New calculation that uses all rec hits in DR<0.5 cone.
    const float caloNewDRp5 () const;     // New calculation that uses all rec hits in DR<0.5 cone.
    const float caloNewEMDRp3 () const;   // New calculation that uses all rec hits in DR<0.3 cone.
    const float caloNewHadDRp3 () const;  // New calculation that uses all rec hits in DR<0.3 cone.
    const float caloNewDRp3 () const;     // New calculation that uses all rec hits in DR<0.3 cone.

    const float caloNewNoPUDRp5 () const; // New calculation that uses all rec hits in DR<0.5 cone.
    const float caloNewNoPUDRp5Calo () const; // New calculation that uses all rec hits in DR<0.5 cone.
    const float caloNewNoPUDRp5CentralCalo () const; // New calculation that uses all rec hits in DR<0.5 cone.
    const float caloNewNoPUDRp3 () const; // New calculation that uses all rec hits in DR<0.3 cone.
    const float caloNewNoPUDRp3Calo () const; // New calculation that uses all rec hits in DR<0.3 cone.
    const float caloNewNoPUDRp3CentralCalo () const; // New calculation that uses all rec hits in DR<0.3 cone.

    void set_caloNewEMDRp5 (double value) { caloNewEMDRp5_  = value; }
    void set_caloNewHadDRp5(double value) { caloNewHadDRp5_ = value; }
    void set_caloNewEMDRp3 (double value) { caloNewEMDRp3_  = value; }
    void set_caloNewHadDRp3(double value) { caloNewHadDRp3_ = value; }
    void set_rhoPUCorr  (double value) { rhoPUCorr_   = value; }
    void set_rhoPUCorrCalo         (double value) { rhoPUCorrCalo_   = value; }
    void set_rhoPUCorrCentralCalo  (double value) { rhoPUCorrCentralCalo_   = value; }

    void set_trackIsoDRp3 (double value) { trackIsoDRp3_ = value; }
    void set_trackIsoDRp5 (double value) { trackIsoDRp5_ = value; }
    void set_trackIsoNoPUDRp3 (double value) { trackIsoNoPUDRp3_ = value; }
    void set_trackIsoNoPUDRp5 (double value) { trackIsoNoPUDRp5_ = value; }
    void set_trackIsoNoFakesDRp3 (double value) { trackIsoNoFakesDRp3_ = value; }
    void set_trackIsoNoFakesDRp5 (double value) { trackIsoNoFakesDRp5_ = value; }
    void set_trackIsoNoPUNoFakesDRp3 (double value) { trackIsoNoPUNoFakesDRp3_ = value; }
    void set_trackIsoNoPUNoFakesDRp5 (double value) { trackIsoNoPUNoFakesDRp5_ = value; }

    void set_trackIsoOldNoPUDRp3 (double value) { trackIsoOldNoPUDRp3_ = value; }
    void set_trackIsoOldNoPUDRp5 (double value) { trackIsoOldNoPUDRp5_ = value; }

    const float deltaRToClosestElectron () const;
    const float deltaRToClosestVetoElectron () const;
    const float deltaRToClosestLooseElectron () const;
    const float deltaRToClosestMediumElectron () const;
    const float deltaRToClosestTightElectron () const;
    const float deltaRToClosestMuon () const;
    const float deltaRToClosestLooseMuon () const;
    const float deltaRToClosestMediumMuon () const;
    const float deltaRToClosestTightMuon () const;
    const float deltaRToClosestTau () const;
    const float deltaRToClosestTauHad () const;

    // number of hits differentiated by location in detector
    const unsigned char numberOfTrackerHits () const;
    const unsigned char numberOfPixelHits () const;
    const unsigned char numberOfStripHits () const;
    const unsigned char numberOfPixelBarrelHits () const;
    const unsigned char numberOfPixelEndcapHits () const;
    const unsigned char numberOfStripTIBHits () const;
    const unsigned char numberOfStripTIDHits () const;
    const unsigned char numberOfStripTOBHits () const;
    const unsigned char numberOfStripTECHits () const;

    // missing hits differentiated by location on track
    const unsigned char missingInnerHits () const;
    const unsigned char missingMiddleHits () const;
    const unsigned char missingOuterHits () const;

    // missing hits differentiated by location in detector
    const unsigned char missingTrackerHits () const;
    const unsigned char missingPixelHits () const;
    const unsigned char missingStripHits () const;
    const unsigned char missingPixelBarrelHits () const;
    const unsigned char missingPixelEndcapHits () const;
    const unsigned char missingStripTIBHits () const;
    const unsigned char missingStripTIDHits () const;
    const unsigned char missingStripTOBHits () const;
    const unsigned char missingStripTECHits () const;

    // expected hits differentiated by location in detector
    const unsigned char expectedTrackerHits () const;
    const unsigned char expectedPixelHits () const;
    const unsigned char expectedStripHits () const;
    const unsigned char expectedPixelBarrelHits () const;
    const unsigned char expectedPixelEndcapHits () const;
    const unsigned char expectedStripTIBHits () const;
    const unsigned char expectedStripTIDHits () const;
    const unsigned char expectedStripTOBHits () const;
    const unsigned char expectedStripTECHits () const;

    const float rhoPUCorr () const;
    const float rhoPUCorrCalo () const;
    const float rhoPUCorrCentralCalo () const;

    const float trackIsoDRp3 () const;
    const float trackIsoDRp5 () const;
    const float trackIsoNoPUDRp3 () const;
    const float trackIsoNoPUDRp5 () const;
    const float trackIsoNoFakesDRp3 () const;
    const float trackIsoNoFakesDRp5 () const;
    const float trackIsoNoPUNoFakesDRp3 () const;
    const float trackIsoNoPUNoFakesDRp5 () const;

    const float trackIsoOldNoPUDRp3 () const;
    const float trackIsoOldNoPUDRp5 () const;

    const float energyOfElectron () const;
    const float energyOfMuon () const;
    const float energyOfTau () const;
    const float energyOfPion () const;
    const float energyOfProton () const;

  private:
    float caloEMDRp3_;
    float caloHadDRp3_;
    float caloEMDRp5_;
    float caloHadDRp5_;
    float caloNewEMDRp5_;   // New calculation that uses all rec hits in DR<0.5 cone.
    float caloNewHadDRp5_;  // New calculation that uses all rec hits in DR<0.5 cone.
    float caloNewEMDRp3_;   // New calculation that uses all rec hits in DR<0.3 cone.
    float caloNewHadDRp3_;  // New calculation that uses all rec hits in DR<0.3 cone.

    float deltaRToClosestElectron_;
    float deltaRToClosestVetoElectron_;
    float deltaRToClosestLooseElectron_;
    float deltaRToClosestMediumElectron_;
    float deltaRToClosestTightElectron_;
    float deltaRToClosestMuon_;
    float deltaRToClosestLooseMuon_;
    float deltaRToClosestMediumMuon_;
    float deltaRToClosestTightMuon_;
    float deltaRToClosestTau_;
    float deltaRToClosestTauHad_;

    float rhoPUCorr_;
    float rhoPUCorrCalo_;
    float rhoPUCorrCentralCalo_;

    float trackIsoDRp3_;
    float trackIsoDRp5_;
    float trackIsoNoPUDRp3_;
    float trackIsoNoPUDRp5_;
    float trackIsoNoFakesDRp3_;
    float trackIsoNoFakesDRp5_;
    float trackIsoNoPUNoFakesDRp3_;
    float trackIsoNoPUNoFakesDRp5_;

    float trackIsoOldNoPUDRp3_;
    float trackIsoOldNoPUDRp5_;

    template<class T> const double getMinDeltaR (const vector<T> &) const;
    const double getMinDeltaRToTauHad (const vector<pat::Tau> &) const;
    const double getMinDeltaRToVetoElectron (const vector<pat::Electron> &, const reco::BeamSpot &, const reco::Vertex &, const edm::Handle<vector<reco::Conversion> > &) const;
    const double getMinDeltaRToLooseElectron (const vector<pat::Electron> &, const reco::BeamSpot &, const reco::Vertex &, const edm::Handle<vector<reco::Conversion> > &) const;
    const double getMinDeltaRToMediumElectron (const vector<pat::Electron> &, const reco::BeamSpot &, const reco::Vertex &, const edm::Handle<vector<reco::Conversion> > &) const;
    const double getMinDeltaRToTightElectron (const vector<pat::Electron> &, const reco::BeamSpot &, const reco::Vertex &, const edm::Handle<vector<reco::Conversion> > &) const;
    const double getMinDeltaRToLooseMuon (const vector<pat::Muon> &) const;
    const double getMinDeltaRToMediumMuon (const vector<pat::Muon> &) const;
    const double getMinDeltaRToTightMuon (const vector<pat::Muon> &, const reco::Vertex &) const;
    const double getTrackIsolation (const reco::Track &, const vector<reco::Track> &, const bool, const bool, const double, const double = 1.0e-12) const;
    const double getOldTrackIsolation (const reco::Track &, const vector<reco::Track> &, const bool, const double, const double = 1.0e-12) const;

    const double caloTotNoPU (double, RhoType = All) const;

    const double energyGivenMass (const double) const;

    bool passesVetoID (const pat::Electron &, const reco::BeamSpot &, const reco::Vertex &, const edm::Handle<vector<reco::Conversion> > &) const;
    bool passesLooseID (const pat::Electron &, const reco::BeamSpot &, const reco::Vertex &, const edm::Handle<vector<reco::Conversion> > &) const;
    bool passesMediumID (const pat::Electron &, const reco::BeamSpot &, const reco::Vertex &, const edm::Handle<vector<reco::Conversion> > &) const;
    bool passesTightID (const pat::Electron &, const reco::BeamSpot &, const reco::Vertex &, const edm::Handle<vector<reco::Conversion> > &) const;
};


#endif

