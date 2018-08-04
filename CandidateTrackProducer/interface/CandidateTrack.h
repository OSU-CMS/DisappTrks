#ifndef CANDIDATETRACK_H
#define CANDIDATETRACK_H

#include "DataFormats/TrackReco/interface/Track.h"
#include "DataFormats/VertexReco/interface/Vertex.h"

// FIXME:  Once OSUT3Analysis works with ROOT6, i.e., releases > CMSSW_7_4_5_ROOT5,
// then uncomment the following line:
// #include "OSUT3Analysis/AnaTools/interface/DataFormat.h"
// and remove these two lines:
#define INVALID_VALUE (numeric_limits<int>::min ())
#define IS_INVALID(x) (x <= INVALID_VALUE + 1)

using namespace std;

class CandidateTrack : public reco::Track
{
  public:
    CandidateTrack ();
    CandidateTrack (const reco::Track &);
    CandidateTrack (const reco::Track &, const vector<reco::Track> &);
    ~CandidateTrack ();

    enum RhoType { All, Calo, CentralCalo };
    enum CaloType { Sum, EM, Had };

    //////////////////////////////////////
    // Un-corrected (rho) calo energies
    //////////////////////////////////////

    // New calculation that uses all rec hits in dR < 0.5 cone.
    const float caloNewEMDRp5 ()  const { return this->caloNewEMDRp5_; };
    const float caloNewHadDRp5 () const { return this->caloNewHadDRp5_; };
    const float caloNewDRp5 ()    const { return this->caloNewEMDRp5_ + this->caloNewHadDRp5_; };

    // dR < 0.3
    const float caloNewEMDRp3 ()  const { return this->caloNewEMDRp3_; };
    const float caloNewHadDRp3 () const { return this->caloNewHadDRp3_; };
    const float caloNewDRp3 ()    const { return this->caloNewEMDRp3_ + this->caloNewHadDRp3_; };

    // dR < 0.2
    const float caloNewEMDRp2 ()  const { return this->caloNewEMDRp2_; };
    const float caloNewHadDRp2 () const { return this->caloNewHadDRp2_; };
    const float caloNewDRp2 ()    const { return this->caloNewEMDRp2_ + this->caloNewHadDRp2_; };

    // dR < 0.1
    const float caloNewEMDRp1 ()  const { return this->caloNewEMDRp1_; };
    const float caloNewHadDRp1 () const { return this->caloNewHadDRp1_; };
    const float caloNewDRp1 ()    const { return this->caloNewEMDRp1_ + this->caloNewHadDRp1_; };

    //////////////////////////////////////
    // Rho-corrected calo energies
    //////////////////////////////////////

    // New calculation that uses all rec hits in dR < 0.5 cone.
    const float caloNewNoPUDRp5 ()                   const { return caloTotNoPU(5, All, Sum); };
    const float caloNewNoPUDRp5JustEm ()             const { return caloTotNoPU(5, All, EM); };
    const float caloNewNoPUDRp5JustHad ()            const { return caloTotNoPU(5, All, Had); };
    
    const float caloNewNoPUDRp5Calo ()               const { return caloTotNoPU(5, Calo, Sum); };
    const float caloNewNoPUDRp5CaloJustEm ()         const { return caloTotNoPU(5, Calo, EM); };
    const float caloNewNoPUDRp5CaloJustHad ()        const { return caloTotNoPU(5, Calo, Had); };

    const float caloNewNoPUDRp5CentralCalo ()        const { return caloTotNoPU(5, CentralCalo, Sum); };
    const float caloNewNoPUDRp5CentralCaloJustEm ()  const { return caloTotNoPU(5, CentralCalo, EM); };
    const float caloNewNoPUDRp5CentralCaloJustHad () const { return caloTotNoPU(5, CentralCalo, Had); };

