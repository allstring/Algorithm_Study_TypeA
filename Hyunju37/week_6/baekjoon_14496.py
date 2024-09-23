from collections import defaultdict
from collections import deque

def main():
    #최소 치환 횟수를 계산하는 함수
    def minimal_switch(mapping, a, b, N):
        #최소 치환 횟수 초기화
        min_switch_count = float('inf')
        #1번~N번노드의 방문여부 표시할 배열
        visited = [False] * (N+1)
        #큐에 시작노드, 거리 0 삽입
        queue = deque([(a,0)])
        #큐가 비어있지 않은 동안 반복
        while queue:
            #dequeue
            current, dist = queue.popleft()
            #목적 노드를 찾음
            if current == b:
                #최소 치환 횟수 갱신
                min_switch_count = min(min_switch_count, dist)
            #현재 노드에서 치환 가능한 모든 노드에 대해
            for switch in mapping[current]:
                #아직 방문하지 않았다면 방문 처리 후 enqueue(거기서부터 다시 탐색할 예정이므로)
                if not visited[switch]:
                    visited[switch] = True
                    queue.append((switch,dist+1))
        if min_switch_count == float('inf'):
            return -1 #최소 치환 횟수가 초기 값에서 한번도 갱신되지 않았다면 -1 리턴
        else:
            return min_switch_count


    a, b = map(int, input().split()) # a --> b
    N, M = map(int, input().split()) #전체 문자의 수 N과 치환 가능한 문자쌍의 수 M
    mapping = defaultdict(list)
    for i in range(M):
        map_info = tuple(map(int, input().split()))
        mapping[map_info[0]].append(map_info[1])
        mapping[map_info[1]].append(map_info[0]) # 이 줄도 추가해줬어야 한다.

    ans = minimal_switch(mapping, a, b, N)
    print(ans)

if __name__ == "__main__":
    main()