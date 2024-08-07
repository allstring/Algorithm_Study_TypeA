# 주식
# Silver II

def main():
    T = int(input())  # 테스트 케이스 개수
    for tc in range(1, T+1):
        N = int(input())
        stocks = list(map(int, input().split()))
        total_profit = 0
        while stocks:
            price = stocks.pop()
            # if not stocks:
            #     break
            # under_prices  = []
            # profit = 0
            while stocks and (price > stocks[-1]):
                # under_prices.append(stocks.pop())
                # if not stocks:
                #     break
            # for under_price in under_prices:
                total_profit += (price - stocks.pop())
            # total_profit += profit
        print(total_profit)


if __name__ == "__main__":
    main()