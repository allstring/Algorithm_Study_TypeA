"""
문제
도현이는 컴퓨터와 컴퓨터를 모두 연결하는 네트워크를 구축하려 한다.
a / b 연결 -> a b로 경로 존재한다
a에서 b를 연결하는 선이 있고, b와 c를 연결하는 선이 있으면 a와 c는 연결이 되어 있다

각 컴퓨터를 연결하는데 필요한 비용 >> 모든 컴퓨터를 연결하는데 필요한 최소비용?

입력
첫째 줄에 컴퓨터의 수 N (1 ≤ N ≤ 1000)가 주어진다.
둘째 줄에는 연결할 수 있는 선의 수 M (1 ≤ M ≤ 100,000)가 주어진다.
셋째 줄부터 M+2번째 줄까지 총 M개의 줄에 각 컴퓨터를 연결하는데 드는 비용이 주어진다.

이 비용의 정보는 세 개의 정수로 주어지는데,
만약에 a b c 가 주어져 있다고 하면 a컴퓨터와 b컴퓨터를 연결하는데 비용이 c (1 ≤ c ≤ 10,000) 만큼 든다는 것을 의미한다.
a와 b는 같을 수도 있다.

출력 : 모든 컴퓨터를 연결하는데 필요한 최소비용을 첫째 줄에 출력한다.
"""
# tc는 잘 나오지만, 사이트에서 답은 틀렸습니다! 
# 최소신장트리 Q 같았지만, dict를 이용한 완전탐색으로 풀어 보았습니다.

import sys
sys.stdin = open('1922.txt')
sys.setrecursionlimit(100000)


def dfs(k, money, visited_k):  # 현재 보고있는 컴퓨터 k / 누적되는 돈 money / 방문한 컴퓨터 list
    global ans

    if money > ans: return  # 가지치기) 최소비용이므로, 갱신된 ans보다 큰 값은 무시해도 된다.

    if len(visited_k) == n:  # 탈출조건) 모든 컴퓨터 방문했을 때에, ans 갱신하고 return 
        ans = min(ans, money)
        return

    for v in computer_dict[k]:  # 완전탐색) case를 2가지로 나눠서 진행 
        if v[0] in visited_k:continue  # 이미 찍었던 숫자는 찍지 말기
        dfs(v[0], money + v[1], visited_k + [k])
        # 연결되어 있는 컴퓨터의 간선을 따라 이동 

        dfs(k, money + v[1], visited_k + [v[0]])  
        # 연결되어 있는 컴퓨터에서 왔다고 생각하며 k 유지 
        # ( 여기서 다른쪽으로 뻗는게 이득일 수 있으니 ) 

    return


n = int(input())
m = int(input())
li = [list(map(int, input().split())) for _ in range(m)]

computers = [i for i in range(1, n+1)]

computer_dict = {}
# 컴퓨터 수 n / 연결 선 수 m / 연결 비용 li
# list[0] 과 list[1] 연결하는 데에 list[2] 의 비용 든다 ( 자기를 연결할 수 있다 < 무시해야 )

for chk in li:
    if chk[0] == chk[1]: continue  # 본인을 잇는건 무시

    # 한방향으로 보면, 키가 없는 컴퓨터가 존재할 수 있어서 ( 예제에서 6 ) 양방향으로 체크
    # k 컴퓨터에서 v[0] 컴퓨터로 가는 데에 v[2]만큼의 비용
    if chk[0] not in computer_dict:
        computer_dict[chk[0]] = [(chk[1], chk[2])]
    else:computer_dict[chk[0]].append((chk[1], chk[2]))  
    
    if chk[1] not in computer_dict:
        computer_dict[chk[1]] = [(chk[0], chk[2])]
    else:computer_dict[chk[1]].append((chk[0], chk[2]))


ans = float('inf')
dfs(1, 0, [1])  # 1부터 시작 / 드는 비용 / 들른 컴퓨터 ( 초기 1 )

print(ans)