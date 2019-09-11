export PYTHONPATH=${PYTHONPATH}:${PWD}/
export PATH=${PATH}:${PWD}/bin/

export BASE_PATH=${PWD}
if [[ $HOSTNAME == *"cmslpc"* ]] ;
then
    echo "In LPC" ; 
    cd /uscms_data/d3/yiting11/WorkDir/singleLepAnalyzer/CMSSW_8_1_0/src/ ;
fi
eval `scramv1 runtime -sh`
cd -
