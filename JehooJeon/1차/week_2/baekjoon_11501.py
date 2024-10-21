# 11501. 주식

import sys
sys.stdin = open("input.txt", "r")

T = int(input())

for _ in range(T):
    # N: 날의 수 (2 <= N <= 1,000,000)
    N = int(input())
    # stock: 날 별 주가 (<= 10,000)
    stock = list(map(int, input().split()))

    # 최대 이익 초기화
    result = 0
    # 뒤에서부터 시작하면서 최댓값으로 설정
    max_price = stock.pop()

    while True:
        # 만약 남은 stock이 없을경우 정지
        if not stock:
            break

        # 만약 앞에 있는 값이 가격이 더 낮을경우 차익실현
        if max_price > stock[-1]:
            result += max_price - stock[-1]
            stock.pop()
        # 만약 앞에 있는 값이 가격이 더 높거나 같을경우 max_price 갱신
        else:
            max_price = stock.pop()

    print(result)


''' 주가가 오르내리락 하는 경우를 고려하지 못함 -> 결과: 틀렸습니다.
for _ in range(T):
    # N: 날의 수 (2 <= N <= 1,000,000)
    N = int(input())
    # stock: 날 별 주가 (<= 10,000)
    stock = list(map(int, input().split()))

    # 최대 이익 초기화
    result = 0
    while stock:

        # 주가가 최대인 위치의 index 반환
        idx = stock.index(max(stock))
        # 주가가 최대인 위치가 첫날이면 정지
        if idx == 0: break
        
        # 주가가 최대인 날까지 주식을 모두 구매한 뒤 최대인 날 판매
        result += stock[idx]*idx - sum(stock[:idx])
        # 최대인 날 이후부터 다시 stock으로 정의하고
        # 만약 주가가 하나만 남아있으면 정지
        if len(stock[idx+1:]) <= 1: break
        else: stock = stock[idx+1:]

    print(result)
'''