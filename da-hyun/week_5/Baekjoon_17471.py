answer = float('inf')  # 무한대 초기화로 변경

def bfs(AList, N, graph, popular):
    global answer
    BList = [i for i in range(N) if i not in AList]
    
    if not AList or not BList:  # 한쪽 그룹이 비어 있으면 무시
        return
    
    visited = [False for _ in range(N)]
    count = 0
    sumA, sumB = 0, 0
    
    for i in range(N):
        if visited[i]: 
            continue
        
        flag = True if i in AList else False
        count += 1
        queue = [i]
        
        while queue:
            tmpNode = queue.pop()
            visited[tmpNode] =True
            if flag: sumA += popular[tmpNode]
            else: sumB += popular[tmpNode]
                
            for node in graph[tmpNode]:
                if visited[node]: continue
                if flag and node in BList: continue
                if not flag and node in AList: continue
                queue.append(node)
                visited[node] = True
    
    if count == 2:  # 두 그룹이 모두 연결된 경우에만 처리
        answer = min(answer, abs(sumA - sumB))


def dfs(bitmask, idx, n, graph, popular):
    if idx == n:
        result = [i for i in range(n) if bitmask & (1 << i)]
        bfs(result, n, graph, popular)
        return

    # 현재 idx를 선택하지 않는 경우
    dfs(bitmask, idx + 1, n, graph, popular)
    
    # 현재 idx를 선택하는 경우
    dfs(bitmask | (1 << idx), idx + 1, n, graph, popular)


def main():
    N = int(input())
    popular = list(map(int, input().split()))
    graph = [[] for _ in range(N)]
    
    for index in range(N):
        tmpValues = list(map(int, input().split()))
        for value in tmpValues[1:]:
            graph[index].append(value - 1)

    dfs(0, 0, N, graph, popular)
    
    if answer == float('inf'): 
        print(-1)
    else: 
        print(answer)


if __name__ == "__main__":
    main()
