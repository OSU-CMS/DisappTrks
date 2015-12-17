################################################################################
# Functions for getting the invariant mass of an object and a track, given
# different mass assumptions for the track.
################################################################################

def invMassGivenEnergy (obj, energy):
    return "sqrt ((" + obj + ".energy + track." + energy + ") * (" + obj + ".energy + track." + energy + ") - (" + obj + ".px + track.px) * (" + obj + ".px + track.px) - (" + obj + ".py + track.py) * (" + obj + ".py + track.py) - (" + obj + ".pz + track.pz) * (" + obj + ".pz + track.pz))"

def invMassWithElectron (obj):
    return invMassGivenEnergy (obj, "energyOfElectron")

def invMassWithMuon (obj):
    return invMassGivenEnergy (obj, "energyOfMuon")

def invMassWithTau (obj):
    return invMassGivenEnergy (obj, "energyOfTau")

def invMassWithPion (obj):
    return invMassGivenEnergy (obj, "energyOfPion")

def invMassWithProton (obj):
    return invMassGivenEnergy (obj, "energyOfProton")
