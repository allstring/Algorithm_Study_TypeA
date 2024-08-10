def count_tiling(n):
    tile_ways = [0] * 251
    tile_ways[0] = 1
    tile_ways[1] = 1 # 1) 2x1 세로로 긴 타일
    tile_ways[2] = 3 # 1) 2x1 세로로 긴 타일 두개 2) 1x2 가로로 긴 타일 두개 3) 2x2 정사각형 타일 두 개
    for i in range(3, n+1):
        # 남은 공간이 2x1일 때
        # (2x1 세로로 긴 타일을 붙이는 한 가지 방법)
        # 남은 공간이 2x2일 때 (2가지 방법)
        #   1) 1x2 가로로 긴 타일 두 개 붙이기
        #   2) 2x2 정사각형 타일 붙이기
        #   ** 2x1 세로로 긴 타일을 붙이는 방법을 카운팅하지 않음 ! -> n-1에서 이미 카운팅 되어있기 때문
        tile_ways[i] = tile_ways[i-1] + 2 * tile_ways[i-2]
    return tile_ways[n]
def main():
    while True:
        try:
            n = int(input())
            print(count_tiling(n))
        except Exception:
            break

if __name__ == '__main__':
    main()