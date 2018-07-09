// Based on MINI_AOD data format specified in OSUT3Analysis/AnaTools/interface/DataFormatMiniAOD.h
// Add definition/include for track collection.

#ifndef CUSTOM_DATA_FORMAT

  #define DISAPP_TRKS

#if DATA_FORMAT_IS_2017

  #include "OSUT3Analysis/AnaTools/interface/DataFormatMiniAOD2017.h"

  #undef  tracks_TYPE
  #undef  secondaryTracks_TYPE

  #define tracks_TYPE  CandidateTrack
  #define secondaryTracks_TYPE  CandidateTrack

#else

  #include "OSUT3Analysis/AnaTools/interface/DataFormatMiniAOD.h"

  #undef  tracks_TYPE
  #undef  tracks_INVALID

  #define tracks_TYPE  CandidateTrack

#endif

  #include "DisappTrks/CandidateTrackProducer/interface/CandidateTrack.h"

#endif
