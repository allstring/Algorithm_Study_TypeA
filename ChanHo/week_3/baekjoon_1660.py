"""
캡틴 이다솜 https://www.acmicpc.net/problem/1660
try
"""
import sys
sys.setrecursionlimit(100000)
from itertools import combinations_with_replacement


def dfs(i):
    if i == 1:return 1
    else:
        if triangle[i] == 0:
            triangle[i] = dfs(i-1) + triangle[i-1]   # 각 사면체의 층에 해당하는 삼각형의 크기 저장 
            fourth[i] = fourth[i-1] + triangle[i-1]  # 각 사면체의 전체 크기를 저장 
        return i


n = int(input())
triangle, fourth = [0] * (n+1), [0] * (n+1)

dfs(n)

# print(triangle)
# print(fourth)  # 3번째부터 하여 각 사면체의 크기 위치. 이들을 중복조합을 통해 ret의 최소값 구하기 

flag = 0
if n == 1: print(1)
elif n == 2: print(2)
else:
    ret = float('inf')
    use = fourth[3:]

    # use 에 대한 중복조합 -> ret 최소값 update
    for q in range(1, n):  # 원소를 1개부터 n개까지 확인 
        chk = combinations_with_replacement(use, q)  # q개에 대한 중복조합 확인
        for c in chk:  # 각 중복조합에서 n과 일치하는 sum의 값이 나올 시, 
            if sum(c) == n:
                flag = 1  
                
                # 사면체 개수 ( 최소값에 대한 조건은 for를 작은 것부터 올라가므로 이미 고려되어 있음 ) 출력 후 탈출
                print(q)

                break

        if flag == 1:break
