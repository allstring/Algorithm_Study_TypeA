# 17406. 배열 돌리기 4

import sys
sys.stdin = open('input.txt', 'r')

from copy import deepcopy

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
    print(rotations)

    def rotate(arr, start, end):
        # arr_copy: arr 원본 값 저장용 리스트
        arr_copy = deepcopy(arr)

        # 만약, start와 end가 같아지면 정지
        # 홀수 * 홀수 형태이기 때문에 마지막에는 무조건 시작과 끝이 같아짐
        while start != end:
            # → 방향 이동
            for i in range(start[1], end[1]):
                arr[start[0]][i+1] = arr_copy[start[0]][i]
            # # ↓ 방향 이동
            # for i in range(start[1], end[1]):
            #     arr[start[0]][i+1] = arr_copy[start[0]][i]
            # # ← 방향 이동
            # for i in range(start[1], end[1]):
            #     arr[start[0]][i+1] = arr_copy[start[0]][i]
            # # ↑ 방향 이동
            # for i in range(start[1], end[1]):
            #     arr[start[0]][i+1] = arr_copy[start[0]][i]

            start[0], start[1] = start[0] + 1, start[1] + 1
            end[0], end[1] = end[0] - 1, end[1] - 1

        return

    print(arr)

    rotate(arr, [0, 1], [4, 5])
    print(arr)

if __name__ == "__main__":
    main()