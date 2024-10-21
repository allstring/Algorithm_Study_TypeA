# 19638. 센티와 마법의 뿅망치

# import sys
# sys.stdin = open('baekjoon_19638_input.txt', 'r')

import heapq

def main():
    # N: 센티를 제외한 거인의 나라의 인구수, H: 센티의 키, T: 마법의 뿅망치의 횟수 제한
    N, H, T = map(int, input().split())
    # heights: 각 거인의 키를 나타내는 리스트
    heights = list(-int(input()) for _ in range(N))
    # cnt: 뿅망치 사용 횟수
    cnt = 0

    heapq.heapify(heights)

    while True:
        max_height = -heapq.heappop(heights)

        # 만약 가장 키가 큰 거인의 키가 센티보다 작으면,
        # YES를 출력하고, 마법의 뿅망치를 최소로 사용한 횟수 출력
        if max_height < H:
            print('YES')
            print(cnt)
            break
        
        # 만약 가장 키가 큰 거인의 키가 센티보다 크거나 같은데,
        # 뿅망치 횟수 제한을 모두 사용한 경우
        # NO를 출력하고, 마법의 뿅망치 사용 이후 거인의 나라에서 키가 가장 큰 거인의 키 출력
        if cnt == T:
            print('NO')
            print(max_height)
            break
        
        # 가장 키가 큰 거인의 키가 1인 경우 뿅망치의 영향 X
        if max_height == 1:
            heapq.heappush(heights, -1)
            cnt += 1
            continue

        # 두 경우 모두 아닌 경우에는 뿅망치를 사용해서
        # 가장 키가 큰 거인의 키를 2로 나눠줌
        new_height = max_height // 2
        heapq.heappush(heights, -new_height)
        cnt += 1

if __name__ == '__main__':
    main()

''' 런타임 에러(PriorityQueue 활용)
from queue import PriorityQueue

def main():
    # N: 센티를 제외한 거인의 나라의 인구수, H: 센티의 키, T: 마법의 뿅망치의 횟수 제한
    N, H, T = map(int, input().split())
    # heights: 각 거인의 키를 나타내는 리스트
    heights = list(int(input()) for _ in range(N))

    queue = PriorityQueue()

    for height in heights:
        queue.put((-height, height))

    # cnt: 뿅망치 사용 횟수
    cnt = 0

    while True:
        # 가장 큰 거인의 키를 출력
        max_height = queue.get()[1]

        # 만약, 가장 큰 거인의 키가 센티의 키보다 작다면,
        # YES를 출력하고 마법의 뿅망치를 최소로 사용한 횟수 출력
        if max_height < H:
            print('YES')
            print(cnt)
            break
        
        # 가장 큰 거인의 키가 센티의 키보다 큰데, 뿅망치 횟수가 0회라면,
        # NO를 출력하고 두 번째 줄에 가장 큰 거인의 키를 출력
        if T == cnt:
            print('NO')
            print(max_height)
            break
        
        # 만약 가장 큰 거인의 키가 1이라면,
        # 더 줄어들 수가 없기 때문에 뿅망치의 영향을 받지 않음
        if max_height == 1:
            queue.put((-max_height, max_height))
            cnt += 1
        else:
            new_height = max_height // 2
            queue.put((-new_height, new_height))
            cnt += 1

if __name__ == '__main__':
    main()
'''