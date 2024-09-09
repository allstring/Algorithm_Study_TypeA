import sys
from queue import PriorityQueue
import math
'''
센티의 키가 커질 때까지 계속 돌리기
'''
input = sys.stdin.readline
n, centi_height, hammer_limit = map(int, input().split())
pq = PriorityQueue()

for _ in range(n):
    pq.put(-int(input())) #우선순위 큐는 오름차순으로 배열되니 내림차순으로 쓰기 위해 음수로 변경

res = -1

for i in range(hammer_limit):
    top_height = -pq.get() #제일 키 큰 거인

    if top_height < centi_height: #센티보다 키가 작으면
        res = i
        pq.put(-top_height)
        break

    if top_height == 1: #제일 키가 큰 거인의 키가 1이면 더이상 계산 x
        pq.put(-top_height)
        break

    pq.put(-math.floor(top_height / 2))

height = -pq.get()

if res == -1:
    if height < centi_height:
        print(f"YES\n{hammer_limit}")
    else:
        print(f"NO\n{height}")
else:
    print(f"YES\n{res}")
