from collections import defaultdict
def count_prereqs(graph, start):
    # Using Recursion => RecursionError

    # Using stack
    visited = set()
    stack = [start]
    count = 0
    while stack:
        current = stack.pop()
        visited.add(current)
        for req in graph[current]:
            if req not in visited:
                visited.add(req)
                count += 1
                stack.append(req)

    return count
N, M = map(int, input().split())
task_graph = defaultdict(list)

for k in range(N):
    task_graph[k] = []

for _ in range(M):
    pre_req, t = list(map(int, input().split()))
    task_graph[t].append(pre_req)

X = int(input())

ans = count_prereqs(task_graph, X)
print(ans)
