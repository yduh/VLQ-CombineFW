import ROOT,glob,os,argparse,subprocess,array,math
from collections import OrderedDict
import Utils.CMS_lumi as CMS_lumi
import Utils.tdrstyle as tdrstyle

from Physics.TpTp_XS import *

ROOT.gROOT.SetBatch(ROOT.kTRUE)

parser = argparse.ArgumentParser()
parser.add_argument("--inputDir",action="store")
parser.add_argument("--outputPath",action="store")
parser.add_argument("--selectStr",action="store",default="")

option = parser.parse_args()

inputDir = option.inputDir

# ________________________________________________________________ ||
# CMS style
# ________________________________________________________________ ||
CMS_lumi.cmsText = "CMS"
CMS_lumi.extraText = "Preliminary"
CMS_lumi.cmsTextSize = 0.65
CMS_lumi.outOfFrame = True
#CMS_lumi.lumi_13TeV = "77.3 fb^{-1}"
#CMS_lumi.lumi_13TeV = "35.9 fb^{-1}"
CMS_lumi.lumi_13TeV = "41 fb^{-1}"
#CMS_lumi.lumi_13TeV = "136.1 fb^{-1}"
#CMS_lumi.lumi_13TeV = "150 fb^{-1}"
tdrstyle.setTDRStyle()

setLogY         = True
expOnly         = True
#quantiles       = ["down2","down1","central","up1","up2","obs"]
quantiles       = ["down2","down1","central","up1","up2",]
varName         = "limit"
plots           = ["r",]
maxFactor       = 1.5
y_label_dict    = {
                    "r": "Signal strength",
                    "xs": "#sigma(TT) [pb]",
                  }
x_label         = "T mass"
draw_theory     = True
model           = "TT"

def calculate(r_value,window_value,what):
    if what == "r":
        return r_value
    elif what == "xs":
        return r_value*xsec[model+'_M'+str(window_value)]
    else:
        raise RuntimeError

# ________________________________________________________________ ||
# Read limit from directory
# ________________________________________________________________ ||
outDict = OrderedDict()
for quantile in quantiles:
    outDict[quantile] = OrderedDict()
for cardDir in glob.glob(inputDir+"*"+option.selectStr+"*/"):
    print "Reading directory "+cardDir
    inputFile = ROOT.TFile(cardDir+"higgsCombineTest.AsymptoticLimits.mH120.root","READ")
    tree = inputFile.Get("limit")
    window_name = cardDir.split("/")[-2]
    #window_value = int(window_name.split("_")[1][1:])
    window_value = int(window_name.split("_")[0][3:])
    if expOnly:
        for i,entry in enumerate(tree):
            outDict[quantiles[i]][window_value] = getattr(entry,varName)
    else:
        raise RuntimeError

# ________________________________________________________________ ||
# Draw limit with outDict
# ________________________________________________________________ ||
outputDir = os.path.dirname(option.outputPath)
if not os.path.exists(outputDir):
    os.makedirs(outputDir)
nPoints = len(outDict["central"])
outGraphDict = {}
for plot in plots:
    W = 800
    H  = 600
    T = 0.08*H
    B = 0.12*H
    L = 0.12*W
    R = 0.04*W
    c = ROOT.TCanvas("c","c",100,100,W,H)
    if setLogY:
        c.SetLogy()
    c.SetFillColor(0)
    c.SetBorderMode(0)
    c.SetFrameFillStyle(0)
    c.SetFrameBorderMode(0)
    c.SetLeftMargin( L/W )
    c.SetRightMargin( R/W )
    c.SetTopMargin( T/H )
    c.SetBottomMargin( B/H )
    c.SetTickx(0)
    c.SetTicky(0)
    c.SetGrid()
    c.cd()
    frame = c.DrawFrame(1.4,0.001, 4.1, 10)
    frame.GetYaxis().CenterTitle()
    frame.GetYaxis().SetTitleSize(0.05)
    frame.GetXaxis().SetTitleSize(0.05)
    frame.GetXaxis().SetLabelSize(0.04)
    frame.GetYaxis().SetLabelSize(0.03)
    frame.GetYaxis().SetTitleOffset(1.2)
    frame.GetXaxis().SetNdivisions(508)
    frame.GetYaxis().CenterTitle(True)
    #frame.GetYaxis().SetTitle("95% upper limit on #sigma / #sigma_{SM}")
    frame.GetYaxis().SetTitle(y_label_dict[plot])
    frame.GetXaxis().SetTitle(x_label)
    #frame.SetMinimum(0 if not setLogY else 0.002)
    yellow = ROOT.TGraph(2*nPoints)
    green = ROOT.TGraph(2*nPoints)
    median = ROOT.TGraph(nPoints)
    #for g in [yellow,green,median]:
    #    g.GetYaxis().SetRangeUser(0 if not setLogY else 0.0002,1.)
    CMS_lumi.CMS_lumi(c,4,11)
    window_values = outDict["central"].keys()
    window_values.sort()
    frame.GetXaxis().SetLimits(min(window_values),max(window_values))
    frame.SetMaximum(max([calculate(outDict[quan][window_value],window_value,plot) for quan in quantiles for window_value in window_values ])*maxFactor)
    for i,window_value in enumerate(window_values):
        yellow.SetPoint( i, window_value,   calculate(outDict["up2"][window_value]         , window_value, plot) )
        yellow.SetPoint( 2*nPoints-1-i, window_value,   calculate(outDict["down2"][window_value]       , window_value, plot) )
        green.SetPoint( i, window_value,    calculate(outDict["up1"][window_value]         , window_value, plot) )
        green.SetPoint( 2*nPoints-1-i, window_value,    calculate(outDict["down1"][window_value]       , window_value, plot) )
        median.SetPoint( i, window_value,   calculate(outDict["central"][window_value]     , window_value, plot) )

    mg = ROOT.TMultiGraph()
    mg.SetMaximum(1.)
    mg.SetMinimum(0.001 if setLogY else 0.)

    yellow.SetFillColor(ROOT.kOrange)
    yellow.SetLineColor(ROOT.kOrange)
    yellow.SetFillStyle(1001)
    mg.Add(yellow,'F')
    #yellow.Draw('F')

    green.SetFillColor(ROOT.kGreen+1)
    green.SetLineColor(ROOT.kGreen+1)
    green.SetFillStyle(1001)
    mg.Add(green,'F')
    #green.Draw('Fsame')

    median.SetLineColor(1)
    median.SetLineWidth(2)
    median.SetLineStyle(2)
    mg.Add(median,'L')
    #median.Draw('Lsame')

    if draw_theory:
        #xsec_graph[model].GetYaxis().SetRangeUser(0.001,0.04)
        xsec_graph[model] = make_graph(xsec,model,lambda x: x >= min(window_values) and x <= max(window_values))
        xsec_graph[model].SetLineColor(ROOT.kRed)
        xsec_graph[model].SetLineWidth(3)
        mg.Add(xsec_graph[model],'L')
        #xsec_graph[model].Draw("Lsame")

    mg.GetYaxis().SetTitle(y_label_dict[plot])
    mg.GetXaxis().SetTitle(x_label)
    mg.Draw("a")

    c.SaveAs(option.outputPath.replace(".pdf","_"+plot+".pdf"))
