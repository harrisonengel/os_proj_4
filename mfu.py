#########################
#
# Most Frequently Used
#
########################

import sys

def alg(refs, frames):
    freq = dict(zip(refs, [0]*(len(refs) -1) ))
    q = []
    faults = 0
    for i in refs:
        freq[i] = freq[i] + 1
        if i not in q:
            faults += 1
            if len(q) >= frames:
                most = 0
                maxElt = 0
                for j in q: #loop through q to find elt with the maximum frequency count
                    if most < freq[j]:
                        most = freq[j]
                        maxElt = q.index(j)
                q[maxElt] = i
            else:
                q.append(i)
    return faults


