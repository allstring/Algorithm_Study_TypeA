from collections import defaultdict
from collections import deque
def main():

    def path_length_dfs(start):
        stack = [(start, 0)] #시작 노드에서의 거리 0
        distance[start] = 0 #dist 배열 저장
        while stack:
            current_node, current_dist = stack.pop()
            for child in tree[current_node]: #각 자식노드에 대해서
                node, w = child
                if distance[node] == -1:
                    distance[node] = current_dist + w #본인이 갖고 있던 거리 + 해당 노드와의 가중치
                    stack.append((node, current_dist + w)) #stack push
        #Recursion Error -> 재귀호출 대신, 명시적 스택 사용

    tree = defaultdict(list)
    n = int(input())
    for _ in range(n-1):
        node1, node2, weight = list(map(int, input().split()))
        tree[node1].append((node2, weight))
        tree[node2].append((node1, weight))
        #두 노드 사이 경로는 한가지 뿐(?)인데 굳이 다익스트라를 쓸 필요? X?

    distance = [-1] * (n+1)
    path_length_dfs(1) #루트노드인 1번노드에서 가장 먼 노드 (말단노드 중 하나)를 찾는다.


    diameter1 = distance.index(max(distance)) #그 노드의 번호 (지름의 양 끝 점 중 하나가 될 것)
    distance = [-1] * (n + 1)
    path_length_dfs(diameter1) #이번엔 그 노드를 기준으로 가장 먼 노드를 찾는다.
    print(max(distance))

if __name__ == "__main__":
    main()