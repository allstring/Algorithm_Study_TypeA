"""
걷다보니 신천역 삼 (Large)  https://www.acmicpc.net/problem/14651
solve / 전형적인 메모이제이션 

dfs를 통해 10까지의 결과값을 본 후
해당 값들에서 점화식 찾아서 유도... 

0, 2, (이전 수 * 3) ... 

"""
import sys
sys.setrecursionlimit(100000)

def memo(i):
    global ans

    if i == 1:        return 0
    elif i == 2:        return 2
    else:
        if ans[i] == -1:
            ans[i] = memo(i-1) * 3

        return ans[i]


n = int(input())
ans = [-1] * (n + 1)
print(int(memo(n) % (10**9+9)))  # 문제에서 요구하는 대로 나머지를 구할 때에 (10**9+9)와의 나머지 구함 


