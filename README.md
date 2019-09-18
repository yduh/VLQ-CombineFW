## VLQ-CombineFW

### Part 1. Set up Higgs-Combine-package 

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

  - Keep it updated by yourself, follow the reference: https://cms-analysis.github.io/HiggsAnalysis-CombinedLimit/#slc6cc7-release-cmssw_8_1_x
  
  
### Part 2. Set up VLQ-ComobineFW (this framework)
  - This framework helps you to generate data cards, prepare commands for Higgs-Combine-package, and make plots.
  
     git clone git@github.com:yduh/VLQ-CombineFW.git
     
### Part 3. Generate data cards & Apply fits & Draw limits
- Edit the work space to your CMSSW directory, set up the environment:

        source setup.sh
        
- Edit Config/NormSyst.txt and Config/ShapeSyst.txt for your systematics. 
- Have input root files ready. Edit mk_all.sh as well. Then do:
 
        ./mk_all.sh
        
    - It runs with Asymptotic Frequentist Limits, which is fairly accurate when the event yields are not too small and the systematic uncertainties don't play a major role in the result, more details can be found in https://cms-analysis.github.io/HiggsAnalysis-CombinedLimit/part3/commonstatsmethods/

- To draw the limit exclusion plot, you can do, for example:

        python PlotScript/plotLimit.py --inputDir temp/ --outputPath temp/limit/test_ExpLimit-TTM_bW0p5_tZ0p25_tH0p25.pdf --selectStr=bW0p5_tZ0p25_tH0p25
        
### Part 4. Further investigation of the fitting results
- Install CombineHarvester for nuisances pulls and impacts plot
        
        bash <(curl -s https://raw.githubusercontent.com/cms-analysis/CombineHarvester/master/CombineTools/scripts/sparse-checkout-ssh.sh)
        
   - Keep it updated by yourself, follow the reference: https://cms-analysis.github.io/HiggsAnalysis-CombinedLimit/#combine-tool
