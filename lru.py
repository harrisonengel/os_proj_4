################################
#
#   Least Recently Used algorithm
#
# Parameters
# ----------
# refs - A list of page references
# frames - The max number of frames to model
#
# Local Variables
# ---------------
# faults - Counts the number of faults
# q - Keeps track of frames in memory
#
################################
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



