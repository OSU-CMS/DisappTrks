#include "DataFormats/TrackReco/interface/Track.h"

using namespace std;

class CandidateTrack : public reco::Track
{
   public:
      CandidateTrack ();
      CandidateTrack (const reco::Track &);
      ~CandidateTrack ();

      const int missingInnerHits () const;
      const int missingMiddleHits () const;
      const int missingOuterHits () const;

      const double caloEMDeltaRp3 () const; 
      const double caloHadDeltaRp3 () const; 
      const double caloTotDeltaRp3 () const; 
      const double caloEMDeltaRp5 () const; 
      const double caloHadDeltaRp5 () const; 
      const double caloTotDeltaRp5 () const; 

      void set_caloEMDeltaRp3 (double value) { caloEMDeltaRp3_  = value; }  
      void set_caloHadDeltaRp3(double value) { caloHadDeltaRp3_ = value; }  
      void set_caloEMDeltaRp5 (double value) { caloEMDeltaRp5_  = value; }  
      void set_caloHadDeltaRp5(double value) { caloHadDeltaRp5_ = value; }  

    private:
      double caloEMDeltaRp3_; 
      double caloHadDeltaRp3_;
      double caloEMDeltaRp5_; 
      double caloHadDeltaRp5_;


};
