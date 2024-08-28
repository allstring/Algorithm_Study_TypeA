# 카드 합체 놀이
# Silver I
# https://www.acmicpc.net/problem/15903

import heapq
"""
풀이 설명 : 
    카드를 정렬하고, 앞에서 2장을 선택해서 합체하는 과정을 m번 반복한다.
"""
def main():
    n, m = map(int, input().split())  # n: 카드 개수, m: 카드 합체 횟수
    numbers = list(map(int, input().split()))  # 맨 처음 카드 상태
    for i in range(m):  # 카드 합체
        numbers.sort()  # 오름차순 정렬
        merge = numbers[0] + numbers[1]  # 가장 작은 두 수 합체
        numbers[0] = merge  # 합친 수로 업데이트
        numbers[1] = merge  # 합친 수로 업데이트

    print(sum(numbers))

def solution2():
    """
    최소힙 사용한 솔루션
    위 코드랑 시간차가 안난다. 오히려 더 느리다. (128ms vs. 136ms)
    :return: None
    """
    n, m = map(int, input().split())
    numbers = list(map(int, input().split()))
    heapq.heapify(numbers)  # 힙
    for _ in range(m):  # 카드 합체
        merge = heapq.heappop(numbers) + heapq.heappop(numbers)  #  최소힙이므로 2개 가져와서 합체
        heapq.heappush(numbers, merge)  # 합친 수 추가
        heapq.heappush(numbers, merge)  # 합친 수 추가

    print(sum(numbers))

if __name__ == "__main__":
    # main()
    solution2()