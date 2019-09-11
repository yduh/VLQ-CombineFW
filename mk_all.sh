#!/bin/bash

inputDir=~/nobackup/WorkDir/singleLepAnalyzer/makeTemplates/templates_NewEl_complete/
outputDir=temp/

python make_data_card_from-theta_Run2017.py --inputDir ${inputDir} --pattern="*minMlbST*TTM*rebinned*.root" --outputDir temp/ 

for d in $(ls ${outputDir}); 
do
    python makeWorkspace.py --inputDir ${outputDir}/${d}/ --pattern "TTM*.txt"
done

combine -M AsymptoticLimits temp/TTM1100_bW0p0_tZ0p5_tH0p5/TTM1100_bW0p0_tZ0p5_tH0p5.root -t -1 --run=blind
combine -M AsymptoticLimits temp/TTM1200_bW0p0_tZ0p5_tH0p5/TTM1200_bW0p0_tZ0p5_tH0p5.root -t -1 --run=blind
combine -M AsymptoticLimits temp/TTM1300_bW0p0_tZ0p5_tH0p5/TTM1300_bW0p0_tZ0p5_tH0p5.root -t -1 --run=blind
combine -M AsymptoticLimits temp/TTM1400_bW0p0_tZ0p5_tH0p5/TTM1400_bW0p0_tZ0p5_tH0p5.root -t -1 --run=blind
combine -M AsymptoticLimits temp/TTM1500_bW0p0_tZ0p5_tH0p5/TTM1500_bW0p0_tZ0p5_tH0p5.root -t -1 --run=blind
combine -M AsymptoticLimits temp/TTM1600_bW0p0_tZ0p5_tH0p5/TTM1600_bW0p0_tZ0p5_tH0p5.root -t -1 --run=blind
combine -M AsymptoticLimits temp/TTM1700_bW0p0_tZ0p5_tH0p5/TTM1700_bW0p0_tZ0p5_tH0p5.root -t -1 --run=blind
combine -M AsymptoticLimits temp/TTM1800_bW0p0_tZ0p5_tH0p5/TTM1800_bW0p0_tZ0p5_tH0p5.root -t -1 --run=blind

combine -M AsymptoticLimits temp/TTM1100_bW0p5_tZ0p25_tH0p25/TTM1100_bW0p5_tZ0p25_tH0p25.root -t -1 --run=blind
combine -M AsymptoticLimits temp/TTM1200_bW0p5_tZ0p25_tH0p25/TTM1200_bW0p5_tZ0p25_tH0p25.root -t -1 --run=blind
combine -M AsymptoticLimits temp/TTM1300_bW0p5_tZ0p25_tH0p25/TTM1300_bW0p5_tZ0p25_tH0p25.root -t -1 --run=blind
combine -M AsymptoticLimits temp/TTM1400_bW0p5_tZ0p25_tH0p25/TTM1400_bW0p5_tZ0p25_tH0p25.root -t -1 --run=blind
combine -M AsymptoticLimits temp/TTM1500_bW0p5_tZ0p25_tH0p25/TTM1500_bW0p5_tZ0p25_tH0p25.root -t -1 --run=blind
combine -M AsymptoticLimits temp/TTM1600_bW0p5_tZ0p25_tH0p25/TTM1600_bW0p5_tZ0p25_tH0p25.root -t -1 --run=blind
combine -M AsymptoticLimits temp/TTM1700_bW0p5_tZ0p25_tH0p25/TTM1700_bW0p5_tZ0p25_tH0p25.root -t -1 --run=blind
combine -M AsymptoticLimits temp/TTM1800_bW0p5_tZ0p25_tH0p25/TTM1800_bW0p5_tZ0p25_tH0p25.root -t -1 --run=blind

