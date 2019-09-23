import ROOT

def cmstext(njets,isPrelim=True):
    xpos = ROOT.gPad.GetLeftMargin()
    ypos = 1.-ROOT.gPad.GetTopMargin()

    lx = ROOT.TLatex(0., 0., 'Z')
    lx.SetNDC(True)
    lx.SetTextFont(62)
    lx.SetTextSize(0.05)
    lx.SetTextAlign(13)
    lx.DrawLatex(xpos+0.04, ypos-0.03, 'CMS')

    if isPrelim:
        lx2 = ROOT.TLatex(0., 0., 'Z')
        lx2.SetNDC(True)
        lx2.SetTextFont(53)
        lx2.SetTextSize(20)
        lx2.SetTextAlign(13)
        lx2.DrawLatex(xpos+0.04, ypos-0.08, '#it{Preliminary}')
    #lx2.DrawLatex(xpos+0.04, ypos-0.08, 'Preliminary')

    lx3 = ROOT.TLatex(0., 0., 'Z')
    lx3.SetNDC(True)
    lx3.SetTextFont(43)
    lx3.SetTextSize(24)
    lx3.SetTextAlign(31)
    #lx3.DrawLatex(0.55,0.92,'%s, %s' %(sys.argv[1],sys.argv[3]))
    lx3.DrawLatex(xpos+0.825, ypos+0.015,'35.8 fb^{-1} (13 TeV)')
    lx3.Draw()

    lx4 = ROOT.TLatex(0., 0., 'Z')
    lx4.SetNDC(True)
    lx4.SetTextFont(63)
    lx4.SetTextSize(25)
    lx4.SetTextAlign(13)
    #lx4.DrawLatex(xpos+0.33, ypos-0.05, 'e/#mu+jets, %s jets' %njets[0])
    lx5 = ROOT.TLatex(0., 0., 'Z')
    lx5.SetNDC(True)
    lx5.SetTextFont(63)
    lx5.SetTextSize(20)
    lx5.SetTextAlign(13)
    if njets[0] == 'c':
        lx4.DrawLatex(xpos+0.17, ypos-0.032, 'e/#mu+jets, #geq 3 jets')
        lx5.DrawLatex(xpos+0.17, ypos-0.085, '(Channels combined)')
    elif njets[0] == '5':
        lx4.DrawLatex(xpos+0.17, ypos-0.032, 'e/#mu+jets, #geq 5 jets')
    else:
        lx4.DrawLatex(xpos+0.17, ypos-0.032, 'e/#mu+jets, %s jets' %njets[0])
    lx4.Draw()
    lx5.Draw()

def cmstext2(njets,isPrelim=True):
    xpos = ROOT.gPad.GetLeftMargin()
    ypos = 1.-ROOT.gPad.GetTopMargin()

    lx = ROOT.TLatex(0., 0., 'Z')
    lx.SetNDC(True)
    lx.SetTextFont(62)
    lx.SetTextSize(0.05)
    lx.SetTextAlign(13)
    lx.DrawLatex(xpos+0.04, ypos-0.03, 'CMS')

    if isPrelim:
        lx2 = ROOT.TLatex(0., 0., 'Z')
        lx2.SetNDC(True)
        lx2.SetTextFont(53)
        lx2.SetTextSize(20)
        lx2.SetTextAlign(13)
        lx2.DrawLatex(xpos+0.04, ypos-0.08, '#it{Preliminary}')
        #lx2.DrawLatex(xpos+0.04, ypos-0.08, 'Preliminary')

    lx3 = ROOT.TLatex(0., 0., 'Z')
    lx3.SetNDC(True)
    lx3.SetTextFont(43)
    lx3.SetTextSize(18)
    lx3.SetTextAlign(31)
    #lx3.DrawLatex(0.937, ypos+0.015,'35.8 fb^{-1} (13 TeV)')
    lx3.DrawLatex(0.92, ypos+0.015,'35.8 fb^{-1} (13 TeV)')
    lx3.Draw()

    lx4 = ROOT.TLatex(0., 0., 'Z')
    lx4.SetNDC(True)
    lx4.SetTextFont(63)
    lx4.SetTextSize(16.5)
    lx4.SetTextAlign(13)
    #lx4.DrawLatex(xpos+0.53, ypos-0.06, 'e/#mu+jets, %s jets' %njets[0])
    #lx4.DrawLatex(xpos+0.24, ypos-0.06, 'e/#mu+jets, all channels combined')
    if njets[0] == 'c':
        lx4.DrawLatex(xpos+0.2, ypos-0.035, 'e/#mu+jets, #geq 3 jets')
        #lx4.DrawLatex(xpos+0.2, ypos-0.085, 'Channels combined')
    elif njets[0] == '5':
        lx4.DrawLatex(xpos+0.2, ypos-0.035, 'e/#mu+jets, #geq 5 jets')
    else:
        lx4.DrawLatex(xpos+0.2, ypos-0.035, 'e/#mu+jets, %s jets' %njets[0])
    lx4.Draw()


def makeNuiPlot(nuisDict,whichFit,histName="postFitNuisance",labelFunc=None):
    nNuis = len(nuisDict)
    hist = ROOT.TH1D(histName,"Nuisance parameters",nNuis,0,nNuis)
    iNuis = 1
    for nuisName,nuisTuple in nuisDict.iteritems():
        if whichFit == "postfit":
            nuisValue,nuisErr = nuisTuple
            hist.SetBinContent(iNuis,nuisValue)
            hist.SetBinError(iNuis,nuisErr)
        else:
            hist.SetBinContent(iNuis,0.)
            hist.SetBinError(iNuis,1.)
        hist.GetXaxis().SetBinLabel(iNuis,nuisName if not labelFunc else labelFunc(nuisName))
        iNuis += 1
    return hist

def plotNuiStyle(hist,color=ROOT.kBlue):
    hist.GetYaxis().SetTitle("#theta - #theta_{0}")
    hist.SetLineColor(color)
    hist.SetMarkerStyle(20)
    hist.SetMarkerSize(1.0)
    hist.SetLineWidth(2)
    hist.GetXaxis().LabelsOption("v")
    hist.SetMaximum(3.)
    hist.SetMinimum(-3.)
    #hist.SetStats(0)
    hist.SetMarkerColor(color)

def getNuiGraph(hist,shift):
    gr = ROOT.TGraphErrors()
    gr.SetName(hist.GetName())
    for i in range(hist.GetNbinsX()):
        x = hist.GetBinCenter(i+1)+shift
        y = hist.GetBinContent(i+1)
        e = hist.GetBinError(i+1)
        gr.SetPoint(i,x,y)
        gr.SetPointError(i,float(abs(shift))*0.1,e)
    return gr
