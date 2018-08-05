import FWCore.ParameterSet.Config as cms

disappTrksOutputCommands = cms.untracked.vstring(
    "keep recoCaloMETs_*_*_*",
    "keep recoMETs_*_*_*",
    "keep recoPFMETs_pfChMet_*_*",
    "keep recoPFMETs_pfMet_*_*",
    "keep recoPFMETs_pfMetEI_*_*",
    "keep CandidateTracks_*_*_*",
    "keep recoGsfTracks_*_*_*",
    "keep CutResults_*_*_*",
)

def customizeMiniAODSIMOutput(process):

    process.load('Configuration.EventContent.EventContent_cff')

    process.MINIAODSIMoutput = cms.OutputModule("PoolOutputModule",
        compressionAlgorithm = cms.untracked.string('LZMA'),
        compressionLevel = cms.untracked.int32(4),
        dataset = cms.untracked.PSet(
            dataTier = cms.untracked.string('MINIAODSIM'),
            filterName = cms.untracked.string('')
        ),
        dropMetaData = cms.untracked.string('ALL'),
        eventAutoFlushCompressedSize = cms.untracked.int32(15728640),
        fastCloning = cms.untracked.bool(False),
        fileName = cms.untracked.string('miniAODWithCandidateTracks.root'),
        outputCommands = process.MINIAODSIMEventContent.outputCommands,
        overrideInputFileSplitLevels = cms.untracked.bool(True)
    )
    process.MINIAODSIMoutput.outputCommands.extend (disappTrksOutputCommands)

def customizeMINIAODElectronVID(process):
    from PhysicsTools.SelectorUtils.tools.vid_id_tools import DataFormat,switchOnVIDElectronIdProducer,setupAllVIDIdsInModule,setupVIDElectronSelection
    switchOnVIDElectronIdProducer(process, DataFormat.MiniAOD)

    my_id_modules = ['RecoEgamma.ElectronIdentification.Identification.cutBasedElectronID_Spring15_25ns_V1_cff']

    if os.environ["CMSSW_VERSION"].startswith ("CMSSW_8_0_") or os.environ["CMSSW_VERSION"].startswith ("CMSSW_9_4_"):
        my_id_modules = ['RecoEgamma.ElectronIdentification.Identification.cutBasedElectronID_Summer16_80X_V1_cff']

    if os.environ["CMSSW_VERSION"].startswith ("CMSSW_9_4_"):
        my_id_modules = ['RecoEgamma.ElectronIdentification.Identification.cutBasedElectronID_Fall17_94X_V1_cff']

    # Setup all the desired modules to be run
    for idmod in my_id_modules:
        setupAllVIDIdsInModule(process, idmod, setupVIDElectronSelection)
    process.egmGsfElectronIDSequence_step = cms.Path(process.egmGsfElectronIDSequence)
    process.schedule.insert(0, process.egmGsfElectronIDSequence_step)

    return process