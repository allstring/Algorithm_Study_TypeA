T = int(input())
for _ in range(T):
    N = int(input())
    prices = list(map(int, input().split()))


    profit = 0
    maxima = 0
    for i in range(N-1, -1, -1):
        if prices[i] > maxima:
            maxima = prices[i]
        else:
            profit += maxima - prices[i]

    print(profit)