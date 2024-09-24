"""
동전 2 https://www.acmicpc.net/problem/2294
try
"""
def dfs(current_money, many):  # 현재 가지고 있는 돈 / 이용한 동전의 개수 
    global ans
    if current_money == k:  # 만들어야 하는 금액에 도달? 최소 개수인지 갱신 
        ans = min(ans, many)
        return

    for v in value:  # 가능한 모든 동전의 경우의 수 체크 
        if current_money + v > k: continue  # k 넘어가면 무시 
        if many + 1 > ans:continue          # ans 넘어가면 무시 
        dfs(current_money + v, many + 1)    # dfs 

    return


n, k = map(int, input().split())
value = [(int(input())) for _ in range(n)]
value = sorted(value, reverse=True)  # 큰거부터 check...? 

ans = float('inf')
dfs(0, 0)
if ans == float('inf'): print(-1)
else:print(ans)