    // dR < 0.3
    const float caloNewNoPUDRp3 ()                   const { return caloTotNoPU(3, All, Sum); };
    const float caloNewNoPUDRp3JustEm ()             const { return caloTotNoPU(3, All, EM); };
    const float caloNewNoPUDRp3JustHad ()            const { return caloTotNoPU(3, All, Had); };
    
    const float caloNewNoPUDRp3Calo ()               const { return caloTotNoPU(3, Calo, Sum); };
    const float caloNewNoPUDRp3CaloJustEm ()         const { return caloTotNoPU(3, Calo, EM); };
    const float caloNewNoPUDRp3CaloJustHad ()        const { return caloTotNoPU(3, Calo, Had); };

    const float caloNewNoPUDRp3CentralCalo ()        const { return caloTotNoPU(3, CentralCalo, Sum); };
    const float caloNewNoPUDRp3CentralCaloJustEm ()  const { return caloTotNoPU(3, CentralCalo, EM); };
    const float caloNewNoPUDRp3CentralCaloJustHad () const { return caloTotNoPU(3, CentralCalo, Had); };

    // dR < 0.2
    const float caloNewNoPUDRp2 ()                   const { return caloTotNoPU(2, All, Sum); };
    const float caloNewNoPUDRp2JustEm ()             const { return caloTotNoPU(2, All, EM); };
    const float caloNewNoPUDRp2JustHad ()            const { return caloTotNoPU(2, All, Had); };
    
    const float caloNewNoPUDRp2Calo ()               const { return caloTotNoPU(2, Calo, Sum); };
    const float caloNewNoPUDRp2CaloJustEm ()         const { return caloTotNoPU(2, Calo, EM); };
    const float caloNewNoPUDRp2CaloJustHad ()        const { return caloTotNoPU(2, Calo, Had); };

    const float caloNewNoPUDRp2CentralCalo ()        const { return caloTotNoPU(2, CentralCalo, Sum); };
    const float caloNewNoPUDRp2CentralCaloJustEm ()  const { return caloTotNoPU(2, CentralCalo, EM); };
    const float caloNewNoPUDRp2CentralCaloJustHad () const { return caloTotNoPU(2, CentralCalo, Had); };

    // dR < 0.1
    const float caloNewNoPUDRp1 ()                   const { return caloTotNoPU(1, All, Sum); };
    const float caloNewNoPUDRp1JustEm ()             const { return caloTotNoPU(1, All, EM); };
    const float caloNewNoPUDRp1JustHad ()            const { return caloTotNoPU(1, All, Had); };
    
    const float caloNewNoPUDRp1Calo ()               const { return caloTotNoPU(1, Calo, Sum); };
    const float caloNewNoPUDRp1CaloJustEm ()         const { return caloTotNoPU(1, Calo, EM); };
    const float caloNewNoPUDRp1CaloJustHad ()        const { return caloTotNoPU(1, Calo, Had); };

    const float caloNewNoPUDRp1CentralCalo ()        const { return caloTotNoPU(1, CentralCalo, Sum); };
    const float caloNewNoPUDRp1CentralCaloJustEm ()  const { return caloTotNoPU(1, CentralCalo, EM); };
    const float caloNewNoPUDRp1CentralCaloJustHad () const { return caloTotNoPU(1, CentralCalo, Had); };

    //////////////////////////////////////
    // Set calo energies
    //////////////////////////////////////

    void set_caloNewEMDRp5 (double value) { caloNewEMDRp5_  = value; };
    void set_caloNewHadDRp5(double value) { caloNewHadDRp5_ = value; };

    void set_caloNewEMDRp3 (double value) { caloNewEMDRp3_  = value; };
    void set_caloNewHadDRp3(double value) { caloNewHadDRp3_ = value; };

    void set_caloNewEMDRp2 (double value) { caloNewEMDRp2_  = value; };
    void set_caloNewHadDRp2(double value) { caloNewHadDRp2_ = value; };

    void set_caloNewEMDRp1 (double value) { caloNewEMDRp1_  = value; };
    void set_caloNewHadDRp1(double value) { caloNewHadDRp1_ = value; };

