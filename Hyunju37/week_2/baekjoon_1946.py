'''
1) 서류점수 기준 2) 면접점수 기준
으로 한 번 정렬하고,
서류점수 기준으로 1등이면 이 사람은 무조건 채용된다.
나머지들은 서류 1등보다는 무조건 서류 점수가 낮다.
그러면 이 나머지들은 서류 1등보다 무조건 면접 점수가 높아야 한다.
--> 그래야, 이미 서류에서 1등보다 뒤진 이 지원자들이 면접점수는 높다는 것을 보장함으로써
채용 기준을 만족한다.
문제이해가안돼요 ㅠㅠㅠ
'''
def main():
    T = int(input())
    for _ in range(T):
        N = int(input()) #지원자 N명
        scores = []
        for i in range(N):
            scores.append(tuple(map(int, input().split())))
        scores.sort(key=lambda x: (-x[0], -x[1]))

        cnt = 1
        resume_1st_interview = scores[0][1]
        for i in range(1, N-1):
            if scores[i][1] > resume_1st_interview:
                cnt += 1
        print(N - cnt)


if __name__ == '__main__':
    main()