# 1058. 친구

import sys
sys.stdin = open('input.txt', 'r')

def floyd_warshall(N, arr, friends):
    for k in range(N):
        for i in range(N):
            for j in range(N):
                # 자기 자신의 경우에는 continue
                if i == j: continue
                # i와 j가 친구이거나, 다른 친구를 경유해서 친구인 경우 2-친구 관계로 설정
                if arr[i][j] == 'Y' or (arr[i][k] == 'Y' and arr[k][j] == 'Y'):
                    friends[i][j] = 1
    return friends

T = int(input())

for _ in range(T):
    # N: 사람의 수
    N = int(input())
    # arr: 친구 관계 리스트
    arr = [list(input()) for _ in range(N)]
    # friends: 2-친구 관계 리스트
    friends = [[0] * N for _ in range(N)]

    friends_list = floyd_warshall(N, arr, friends)

    result = 0
    # 각 행별 합 = 각 사람들의 2-친구의 수 이므로 최댓값을 출력
    for row in friends_list:
        result = max(result, sum(row))

    print(result)





                