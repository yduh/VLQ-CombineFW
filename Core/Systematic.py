class Systematic(object):
    def __init__(self,name,process,correlation=None,factor=1.,systNamePrefix=""):
        self.name = name
        self.process = process
        self.correlation = correlation
        self.systNamePrefix = systNamePrefix
        self.factor= factor
        self.skipDC= False
        self.forceSymmetric = False
        self.forceNormalization = False

    def getSystName(self):
        return self.name

class lnNSystematic(Systematic):
    def __init__(self,name,process,magnitudeFunc=None,correlation=None,factor=1.,systNamePrefix="",magnitude=None,processFunc=None):
        super(lnNSystematic,self).__init__(name,process,correlation=correlation,factor=factor,systNamePrefix=systNamePrefix)
        self.systType = "lnN"
        self.name = name
        self.process = process
        self.magnitudeFunc = magnitudeFunc
        self.magnitude = magnitude
        self.correlation = correlation
        self.processFunc = processFunc

class ShapeSystematic(Systematic):
    def __init__(self,name,process,magnitudeFunc=None,correlation=None,factor=1.,systNamePrefix="",):
        super(ShapeSystematic,self).__init__(name,process,correlation=correlation,factor=factor,systNamePrefix=systNamePrefix,)
        self.systType = "shape"
        self.magnitudeFunc = magnitudeFunc
