# 촌수계산
# Silver II

from collections import defaultdict, deque
"""
풀이 설명 :
    트리 형태의 부모-자식 관계에서 bfs를 이용해 촌수를 계산하며 두 사람의 촌수를 찾아낸다.
"""

def main():

    n = int(input())  # 전체 사람의 수
    t1, t2 = map(int, input().split())  # 촌 수를 계산해야 하는 두 사람의 번호
    m = int(input())  # 부모 자식들 간의 관계 개수
    relations = defaultdict(list)  # 부모 자식 관계 딕셔너리

    visited = [0 for _ in range(n+1)]  # 방문 체크 리스트

    for _ in range(m):
        # 입력 및 관계 딕셔너리 추가
        parent, child = map(int, input().split())
        relations[parent].append(child)
        relations[child].append(parent)

    # bfs queue
    queue = deque(relations[t1])
    # 초기 방문 +1
    visited[t1] = 1
    while queue:
        p = queue.popleft()
        # p와 관계가 있는 사람들 모두 탐색
        for i in relations[p]:
            if visited[i]: continue  # 방문한 경우 스킵
            # i번 idx의 사람은 p번 idx의 사람과 1촌 관계 이므로, t1과 p의 촌수보다 1만큼 크다.
            visited[i] = visited[p] + 1
            # queue에 i 추가
            queue.append(i)

    # 방문한 적이 있는 경우 촌수 출력
    if visited[t2]: print(visited[t2]+1)
    # 방문한 적이 없는 경우 : 관계가 없다 -> -1 출력
    else: print(-1)

if __name__ == "__main__":
    main()