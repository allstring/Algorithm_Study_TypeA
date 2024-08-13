'''
1) 서류순위 기준 2) 면접순위 기준
으로 한 번 정렬하고,
서류점수 기준으로 1등이면 이 사람은 무조건 채용된다.
나머지들은 서류 1등보다는 무조건 서류등수가 낮다.
그러면 이 나머지들은 서류 1등보다 무조건 면접 순위가 높아야 한다.
--> 그래야, 이미 서류에서 1등보다 뒤진 이 지원자들이 면접순위는 높다는 것을 보장함으로써
채용 기준을 만족한다.
단순히 1등보다 순위가 높으면 되는게 아니라
1등의 면접순위부터 시작해서 아래로 갈수록 면접순위는 계속 높아져야 한다
비 1등 지원자들 끼리 어떤 지원자가 어떤 지원자보다 서류도낮고 면접도낮으면
걔네 둘 다 1등것보다는 높더라도 둘 중 (순위가 낮은)
하나는 통과
못하는 경우 있을수있기때문
'''
def main():
    T = int(input())
    for _ in range(T):
        N = int(input()) #지원자 N명
        scores = []
        for i in range(N):
            scores.append(tuple(map(int, input().split())))
        scores.sort()

        cnt = 1
        current_first = scores[0][1]
        for i in range(1, N):
            if scores[i][1] < current_first:
                current_first = scores[i][1]
                cnt += 1
        print(cnt)


if __name__ == '__main__':
    main()