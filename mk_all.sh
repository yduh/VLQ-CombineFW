#!/bin/bash

# ==============================================================================
# Give the path of your input root files (from Analyzer) and the output folder
# ==============================================================================
inputDir=~/nobackup/WorkDir/singleLepAnalyzer/makeTemplates/templates_NewEl_complete/
outputDir=temp_ShapeSyst/

# ================================================================================================
# Prepare root file and the corresponding data card: ${SigModel}_shapes.root, ${SigModel}.txt 
# ================================================================================================
#python make_data_card_from-theta_Run2017.py --inputDir ${inputDir} --pattern="*minMlbST*TTM*rebinned*.root" --outputDir ${outputDir} 


# ========================================================================================================
# Convert data crad and root file to ROOT workspace for Combine: the output will be ${SigModel}.root 
# ========================================================================================================
#for d in $(ls ${outputDir}); 
#do
#    python makeWorkspace.py --inputDir ${outputDir}/${d}/ --pattern "TTM*.txt"
#done

# =============================================================
# Fit applied for each signal model, Asymptotic limit. 
# You can do this separately/parallel
# =============================================================
# B(tH) = B(tZ) = 0.5, doublet
for m in $(seq 11 18);
do
    cd ${outputDir}TTM${m}00_bW0p0_tZ0p5_tH0p5 
    combine -M AsymptoticLimits TTM${m}00_bW0p0_tZ0p5_tH0p5.root -t -1 --run=blind
    cd - 
    # Or:
    #combine -M AsymptoticLimits ${outputDir}/TTM${m}00_bW0p0_tZ0p5_tH0p5/TTM${m}00_bW0p0_tZ0p5_tH0p5.root -t -1 --run=blind
    #mv higgsCombineTest.AsymptoticLimits.mH120.root ${outputDir}TTM${m}00_bW0p0_tZ0p5_tH0p5 
done

# B(bW) = 2B(tZ,tH) = 0.5, Singlet
for m in $(seq 11 18);
do
    cd ${outputDir}TTM${m}00_bW0p5_tZ0p25_tH0p25 
    combine -M AsymptoticLimits TTM${m}00_bW0p5_tZ0p25_tH0p25.root -t -1 --run=blind
    cd - 
done

# B(bW) = 1.0
for m in $(seq 11 18);
do
    cd ${outputDir}TTM${m}00_bW0p5_tZ0p25_tH0p25 
    combine -M AsymptoticLimits TTM${m}00_bW1p0_tZ0p0_tH0p0.root -t -1 --run=blind
    cd - 
done

# B(tH) = 1.0
for m in $(seq 11 18);
do
    cd ${outputDir}TTM${m}00_bW0p5_tZ0p25_tH0p25 
    combine -M AsymptoticLimits TTM${m}00_bW0p0_tZ0p0_tH1p0.root -t -1 --run=blind
    cd - 
done

# B(tZ) = 1.0
for m in $(seq 11 18);
do
    cd ${outputDir}TTM${m}00_bW0p5_tZ0p25_tH0p25 
    combine -M AsymptoticLimits TTM${m}00_bW0p0_tZ1p0_tH0p0.root -t -1 --run=blind
    cd - 
done

