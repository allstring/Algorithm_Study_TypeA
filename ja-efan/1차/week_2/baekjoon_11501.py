# 주식
# Silver II
"""
풀이 설명 :
    주어진 주식 가격(stocks)을 뒤(idx:-1)에서부터 접근합니다.
    가격(stocks[-1])으로 팔 경우 이익이 발생 하는 주식을 찾아서 총 이익을 구해줍니다.
    홍준이가 하는 행동 중 2번에 '원하는 만큼 가지고 있는 주식을 판다.'라는 말이 있는데,
    사실 싸게 사서 '가장 비싸게' 파는게 최대 이익을 내는 방법 이기 때문에,
    주식 가격을 뒤에서부터 접근한다면 해당 가격으로 팔 수 있는 주식을 모두 구할 수 있습니다.
"""

def main():
    T = int(input())  # 테스트 케이스 개수
    for tc in range(1, T+1):
        N = int(input())  # 날의 수
        stocks = list(map(int, input().split()))
        total_profit = 0  # 누적 이익
        while stocks:  # 주식이 존재할 동안 반복
            price = stocks.pop()  # 마지막 날 주식
            while stocks and (price > stocks[-1]):  # 살 수 있는 주식이 존재 하고, price로 팔면 이익인 경우에 반복
                total_profit += (price - stocks.pop())   # 누적 이익에 더한다.
        print(total_profit)  # 최대 이익 출력


if __name__ == "__main__":
    main()