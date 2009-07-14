"""
@brief Event classes for Pass 6 reprocessing.  This version just copies
CTBClassLevel to EVENT_CLASS.
"""
#
# $Header$
#
from EventClassifier import EventClassifier

meritVariables = """
CTBClassLevel
""".split()

class Pass6ReprocessingClassifier(object):
    def __init__(self):
        pass
    def __call__(self, row):
        return row['CTBClassLevel']

eventClassifier = Pass6ReprocessingClassifier()

if __name__ == '__main__':
    rows = [{'CTBClassLevel' : 0}, 
            {'CTBClassLevel' : 1}, 
            {'CTBClassLevel' : 2},
            {'CTBClassLevel' : 3},
            {'CTBClassLevel' : 4}]
    classes = range(5)
    for row, id in zip(rows, classes):
        assert(id == eventClassifier(row))
