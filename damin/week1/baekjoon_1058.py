'''
2-친구
: 둘이 친구거나 혹은 둘 모두와 친구인 사람이 있을 때
1. 둘이 친구인 경우
-> input에 주어짐
2. 둘과 친구인 사람이 있는 경우
-> 둘 사이의 중간 경로가 될 수 있으니 bfs로 구함
친구를 중복으로 셀 수 있으니 친구 여부 기록
'''



from collections import deque
import sys

def friend(a):
    global chk_list
    friend_cnt = 0
    q = deque()

    for i in range(n):
        if i == a: continue
        if friend_list[a][i] == 'Y': #직접적으로 친구
            chk_list[a][i] = 1 #친구 표시
            friend_cnt += 1
            q.append(i) #간접적으로 친구 구하기
    
    while q:
        now = q.popleft()
        for i in range(n):
            # 둘이 친구 & a - b - a 형태로 사이클 만들지 않고 & 직접적으로 친구가 아니면
            if i != a and friend_list[now][i] == 'Y' and chk_list[a][i] == -1:
                chk_list[a][i] = 1 #친구 표시
                friend_cnt += 1
    return friend_cnt

input = sys.stdin.readline
n = int(input())
friend_list = [input() for _ in range(n)]
chk_list = [[-1 for _ in range(n)] for _ in range(n)]
res = 0

for i in range(n):
    temp = friend(i)
    res = max(res, temp)

print(res)