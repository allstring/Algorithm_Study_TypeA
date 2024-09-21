def dfs(cur_idx, cur, prev_cur):
    global ans

    # 한줄을 저장했을 때에 
    if len(cur) == m:
        if prev_cur == '':  # 맨 첫줄이면, 비교할게 없으므로 prev_cur에 넘기고 dfs 
            prev_cur = cur
            cur = ''
        else:               # 첫줄이 아니라면, 이전 줄과 지금 줄을 비교해 1 1 << 이 동일한 행에 있을 때에 return 
            temp = [prev_cur, cur]
            temp_set = []
            for i in range(2):
                for j in range(m):
                    if j == 0:continue
                    if i == 0:
                        if temp[i][j] == '1' and temp[i][j-1] == '1':
                            temp_set.append((j, j-1))
                    else:
                        if temp[i][j] == '1' and temp[i][j-1] == '1':
                            if (j, j-1) in temp_set:
                                return
            prev_cur = cur
            cur = ''

    if cur_idx == n*m:  # 조건에 걸리지 않아서 괜찮다면 답 
        ans += 1
        return

    dfs(cur_idx + 1, cur + '0', prev_cur)  # 0 1 가능한 모든 조합으로 dfs 
    dfs(cur_idx + 1, cur + '1', prev_cur)
    return


n, m = map(int, input().split())
string = []
ans = 0
dfs(0, '', '')
print(ans)
