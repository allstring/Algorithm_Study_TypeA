import sys
input = sys.stdin.readline
sys.setrecursionlimit(2*10**5)

def recursive(workList, index, didIt):
    if index in didIt: return 0
    didIt.add(index)
    tmpAnswer = 1
    for work in workList.get(index, []):
        if(work in didIt): continue
        tmpAnswer += recursive(workList, work, didIt)
    return tmpAnswer

def main():
    N, M  = map(int, input().split())
    workList = {}
    
    for _ in range(M):
        A, B = map(int, input().split())
        try:
            workList[B].append(A)
        except KeyError:
            workList[B] = [A]
    X = int(input())
    didIt = set()
    print(recursive(workList, X, didIt)-1)

if __name__ == "__main__":
    main()