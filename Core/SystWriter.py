from collections import OrderedDict

class SystWriter(object):
    def makeMCSystLine(self,binList):
        outputStr = ""
        systDict = OrderedDict()
        for analysisBin in binList:
            for syst in analysisBin.systList:
                if syst.name not in systDict:
                    systDict[syst.name] = syst
        for systName in systDict:
            for analysisBin in binList:
                systematics = analysisBin.systList
                foundSyst = False
                for systematic in systematics:
                    if systematic.name == systName:
                        foundSyst = True
                        break
                processList = analysisBin.processList
                if systematic.skipDC: continue
                if foundSyst:
                    outputStr += self.makelnNLine(systematic,processList,analysisBin,lineExist=systName in outputStr,forceDash=False)
                else:
                    outputStr += self.makelnNLine(systDict[systName],processList,analysisBin,lineExist=systName in outputStr,forceDash=True)
            outputStr +="\n"
        return outputStr

    @staticmethod
    def makelnNLine(systematic,processList,analysisBin,lineExist=False,forceDash=False,writeNameOnly=False):
        outputStr = ""
        if not lineExist:
            systName = systematic.getSystName() if not systematic.correlation else systematic.correlation(systematic.systNamePrefix,systematic,analysisBin,"",whichType="card")
            outputStr += systName+"\tlnN\t"
        correlationStr = ""
        if not writeNameOnly:
            for eachProcess in processList:
                if systematic.processFunc:
                    processFuncBool = systematic.processFunc(eachProcess)
                else:
                    processFuncBool = False
                if (eachProcess.name not in systematic.process and not processFuncBool) or forceDash:
                    correlationStr += "-\t"
                elif systematic.magnitude:
                    correlationStr += "%s\t"%systematic.magnitude
                elif systematic.magnitudeFunc:
                    if eachProcess.name in systematic.process:
                        correlationStr += "%s\t"%systematic.magnitudeFunc(systematic,eachProcess.name,analysisBin)
                    elif processFuncBool:
                        correlationStr += "%s\t"%systematic.magnitudeFunc(systematic,systematic.processFunc(eachProcess),analysisBin)
            outputStr += correlationStr
        #outputStr +="\n"
        return outputStr
