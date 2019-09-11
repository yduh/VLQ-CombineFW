import ROOT,array

xsec = {}

xsec['TT_M700']   = 0.455 # from https://twiki.cern.ch/twiki/bin/view/CMS/B2GMonteCarlo
xsec['TT_M800']  = 0.196 # from https://twiki.cern.ch/twiki/bin/view/CMS/B2GMonteCarlo
xsec['TT_M900']   = 0.0903 # from https://twiki.cern.ch/twiki/bin/view/CMS/B2GMonteCarlo
xsec['TT_M1000']  = 0.0440 # from https://twiki.cern.ch/twiki/bin/view/CMS/B2GMonteCarlo
xsec['TT_M1100']  = 0.0224 # from https://twiki.cern.ch/twiki/bin/view/CMS/B2GMonteCarlo
xsec['TT_M1200'] = 0.0118 # from https://twiki.cern.ch/twiki/bin/view/CMS/B2GMonteCarlo
xsec['TT_M1300']  = 0.00639 # from https://twiki.cern.ch/twiki/bin/view/CMS/B2GMonteCarlo
xsec['TT_M1400'] = 0.00354 # from https://twiki.cern.ch/twiki/bin/view/CMS/B2GMonteCarlo
xsec['TT_M1500']  = 0.00200 # from https://twiki.cern.ch/twiki/bin/view/CMS/B2GMonteCarlo
xsec['TT_M1600'] = 0.001148 # from https://twiki.cern.ch/twiki/bin/view/CMS/B2GMonteCarlo
xsec['TT_M1700']  = 0.000666 # from https://twiki.cern.ch/twiki/bin/view/CMS/B2GMonteCarlo
xsec['TT_M1800'] = 0.000391 # from https://twiki.cern.ch/twiki/bin/view/CMS/B2GMonteCarlo

def make_graph(xsec_dict,prefix,selFunc=lambda x: True):
    x_points = [ float(name.split("_")[1][1:]) for name in xsec_dict if name.startswith(prefix) if selFunc(float(name.split("_")[1][1:])) ]
    x_points.sort()
    x_array = array.array('d',x_points)
    y_array = array.array('d',[xsec[prefix+"_M"+str(int(x))] for x in x_points])
    gr = ROOT.TGraph(len(x_points),x_array,y_array)
    return gr

xsec_graph = { prefix: make_graph(xsec,prefix) for prefix in ["TT",] }
