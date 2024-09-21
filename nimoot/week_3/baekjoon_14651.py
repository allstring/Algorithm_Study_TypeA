# 배수판정법 쓰려고 하니까 시간/메모리 초과..
# 0 2 6 18 ... n이 2이상일 때 그 전 값에 3배 됨 확인해서 아래 코드 작성

num=int(input())

dp=[0]*3
dp[2]=2

if num>=3:
    print(dp[2]*pow(3,num-2)%1000000009) # 2*3^(num-2) 계산
else:
    print(dp[num])