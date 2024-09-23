# 그대, 그머가 되어
# Silver II

"""
풀이 설명 :
    단순 BFS using 2 stacks
    is_find 라는 플래그 사용으로 타겟 문자 치환 완료 시 탐색 중지

엣지...
    a -> a 인 경우 생각을 안하고 풀었다...
"""
# 최단 경로
from collections import defaultdict


def main():
    a, b = map(int, input().split())
    N, M = map(int, input().split())

    # src = target 인 경우 치환 과정이 필요 없음
    if a == b:
        print(0)
        return

    # 치환 가능한 문자 연결 간선
    edges = defaultdict(list)
    for _ in range(M):
        s, d = map(int, input().split())
        edges[s].append(d)
        edges[d].append(s)

    stack = [a]  # 메인 스택
    visited = {a}  # 방문 여부 집합
    cnt = 0  # 누적 치환 횟수
    is_find = False  # 타겟 문자 플래그
    while stack:
        cnt += 1  # 치환 1회 추가
        tmp_stack = []  # 임시 스택
        while stack:
            s = stack.pop()
            for adj in edges[s]:  # 치환 가능한 문자 순회
                if adj == b:  # 타겟인 경우
                    is_find = True  # 플래그 변경
                    visited.add(adj)  # visit 추가
                    break  # 반복문 탈출
                if adj in visited: continue  # 방문한 경우 스킵
                visited.add(adj)  # 방문처리 후
                tmp_stack.append(adj)  # 스택 추가
        if is_find: break  # 타겟 단어 찾은 경우 반복문 탈출 
        stack = tmp_stack  # 임시 스택을 메인 스택으로 변경 

    # 타겟 단어를 찾지 못한 경우 -1 출력
    if b not in visited:
        print(-1)
        return
    # 타겟 단어를 찾은 경우 치환 횟수 출력 
    print(cnt)


if __name__ == "__main__":
    main()