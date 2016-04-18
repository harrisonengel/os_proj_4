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
                least = sys.maxsize
                minElt = 0
                for j in q:
                    if least > freq[j]:
                        least = freq[j]
                        minElt = j
                q.pop(q.index(minElt))
            q.append(i)
    return faults

            

