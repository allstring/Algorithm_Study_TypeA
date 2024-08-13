# 신입 사원
# Silver I
# https://www.acmicpc.net/problem/1946
from collections import deque


def main():
    T = int(input())  # 테스트 케이스 개수 (1 <= T <= 20)
    for tc in range(1, T + 1):
        N = int(input())  # 지원자 수 (1 <= N <= 100,000)
        resume_rank = [-1 for _ in range(N)]
        # interview_rank = [-1 for _ in range(N)]
        # resume_rank_dict = dict()
        interview_rank_dict = dict()
        for i in range(N):
            # i 번째 지원자의 서류 순위(resume), 면접 순위(interview)
            resume, interview = map(int, input().split())
            # n 번째 인덱스에 서류 점수 n+1등 지원자 번호(i)
            resume_rank[resume - 1] = i
            # key: 지원자 번호, value: 인터뷰 순위
            interview_rank_dict[i] = interview - 1

        # deque로 변경
        resume_rank = deque(resume_rank)
        # 최종 합격 지원자 리스트
        final_pass = list()
        # 서류 기준 지원자 남은 동안 반복
        while resume_rank:
            applicant = resume_rank.popleft()  # 가장 순위가 높은 지원자
            if not final_pass:
                # 통과한 지원자가 없는 경우 (서류 기준으로 해당 지원자보다 높은 순위의 지원자가 없음)
                final_pass.append(applicant)  # 최종 합격
            if final_pass and (interview_rank_dict[applicant] < interview_rank_dict[final_pass[-1]]):
                # 통과한 지원자가 존재하고,
                # 현재 지원자의 면접 순위보다 이전 통과자의 면접 순위가 더 낮은 경우(숫자는 더 높다.)
                final_pass.append(applicant)  # 최종 합격

        print(len(final_pass))


if __name__ == '__main__':
    main()
