import pager

def main():
    refStr = input() 
    frames = int(input())
    print("Page Referene String:\n", refStr)
    print("Number of Frames: ", str(frames))
    refs = list(map(int, refStr.split()))
    while(True):
        alg = input()
        fun = pager.getPageAlg(alg)
        faults = fun(refs, frames)
        print(alg, ": ", str(faults))
main()
