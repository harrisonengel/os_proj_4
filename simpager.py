import pager

def main():
    refs = map(int, input().split())
    frames = int(input())
    #print("Page Referene String:\n",' '.join(map(str,refs)))
    #print("Number of Frames: ", str(frames))
    while(True):
        alg = input()
        fun = pager.getPageAlg(alg)
        faults = fun(refs, frames)
        print(alg, ": ", str(faults))
main()
