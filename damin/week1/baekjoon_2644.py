'''
주어진 두 사람(a, b)이 몇 촌 관계인지 알아보기 -> bfs
a에서부터 시작해서 b에서 끝
b는 a기준 위쪽에 있을 수도 있고 아래 쪽에 있을 수도 있으니 a의 부모 & 자식 둘 다 탐색
visited로 몇 촌 관계인지 기록
탐색하면서 b에 도달하면 종료
'''

from collections import deque
import sys

def bfs(a, b):
    #a는 부모일수도 자식일수도 있음
    q = deque()
    for key in cousin_list: #a의 부모님 찾기
        if a in cousin_list[key]:
            q.append(key)
            visited[key] = 1
    if a in cousin_list: #a의 자식 찾기
        for i in cousin_list[a]:
            visited[i] = 1
            q.append(i)
    
    while q:
        now = q.popleft()
        for key in cousin_list: # 부모 찾기
            if now in cousin_list[key] and visited[key] == -1:
                visited[key] = visited[now] + 1
                if key == b:
                    return
                else:
                    q.append(key)
        
        if now in cousin_list: #자식 찾기
            for atom in cousin_list[now]:
                if visited[atom] == -1:
                    visited[atom] = visited[now] + 1
                    q.append(atom)


input = sys.stdin.readline
n = int(input())
a, b = map(int, input().split())
relation_cnt = int(input())
visited = [-1 for _ in range(101)]
cousin_list = {}
for i in range(relation_cnt): #가족 구조 만들기 {부모 : {자식1, 자식2, 자식3} ...}
    parent, kid = map(int, input().split())
    if parent in cousin_list:
        cousin_list[parent].add(kid)
    else:
        cousin_list[parent] = {kid}
res = bfs(a, b)

print(visited[b])