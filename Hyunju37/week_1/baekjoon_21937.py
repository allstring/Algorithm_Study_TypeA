from collections import defaultdict
def count_prereqs(graph, start):
    # Using Recursion => RecursionError
    '''global visited
    visited.add(start)
    for req in graph[start]:
        if req not in visited:
            global count
            count += 1
            count_prereqs(graph, req)'''

    # Using stack
    visited = set()
    stack = [start]
    count = 0
    while stack:
        current = stack.pop()
        visited.add(current)
        for req in graph[current]:
            if req not in visited:
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

#visited = set()
#count = 0
ans = count_prereqs(task_graph, X)
print(ans)
