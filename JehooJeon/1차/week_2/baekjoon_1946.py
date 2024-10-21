# 1946. 신입사원

import sys
sys.stdin = open("input.txt", "r")

T = int(input())

for _ in range(T):
    # N: 지원자의 숫자(1 <= N <= 100,000)
    N = int(input())
    # arr: 지원자들의 면접 성적 입력할 리스트(서류심사 성적 : 인덱스 + 1)
    arr = [0] * N

    # 지원자들의 면접 성적 입력
    for _ in range(N):
        i, j = map(int, input().split())
        arr[i-1] = j

    # 서류심사 1등의 면접 성적을 max_score로 정의
    max_score = arr[0]
    # result: 선발할 수 있는 신입사원의 수
    # 서류심사 1등은 무조건 선발하므로 1로 시작
    result = 1

    for i in range(1, N):
        # 만약 다음 서류심사 등수가 면접 성적이 더 높으면 선발
        if arr[i] < max_score:
            result += 1
            # max_score를 선발된 인원의 면접 성적으로 갱신
            max_score = arr[i]

    print(result)


''' 지원자의 숫자 많아지면 시간복잡도 O(N^2)으로 기하급수적으로 올라감 -> 결과: 시간 초과
T = int(input())

for _ in range(T):
    # N: 지원자의 숫자(1 <= N <= 100,000)
    N = int(input())
    # scores: 지원자의 서류심사 성적, 면접 성적의 순위
    scores = [list(map(int, input().split())) for _ in range(N)]
    
    # 서류심사 순서대로 정렬
    scores.sort()
    # 선발할 수 있는 최대 인원수 변수 정의
    result = 0

    for i in range(N):
        # 서류심사 1등의 경우에는 무조건 선발
        if i == 0:
            result += 1
            continue

        # 서류심사 1등 외에는 더 높은 서류심사 성적인 인원들보다 면접 성적 낮으면 탈락
        cnt = 0
        for j in range(i):
            if scores[i][1] > scores[j][1]:
                cnt += 1
        if cnt > 0:
            continue

        # 면접 성적이 높으므로 선발
        result += 1

    print(result)
'''