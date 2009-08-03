"""
@brief Pass 6 event classes.  See
http://www-glast.stanford.edu/protected/mail/irf/0157.html

These definitions partition the events into three classes.
"""
#
# $Header$
#
from EventClassifier import EventClassifier

meritVariables = """
CTBClassLevel
CTBCORE
CTBBestEnergyProb
Tkr1FirstLayer
""".split()

#
# Note that the prefilter cuts applied by ROOT (the TCuts par file
# option), should contain the cuts that are common to all event
# classes.
#
eventClassCuts = ["(CTBClassLevel==0)", 
                  "(CTBClassLevel==1) || ((CTBCORE<=0.1) || (CTBBestEnergyProb<=0.1))",
                  "(CTBClassLevel==2) && (CTBCORE>0.1) && (CTBBestEnergyProb>0.1)",
                  "(CTBClassLevel==3) && (CTBCORE>0.1) && (CTBBestEnergyProb>0.1)"]

eventClassifier = EventClassifier(eventClassCuts)

if __name__ == '__main__':
    rows = [{'CTBClassLevel' : 1},
            {'CTBClassLevel' : 2,
             'CTBCORE' : 0.05,
             'CTBBestEnergyProb' : 0.05},
            {'CTBClassLevel' : 3,
             'CTBCORE' : 0.05,
             'CTBBestEnergyProb' : 0.11},
            {'CTBClassLevel' : 2,
             'CTBCORE' : 0.11,
             'CTBBestEnergyProb' : 0.11},
            {'CTBClassLevel' : 3,
             'CTBCORE' : 0.11,
             'CTBBestEnergyProb' : 0.11}]
    classes = (1, 1, 1, 2, 3)

    for row, id in zip(rows, classes):
        assert(id == eventClassifier(row))
