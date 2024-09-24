def dfs(idx, current, is_greater, is_smaller, used, target, min_diff):
    if idx == len(target):
        num = int(current)  # 현재까지 만든 숫자를 정수로 변환
        diff = abs(num - int(target))  # 목표 값과의 차이 계산
        if diff < min_diff[0] or (diff == min_diff[0] and num < min_diff[1]):
            # 최소 차이 갱신
            min_diff[0] = diff
            min_diff[1] = num
        return



    # 제일 큰 값을 만들고 있는 중
    if is_greater:
        for i in range(9, -1, -1):  # 9부터 0까지 시도
            if not used[i]:
                used[i] = True
                dfs(idx + 1, current + str(i), True, False, used, target, min_diff)
                used[i] = False
                return

    # 제일 작은 값을 만들고 있는 중
    elif is_smaller:
        for i in range(0, 10, 1):  # 현재 자리 숫자까지 시도
            if not used[i]:
                used[i] = True
                dfs(idx + 1, current + str(i), False, True, used, target, min_diff)
                used[i] = False
                return

    # 동일한 자리 숫자나 더 크거나 작은 숫자를 모두 탐색
    else:
        current_digit = int(target[idx])  # 현재 자리의 목표 숫자
        # 현재 자리 숫자와 동일한 경우
        if not used[current_digit]:
            used[current_digit] = True
            dfs(idx + 1, current + str(current_digit), False, False, used, target, min_diff)
            used[current_digit] = False

        # 더 큰 숫자를 시도하는 경우
        # 뒤의 숫자는 가장 작은 형태가 와야한다.
        for i in range(current_digit + 1, 10):
            if not used[i]:
                used[i] = True
                dfs(idx + 1, current + str(i), False, True, used, target, min_diff)
                used[i] = False
                break

        # 더 작은 숫자를 시도하는 경우
        # 뒤의 숫자는 가장 큰 형태가 와야한다.
        for i in range(current_digit - 1, -1, -1):
            if not used[i]:
                used[i] = True
                dfs(idx + 1, current + str(i), True, False, used, target, min_diff)
                used[i] = False
                break


def main():
    N = int(input())  # 목표 숫자 입력
    if N >= 9876543210:
        print(9876543210)  # 가능한 최대 숫자 출력
        return

    min_diff = [float('inf'), 0]  # 최소 차이와 그에 해당하는 숫자
    used = [False] * 10  # 숫자 사용 여부 기록

    # DFS 탐색 실행
    dfs(0, '', False, False, used, str(N), min_diff)

    used[9] = True
    dfs(2, "9", True, False, used, str(N), min_diff)  # 숫자 9부터 탐색
    used[9] = False

    used[1] = True
    dfs(0, "1", False, True, used, str(N), min_diff)  # 숫자 1부터 탐색
    used[1] = False

    print(min_diff[1])  # 최소 차이에 해당하는 숫자 출력


if __name__ == '__main__':
    main()
