// Based on MINI_AOD data format specified in OSUT3Analysis/AnaTools/interface/DataFormatMiniAOD.h
// Add definition/include for track collection.

#ifndef CUSTOM_DATA_FORMAT

  #include "OSUT3Analysis/AnaTools/interface/DataFormatMiniAOD.h"

  #undef  tracks_TYPE
  #undef  tracks_INVALID

  #define tracks_TYPE  CandidateTrack

  #include "DisappTrks/CandidateTrackProducer/interface/CandidateTrack.h"

#endif
