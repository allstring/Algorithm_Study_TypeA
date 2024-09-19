import sys
from collections import defaultdict, deque
'''
치환의 최소 횟수 -> 최소 거리 (BFS)
따라서 최소 횟수는 visited로 체크
'''
input = sys.stdin.readline
a, b = map(int, input().split()) # 현재 문자, 바꾸고 싶은 문자
n, m = map(int, input().split()) # 전체 문자의 수, 치환 가능한 문자쌍의 수
switch_graph = defaultdict(set)

for _ in range(m): #그래프 생성 a->b b->a가 가능하니까 양방향 그래프
    i, j = map(int, input().split())
    switch_graph[i].add(j)
    switch_graph[j].add(i)

if a == b: #현재 문자가 바꾸고 싶은 문자와 같으면 치환할 필요가 없음
    print(0)
else:
    visited = [0] * (n+1)
    q = deque()
    q.append(a)
    while q:
        now = q.popleft()
        for val in switch_graph[now]: #치환 가능하면
            if visited[val] == 0: # 해당 방식으로 치환했는지 확인
                q.append(val)
                visited[val] = visited[now] + 1 # 지금까지 치환한 횟수 + 1

    if visited[b] == 0: # 바꾸고 싶은 문자에 방문하지 못했다는 건 치환을 해도 그 문자가 되지 못한 것
        print(-1)
    else:
        print(visited[b]) #그 외는 치환 횟수 출력