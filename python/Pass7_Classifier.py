"""
@brief Pass 7 event classes.  See
http://www-glast.stanford.edu/protected/mail/irf/0157.html
and
https://confluence.slac.stanford.edu/display/SCIGRPS/CTBClassLevel+Definition+for+P7

These definitions partition the events into three classes.
"""
#
# $Header$
#
from EventClassifier import EventClassifier

meritVariables = """
FT1EventClass
""".split()

#
# Note that the prefilter cuts applied by ROOT (the TCuts par file
# option), should contain the cuts that are common to all event
# classes.
#

#
# Event classes in P7 will simply be a direct mapping from the Ft1EventClass
# variable in merit.  These values will be integers from 1 to 9.  See
# https://confluence.slac.stanford.edu/display/SCIGRPS/CTBClassLevel+Definition+for+P7
#
eventClassCuts = ["FT1EventClass == %i" % i for i in range(0, 9)]

eventClassifier = EventClassifier(eventClassCuts)

if __name__ == '__main__':
    rows = [{'FT1EventClass' : 1}, 
            {'FT1EventClass' : 2}]
    classes = (1, 2)
    for row, id in zip(rows, classes):
        assert(id == eventClassifier(row))
