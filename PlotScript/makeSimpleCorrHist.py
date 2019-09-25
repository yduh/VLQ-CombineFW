import os,argparse,ROOT
#from Utils.rootHistTools import SetPalette

#setPalette = SetPalette()
#setPalette('kBird')

parser = argparse.ArgumentParser()
parser.add_argument("--inputPath",action="store")
parser.add_argument("--outputPath",action="store")

ROOT.gROOT.SetBatch(ROOT.kTRUE)

option = parser.parse_args()

inputFile = ROOT.TFile(option.inputPath,"READ")
fit_b = inputFile.Get("fit_b")
if fit_b == None or fit_b.ClassName()   != "RooFitResult": raise RuntimeError, "File %s does not contain the output of the background fit 'fit_b'" % fitFile
fullCorrHist = fit_b.correlationHist()

nuisList = []
nBinsX = fullCorrHist.GetNbinsX()
for ibinX in range(1,nBinsX+1):
    nuisName = fullCorrHist.GetXaxis().GetBinLabel(ibinX)
    if "prop_bin" in nuisName: continue
    nuisList.append((nuisName,ibinX))

hist = ROOT.TH2D("simple_correlation","simple_correlation",len(nuisList),-0.5,len(nuisList)-0.5,len(nuisList),-0.5,len(nuisList)-0.5)
for ibinX,(nuisName_i,i) in enumerate(nuisList):
    for ibinY,(nuisName_j,j) in enumerate(nuisList):
        binContent = fullCorrHist.GetBinContent(i,nBinsX-j+1)
        hist.SetBinContent(ibinX+1,ibinY+1,binContent)
        hist.GetXaxis().SetBinLabel(ibinX+1,nuisName_i)
        hist.GetYaxis().SetBinLabel(ibinY+1,nuisName_j)

c = ROOT.TCanvas()
hist.SetStats(0)
hist.GetZaxis().SetRangeUser(-1.,1.)
hist.GetXaxis().SetLabelSize(0.04)
hist.GetYaxis().SetLabelSize(0.04)
hist.Draw("colz")
if not os.path.exists(os.path.abspath(os.path.dirname(option.outputPath))):
    os.makedirs(os.path.abspath(os.path.dirname(option.outputPath)))
c.SaveAs(option.outputPath)
