# 2644. 촌수 계산

import sys
sys.stdin = open('input.txt', 'r')

def dfs(r_x, r_y, count):
    global result
    # 방문 여부 처리
    visited[r_x] = 1
    
    # 만약 두 사람의 번호가 만나면, 촌수를 결과 리스트에 추가
    if r_x == r_y:
        result = count
    
    # 촌수 계산 대상의 자식들
    for i in graph[r_x]:
        # 만약 방문한 적이 없다면, dfs 실행
        if not visited[i]:
            # dfs 실행 시 촌수 + 1
            dfs(i, r_y, count + 1)

T = int(input())

for _ in range(T):
    # n: 전체 사람의 수
    n = int(input())
    # r_x, r_y: 촌수를 계산해야 하는 서로 다른 두 사람의 번호
    r_x, r_y = map(int, input().split())
    # m: 부모 자식들 간의 관계의 개수
    m = int(input())
    # graph: 부모-자식 관계 리스트
    graph = [[] for _ in range(n+1)]
    # visited: 방문 여부 리스트
    visited = [0] * (n+1)

    # 입력 요소들을 받아서 부모-자식 관계 리스트에 저장
    for i in range(m):
        x, y = map(int, input().split())
        graph[x].append(y)
        graph[y].append(x)

    # result: 결과를 저장할 리스트
    result = 0

    # r_x와 r_y의 촌수 계산을 위해 dfs 실행
    dfs(r_x, r_y, 0)

    # 만약 촌수 계산 결과가 없다면, -1
    if result == 0:
        print(-1)
    else:
        print(result)


''' 실패한 풀이 : 서로소 집합 활용 -> 마지막 촌수 계산 실패
def find_set(x):
    if x != p[x]:
        p[x] = find_set(p[x])
    return p[x]

T = int(input())

for _ in range(T):
    # n: 전체 사람의 수
    n = int(input())
    # r_x, r_y: 촌수를 계산해야 하는 서로 다른 두 사람의 번호
    r_x, r_y = map(int, input().split())
    # m: 부모 자식들 간의 관계의 개수
    m = int(input())
    # p: 부모 자식 리스트 (base: 자기 자신이 부모)
    p = list(range(n+1))
    # rank: 각 촌수의 depth를 계산
    rank = [0] * (n+1)

    # x, y를 입력받아 y의 부모를 x로 설정
    for _ in range(m):
        x, y = map(int, input().split())
        p[y] = x
        rank[x] = max(rank[y], rank[x]) + 1

    # px, py: r_x와 r_y의 대표자
    px = find_set(r_x)
    py = find_set(r_y)

    # 만약 대표자가 다르다면, 서로 촌수를 계산할 수 없으므로 -1 반환
    if px != py:
        result = -1
    # 만약 대표자가 같다면, 서로 촌수를 계산
    else:
    
    print(result)
'''



