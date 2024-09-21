from collections import deque

def bfs(start, end, arr):
    distances[start] = 0
    queue = deque([start])
    
    while queue:
        current = queue.popleft()
        
        if current == end: # 목표 숫자 찾음
            return distances[current]
        
        for connect in arr[current]: # current에서 연결된 정점 탐색
            if distances[connect] == -1:
                distances[connect] = distances[current] + 1
                queue.append(connect)
    
    return -1 # 목표 단어에 도달 X

a, b = map(int, input().split())
n, m = map(int, input().split())

arr = [[] for _ in range(n + 1)]
distances = [-1] * (n + 1)

for _ in range(m):
    x, y = map(int, input().split())
    arr[x].append(y)
    arr[y].append(x)

answ = bfs(a, b, arr)
print(answ)