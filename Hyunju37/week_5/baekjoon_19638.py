import heapq

def main():
    N, H, T = map(int, input().split())
    heights = [int(input())*(-1) for _ in range(N)]
    heapq.heapify(heights)
    chance = T #남아있는 때리기횟수
    while chance: #가능한 때리기횟수가 남아 있는 동안 반복
        tallest = heapq.heappop(heights) * (-1) #우선순위 큐에서 가장 큰 키 뽑기
        if tallest < H: #우선순위 큐에 있는 모든 키가 다 H보다 작다(성공)
            print('YES')
            print(T-chance)
            return
        elif tallest == 1: #edge case - 가장 키가 큰 사람이 1일때
            heapq.heappush(heights, -1) #일단 다시 넣고 break
            break #(센티의 키는 1보다 크거나 같다. ->센티의 키가 1보다는 클 경우 성공이고 1이라면 실패일 것)
        else:
            tallest = int(tallest / 2) #뿅망치 때리기
            heapq.heappush(heights, tallest*(-1))
            chance -= 1 #때리기 기회를 한 번 씀

    tallest = heapq.heappop(heights) * (-1)
    if tallest < H: #모든 키가 센티보다 작다는 것이 보장됨
        print('YES')
        print(T)
    else:
        print('NO')
        print(tallest)


if __name__ == "__main__":
    main()