"""
집 n개 - 각 집 [ 빨 / 초 / 파 ]로 칠하는 비용?
이전 집과 다른 색깔이어야! 
"""
# tc는 잘 나오지만, 사이트에서 답은 틀렸습니다! 
# DP Q 같았지만, 완전탐색으로 풀어 보았습니다.

import sys
sys.stdin = open('1149.txt')


def dfs(n_idx, cur, money):  # 몇번째 집인지 / 지금 집 / 
    global ans

    if ans < money: return  # 가지치기) 최소 비용 구하는 Q이기 때문에 

    if n_idx == n:  # n개의 집 방문하면 ( 탈출조건 ) 
        ans = min(ans, money)  # 무조건 선택하며 dfs 들어가므로, 바로 ans 갱신 
        return

    # 완전탐색) 

    if n_idx == 0:  # 첫번째 집 : 선택지 3가지에 대해 모두 DFS
        for i in range(3):dfs(n_idx + 1, i, money + li[n_idx][i])

    elif n_idx >= 1:  # 이후의 집 : 이전 집의 색깔 제외하고 
        for i in range(3):
            if i != cur:
                dfs(n_idx + 1, i, money + li[n_idx][i])


n = int(input())
li = [list(map(int, input().split())) for _ in range(n)]
ans = float('inf')

dfs(0, 0, 0)
print(ans)
