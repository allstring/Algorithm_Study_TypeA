# 15903. 카드 합체 놀이

import sys
sys.stdin = open('input.txt', 'r')

'''
    문제유형 파악 : 
    정렬? 그리디? 문제 파악 애매하다고 생각했지만 그리디로 푸는 것이 더 쉽다고 판단하고 진행함
    
    풀이과정 :
    2개의 카드를 더한 뒤 계산한 값을 덮어 쓰는데, 최종적인 총 점수의 값이 가장 작아야 함
    -> 계속 최솟값 2개를 골라서 값을 덮어 써야 총 점수의 값이 가장 작아진다고 생각함
    -> sort를 함으로써 최솟값을 찾고 덮어 쓰기 => 다시 sort 후 반복함으로써 풀이
    -> 카드의 개수는 2 ~ 1,000개, 횟수는 0 ~ 15,000번 => 충분히 sort를 계속 할 수 있다고 판단함
'''

def main():
    def worst_sum_cards(cards, m):
        for i in range(m):
            cards.sort()
            sum_cards = cards[0] + cards[1]
            cards[0] = sum_cards
            cards[1] = sum_cards
        return sum(cards)

    # n: 카드의 개수, m: 카드 합체를 몇 번 하는지
    n, m = map(int, input().split())
    # cards: 카드의 상태를 나타내는 자연수 리스트
    cards = list(map(int, input().split()))

    result = worst_sum_cards(cards, m)

    print(result)

if __name__ == "__main__":
    main()