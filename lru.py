
def alg(refs, frames):
    q = []
    faults = 0
    for i in refs:
        if i in q:
            q.pop(q.index(i))
            q.insert(0,i)
        else:
            faults += 1
            if len(q) >= frames:
                q.pop()
            q.insert(0,i)
    return faults



