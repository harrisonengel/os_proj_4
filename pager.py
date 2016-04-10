import fifo


def getPageAlg(alg):
    pageAlgs = {
    "FIFO" : fifo.fifo,
    "LRU" : print,
    "LFU" : print,
    "OPT" : print,
    "RAND" : print,
    "MFU" : print,
    "MRU" : print
    }
    return pageAlgs.get(alg)

