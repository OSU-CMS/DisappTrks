#!/usr/bin/env python3
import FWCore.ParameterSet.Config as cms

process = cms.Process("Demo")
process.load("FWCore.MessageService.MessageLogger_cfi")
process.maxEvents = cms.untracked.PSet(input = cms.untracked.int32(-1))
process.source = cms.Source("PoolSource",
                            fileNames = cms.untracked.vstring(
                            'file:/share/scratch0/rsantos/CMSSW_12_4_11_patch3/src/DisappTrks/BackgroundEstimation/test/condor/2022/EGammaFiducialMapWithoutIsoCut/EGamma_2022G/ElectronFiducialCalcBeforeOldCuts/skim_27.root'))
process.demo = cms.EDProducer('OSUGenericTrackProducer')
process.p = cms.Path(process.demo)
