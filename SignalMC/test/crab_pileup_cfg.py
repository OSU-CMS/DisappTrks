#!/usr/bin/env python3
from CRABClient.UserUtilities import config

config = config()

# ── General ───────────────────────────────────────────────────────────────────
config.General.requestName     = 'PileupDist_RunIIISummer24PrePremix'
config.General.workArea        = 'crab_pileup'
config.General.transferOutputs = True
config.General.transferLogs    = True

# ── JobType ───────────────────────────────────────────────────────────────────
config.JobType.pluginName  = 'Analysis'
config.JobType.psetName    = 'pileup_cfg.py'  # CMSSW config (see below)
config.JobType.outputFiles = ['pileup_output.root']

# ── Data ──────────────────────────────────────────────────────────────────────
config.Data.inputDataset     = '/Neutrino_E-10_gun/RunIIISummer24PrePremix-Premixlib2024_140X_mcRun3_2024_realistic_v26-v1/PREMIX'
config.Data.inputDBS         = 'global'
config.Data.splitting        = 'Automatic'
config.Data.outLFNDirBase    = '/store/user/delossan/'
config.Data.publication      = False

# ── Site ──────────────────────────────────────────────────────────────────────
config.Data.outLFNDirBase = "/store/group/lpclonglived/DisappTrks/"
config.Site.storageSite = 'T3_US_FNALLPC'
