
def alg(refs, frames):
    faults = 0
    q = []
    print(str(len(refs)))
    for i in refs:
        if i not in q:
            faults += 1
            if len(q) >= frames:
                q.pop(0)
            q.append(i)
    return faults


