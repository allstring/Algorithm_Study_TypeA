import heapq


def check(li):  # 문제에서 원하는 조건 만족하는지 체크하는 함수
    for l in li:
        if -l >= h:
            return 0
    return 1


n, h, t = list(map(int, input().split()))  # 인구 / 센티 키 / 뿅망치 횟수
arr = [-1 * int(input()) for _ in range(n)]
heapq.heapify(arr)  # 최대힙 구현 위해 -1 곱해줘서 원소 넣음

if h == 1 and h == -1 * arr[0]:    print('NO\n1')  # edge case 하나 체크
else:
    flag = 0
    t_cnt = 0

    if check(arr) == 1:  # 들어가기 전, 처리해야 할지 말지를 체크
        print(f'YES\n{t_cnt}')
        flag = 1

    else:
        for _ in range(t):  # t 번만큼 뿅망치 때리며 만족하는지 확인
            max_v = -heapq.heappop(arr)
            heapq.heappush(arr, -(max_v // 2))
            t_cnt += 1

            if check(arr) == 1:
                print(f'YES\n{t_cnt}')
                flag = 1
                break

    if flag == 0:  # 만족 못했으면, 최대값 출력
        print(f'NO\n{-min(arr)}')
