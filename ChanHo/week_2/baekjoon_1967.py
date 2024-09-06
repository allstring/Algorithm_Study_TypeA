"""
dfs를 갈건데,
자식이 없는 노드에서 출발해서
자식이 없는 노드에 도착할 때까지

이때 신경써야 하는 점)
1. 자식이 없는 노드에서 올라가기만 하다가 모든 v에 대해 자식이 없을 때까지 내려가야
2. root에 자식이 하나밖에 없다면, root도 리프 노드의 역할을 할 수 있다
"""
import sys
sys.setrecursionlimit(100000)


def dfs(vertex, switch_flag, res_sum, visited):
    global ans

    # 시작을 자식이 없는 것부터 했으므로, 부모로 계속 올라가다가 내려와야

######################################################################

    if vertex in graph_dict:  # 자식이 있다 : 내려가거나 올라가야
        if switch_flag == 0:  # 방향 전환 안했다

            # 방향 돌려서 내려가기
            for val in graph_dict[vertex]:  # 해당 자식들에 대해서 모두 내려가기
                if val[0] in visited:continue  # 방문했던거면 pass
                visited.add(val[0])
                dfs(val[0], switch_flag + 1, res_sum + val[1], visited)
                visited.discard(val[0])

            # 방향 안돌리고 올라가기
            # case 2개 / root 거나 중간이거나 - root 면 continue / 중간이면 올리기만
            if vertex not in hparg_dict:  # root node중 자식이 하나면 끝나는 점이 될 수 있음  
                if len(graph_dict[vertex]) == 1:
                    ans = max(ans, res_sum)
                    return
                    
            else:  # 중간이면 올리기만 
                k, gaz = hparg_dict[vertex][0], hparg_dict[vertex][1]
                visited.add(vertex)
                dfs(k, switch_flag, res_sum + gaz, visited)
                visited.discard(vertex)

        else:  # flag == 1 : 방향전환 했고, 내려가고 있다 > 내려갈 수 있는 모든 경로에 대해 내려가기
            for val in graph_dict[vertex]:
                if val[0] in visited:continue
                visited.add(val[0])
                dfs(val[0], switch_flag, res_sum + val[1], visited)
                visited.discard(val[0])

######################################################################

    else:  # 자식이 없다 : 처음이나 끝이다
        if switch_flag == 0:  # 처음이다 : 올라갈 수 있는 곳으로 올라가
            k, gaz = hparg_dict[vertex][0], hparg_dict[vertex][1]
            visited.add(vertex)
            dfs(k, switch_flag, res_sum + gaz, visited)
            visited.discard(vertex)

        else:  # 끝이다. 탈출조건
            ans = max(ans, res_sum)
            return

    return

#######################################################################


n = int(input())
edges = [list(map(int, input().split())) for _ in range(n-1)]

if n == 1:print(0)  # edge case 
else:
    # 1. 부모 : 자식 / 자식 : 부모 dict 형성 ( 전자 : 트리구조 / 후자 : 이후에 search 쉽게 하기 위해 )
    graph_dict = {}
    for e in edges:
        if e[0] in graph_dict:        graph_dict[e[0]].append((e[1], e[2]))
        else:                         graph_dict[e[0]] = [(e[1], e[2])]

    hparg_dict = {}
    for e in edges:
        hparg_dict[e[1]] = (e[0], e[2])

    ans = 0
    visited_set = set()  # visited를 체크할 set / 항상 list search 보다 set이 더 이득 
    for i in range(1, n+1):  # 모든 사람에 대해 돌리지만, 리프노드에서만 출발할 것
        if i in graph_dict: continue  # ( 키값으로 있으면 ( 자식 있으면 ) 건뛰 )
        dfs(i, 0, 0, visited_set)
    
    print(ans)