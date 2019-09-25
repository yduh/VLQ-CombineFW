#!/bin/bash

# ==============================================================================
# Give the path of your input root files (from Analyzer) and the output folder
# ==============================================================================
inputPath=temp_Test/
outputPath=temp_Test/

seed=123456

###
cd ${HCTBASE}
eval `scramv1 runtime -sh`
cd -

harvestBase=${HCTBASE}/src/CombineHarvester/CombineTools/scripts/
# ===================================
# Limit exclusion plots
# ===================================
# B(tH) = B(tZ) = 0.5, doublet
#python PlotScript/plotLimit.py --inputPath ${inputPath} --outputPath ${outputPath}/plots/ExpLimit-TTM_bW0p0_tZ0p5_tH0p5.pdf --selectStr=bW0p0_tZ0p5_tH0p5

## B(bW) = 2B(tZ,tH) = 0.5, Singlet
#python PlotScript/plotLimit.py --inputPath ${inputPath} --outputPath ${outputPath}/plots/ExpLimit-TTM_bW0p5_tZ0p25_tH0p25.pdf --selectStr=bW0p5_tZ0p25_tH0p25

## B(bW) = 1.0
#python PlotScript/plotLimit.py --inputPath ${inputPath} --outputPath ${outputPath}/plots/ExpLimit-TTM_bW1p0_tZ0p0_tH0p0.pdf --selectStr=bW1p0_tZ0p0_tH0p0

## B(tH) = 1.0
#python PlotScript/plotLimit.py --inputPath ${inputPath} --outputPath ${outputPath}/plots/ExpLimit-TTM_bW0p0_tZ0p0_tH1p0.pdf --selectStr=bW0p0_tZ0p0_tH1p0

## B(tZ) = 1.0
#python PlotScript/plotLimit.py --inputPath ${inputPath} --outputPath ${outputPath}/plots/ExpLimit-TTM_bW0p0_tZ1p0_tH0p0.pdf --selectStr=bW0p0_tZ1p0_tH0p0



# ===================================================================================================
# Plot for nuisances difference & correlation
# This is reported when r assumed to be 0 (b-only)
# So only performing any one of the signal model fit is enough. All the nuisances differences on each signal mass and branching fraction are the same. 
#
# --saveShapes: to save pre- and post-fit plots in fitDiagnostics.root
# --saveWithUncertainties: to add uncertainties on shapes; usually run together with --saveShapes
# --saveOverallShapes: to save covariance between all bins across all channels
# ===================================================================================================
#inputWs=TTM1100_bW0p0_tZ0p5_tH0p5

#cd ${outputPath}${inputWs}
#combine -M FitDiagnostics ${inputWs}.root --saveShapes --saveWithUncertainties --saveOverallShapes --numToysForShapes 200 -s ${seed} -t -1
#cd - 

#python PlotScript/plotNuisances.py --inputPath ${outputPath}${inputWs}/fitDiagnostics.root --outputPath ${outputPath}/plots/DiffNuisances.pdf
#python PlotScript/makeSimpleCorrHist.py --inputPath ${outputPath}${inputWs}/fitDiagnostics.root --outputPath ${outputPath}/plots/Correlation.pdf



# ========================================================================================================
# Impact plots 
# (run combineTool 3 times, so totally 3 x (# of nuisances) of fits will be applied, it takes longer)
# Outputs from fit are higgsCombine_paramFit_Test_<<NUISANCE>>.MultiDimFit.mH125.root
# ========================================================================================================
inputWs=TTM1100_bW0p0_tZ0p5_tH0p5

mkdir -p ${outputPath}${inputWs}/impacts
cd ${outputPath}${inputWs}/impacts
${harvestBase}combineTool.py -M Impacts --doInitialFit -d ../${inputWs}.root -s ${seed} -m 125 -t -1 
#--minimizerStrategyForMinos 1 --minimizerToleranceForMinos 5.001e-06
${harvestBase}combineTool.py -M Impacts --doFits -d ../${inputWs}.root -s ${seed} --parallel 4 -m 125 -t -1
${harvestBase}combineTool.py -M Impacts -d ../${inputWs}.root -o impacts.json -m 125 -t -1
cd -

postfit=Asimov
python PlotScript/plotImpacts.py -i ${outputPath}${inputWs}/impacts.json -o ${outputPath}/plots/Impact${postfix}.pdf



