# 11403. 경로 찾기

import sys
sys.stdin = open('input.txt', 'r')

def main():
    T = int(input())

    for _ in range(T):
        # N: 정점의 개수
        N = int(input())
        graphs = [list(map(int, input().split())) for _ in range(N)]
        # print(graphs)

        for i in range(0, N):
            for j in range(0, N):
                for k in range(0, N):
                    if graphs[j][i] == 1 and graphs[i][k] == 1:
                        graphs[j][k] = 1

        # print(graphs)
        for graph in graphs:
            for result in graph:
                print(result, end=' ')
            print()

if __name__ == "__main__":
    main()