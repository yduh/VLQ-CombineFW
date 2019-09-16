import os,copy,math,argparse,ROOT,glob

from Core.DataCard import DataCard,CardConfig
from Core.Systematic import *
from Core.Process import *
from Core.Reader import *
from Core.Channel import Bin
from Core.FileReader import FileReader

from Core.BaseObject import BaseObject

from Utils.Hist import getCountAndError,getIntegral,removeOverflow
from Utils.DataCard import SignalModel
from Utils.mkdir_p import mkdir_p

from Physics.Br import *

# __________________________________________________________________ ||
parser = argparse.ArgumentParser()
parser.add_argument("--inputDir",action="store")
parser.add_argument("--outputDir",action="store")
parser.add_argument("--pattern",action="store")
parser.add_argument("--verbose",action="store_true")
option = parser.parse_args()

# __________________________________________________________________ ||
nameMap = {
            "sig": "sig",
            "top": "top",
            "ewk": "ewk",
            "qcd": "qcd",
            "DATA": "data_obs",
        }
varyMap = {
            "plus": "Up",
            "minus": "Down",
        }

zero = 1E-12
autoMCStatsLine = "* autoMCStats 10."
# Ref: https://cms-analysis.github.io/HiggsAnalysis-CombinedLimit/part2/bin-wise-stats/

# __________________________________________________________________ ||
for inputPath in glob.glob(option.inputDir+option.pattern):
    print "-"*40
    print "Running on input: "+inputPath
    signal_name = "_".join(os.path.basename(inputPath).split("_")[2:6])
    print "Signal model: "+signal_name
    inputFile = ROOT.TFile(inputPath,"READ")
    rootObjs = [inputFile.Get(k.GetName()) for k in inputFile.GetListOfKeys()]
    categoryDict = {}
    for obj in rootObjs:
        items = obj.GetName().split("__")
        catStr = "_".join(items[0].split("_")[2:])
        sample = items[1]
        if len(items) == 2:
            vary = "central"
            syst = "nominal"
        elif len(items) == 4:
            syst = items[2]
            vary = items[3]
        if catStr not in categoryDict:
            categoryDict[catStr] = BaseObject(catStr,sampleDict=dict(),)
        if sample not in categoryDict[catStr].sampleDict:
            categoryDict[catStr].sampleDict[sample] = BaseObject(nameMap[sample],systList=list(),)
        if syst == "nominal":
            categoryDict[catStr].sampleDict[sample].hist = obj
        else:
            if syst not in categoryDict[catStr].sampleDict[sample].systList: categoryDict[catStr].sampleDict[sample].systList.append(BaseObject(syst,hist=obj,vary=varyMap[vary]))

    # __________________________________________________________________ ||
    lnSystFile      = "Config/NormSyst.txt"
    shapeSystFile   = "Config/ShapeSyst.txt"
    shapeStr        = "shapes * * {fileName} $CHANNEL/$PROCESS $CHANNEL/$PROCESS_$SYSTEMATIC\n"

    # __________________________________________________________________ ||
    config = CardConfig(signal_name)
    config.shapeStr = shapeStr.format(fileName=signal_name+"_shapes.root")
    dataCard = DataCard(config)
    cardDir = option.outputDir+"/"+dataCard.makeOutFileName("/","")
    reader = FileReader()
    mkdir_p(option.outputDir)
    writeObjDict = {}
    binList = []
    for catStr,cat in categoryDict.iteritems():
        bin = BaseObject(catStr,
                lnSystFile=lnSystFile,
                shapeSystFile=shapeSystFile,
                processList=list(),
                signalNames=[signal_name,],
                isSignal=lambda x: x == "sig",
                systList=list(),
                rateParams=[],
                parameterList=[],
                )
        binList.append(bin)
        for sampleName,sample in cat.sampleDict.iteritems():
            count,error = getIntegral(sample.hist)
            process = Process(sample.name,count if count > 0. else zero,error)
            if sample.name != "data_obs":
                bin.processList.append(process)
            else:
                bin.data = process
        lnSystReader = LogNormalSystReader()
        bin.systList += lnSystReader.makeLnSyst(bin.lnSystFile)
        shapeSystReader = ShapeSystReader()
        bin.systList += shapeSystReader.makeShapeSyst(bin.shapeSystFile)
    mkdir_p(cardDir)
    dataCard.makeCard(cardDir,binList,autoMCStatsLine=autoMCStatsLine)
    shapeFilePath = os.path.join(cardDir,signal_name+"_shapes.root")
    outputFile = ROOT.TFile(shapeFilePath,"RECREATE")
    for ibin,bin in enumerate(binList):
        outputFile.mkdir(bin.name)
        binDir = outputFile.Get(bin.name)
        binDir.cd()
        for sampleName,sample in categoryDict[bin.name].sampleDict.iteritems():
            histClone = sample.hist.Clone(sample.name)
            histClone.Write()
            for syst in sample.systList:
                histClone = syst.hist.Clone(sample.name+"_"+syst.name+syst.vary)
                histClone.Write()
    outputFile.Write()
    outputFile.cd()
    outputFile.Close()
    inputFile.Close()
