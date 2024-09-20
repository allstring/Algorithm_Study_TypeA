import sys

def dfs(num_len, cnt, num):
    global res
    if num_len == cnt:
        if abs(res - n) > abs(num - n): #차이가 적은 것이 답
            res = num
        elif abs(res - n) == abs(num - n): # 이전의 값의 차이와 현재 값의 차이가 같다면
            res = min(res, num) # 그 중 작은 숫자가 답
        return
    for idx in range(10):
        if not visited[idx]: # 지금까지 사용한 숫자가 아니면 방문
            visited[idx] = True
            dfs(num_len, cnt+1, num*10+idx)
            visited[idx] = False

input = sys.stdin.readline
str_n = input() #강민이가 질문하는 숫자
n = int(str_n)
num_len = len(str_n) #강민이가 질문하는 숫자 길이
start_num = int(str_n[0]) #질문하는 숫자의 첫자리 수(n을 문자형으로 받은 이유)
visited = [False] * 10 #0~9까지의 숫자를 1번씩 사용해야하므로 visited로 체크
res = float('inf') # n과 가장 차이가 적은 숫자 출력이므로 가장 큰 값으로 초기화
if n >= 9876543210: #9876543210보다 크면 해당 값과 가장 적은 값의 차이를 나타내는 건 1가지 밖에 없음
    res = 9876543210
else:
    # 강민이가 질문하는 숫자와 작은 차이를 만들어 내려면
    for num_length in range(num_len-1, 11 if num_len >= 9 else num_len+2): # 강민이가 질문한 숫자 자리수의 -1~ +1
        # (n의 자리수가 10이면 9~11자리 수를 생성하는데 숫자는 0~9까지의 10개 숫자만으로 생성할 수 있어 11자리 수 생성 불가라 제한 걸어 놓음)
        for start_number in range(start_num-1, 10 if start_num+2 > 10 else start_num+2): # 강민이가 질문하는 숫자의 첫자리 숫자의 -1~ +1
            # (첫자리 숫자가 9면 범위가 8~10으로 시작 숫자가 10이 될 수 있어 제한 걸기)
            visited[start_number] = True
            dfs(num_length, 1, start_number)
            visited[start_number] = False

print(res)