    //////////////////////////////////////
    // Set rhos
    //////////////////////////////////////

    void set_rhoPUCorr  (double value) { rhoPUCorr_   = value; };
    void set_rhoPUCorrCalo         (double value) { rhoPUCorrCalo_   = value; };
    void set_rhoPUCorrCentralCalo  (double value) { rhoPUCorrCentralCalo_   = value; };

    //////////////////////////////////////
    // Set track isolations
    //////////////////////////////////////

    void set_trackIsoDRp5 (double value) { trackIsoDRp5_ = value; };
    void set_trackIsoDRp3 (double value) { trackIsoDRp3_ = value; };
    void set_trackIsoDRp2 (double value) { trackIsoDRp2_ = value; };
    void set_trackIsoDRp1 (double value) { trackIsoDRp1_ = value; };

    void set_trackIsoNoPUDRp5 (double value) { trackIsoNoPUDRp5_ = value; };
    void set_trackIsoNoPUDRp3 (double value) { trackIsoNoPUDRp3_ = value; };
    void set_trackIsoNoPUDRp2 (double value) { trackIsoNoPUDRp2_ = value; };
    void set_trackIsoNoPUDRp1 (double value) { trackIsoNoPUDRp1_ = value; };

    void set_trackIsoNoFakesDRp5 (double value) { trackIsoNoFakesDRp5_ = value; };
    void set_trackIsoNoFakesDRp3 (double value) { trackIsoNoFakesDRp3_ = value; };
    void set_trackIsoNoFakesDRp2 (double value) { trackIsoNoFakesDRp2_ = value; };
    void set_trackIsoNoFakesDRp1 (double value) { trackIsoNoFakesDRp1_ = value; };

    void set_trackIsoNoPUNoFakesDRp5 (double value) { trackIsoNoPUNoFakesDRp5_ = value; };
    void set_trackIsoNoPUNoFakesDRp3 (double value) { trackIsoNoPUNoFakesDRp3_ = value; };
    void set_trackIsoNoPUNoFakesDRp2 (double value) { trackIsoNoPUNoFakesDRp2_ = value; };
    void set_trackIsoNoPUNoFakesDRp1 (double value) { trackIsoNoPUNoFakesDRp1_ = value; };

    void set_trackIsoOldNoPUDRp5 (double value) { trackIsoOldNoPUDRp5_ = value; };
    void set_trackIsoOldNoPUDRp3 (double value) { trackIsoOldNoPUDRp3_ = value; };
    void set_trackIsoOldNoPUDRp2 (double value) { trackIsoOldNoPUDRp2_ = value; };
    void set_trackIsoOldNoPUDRp1 (double value) { trackIsoOldNoPUDRp1_ = value; };

    //////////////////////////////////////
    // Get rhos
    //////////////////////////////////////

    const float rhoPUCorr ()            const { return this->rhoPUCorr_; };
    const float rhoPUCorrCalo ()        const { return this->rhoPUCorrCalo_; };
    const float rhoPUCorrCentralCalo () const { return this->rhoPUCorrCentralCalo_; };

    //////////////////////////////////////
    // Get track isolations
    //////////////////////////////////////

    const float trackIsoDRp5 ()            const { return this->trackIsoDRp5_; };
    const float trackIsoDRp3 ()            const { return this->trackIsoDRp3_; };
    const float trackIsoDRp2 ()            const { return this->trackIsoDRp2_; };
    const float trackIsoDRp1 ()            const { return this->trackIsoDRp1_; };

    const float trackIsoNoPUDRp5 ()        const { return this->trackIsoNoPUDRp5_; };
    const float trackIsoNoPUDRp3 ()        const { return this->trackIsoNoPUDRp3_; };
    const float trackIsoNoPUDRp2 ()        const { return this->trackIsoNoPUDRp2_; };
    const float trackIsoNoPUDRp1 ()        const { return this->trackIsoNoPUDRp1_; };
    
