'''
https://www.acmicpc.net/problem/14712

모든 경우의 수를 구해서 탐색하기 -> 시간 초과
'''
import sys
import time
from itertools import combinations
def combi(n, r):
    if r > n:
        return 0
    if r == 0 or r == n:
        return 1
    r = min(r, n - r)
    upper = lower = 1
    for i in range(r):
        upper *= (n - i)
        lower *= (i + 1)
    return upper // lower

def chk_nemo():
    global temp
    for y in range(row-1):
        for x in range(col-1):
            if visited[y][x] and visited[y][x+1] and visited[y+1][x] and visited[y+1][x+1]:
                return
    temp += 1
    return
start = time.time()
sys.stdin = open('nemo_input.txt', 'r')
input = sys.stdin.readline
col, row = map(int, input().split())
total_box = col*row
nemo = []
for y in range(row):
    for x in range(col):
        nemo.append((x,y))

res = []
res.append(1)
res.append(combi(total_box, 1)) # 판에 1~3개 넣을 때는 넴모 생성 x
res.append(combi(total_box, 2))
res.append(combi(total_box, 3))
for color_cnt in range(4, total_box-3):
    temp = 0
    for combi_list in combinations(nemo, color_cnt):
        visited = [[False for _ in range(col)] for _ in range(row)]
        for dx, dy in combi_list:
            visited[dy][dx] = True
        chk_nemo()
    res.append(temp)
print(res)
print("time: ", time.time() - start)