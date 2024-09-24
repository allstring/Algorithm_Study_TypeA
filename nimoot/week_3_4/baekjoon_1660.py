n = int(input())

pirate = [] # 사면체 배열
i = 1
while True:
    tetra = i * (i + 1) * (i + 2) // 6
    if tetra > 300000:  # N이 최대 300000라서 break 걸기
        break
    pirate.append(tetra)
    i += 1
    
dp = [float('inf')] * (n + 1)
dp[0] = 0

for num in pirate:
    for i in range(num, n + 1):
        dp[i] = min(dp[i], dp[i - num] + 1)

print(dp[n])
