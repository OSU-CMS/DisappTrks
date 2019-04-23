MCHI=$1
MNEU=$2
CTAU=$3
PT=$4
dR=$5

python Setup_cfg.py $MCHI $MNEU $CTAU $PT $dR

python ${CMSSW_BASE}/src/DisappTrks/SignalMC/data/Setup_SLHA_toymodel.py $MCHI $MNEU $CTAU


