"""
숫자 조각  https://www.acmicpc.net/problem/14629
solve
"""
def dfs(str_num, v):
    global ans
    global print_ans

    diff = abs(n - int(str_num))  # 목표 숫자와 만든 숫자의 diff를 저장 

    if diff == 0:  return n  # 차이가 0? n을 만들 수 있다. 
    
    if ans == diff:  # 답이 여러 개일 경우, 더 작은 숫자를 출력하기 위해 print_ans 를 초기화 
        print_ans = min(print_ans, int(str_num))

    else:
        if ans != min(ans, diff):  # 값이 바뀌었다 -> 차이가 적어졌다. -> ans과 print_ans update 
            ans = min(ans, diff)
            print_ans = int(str_num)

    for j in range(10):  # 안쓴숫자 붙이기 위해 for문 돌며 dfs  
        if v[j]:continue
        else:
            v[j] = True
            dfs(str_num + str(j), v)
            v[j] = False

    return


n = int(input())
ans, print_ans = float('inf'), 0
visited = [False] * 10

flag = 0
for i in range(1, 10):  # 시작하는 숫자 선택, 0은 생각하지 않음 
    visited[i] = True  # 해당 숫자를 썼으므로, visited를 True로 하고 넘김 

    if dfs(str(i), visited) == n:  # n의 수를 만들 수 있다면, 답이 나온 것이므로 flag 찍고 break 
        flag = 1
        break

    visited[i] = False  # 다음 숫자 사용할 때에 이 숫자 사용해야 하므로, visited False로 

if flag == 1: print(n)
else: print(print_ans)