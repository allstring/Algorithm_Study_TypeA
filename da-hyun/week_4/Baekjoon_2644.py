def main():
    # 입력: 사람의 수 N
    N = int(input())

    # 입력: 찾고자 하는 두 사람의 번호 targetX와 targetY
    targetX, targetY = map(int, input().split())

    # 입력: 관계의 수 numRelation
    numRelation = int(input())

    # 관계를 저장할 인접 리스트 선언 (1부터 시작하는 인덱스를 사용하므로 N+1 크기로 선언)
    relationMap = [[] for _ in range(N+1)]

    # BFS 탐색에 사용할 큐와 방문 여부를 저장할 리스트
    queue = []
    visited = [False] * (N+1)

    # 입력: 사람 간의 관계를 relationMap에 저장
    for _ in range(numRelation):
        a, b = map(int, input().split())
        relationMap[a].append(b)  # a와 b는 서로 연결된 관계
        relationMap[b].append(a)

    # BFS 탐색 시작: targetX에서 시작
    queue.append(targetX)
    
    # 초기 답을 -1로 설정하고, 관계의 깊이 count를 0으로 초기화
    answer = -1
    count = 0

    # BFS 반복
    while queue:
        # 깊이 1 증가
        count += 1
        
        # 임시 큐 생성 (현재 큐에 있는 모든 노드를 처리하고 나서 사용할 예정)
        tmpQueue = []
        
        # 현재 큐에 있는 모든 노드 처리
        while queue:
            tmpNum = queue.pop()
            
            # 현재 노드 tmpNum에 연결된 모든 노드 탐색
            for target in relationMap[tmpNum]:
                if visited[target]:  # 이미 방문한 노드는 무시
                    continue
                if target == targetY:  # 목표 노드(targetY)를 찾으면 현재 깊이(count) 반환
                    return count
                tmpQueue.append(target)  # 임시 큐에 추가
                visited[target] = True  # 방문 처리
        
        # 큐를 임시 큐로 갱신 (다음 단계로 이동)
        queue = tmpQueue
    
    # 목표 노드(targetY)를 찾지 못하면 -1 반환
    return -1


if __name__ == "__main__":
    # main 함수의 결과를 출력
    print(main())

##################
##################
"""
queue 두개 대신 dequeue로 개선

from collections import deque

def main():
    # 입력: 사람의 수 N
    N = int(input())

    # 입력: 두 사람의 번호 targetX와 targetY
    targetX, targetY = map(int, input().split())

    # 입력: 관계의 수 numRelation
    numRelation = int(input())

    # 관계를 저장할 인접 리스트 선언 (1부터 시작하는 인덱스를 사용하므로 N+1 크기로 선언)
    relationMap = [[] for _ in range(N+1)]

    # 관계 정보 입력 및 인접 리스트 작성
    for _ in range(numRelation):
        a, b = map(int, input().split())
        relationMap[a].append(b)
        relationMap[b].append(a)

    # BFS를 위한 큐와 방문 여부 리스트 초기화
    queue = deque([targetX])
    visited = [False] * (N+1)
    visited[targetX] = True  # 시작 노드 방문 처리
    count = 0  # 단계 카운트

    # BFS 수행
    while queue:
        count += 1
        for _ in range(len(queue)):  # 현재 큐에 있는 모든 노드 처리
            current = queue.popleft()
            for neighbor in relationMap[current]:
                if not visited[neighbor]:
                    if neighbor == targetY:  # 목표 노드를 찾으면 현재 깊이 반환
                        return count
                    visited[neighbor] = True
                    queue.append(neighbor)
    
    # 목표 노드(targetY)를 찾지 못하면 -1 반환
    return -1

if __name__ == "__main__":
    print(main())


"""
