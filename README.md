## VLQ-CombineFW

### Part 1. Set up Higgs-Combine & CombineHarvester

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
        
    bash <(curl -s https://raw.githubusercontent.com/cms-analysis/CombineHarvester/master/CombineTools/scripts/sparse-checkout-ssh.sh)
    # compile
        
   - CombineHarvester is optional, I use CombineHarvester/CombineTools for nuisances pulls and impacts plot
   - Keep it updated by yourself, follow the reference: https://cms-analysis.github.io/HiggsAnalysis-CombinedLimit/#combine-tool

### Part 2. Set up VLQ-ComobineFW (this framework)
This framework helps you to generate data cards, prepare commands for Higgs-Combine-package, and make plots.
        
    git clone git@github.com:yduh/VLQ-CombineFW.git
     
### Part 3. Generate data cards & Apply for fit
1. Edit the work space to your CMSSW directory, set up the environment:
    
        source setup.sh
        
2. Edit Config/NormSystElectron.txt, Config/NormSystMuon.txt and Config/ShapeSystElectron.txt, Config/ShapeSystMuon.txt for your systematics. You can keep electron/muon channel systematics are the same or make them differently.

3. Edit mk_all.sh for your purpose. Have input root files ready. Then do:
 
        ./mk_all.sh

    - It runs with Asymptotic Frequentist Limits, which is fairly accurate when the event yields are not too small and the systematic uncertainties don't play a major role in the result, more details can be found in https://cms-analysis.github.io/HiggsAnalysis-CombinedLimit/part3/commonstatsmethods/
    - Input root files can contain more histograms than what will be used in a fit. Only MC components defined in 'make_data_card_from-theta.py' and systematics assignned in 'Config' will be included in data cards.
    - Bin-by-bin statistical uncertainties are included automatically in data cards using 'autoMCStats', reference https://cms-analysis.github.io/HiggsAnalysis-CombinedLimit/part2/bin-wise-stats/
    - Option '--removeCategory' supports to remove some categories from a fit. It's handy for test or optimization without re-preparing input root files.
        

### Part 4. Draw limits & Further investigation of the fit

To draw the limit exclusion plot, for example, you can do:

    python PlotScript/plotLimit.py --inputDir temp/ --outputPath temp/limit/test_ExpLimit-TTM_bW0p5_tZ0p25_tH0p25.pdf --selectStr=bW0p5_tZ0p25_tH0p25

To draw the signbificance plot, for example, you can do:

    python PlotScript/ --inputDir temp/ --outputPath temp/limit/test_ExpLimit-TTM_bW0p5_tZ0p25_tH0p25.pdf --selectStr=bW0p5_tZ0p25_tH0p25

Besides, the following figures are commonly required for analysis review:

   1. Nuisasnce difference before and after the fit
    
    combine -M FitDiagnostics ${inputWs}.root --saveShapes --saveWithUncertainties --saveOverallShapes -t -1
    python PlotScript/plotNuisances.py --inputPath ${outputDir}${inputWs}/fitDiagnostics.root --outputPath ${outputDir}/plots/DiffNuisances.pdf
        
   2. Nuisance correlation
    
    python PlotScript/makeSimpleCorrHist.py --inputPath ${outputDir}${inputWs}/fitDiagnostics.root --outputPath ${outputDir}/plots/Correlation.pdf
    
   3. Nuisance impacts (it takes longer)

    ${harvestBase}combineTool.py -M Impacts --doInitialFit -d ${inputWs}.root -s ${seed} -m 125 -t -1
    ${harvestBase}combineTool.py -M Impacts --doFit -d ${inputWs}.root -s ${seed} --parallel 4 -m 125 -t -1
    ${harvestBase}combineTool.py -M Impacts -d ${inputWs}.root -o ${outputDir}${inputWs}/impacts.json -m 125 -t -1
    python PlotScripts/plotImpacts.py ${outputDir}${inputWs}/impacts.json -o ${outputDir}/plots/Impact${postfix}.pdf
    

For any other requests above the list, you can always make it yourself by getting the fitting results from the corresponding root files.   

A collection of commands to make plots above is in plotter.sh, do:

    ./plotter.sh
    
    
