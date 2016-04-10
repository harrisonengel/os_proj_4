import random

def alg(refs, frames):
    random.seed()
    faults = 0
    q = []
    for i in refs:
        if i not in q:
            faults += 1
            if len(q) >= frames:
                q.pop(random.randint(0,frames - 1))
            q.append(i)
    return faults

