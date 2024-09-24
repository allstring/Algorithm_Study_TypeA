"""
그대, 그머가 되어  https://www.acmicpc.net/problem/14496
try
논리 자체는 맞는 것 같은데, 메모리 초과가 떠서, maps를 2차원 list가 아닌 다른 방식으로 진행해야 할듯 ... 
"""
from collections import deque


def bfs():
    depth = 1
    queue, temp_queue = deque(), deque()

    for i in range(n):
        if maps[a][i] == 1:  queue.append(i)  # 시작점에서 붙어있는 edge로 뻗기 위해 초기 queue에 append 

    while 1:  # 토마토 느낌으로, 한번 queue를 돌릴떄마다 갱신

        if b in queue:return depth  # 연결되어 있는 vertex 중, b가 있다면 최소거리 depth return

        while queue:  # 보고있는 점에서 연결되어 있는 edge들 모두 순회 
            target = queue.popleft()  # target에 연결된 edge 확인
            visited[target] = True    # 방문한 target은 방문했다고 표시 
            for i in range(n):        # target에 연결되어 있는 vertex 중 갈수있는데 있는지 확인
                if maps[target][i] == 1 and visited[i] == False:  # 안가봤는데 갈 수 있다?
                    temp_queue.append(i)                          # 다음 회차에 갈거니까 temp_queue에 붙

        depth += 1  # 한번 더 들어가니까, depth를 + 1 

        queue = temp_queue  # queue를 갱신 
        temp_queue = deque()  # 임시 덱 초기화

        if not queue:return -1  # 방문할 요소가 없다면 ( 모든걸 다 돌았는데 b를 못갔을 때에 ) return -1 


a, b = map(int, input().split())  # a를 b로 바꾸려 한다 
n, m = map(int, input().split())  # n개의 문자, 치환 가능한 문자쌍 m개
li = [list(map(int, input().split())) for _ in range(m)]  # 치환하는 문자쌍을 받음. 

maps = [[0] * n for _ in range(n)]

for l in li:  # 갈 수 있는 모든 요소들 maps에 1로 표시 
    maps[l[0]-1][l[1]-1] = 1
    maps[l[1]-1][l[0]-1] = 1  # 양방향인데, 한방향만의 data를 주기 때문에, 반대로도 

a -= 1  # a, b가 @번째 값이기 때문에, idx로 치환 위해 1씩 빼준다. 
b -= 1

visited = [False] * n  # 방문한 문자는 보지 않겠다. bfs니까 최단거리를 볼 수 있음 
visited[a] = True

print(bfs())