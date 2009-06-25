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
# Electrons and positrons. See
# https://confluence.slac.stanford.edu/display/SCIGRPS/CTBClassLevel+Definition+for+P7
#

class ElectronClassifier(object):
    def __init__(self):
        pass
    def __call__(self, row):
        return row['FT1EventClass']

eventClassifier = ElectronClassifier()

if __name__ == '__main__':
    rows = [{'FT1EventClass' : 1}, 
            {'FT1EventClass' : 2}]
    classes = (1, 2)
    for row, id in zip(rows, classes):
        assert(id == eventClassifier(row))
