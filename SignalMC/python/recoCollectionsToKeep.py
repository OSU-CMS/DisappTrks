def customize (process):
  outputTypes = ["RAWSIM", "RECOSIM", "AODSIM", "MINIAODSIM"]
  for a in outputTypes:
    b = a + "output"
    if hasattr (process, b):
      getattr (process, b).outputCommands.append ("keep *_generalTracks_*_*")
      getattr (process, b).outputCommands.append ("keep *_candidateDisappearingTracks_*_*")
      getattr (process, b).outputCommands.append ("keep recoCaloMETs_*_*_RECO")
      getattr (process, b).outputCommands.append ("keep recoMETs_*_*_RECO")
      getattr (process, b).outputCommands.append ("keep recoPFMETs_*_*_RECO")
      getattr (process, b).outputCommands.append ("keep *_reducedEcalRecHitsEE_*_*")
      getattr (process, b).outputCommands.append ("keep *_reducedEcalRecHitsEB_*_*")
      getattr (process, b).outputCommands.append ("keep *_reducedHcalRecHits_*_*")
      getattr (process, b).outputCommands.append ("keep *_dt4DSegments_*_*")
      getattr (process, b).outputCommands.append ("keep *_cscSegments_*_*")
      getattr (process, b).outputCommands.append ("keep *_*_rho_*")

  return process
