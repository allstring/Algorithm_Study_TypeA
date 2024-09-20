def main():
    N = int(input())
    tag = [0] * (N+1)

    #단위 정사면체들의 사이즈 정의해 두기 (가장 작은 것부터 최대 삼십만 개가 필요한 최대 크기 까지)
    coin = [1]
    #n번째 정사면체는 이전 정사면체 사이즈에 1+2+3+....n만큼을 더한 사이즈를 갖는다
    n = 2
    while True:
        if coin[-1] >= 300000: #최대 정사면체사이즈를 넘으면 정사면체사이즈 구하기 중단
            break
        coin.append(coin[-1]+(n*(n+1)//2))
        n += 1

    tag[0] = 1 #초깃값
    for i in range(1, N+1):
        if i in coin:
            tag[i] = 1 #딱 i사이즈의 정사면체가 있다면 그 사이즈로 가져가면 됨 (단 하나의 정사면체 만들기 가능)
            continue
        smaller_coins = [c for c in coin if c <= i] #현재 기준 사이즈보다 작은 단위정사면체들만을 고려
        min_way = min(tag[i-s]+1 for s in smaller_coins) #Dynamic programming (사이즈 s짜리 단위정사면체들을 사용하는 모든 경우를 고려해서 최솟값 찾기)
        tag[i] = min_way #정사면체 개수의 최솟값

    print(tag[N])

if __name__ == "__main__":
    main()