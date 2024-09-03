"""
가장 유명한 사람을 구하는 방법 > 각 사람의 2-친구를 구하면 된다. 

A B의 2-친구가 되기 위해서 : 두 사람이 친구 / A와 or B와 친구인 C가 존재

여기서 가장 유명한 사람은 2-친구의 수가 가장 많은 사람이다. 
가장 유명한 사람의 2-친구의 수를 출력하는 프로그램을 작성하시오.
A와 B가 친구면, B와 A도 친구이고, A와 A는 친구가 아니다.


입력
첫째 줄에 사람의 수 N이 주어진다. 
N은 50보다 작거나 같은 자연수이다. 
둘째 줄부터 N개의 줄에 각 사람이 친구이면 Y, 아니면 N이 주어진다.

출력
첫째 줄에 가장 유명한 사람의 2-친구의 수를 출력한다.
"""
import sys
sys.stdin = open('1058.txt')


def dfs(who, depth, _set):

    # 시작 부분에서 갈 수 있는 요소 : SET에 ADD ( 나중에 중복 무시하기 위해 ) 
    if depth == 2:
        _set.add(who)
        return

    if who not in friends_dict: return  
    # DEPTH 아직 2 안됐는데, 연결되어 있는 요소 없으면 RETURN

    # 여기 왔다는건, 연결되어 있는 친구가 있고, DEPTH가 2가 아니라는 것 ( 더 들어가야 )
    for v in friends_dict[who]:  # 연결되어 있는 요소들에 대해서 
        _set.add(v)              # 방문했다고 찍고 DFS 들어가기
        dfs(v, depth + 1, _set)


n = int(input())
friends = [list(map(str, input())) for _ in range(n)]
two_friends = [0] * n  # 각 사람들의 2-친구 명수 저장할 리스트

# 친구의 연결도 저장할 dict
friends_dict = {}
for i in range(n):
    for j in range(n):
        if friends[i][j] == 'Y':
            if i not in friends_dict:
                friends_dict[i] = [j]
            else: friends_dict[i].append(j)

for i in range(n):      # 모든 사람들에 대해 
    temp_set = set()    # 방문한 요소들을 넣을 임시 set
    dfs(i, 0, temp_set)

    if not temp_set:    # 아무도 연결되어 있지 않다? 0 넣고 다음사람
        two_friends[i] = 0  
        continue

    # 연결된 사람 있다 -> 본인 제외하고 중복을 걸러낸 2-친구 저장
    temp_set.remove(i)
    two_friends[i] = len(temp_set)

print(max(two_friends))  # 2-친구가 가장 많은 사람의 명수 출력

# 개선점 회고 : 시간과 공간을 필요없이 2배정도 사용하고 있는 것 같은데, 구현을 우선해서 풀긴 했지만 좋은 코드는 아닌..