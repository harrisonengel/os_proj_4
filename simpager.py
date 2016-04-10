import pager

def main():
    refs = map(int, input().split())
    frames = int(input())
        
    while(True):
        alg = input()
        fun = pager.getPageAlg(alg)
        faults = fun(refs, frames)
        print(str(faults))
main()
