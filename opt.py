import copy
        
def alg(refs, frames):
    crefs = copy.deepcopy(refs) #copy of page references
    q = []
    faults = 0
    for i in refs:
        crefs.pop(0)
        if i not in q:
            faults += 1
            if len(q) >= frames:

                optDist = 0 # Distance of optimal element to remove (farthest)
                rem = 0 # Index in q of the optimal element to remove
                for j in q: 
                    if j in crefs:
                        if crefs.index(j) > optDist:
                            optDist = crefs.index(j)
                            rem = q.index(j)
                    else:
                        rem = q.index(j)
                        break
                q.pop(rem)
            q.append(i)
    return faults


