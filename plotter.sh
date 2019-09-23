#!/bin/bash

# ==============================================================================
# Give the path of your input root files (from Analyzer) and the output folder
# ==============================================================================
inputDir=temp_Test/
outputDir=temp_Test/

seed=123456
# ===================================
# Limit exclusion plots
# ===================================
# B(tH) = B(tZ) = 0.5, doublet
#python PlotScript/plotLimit.py --inputDir ${inputDir} --outputPath ${outputDir}/plots/limit/ExpLimit-TTM_bW0p0_tZ0p5_tH0p5.pdf --selectStr=bW0p0_tZ0p5_tH0p5

## B(bW) = 2B(tZ,tH) = 0.5, Singlet
#python PlotScript/plotLimit.py --inputDir ${inputDir} --outputPath ${outputDir}/plots/limit/ExpLimit-TTM_bW0p5_tZ0p25_tH0p25.pdf --selectStr=bW0p5_tZ0p25_tH0p25

## B(bW) = 1.0
#python PlotScript/plotLimit.py --inputDir ${inputDir} --outputPath ${outputDir}/plots/limit/ExpLimit-TTM_bW1p0_tZ0p0_tH0p0.pdf --selectStr=bW1p0_tZ0p0_tH0p0

## B(tH) = 1.0
#python PlotScript/plotLimit.py --inputDir ${inputDir} --outputPath ${outputDir}/plots/limit/ExpLimit-TTM_bW0p0_tZ0p0_tH1p0.pdf --selectStr=bW0p0_tZ0p0_tH1p0

## B(tZ) = 1.0
#python PlotScript/plotLimit.py --inputDir ${inputDir} --outputPath ${outputDir}/plots/limit/ExpLimit-TTM_bW0p0_tZ1p0_tH0p0.pdf --selectStr=bW0p0_tZ1p0_tH0p0



# ===================================================================================================
# Plot for nuisances difference
# This is reported when r assumed to be 0 (b-only)
# So only performing any one of the signal model fit is enough. All the nuisances differences on each signal mass and branching fraction are the same. 
#
# --saveShapes: to save pre- and post-fit plots in fitDiagnostics.root
# --saveWithUncertainties: to add uncertainties on shapes; usually run together with --saveShapes
# --saveOverallShapes: to save covariance between all bins across all channels
# ===================================================================================================
#inputWs=TTM1100_bW0p0_tZ0p5_tH0p5
#cd ${outputDir}${inputWs}

#combine -M FitDiagnostics ${inputWs}.root --saveShapes --saveWithUncertainties --saveOverallShapes -t -1
#cd - 

#python PlotScript/plotNuisances.py --inputPath ${outputDir}${inputWs}/fitDiagnostics.root --outputPath ${outputDir}/plots/DiffNuisances.pdf



# ================================================
# Impact plots (run combineTool 3 times) 
# ================================================
inputWs=TTM1100_bW0p0_tZ0p5_tH0p5
cd ${outputDir}${inputWs}

${HCTBASE}/src/CombineHarvester/CombineTools/scripts/combineTool.py -M Impacts --doInitialFit -d ${inputWs}.root -s ${seed} -t -1
#-m 125 --minimizerStrategyForMinos 1 --minimizerToleranceForMinos 5.001e-06
${HCTBase}/src/CombineHarvester/CombineTools/scripts/combineTool.py -M Impacts --doFit -d ${inputWs}.root -s ${seed} --parallel 4 -t -1
${HCTBase}/src/CombineHarvester/CombineTools/scripts/combineTool.py -M Impacts -d ${inputWs}.root -o ${outputDir}${inputWs}/impacts.json -t -1
cd-

postfit=Asimov
python PlotScripts/plotImpacts.py ${outputDir}${inputWs}/impacts.json -o ${outputDir}/plots/Impact${postfix}.pdf



# ================================================
# Correlation plot 
# ================================================
