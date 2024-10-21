# 17406. 배열 돌리기 4

import sys
sys.stdin = open('input.txt', 'r')

from copy import deepcopy
from itertools import permutations

def rotate(arr, start, end):
    # arr_copy: arr 원본 값 저장용 리스트
    arr_copy = deepcopy(arr)
    x = start.copy()
    y = end.copy()

    # 만약, start와 end가 같아지면 정지
    # 홀수 * 홀수 형태이기 때문에 마지막에는 무조건 시작과 끝이 같아짐
    while x != y:
        # → 방향 이동
        for i in range(x[1], y[1]):
            arr[x[0]][i + 1] = arr_copy[x[0]][i]
        # ↓ 방향 이동
        for i in range(x[0], y[0]):
            arr[i + 1][y[1]] = arr_copy[i][y[1]]
        # ← 방향 이동
        for i in range(x[1] + 1, y[1] + 1):
            arr[y[0]][i - 1] = arr_copy[y[0]][i]
        # ↑ 방향 이동
        for i in range(x[0] + 1, y[0] + 1):
            arr[i - 1][x[1]] = arr_copy[i][x[1]]

        x[0], x[1] = x[0] + 1, x[1] + 1
        y[0], y[1] = y[0] - 1, y[1] - 1

    return

def arr_min_sum(arr, N):
    sum_list = []
    for i in range(N):
        sum_list.append(sum(arr[i]))
    return min(sum_list)

def main():
    # N, M: 배열 A의 크기, K: 회전 연산의 개수
    N, M, K = map(int, input().split())
    # arr: 배열 A
    arr = [list(map(int, input().split())) for _ in range(N)]
    # rscs: 회전 연산의 정보 리스트
    rscs = [list(map(int, input().split())) for _ in range(K)]
    # rotations: 각 회전 연산의 가장 왼쪽 윗 칸(r-s, c-s), 가장 오른쪽 아랫 칸(r+s, c+s)
    # 차이가 2s 이므로 2s+1개 -> 회전 배열의 영역은 무조건 홀수 * 홀수 형태
    rotations = [[[rsc[0]-rsc[2]-1, rsc[1]-rsc[2]-1], [rsc[0]+rsc[2]-1, rsc[1]+rsc[2]-1]] for rsc in rscs]
    # 회전 연산의 순서 정하기
    rotate_order = permutations(rotations, K)

    result = float('inf')
    for orders in rotate_order:
        arr_rotate = deepcopy(arr)
        for order in orders:
            rotate(arr_rotate, order[0], order[1])
        arr_min = arr_min_sum(arr_rotate, N)
        result = min(result, arr_min)

    print(result)

if __name__ == "__main__":
    main()