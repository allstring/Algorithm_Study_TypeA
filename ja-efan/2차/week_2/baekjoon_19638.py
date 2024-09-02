# 센티와 마법의 뿅망치

import heapq


def main():

    # N: 인구 수, H: 센티 키, T: 뿅망치 횟수
    N, H, T = map(int, input().split())

    # 최소 힙 사용을 위해 음수로 변환 후 삽입
    height_of_giants = [-int(input()) for _ in range(N)]

    # 최소 힙 변환
    heapq.heapify(height_of_giants)

    stop_flag = False
    ppyong_cnt = 0
    for i in range(T):
        tallest = -heapq.heappop(height_of_giants)

        if tallest == 1:
            heapq.heappush(height_of_giants, -tallest)
            stop_flag = True
            break

        if tallest >= H:

            tallest //= 2
            heapq.heappush(height_of_giants, -tallest)
            ppyong_cnt += 1
        else:
            # tallest < H
            break

    tallest = -height_of_giants[0]
    if tallest >= H:
        print('NO')
        print(tallest)
    else:
        print("YES")
        print(ppyong_cnt)



if __name__ == "__main__":
    main()