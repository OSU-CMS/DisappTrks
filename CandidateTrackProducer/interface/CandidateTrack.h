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

    // New calculation that uses all rec hits in DR<0.5 cone.
    const float caloNewEMDRp5 ()  const { return this->caloNewEMDRp5_; };
    const float caloNewHadDRp5 () const { return this->caloNewHadDRp5_; };
    const float caloNewDRp5 ()    const { return this->caloNewEMDRp5_ + this->caloNewHadDRp5_; };
    const float caloNewEMDRp3 ()  const { return this->caloNewEMDRp3_; };
    const float caloNewHadDRp3 () const { return this->caloNewHadDRp3_; };
    const float caloNewDRp3 ()    const { return this->caloNewEMDRp3_ + this->caloNewHadDRp3_; };

    // New calculation that uses all rec hits in DR<0.5 cone.
    const float caloNewNoPUDRp5 ()            const { return caloTotNoPU(0.5); };
    const float caloNewNoPUDRp5Calo ()        const { return caloTotNoPU(0.5, Calo); };
    const float caloNewNoPUDRp5CentralCalo () const { return caloTotNoPU(0.5, CentralCalo); };
    const float caloNewNoPUDRp3 ()            const { return caloTotNoPU(0.3); };
    const float caloNewNoPUDRp3Calo ()        const { return caloTotNoPU(0.3, Calo); };
    const float caloNewNoPUDRp3CentralCalo () const { return caloTotNoPU(0.3, CentralCalo); };

    const float caloNewNoPUDRp5CentralCaloJustEm () const { return caloTotNoPU(0.5, CentralCalo, EM); };
    const float caloNewNoPUDRp5CentralCaloJustHad () const { return caloTotNoPU(0.5, CentralCalo, Had); };
    const float caloNewNoPUDRp3CentralCaloJustEm () const { return caloTotNoPU(0.3, CentralCalo, EM); };
    const float caloNewNoPUDRp3CentralCaloJustHad () const { return caloTotNoPU(0.3, CentralCalo, Had); };

    void set_caloNewEMDRp5 (double value) { caloNewEMDRp5_  = value; };
    void set_caloNewHadDRp5(double value) { caloNewHadDRp5_ = value; };
    void set_caloNewEMDRp3 (double value) { caloNewEMDRp3_  = value; };
    void set_caloNewHadDRp3(double value) { caloNewHadDRp3_ = value; };
    void set_rhoPUCorr  (double value) { rhoPUCorr_   = value; };
    void set_rhoPUCorrCalo         (double value) { rhoPUCorrCalo_   = value; };
    void set_rhoPUCorrCentralCalo  (double value) { rhoPUCorrCentralCalo_   = value; };

    void set_trackIsoDRp3 (double value) { trackIsoDRp3_ = value; };
    void set_trackIsoDRp5 (double value) { trackIsoDRp5_ = value; };
    void set_trackIsoNoPUDRp3 (double value) { trackIsoNoPUDRp3_ = value; };
    void set_trackIsoNoPUDRp5 (double value) { trackIsoNoPUDRp5_ = value; };
    void set_trackIsoNoFakesDRp3 (double value) { trackIsoNoFakesDRp3_ = value; };
    void set_trackIsoNoFakesDRp5 (double value) { trackIsoNoFakesDRp5_ = value; };
    void set_trackIsoNoPUNoFakesDRp3 (double value) { trackIsoNoPUNoFakesDRp3_ = value; };
    void set_trackIsoNoPUNoFakesDRp5 (double value) { trackIsoNoPUNoFakesDRp5_ = value; };

    void set_trackIsoOldNoPUDRp3 (double value) { trackIsoOldNoPUDRp3_ = value; };
    void set_trackIsoOldNoPUDRp5 (double value) { trackIsoOldNoPUDRp5_ = value; };

    const float rhoPUCorr ()            const { return this->rhoPUCorr_; };
    const float rhoPUCorrCalo ()        const { return this->rhoPUCorrCalo_; };
    const float rhoPUCorrCentralCalo () const { return this->rhoPUCorrCentralCalo_; };

    const float trackIsoDRp3 ()            const { return this->trackIsoDRp3_; };
    const float trackIsoDRp5 ()            const { return this->trackIsoDRp5_; };
    const float trackIsoNoPUDRp3 ()        const { return this->trackIsoNoPUDRp3_; };
    const float trackIsoNoPUDRp5 ()        const { return this->trackIsoNoPUDRp5_; };
    const float trackIsoNoFakesDRp3 ()     const { return this->trackIsoNoFakesDRp3_; };
    const float trackIsoNoFakesDRp5 ()     const { return this->trackIsoNoFakesDRp5_; };
    const float trackIsoNoPUNoFakesDRp3 () const { return this->trackIsoNoPUNoFakesDRp3_; };
    const float trackIsoNoPUNoFakesDRp5 () const { return this->trackIsoNoPUNoFakesDRp5_; };

    const float trackIsoOldNoPUDRp3 () const { return this->trackIsoOldNoPUDRp3_; };
    const float trackIsoOldNoPUDRp5 () const { return this->trackIsoOldNoPUDRp5_; };

    // missing hits differentiated by location on track
    // re-implement these methods from osu::Track to provide a getter function when plotting osu::Track::matchedCandidateTrack()
    const unsigned char missingInnerHits_ ()  const { return this->hitPattern().trackerLayersWithoutMeasurement(reco::HitPattern::MISSING_INNER_HITS); };
    const unsigned char missingMiddleHits_ () const { return this->hitPattern().trackerLayersWithoutMeasurement(reco::HitPattern::TRACK_HITS); };
    const unsigned char missingOuterHits_ ()  const { return this->hitPattern().trackerLayersWithoutMeasurement(reco::HitPattern::MISSING_OUTER_HITS); };

  private:
    float caloEMDRp3_;
    float caloHadDRp3_;
    float caloEMDRp5_;
    float caloHadDRp5_;

    // New calculation that uses all rec hits in DR<0.5 cone.
    float caloNewEMDRp5_;
    float caloNewHadDRp5_;
    float caloNewEMDRp3_;
    float caloNewHadDRp3_;

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

    const double getTrackIsolation (const reco::Track &, const vector<reco::Track> &, const bool, const bool, const double, const double = 1.0e-12) const;
    const double getOldTrackIsolation (const reco::Track &, const vector<reco::Track> &, const bool, const double, const double = 1.0e-12) const;

    const double caloTotNoPU (double, RhoType = All, CaloType = Sum) const;
};


#endif

