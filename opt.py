
def removeOptimal(arr, curQ, ind):
    occur = []
    pos = 0
    for i in range(ind+1, len(arr)):
        cur = arr[i]
        if arr[i] not in occur:
            if arr[i] in curQ:
                pos = curQ.index(arr[i])
                occur.append(arr[i])
    curQ.pop(pos)
        
def alg(refs, frames):
    q = []
    faults = 0
    for i in range(0,len(refs)):
        if refs[i] not in q:
            faults += 1
            if len(q) >= frames:
                removeOptimal(refs, q, i)
            q.append(refs[i])
    return faults
