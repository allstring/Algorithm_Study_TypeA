import sys

input = sys.stdin.readline


def main():
    # 회의의 수 입력
    n = int(input())

    # 각 회의의 시작 시간과 종료 시간 입력
    meetings = [tuple(map(int, input().split())) for _ in range(n)]

    # 끝나는 시간을 기준으로 회의들을 정렬
    meetings.sort(key=lambda x: (x[1], x[0]))
    # 선택된 회의 개수 및 끝나는 시간 초기화
    count = 0
    end_time = 0

    # 각 회의를 순차적으로 확인하며 회의실에 배정
    for start, end in meetings:
        if start >= end_time:
            # 회의가 끝난 이후에 시작되는 경우 회의실 사용
            count += 1
            end_time = end

    # 최대 사용할 수 있는 회의의 수 출력
    print(count)


if __name__ == "__main__":
    main()