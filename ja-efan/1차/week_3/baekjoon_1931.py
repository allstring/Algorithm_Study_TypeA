# 회의실 배정
# Silver I
# https://www.acmicpc.net/problem/1931
"""
풀이 설명 :
    접근 방법: 그리디
    그리디 알고리즘의 대명사인 문제로,, 설명이 필요한가 싶다,,
"""
def main():
    N = int(input())  # 회의 개수 (1 <= N <= 100,000)
    meetings = [tuple(map(int, input().split())) for _ in range(N)]

    # 끝나는 시각 기준 정렬(ASC) -> 끝나는 시각이 겹치는 경우 시작 시간 순 정렬
    meetings.sort(key=lambda x : (x[1], x[0]))
    pre_meeting = meetings[0]  # 가장 먼저 끝나는 회의
    cnt = 1  # 회의 카운트
    for meeting in meetings[1:]:
        if meeting[0] < pre_meeting[1]:  # 회의 시작 시각이 이전 회의 종료 시각보다 빠른 경우
            continue
        cnt += 1  # 회의 카운트 + 1
        pre_meeting = meeting  # 현재 회의를 이전 회의로 할당

    print(cnt)  # 결과 출력


if __name__ == "__main__":
    main()