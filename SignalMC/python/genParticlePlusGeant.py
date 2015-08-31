def customize (process):
  outputTypes = ["RAWSIM", "RECOSIM", "AODSIM", "MINIAODSIM"]
  for a in outputTypes:
    b = a + "output"
    if hasattr (process, b):
      getattr (process, b).outputCommands.append ("keep *_genParticlePlusGeant_*_*")

  return process
