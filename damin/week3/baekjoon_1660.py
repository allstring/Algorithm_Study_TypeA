import sys
'''
삼각형 -> 이전 삼각형에 n개씩 밑에 덧붙이면 된다
사면체 -> 이전 사면체에 현재 삼각형을 사면체 밑에 덧붙인다고 생각하면 된다
'''
input = sys.stdin.readline
n = int(input())
triangle = [0]
for i in range(1, n+1):
    triangle.append(triangle[i - 1] + i) 
    if triangle[i-1] + i <= n: # 삼각형의 개수가 n과 작거나 동일할 때는 계속 진행
        continue
    else: # n보다 커지면 삼각형 생성 중지
        break

tetrahedral = [0]*len(triangle) #사면체
for i in range(1, len(tetrahedral)):
    tetrahedral[i] = tetrahedral[i-1] + triangle[i]

dp = [i for i in range(n+1)] # 사면체가 1인 것으로만 채웠다고 가정(이게 사면체를 채울 때 가장 많은 개수가 필요한 방식이니까)
idx = 2 # n은 순차적으로 증가하니 n이 어떤 사면체의 대포알 개수를 넘기 전까지는 n이 가질 수 있는 제일 큰 사면체는 동일하니까 idx를 따로 둠
for i in range(2, n+1):
    if i < tetrahedral[idx]: # 사면체의 대포알 개수보다 작다면
        for j in range(1, idx): # 사면체의 대포알이 1일 때부터 시작해서 최대치까지 순회
            dp[i] = min(dp[i], dp[i-tetrahedral[j]]+1) # '사면체가 가진 대포알 개수 만큼 빼서 사면체 1개 만들기' 를 했을 때 사면체 개수의 최소 값 찾기

    elif i == tetrahedral[idx]: # i가 사면체가 가진 대포알 개수와 동일하다면
        dp[i] = 1 # 사면체의 최소 개수는 1
        idx += 1 # i 다음 숫자는 현재 idx의 사면체가 가진 대포알 개수보다 크니 idx 증가시킴

print(dp[n])