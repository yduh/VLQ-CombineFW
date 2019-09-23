import ROOT,argparse,sys,os
from collections import OrderedDict
from Utils.DrawFunc import makeNuiPlot,plotNuiStyle,getNuiGraph

# __________________________________________________________________________________________________________ ||
parser = argparse.ArgumentParser()

parser.add_argument('--inputPath',action='store')
parser.add_argument('--outputPath',action='store')
parser.add_argument('--verbose',action='store_true')
parser.add_argument('--fitResultName',action='store')

option = parser.parse_args()

ROOT.gROOT.SetBatch(ROOT.kTRUE)
ROOT.gStyle.SetOptStat(0)

# __________________________________________________________________________________________________________ ||
inputFile = ROOT.TFile(option.inputPath,"READ")
fitResult = inputFile.Get("fit_b" if not option.fitResultName else option.fitResultName).floatParsFinal()

nuisDict = OrderedDict()
for i in range(fitResult.getSize()):
    nuis = fitResult.at(i)
    nuisName = nuis.GetName()
    if "prop_bin" in nuisName: continue #nuisances of bin-by-bin statistics uncertainties
    if option.verbose: print "Processing ",nuisName
    nuisDict[nuisName] = (nuis.getVal(),nuis.getError())

# __________________________________________________________________________________________________________ ||
#postFitHist = makeNuiPlot(nuisDict,"postfit")
#preFitHist = makeNuiPlot(nuisDict,"prefit")
#postFitPlot = getNuiGraph(postFitHist,0.)
#preFitPlot = getNuiGraph(preFitHist,0.)
postFitPlot = makeNuiPlot(nuisDict,"postfit")
preFitPlot = makeNuiPlot(nuisDict,"prefit")
plotNuiStyle(postFitPlot,color=ROOT.kBlue)
plotNuiStyle(preFitPlot,color=ROOT.kBlack)
postFitPlot.GetYaxis().SetRangeUser(-3.,3.)
preFitPlot.GetYaxis().SetRangeUser(-3.,3.)
c = ROOT.TCanvas()
preFitPlot.SetFillColor(ROOT.kGray)
preFitPlot.SetMarkerSize(0.001)
preFitPlot.Draw("E2")
preFitPlot.GetXaxis().SetLabelSize(0.04)
postFitPlot.GetXaxis().SetLabelSize(0.04)
postFitPlot.Draw("Esame")
c.SetGridx()
c.SetGridy()
c.RedrawAxis('g')
if not os.path.exists(os.path.dirname(os.path.abspath(option.outputPath))):
    os.makedirs(os.path.dirname(os.path.abspath(option.outputPath)))
c.SaveAs(option.outputPath)

# __________________________________________________________________________________________________________ ||
