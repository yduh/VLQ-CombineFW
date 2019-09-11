def BrTpTpFromBrTp(brTZ=1./3.,brTH=1./3.,brBW=1./3.):
    brDict = {}
    brDict["BW-BW"] = brBW**2
    brDict["TZ-TZ"] = brTZ**2
    brDict["TH-TH"] = brTH**2
    brDict["TH-BW"] = brTH*brBW*2
    brDict["TZ-BW"] = brTZ*brBW*2
    brDict["TZ-TH"] = brTZ*brTH*2
    return brDict
