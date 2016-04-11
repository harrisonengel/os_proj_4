import sys

def alg(refs, frames):
    freq = dict(zip(refs, [0]*len(refs)))
    q = []
    faults = 0
    for i in refs:
        freq[i] += 1
        if i not in q:
            faults += 1
            if len(q) >= frames:
                most= 0
                maxElt = 0
                for j in q:
                    if most < freq[j]:
                        most = freq[j]
                        maxElt = j
                q.pop(q.index(maxElt))
            q.append(i)
    return faults