    const float trackIsoNoFakesDRp5 ()     const { return this->trackIsoNoFakesDRp5_; };
    const float trackIsoNoFakesDRp3 ()     const { return this->trackIsoNoFakesDRp3_; };
    const float trackIsoNoFakesDRp2 ()     const { return this->trackIsoNoFakesDRp2_; };
    const float trackIsoNoFakesDRp1 ()     const { return this->trackIsoNoFakesDRp1_; };
    
    const float trackIsoNoPUNoFakesDRp5 () const { return this->trackIsoNoPUNoFakesDRp5_; };
    const float trackIsoNoPUNoFakesDRp3 () const { return this->trackIsoNoPUNoFakesDRp3_; };
    const float trackIsoNoPUNoFakesDRp2 () const { return this->trackIsoNoPUNoFakesDRp2_; };
    const float trackIsoNoPUNoFakesDRp1 () const { return this->trackIsoNoPUNoFakesDRp1_; };

    const float trackIsoOldNoPUDRp5 () const { return this->trackIsoOldNoPUDRp5_; };
    const float trackIsoOldNoPUDRp3 () const { return this->trackIsoOldNoPUDRp3_; };
    const float trackIsoOldNoPUDRp2 () const { return this->trackIsoOldNoPUDRp2_; };
    const float trackIsoOldNoPUDRp1 () const { return this->trackIsoOldNoPUDRp1_; };

    // missing hits differentiated by location on track
    // re-implement these methods from osu::Track to provide a getter function when plotting osu::Track::matchedCandidateTrack()
    const unsigned char missingInnerHits_ ()  const { return this->hitPattern().trackerLayersWithoutMeasurement(reco::HitPattern::MISSING_INNER_HITS); };
    const unsigned char missingMiddleHits_ () const { return this->hitPattern().trackerLayersWithoutMeasurement(reco::HitPattern::TRACK_HITS); };
    const unsigned char missingOuterHits_ ()  const { return this->hitPattern().trackerLayersWithoutMeasurement(reco::HitPattern::MISSING_OUTER_HITS); };

  private:
    // New calculation that uses all rec hits in DR<0.5 cone.
    float caloNewEMDRp5_;
    float caloNewHadDRp5_;

    float caloNewEMDRp3_;
    float caloNewHadDRp3_;

    float caloNewEMDRp2_;
    float caloNewHadDRp2_;

    float caloNewEMDRp1_;
    float caloNewHadDRp1_;

    float rhoPUCorr_;
    float rhoPUCorrCalo_;
    float rhoPUCorrCentralCalo_;

    float trackIsoDRp5_;
    float trackIsoDRp3_;
    float trackIsoDRp2_;
    float trackIsoDRp1_;

    float trackIsoNoPUDRp5_;
    float trackIsoNoPUDRp3_;
    float trackIsoNoPUDRp2_;
    float trackIsoNoPUDRp1_;

    float trackIsoNoFakesDRp5_;
    float trackIsoNoFakesDRp3_;
    float trackIsoNoFakesDRp2_;
    float trackIsoNoFakesDRp1_;

    float trackIsoNoPUNoFakesDRp5_;
    float trackIsoNoPUNoFakesDRp3_;
    float trackIsoNoPUNoFakesDRp2_;
    float trackIsoNoPUNoFakesDRp1_;

    float trackIsoOldNoPUDRp5_;
    float trackIsoOldNoPUDRp3_;
    float trackIsoOldNoPUDRp2_;
    float trackIsoOldNoPUDRp1_;

    const double getTrackIsolation (const reco::Track &, const vector<reco::Track> &, const bool, const bool, const double, const double = 1.0e-12) const;
    const double getOldTrackIsolation (const reco::Track &, const vector<reco::Track> &, const bool, const double, const double = 1.0e-12) const;

    const double caloTotNoPU (int, RhoType = All, CaloType = Sum) const;
};


#endif

