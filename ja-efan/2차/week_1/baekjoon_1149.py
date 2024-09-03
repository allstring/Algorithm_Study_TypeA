# RGB거리
# Silver I

"""
풀이 설명 :
    이웃한 두 집의 색이 같아서는 안된다.

    i번째 집에서 r을 골랏을 때의 최소 비용
    -> i-1번째 집에서 g/b를 골랐을 때, 더 저렴한 경우 + i번째 집에서 r을 색칠
    => memo(i,r) = min(memo(i-1, g), memo(i-1, b))  + painting_cost(i, r)
    -> memo(a,c)는 a번째 집에서 c 색상을 골랐을 때 최소 비용을 저장하고 있다.
"""
def main():
    N = int(input())  # 집의 수
    painting_cost = [list(map(int, input().split())) for _ in range(N)]

    # 첫 번째 집은 무슨 색을 칠해도 최소 비용이다.
    # -> 이전 집이 없기 때문에 무슨 색을 칠해도 해당 색에 대한 최소 비용이다.
    memo = [painting_cost[0]]

    for i in range(1, N):
        # i번째 집에 R(0)을 칠하는 경우
        cost_r = min(memo[i - 1][1], memo[i - 1][2]) + painting_cost[i][0]
        # i번째 집에 G(1)을 칠하는 경우
        cost_g = min(memo[i - 1][0], memo[i - 1][2]) + painting_cost[i][1]
        # i번째 집에 B(2)을 칠하는 경우
        cost_b = min(memo[i - 1][0], memo[i - 1][1]) + painting_cost[i][2]
        memo.append([cost_r, cost_g, cost_b])

    print(min(memo[-1]))


if __name__ == "__main__":
    main()