# 센티와 마법의 뿅망치

"""
풀이 설명:
    우선순위 큐(heapq)를 사용해서, 가장 큰 거인의 키를 계속 반으로 줄인다.
    python에서 제공하는 heapq의 경우 최소 힙 이므로, -를 붙여 최대 힙으로 커스텀 해주었다.

"""
import heapq


def main():

    # N: 인구 수, H: 센티 키, T: 뿅망치 횟수
    N, H, T = map(int, input().split())

    # 최소 힙 사용을 위해 음수로 변환 후 삽입
    height_of_giants = [-int(input()) for _ in range(N)]

    # 최소 힙 변환
    heapq.heapify(height_of_giants)

    ppyong_cnt = 0  # 뿅망치 사용 횟수
    while -height_of_giants[0] >= H:  # 센티보다 크거나 같은 거인이 존재하는 경우
        if -height_of_giants[0] == 1:  # 하지만 거인의 키가 1이라면
            print("NO")  # NO와
            print(-height_of_giants[0])  # 거인의 키 출력
            return

        if ppyong_cnt == T:  # 뿅망치를 최대치로 사용해버린 경우
            print("NO")  # NO와
            print(-height_of_giants[0])  # 거인의 키 출력
            return
        giant = -heapq.heappop(height_of_giants)  # 거인의 키 (heappop())
        giant //= 2  # 뿅망치 때려주고
        ppyong_cnt += 1  # 뿅망치 카운트 + 1
        heapq.heappush(height_of_giants, -giant)  # 반으로 줄어든 거인의 키를 음수 변환 후 heap에 추가

    # 도달하는 경우: 센티보다 크거나 같은 거인이 없고, 뿅망치를 최대치 이하로 사용한 경우
    print("YES")
    print(ppyong_cnt)


if __name__ == "__main__":
    main()