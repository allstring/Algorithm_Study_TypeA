T = int(input())
for _ in range(T):
    N = int(input())
    prices = list(map(int, input().split()))

    #local maxima를 찾아서, 거기에서 이전에 갖고있던 주식을 팔아야함
    mx = []

    if prices[0] > prices[1]:
        mx.append(0)

    for i in range(1, N-1):
        if prices[i-1] < prices[i] > prices[i+1]:
            mx.append(i)

    if prices[-1] > prices[-2]:
        mx.append(N-1)

    #print([prices[i] for i in mx])

    buy_idx = 0
    profit = 0

    for i in mx:
        for j in range(buy_idx, i):
            profit += (prices[i] - prices[j])
        buy_idx = i + 1

    print(profit)