combine -M AsymptoticLimits temp/TTM1100_bW1p0_tZ0p0_tH0p0/TTM1100_bW1p0_tZ0p0_tH0p0.root -t -1 --run=blind
combine -M AsymptoticLimits temp/TTM1200_bW1p0_tZ0p0_tH0p0/TTM1200_bW1p0_tZ0p0_tH0p0.root -t -1 --run=blind
combine -M AsymptoticLimits temp/TTM1300_bW1p0_tZ0p0_tH0p0/TTM1300_bW1p0_tZ0p0_tH0p0.root -t -1 --run=blind
combine -M AsymptoticLimits temp/TTM1400_bW1p0_tZ0p0_tH0p0/TTM1400_bW1p0_tZ0p0_tH0p0.root -t -1 --run=blind
combine -M AsymptoticLimits temp/TTM1500_bW1p0_tZ0p0_tH0p0/TTM1500_bW1p0_tZ0p0_tH0p0.root -t -1 --run=blind
combine -M AsymptoticLimits temp/TTM1600_bW1p0_tZ0p0_tH0p0/TTM1600_bW1p0_tZ0p0_tH0p0.root -t -1 --run=blind
combine -M AsymptoticLimits temp/TTM1700_bW1p0_tZ0p0_tH0p0/TTM1700_bW1p0_tZ0p0_tH0p0.root -t -1 --run=blind
combine -M AsymptoticLimits temp/TTM1800_bW1p0_tZ0p0_tH0p0/TTM1800_bW1p0_tZ0p0_tH0p0.root -t -1 --run=blind

combine -M AsymptoticLimits temp/TTM1100_bW0p0_tZ0p0_tH1p0/TTM1100_bW0p0_tZ0p0_tH1p0.root -t -1 --run=blind
combine -M AsymptoticLimits temp/TTM1200_bW0p0_tZ0p0_tH1p0/TTM1200_bW0p0_tZ0p0_tH1p0.root -t -1 --run=blind
combine -M AsymptoticLimits temp/TTM1300_bW0p0_tZ0p0_tH1p0/TTM1300_bW0p0_tZ0p0_tH1p0.root -t -1 --run=blind
combine -M AsymptoticLimits temp/TTM1400_bW0p0_tZ0p0_tH1p0/TTM1400_bW0p0_tZ0p0_tH1p0.root -t -1 --run=blind
combine -M AsymptoticLimits temp/TTM1500_bW0p0_tZ0p0_tH1p0/TTM1500_bW0p0_tZ0p0_tH1p0.root -t -1 --run=blind
combine -M AsymptoticLimits temp/TTM1600_bW0p0_tZ0p0_tH1p0/TTM1600_bW0p0_tZ0p0_tH1p0.root -t -1 --run=blind
combine -M AsymptoticLimits temp/TTM1700_bW0p0_tZ0p0_tH1p0/TTM1700_bW0p0_tZ0p0_tH1p0.root -t -1 --run=blind
combine -M AsymptoticLimits temp/TTM1800_bW0p0_tZ0p0_tH1p0/TTM1800_bW0p0_tZ0p0_tH1p0.root -t -1 --run=blind

combine -M AsymptoticLimits temp/TTM1100_bW0p0_tZ1p0_tH0p0/TTM1100_bW0p0_tZ1p0_tH0p0.root -t -1 --run=blind
combine -M AsymptoticLimits temp/TTM1200_bW0p0_tZ1p0_tH0p0/TTM1200_bW0p0_tZ1p0_tH0p0.root -t -1 --run=blind
combine -M AsymptoticLimits temp/TTM1300_bW0p0_tZ1p0_tH0p0/TTM1300_bW0p0_tZ1p0_tH0p0.root -t -1 --run=blind
combine -M AsymptoticLimits temp/TTM1400_bW0p0_tZ1p0_tH0p0/TTM1400_bW0p0_tZ1p0_tH0p0.root -t -1 --run=blind
combine -M AsymptoticLimits temp/TTM1500_bW0p0_tZ1p0_tH0p0/TTM1500_bW0p0_tZ1p0_tH0p0.root -t -1 --run=blind
combine -M AsymptoticLimits temp/TTM1600_bW0p0_tZ1p0_tH0p0/TTM1600_bW0p0_tZ1p0_tH0p0.root -t -1 --run=blind
combine -M AsymptoticLimits temp/TTM1700_bW0p0_tZ1p0_tH0p0/TTM1700_bW0p0_tZ1p0_tH0p0.root -t -1 --run=blind
combine -M AsymptoticLimits temp/TTM1800_bW0p0_tZ1p0_tH0p0/TTM1800_bW0p0_tZ1p0_tH0p0.root -t -1 --run=blind

#python runCombineTask.py --inputDir ${outputDir} --selectStr "TTM" --option "-t -1 --run=blind"
#python runCombineTask.py --inputDir ${outputDir} --selectStr "TTM" --option "-t -1 --expectSignal=1" --method=Significance
