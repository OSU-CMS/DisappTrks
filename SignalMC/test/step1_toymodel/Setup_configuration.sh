#! /bin/sh
MAXPT='10.01'
MINPT='9.99'
cmsRun Batch_SingleMu_pythia8_cfi_py_GEN_SIM_DIGI_L1_DIGI2RAW_RAW2DIGI_RECO.py $1 $MAXPT $MINPT
#cmsRun write_a_file.py $1 $MAXPT $MINPT

