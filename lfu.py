#################################
#
# Least Frequently Used Algorithm
#
# Parameters
# ----------
# refs - List of page frame refrences
# frames - Number of frames to model
#
# Local Variables
# ---------------
# freq - Dictionary to keep track of freqencies of each page
# faults - Counts the number of faults
# q - Represents pages currently in memory
# least - Keeps track for least freqent element
# minElt - Keeps track least frequent elemnt index
#
##################################

import sys

def alg(refs, frames):
    freq = dict(zip(refs, [0]*len(refs)))
    q = []
    faults = 0
    for i in refs:
        freq[i] = freq[i] + 1
        if i not in q:
            faults += 1
            if len(q) >= frames:
                least = sys.maxsize
                minElt = 0
                for j in q:
                    if least > freq[j]:
                        least = freq[j]
                        minElt = q.index(j)
                q.pop(minElt)
            q.append(i)
    return faults

            

