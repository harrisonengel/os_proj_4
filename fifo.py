#############################
#
# FIFO Paging Algorithm
#
# Parameters:
# ----------------
# refs - The page reference numbers
# frames - The number of frames to use
#
# Local Variables:
# ----------------
# faults - Counts the number of faults
# q - Represents pages in memory
#
#############################
def alg(refs, frames):
    faults = 0
    q = []
    for i in refs:
        if i not in q:
            faults += 1
            if len(q) >= frames:
                q.pop(0)
            q.append(i)
    return faults


