import sys
sys.setrecursionlimit(100000) # 재귀 깊이 제한 늘리기

def find_set(a):
    if vertice[a] != a:
        vertice[a] = find_set(vertice[a])
        return vertice[a]
    return a

def union(a, b):
    a = find_set(a)
    b = find_set(b)

    if a < b:
        vertice[b] = a
    else:
        vertice[a] = b

input = sys.stdin.readline
computer = int(input())
input_cnt = int(input())
vertice = [i for i in range(computer+1)]
edge = [list(map(int, input().split())) for _ in range(input_cnt)]
edge.sort(key=lambda x: x[2]) # 가중치 오름차순 정렬
res = 0
for a, b, weight in edge:
    if find_set(a) != find_set(b): #사이클 확인
        union(a, b)
        res += weight
print(res)