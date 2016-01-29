#ifndef CANDIDATETRACK_H
#define CANDIDATETRACK_H

#include "DataFormats/BeamSpot/interface/BeamSpot.h"

#include "DataFormats/EgammaCandidates/interface/Conversion.h"

#include "DataFormats/PatCandidates/interface/Electron.h"
#include "DataFormats/PatCandidates/interface/Muon.h"
#include "DataFormats/PatCandidates/interface/Tau.h"

#include "DataFormats/TrackReco/interface/Track.h"

#include "DataFormats/VertexReco/interface/Vertex.h"

using namespace std;

class CandidateTrack : public reco::Track
{
  public:
    CandidateTrack ();
    CandidateTrack (const reco::Track &);
    CandidateTrack (const reco::Track &, const vector<reco::Track> &, const vector<pat::Electron> &, const vector<pat::Muon> &, const vector<pat::Tau> &, const reco::BeamSpot &, const vector<reco::Vertex> &, const edm::Handle<vector<reco::Conversion> > &);
    ~CandidateTrack ();

    
    enum RhoType { All, Calo, CentralCalo };

    const double caloEMDRp3 () const;
    const double caloHadDRp3 () const;
    const double caloTotDRp3 () const;
    const double caloEMDRp5 () const;
    const double caloHadDRp5 () const;
    const double caloTotDRp5 () const;
    const double caloTotNoPU (double dR = 0.5, RhoType rhoType = All) const;
    const double caloTotNoPUDRp3 () const;
    const double caloTotNoPUDRp4 () const;
    const double caloTotNoPUDRp5 () const;
    const double caloTotNoPUDRp5Calo () const;
    const double caloTotNoPUDRp5CentralCalo () const;

    void set_caloEMDRp3 (double value) { caloEMDRp3_  = value; }
    void set_caloHadDRp3(double value) { caloHadDRp3_ = value; }
    void set_caloEMDRp5 (double value) { caloEMDRp5_  = value; }
    void set_caloHadDRp5(double value) { caloHadDRp5_ = value; }
    void set_rhoPUCorr  (double value) { rhoPUCorr_   = value; }
    void set_rhoPUCorrCalo         (double value) { rhoPUCorrCalo_   = value; }
    void set_rhoPUCorrCentralCalo  (double value) { rhoPUCorrCentralCalo_   = value; }

    const double deltaRToClosestElectron () const;
    const double deltaRToClosestVetoElectron () const;
    const double deltaRToClosestLooseElectron () const;
    const double deltaRToClosestMediumElectron () const;
    const double deltaRToClosestTightElectron () const;
    const double deltaRToClosestMuon () const;
    const double deltaRToClosestLooseMuon () const;
    const double deltaRToClosestMediumMuon () const;
    const double deltaRToClosestTightMuon () const;
    const double deltaRToClosestTau () const;
    const double deltaRToClosestTauHad () const;

    const int missingInnerHits () const;
    const int missingMiddleHits () const;
    const int missingOuterHits () const;

    const double rhoPUCorr () const;
    const double rhoPUCorrCalo () const;
    const double rhoPUCorrCentralCalo () const;

    const double trackIsoDRp3 () const;
    const double trackIsoDRp5 () const;
    const double trackIsoNoPUDRp3 () const;
    const double trackIsoNoPUDRp5 () const;

    const double energyOfElectron () const;
    const double energyOfMuon () const;
    const double energyOfTau () const;
    const double energyOfPion () const;
    const double energyOfProton () const;

  private:
    double caloEMDRp3_;
    double caloHadDRp3_;
    double caloEMDRp5_;
    double caloHadDRp5_;

    double deltaRToClosestElectron_;
    double deltaRToClosestVetoElectron_;
    double deltaRToClosestLooseElectron_;
    double deltaRToClosestMediumElectron_;
    double deltaRToClosestTightElectron_;
    double deltaRToClosestMuon_;
    double deltaRToClosestLooseMuon_;
    double deltaRToClosestMediumMuon_;
    double deltaRToClosestTightMuon_;
    double deltaRToClosestTau_;
    double deltaRToClosestTauHad_;

    double rhoPUCorr_;
    double rhoPUCorrCalo_;
    double rhoPUCorrCentralCalo_;

    double trackIsoDRp3_;
    double trackIsoDRp5_;
    double trackIsoNoPUDRp3_;
    double trackIsoNoPUDRp5_;

    static const int MAX_DR = 99;

    template<class T> const double getMinDeltaR (const vector<T> &) const;
    const double getMinDeltaRToTauHad (const vector<pat::Tau> &) const;
    const double getMinDeltaRToVetoElectron (const vector<pat::Electron> &, const reco::BeamSpot &, const reco::Vertex &, const edm::Handle<vector<reco::Conversion> > &) const;
    const double getMinDeltaRToLooseElectron (const vector<pat::Electron> &, const reco::BeamSpot &, const reco::Vertex &, const edm::Handle<vector<reco::Conversion> > &) const;
    const double getMinDeltaRToMediumElectron (const vector<pat::Electron> &, const reco::BeamSpot &, const reco::Vertex &, const edm::Handle<vector<reco::Conversion> > &) const;
    const double getMinDeltaRToTightElectron (const vector<pat::Electron> &, const reco::BeamSpot &, const reco::Vertex &, const edm::Handle<vector<reco::Conversion> > &) const;
    const double getMinDeltaRToLooseMuon (const vector<pat::Muon> &) const;
    const double getMinDeltaRToMediumMuon (const vector<pat::Muon> &) const;
    const double getMinDeltaRToTightMuon (const vector<pat::Muon> &, const reco::Vertex &) const;
    const double getTrackIsolation (const reco::Track &, const vector<reco::Track> &, const bool, const double, const double = 1.0e-12) const;

    const double energyGivenMass (const double) const;

    bool passesVetoID (const pat::Electron &, const reco::BeamSpot &, const reco::Vertex &, const edm::Handle<vector<reco::Conversion> > &) const;
    bool passesLooseID (const pat::Electron &, const reco::BeamSpot &, const reco::Vertex &, const edm::Handle<vector<reco::Conversion> > &) const;
    bool passesMediumID (const pat::Electron &, const reco::BeamSpot &, const reco::Vertex &, const edm::Handle<vector<reco::Conversion> > &) const;
    bool passesTightID (const pat::Electron &, const reco::BeamSpot &, const reco::Vertex &, const edm::Handle<vector<reco::Conversion> > &) const;
};


#endif

