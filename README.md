### VLQ-CombineFW

<< Part 1. Set up Combine >>

    export SCRAM_ARCH=slc6_amd64_gcc530
    cmsrel CMSSW_8_1_0
    cd CMSSW_8_1_0/src
    cmsenv
    git clone https://github.com/cms-analysis/HiggsAnalysis-CombinedLimit.git HiggsAnalysis/CombinedLimit
    cd HiggsAnalysis/CombinedLimit

    cd $CMSSW_BASE/src/HiggsAnalysis/CombinedLimit
    git fetch origin
    git checkout v7.0.13
    scramv1 b clean; scramv1 b

  - Keep it updated according to the reference: https://cms-analysis.github.io/HiggsAnalysis-CombinedLimit/#slc6cc7-release-cmssw_8_1_x
  
  
<< Part 2. Set up VLQ-ComobineFW >>

     git clone git@github.com:yduh/VLQ-CombineFW.git
     
<< Part 3. Generate data cards & Apply fits & Draw results >>

- After setting up everything, having target root files ready, and finishing the edit for systematics. Do:

        source setup.sh
        ./mk_all.sh

- To draw the limit exclusion plot, for example, can do:

        python PlotScript/plotLimit.py --inputDir temp/ --outputPath temp/limit/test_ExpLimit-TTM_bW0p5_tZ0p25_tH0p25.pdf --selectStr=bW0p5_tZ0p25_tH0p25
