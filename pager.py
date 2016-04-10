import fifo
import lru
import lfu
import opt
import rand
import mfu
import mru

def getPageAlg(alg):
    pageAlgs = {
    "FIFO" : fifo.alg,
    "LRU" : lru.alg,
    "LFU" : lfu.alg,
    "OPT" : opt.alg,
    "RAND" : rand.alg,
    "MFU" : mfu.alg,
    "MRU" : mru.alg
    }
    return pageAlgs.get(alg)

