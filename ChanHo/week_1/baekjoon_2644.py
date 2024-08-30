"""
dfs 적으로 생각...
k가 아닐 때까지 올리기 / v 있으면 v에 모두 보내기 / depth 하나씩 올리면서 해당 값이 b면 depth return
"""
import sys
sys.stdin = open('2644.txt')
sys.setrecursionlimit(100000)


def dfs(current, depth, visited):  # 지금 보고있는 요소 / 깊이 / 방문 배열 
    global ans

    if current == b:  # 탈출 조건) 원하는 목표 도착하면 depth 갱신 
        ans = min(ans, depth)
        return

    # 부모 check  -  자식 check 먼저 하면 안되는 이유? 자식 없는 리프 노드면 바로 return 
    for k, v in family_dict.items():
        if current in v:  # 부모는 한명 있다 = 여러명 아니기 때문에 dfs 보내고 break
            if k not in visited:  # 방문한 노드 아니라면, dfs
                dfs(k, depth + 1, visited + [current])
            break

    # 자식 check
    if current in family_dict:  # 자식이 있다 -> 방문한 적 없는 모든 자식 노드에 대해 dfs 
        for v in family_dict[current]:
            if v not in visited:
                dfs(v, depth + 1, visited + [current])                
    else:  # 리프노드 : 부모로는 이미 보냈으니 return 
        return

    # 부모 / 자식으로 모두 보냄 ( 체크 완료 ) -> return 
    return


n = int(input())  # 사람 수
a, b = map(int, input().split())  # 촌수 계산해야 하는 서로 다른 두 사람의 번호
m = int(input())  # 부모 자식간의 관계의 개수


xy = [list(map(int, input().split())) for _ in range(m)]  # 부모 < 자식
family_dict = {}
for fam in xy:  # 유사 트리
    if fam[0] not in family_dict:
        family_dict[fam[0]] = [fam[1]]
    else:family_dict[fam[0]].append(fam[1])

ans = float('inf')
dfs(a, 0, [])

if ans == float('inf'):print(-1)  # ans 갱신 안된다 -> 연결 X
else: print(ans)