import ROOT,math

def getIntegral(hist):
    error = ROOT.Double(0.)
    integral = hist.IntegralAndError(
            0,
            hist.GetNbinsX()+1,
            #1,
            #hist.GetNbinsX(),
            error,
            )
    return integral,error

def getCountAndError(hist,central,width,isSR=True):
    lower_value = central-width
    upper_value = central+width

    if isSR:
        error = ROOT.Double(0.)
        integral = hist.IntegralAndError(
                hist.GetXaxis().FindFixBin(lower_value),
                hist.GetXaxis().FindFixBin(upper_value),
                error,
                )
    else:
        error1 = ROOT.Double(0.)
        integral1 = hist.IntegralAndError(
                0,
                hist.GetXaxis().FindFixBin(lower_value)-1,
                error1,
                )
        error2 = ROOT.Double(0.)
        integral2 = hist.IntegralAndError(
                hist.GetXaxis().FindFixBin(upper_value)+1,
                hist.GetNbinsX()+1,
                error2,
                )
        integral = integral1+integral2
        error = math.sqrt(error1**2+error2**2)
    return integral,error

def removeOverflow(h):
    if h.GetBinContent(h.GetNbinsX()+1):
        h.SetBinContent(h.GetNbinsX(),h.GetBinContent(h.GetNbinsX())+h.GetBinContent(h.GetNbinsX()+1))
        h.SetBinError(h.GetNbinsX(),math.sqrt(h.GetBinError(h.GetNbinsX())**2+h.GetBinError(h.GetNbinsX()+1)**2))
