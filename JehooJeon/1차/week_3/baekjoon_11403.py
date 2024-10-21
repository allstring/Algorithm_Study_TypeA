# 11403. 경로 찾기

import sys
sys.stdin = open('input.txt', 'r')

'''
   문제유형 파악 :
   누가봐도 그래프 문제
   자기 자신으로 돌아오는 loop를 고려해야하는 문제라고 생각함
   
   문제풀이 과정 :
   그래프에 대한 감이 전혀 잡히지 않아서, 고민 하다가 관련 알고리즘 검색
   -> 플로이드 워셜 알고리즘이 적합하다고 생각해서 적용
   -> 플로이드 워셜 알고리즘 : 모든 노드에서 다른 모든 노드까지의 최단경로를 구하는 알고리즘 (시간 복잡도 : O(N^3))
   -> 이 문제에서는 N이 1 ~ 100이므로, N^3 = 1,000,000 => 가능할 것으로 생각됨
   
   Fail 이유 :
   혼자 예제 입력하기 위한 T = int(input())을 포함시켜서 제출하는 바람에 실패함
   제대로 넣으니 바로 성공
'''

def main():
    T = int(input())

    for _ in range(T):
        # N: 정점의 개수
        N = int(input())
        graphs = [list(map(int, input().split())) for _ in range(N)]
        # print(graphs)

        # 플로이드 워셜 알고리즘 적용
        for i in range(0, N):    # 중간노드
            for j in range(0, N):    # 시작노드
                for k in range(0, N):    # 끝노드
                    # 길이(시작, 끝) = min[길이(시작, 끝), 길이(시작~중간, 중간~끝)]
                    # 이 문제에서는 길이가 양수인 경로가 있으면 1로 출력
                    # 따라서, 길이(시작~중간), 길이(중간~끝)가 1이면 길이(시작, 끝)은 1
                    if graphs[j][i] == 1 and graphs[i][k] == 1:
                        graphs[j][k] = 1

        # print(graphs)
        for graph in graphs:
            for result in graph:
                print(result, end=' ')
            print()

if __name__ == "__main__":
    main()