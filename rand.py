import random

def alg(refs, frames):
    random.seed()
    faults = 0
    q = []
    for i in refs:
        if len(q) >= frames:
            faults += 1
            q.pop(random.randint(0,frames - 1))
        q.append(i)
    return faults

