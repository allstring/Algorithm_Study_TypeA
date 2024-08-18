def main():
    n, m = list(map(int, input().split()))
    cards = list(map(int, input().split()))
    cards.sort() #오름차순 정렬
    for i in range(m):
        cards[0] = cards[0] + cards[1]
        cards[1] = cards[0]
        #가장 작은 두 개의 카드를 합체하기
        cards.sort() #재정렬
    print(sum(cards))

if __name__ == '__main__':
    main()