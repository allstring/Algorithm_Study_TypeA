answer = 0
import sys
sys.setrecursionlimit(10**6)  # 재귀 한도 설정

def dfs(tree, index):
    global answer
    lengths = []
    
    # 현재 노드의 자식 노드 탐색
    for node, length in tree[index]:
        lengths.append(length + dfs(tree, node))
    
    # 자식 노드로부터 얻은 길이들을 내림차순 정렬
    lengths.sort(reverse=True)
    
    # 자식 노드가 없는 경우 0 리턴
    if len(lengths) == 0:
        return 0
    
    # 두 개 이상의 경로가 있는 경우 최댓값 갱신
    if len(lengths) >= 2:
        answer = max(answer, lengths[0] + lengths[1])
    
    # 루트 노드(1번 노드)의 경우 최댓값 갱신
    if index == 1:
        answer = max(answer, lengths[0])
    
    return lengths[0]  # 가장 긴 경로 리턴

def main():
    N = int(input())  # 노드 수 입력
    tree = [[] for _ in range(N + 1)]  # 트리 구조 초기화
    
    # 트리 구성
    for _ in range(N - 1):
        a, b, c = map(int, input().split())
        tree[a].append((b, c))
    
    # DFS 시작
    dfs(tree, 1)
    
    # 정답 출력
    print(answer)

if __name__ == "__main__":
    main()
