"""
@brief P6_V3 event classes + Pass6 dataclean

See 

https://confluence.slac.stanford.edu/display/DC2/Summary+of+response+function+sets

and 

https://confluence.slac.stanford.edu/display/SCIGRPS/Data+selection+for+the+extra-galactic+diffuse+analysis

These definitions partition the events into 4 classes (Transient,
Source, Diffuse, dataclean) and sets EVENT_CLASS to -1 if the event is
not classified.
"""
#
# $Header$
#
from EventClassifier import EventClassifier
from math import *


meritVariables = """
CTBCORE
CTBBestEnergyProb
CTBBestEnergy
CTBBestEnergyRatio
CTBClassLevel
CalTrSizeTkrT100
CTBBestLogEnergy
CTBAllProb
AcdCornerDoca
Tkr1FirstLayer
Tkr1ToTAve
CalTrSizeCalT100
""".split()

class DataCleanClassifier(EventClassifier):
    def __init__(self, eventClassCuts):
        EventClassifier.__init__(self, eventClassCuts)
        self.nclass = len(self.event_classes)
    def __call__(self, row):
        for key in row:
            exec("%s = row['%s']" % (key, key))
        for i, cut in zip(range(1,self.nclass+1,1), self.event_classes):
            if eval(cut):
                return 5-i
        return -1

eventClassCuts = [
    "&&".join((
    "(CTBCORE>0.1 && ((Tkr1ToTAve<(4.5+1.*max(CTBBestLogEnergy-3,0)))))",
    "((CalTrSizeCalT100>(15-5*max(3.5-CTBBestLogEnergy,0))))",
    "((CalTrSizeTkrT100<(32+80*max(4-CTBBestLogEnergy,0)**4)))",
    "((CTBAllProb>(0.94*(1-exp(-0.0023*(CTBBestEnergy+450.)))*(CTBBestLogEnergy>2.7))))",
    "((abs(AcdCornerDoca)>(180.-200.*max(CTBBestLogEnergy-2.7,0))))",
    "(CTBCORE>0.1 && CTBBestEnergyProb>0.1 && CTBBestEnergy>10 && CTBBestEnergyRatio<5 && CTBClassLevel>2)")),
                  "CTBCORE>0.1 && CTBBestEnergyProb>0.1 && CTBBestEnergy>10 && CTBBestEnergyRatio<5 && CTBClassLevel>2",
                  "CTBCORE>0.1 && CTBBestEnergyProb>0.1 && CTBBestEnergy>10 && CTBBestEnergyRatio<5 && CTBClassLevel>1",
                  "CTBCORE>0. && CTBBestEnergyProb>0. && CTBBestEnergy>10 && CTBBestEnergyRatio<5 && CTBClassLevel>0"]




#eventClassCuts.reverse()

eventClassifier = DataCleanClassifier(eventClassCuts)
