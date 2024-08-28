import itertools
from collections import deque

'''
1. 벽을 세울 수 있는 모든 조합 찾기
2. 각 조합에 대해서 safe zone을 카운팅
3. 그러기 위해서는 바이러스를 전파시켜야 함 (BFS)
4. 조합들을 순회하면서, max safe zone 찾기
'''

def main():
    #바이러스가 퍼지는 영역을 모두 표시하는 함수(너비 우선 탐색)
    def spread_virus_bfs(x, y):
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        queue = deque([(x, y)])
        while queue:
            cx, cy = queue.popleft()
            for dx, dy in directions:
                nx, ny = cx + dx, cy + dy
                if 0 <= nx < N and 0 <= ny < M:
                    if map_copy[nx][ny] == 0:
                        map_copy[nx][ny] = 2 #바이러스 전파된 위치 표시
                        queue.append((nx, ny)) #enqeue

    N, M = map(int, input().split())
    v_map = [list(map(int, input().split())) for _ in range(N)]
    #0인 부분 좌표들
    empty_spaces = [(i, j) for i in range(N) for j in range(M) if v_map[i][j] == 0]
    #0인 부분 좌표들로 3개 조합들 생성
    possible_wall_combinations = tuple(itertools.combinations(empty_spaces, 3))

    max_wall_combinations_idx = -1 #디버깅용으로 만들어뒀던 변수(최종적으로 가장 유리한 벽 위치들이 어디인지)
    max_safe_zone_count = 0

    for idx, combination in enumerate(possible_wall_combinations):
        map_copy = [row[:] for row in v_map]
        for wall in combination:
            map_copy[wall[0]][wall[1]] = 1  # 벽 설치

        for i in range(N):
            for j in range(M):
                if map_copy[i][j] == 2:
                    spread_virus_bfs(i, j)
        safe_zone_count = sum(cell == 0 for row in map_copy for cell in row) #safe zone 카운트
        '''if max_safe_zone_count < safe_zone_count:
            max_safe_zone_count = safe_zone_count
            max_wall_combinations_idx = idx'''
        max_safe_zone_count = max(safe_zone_count, max_safe_zone_count)

    #print(possible_wall_combinations[max_wall_combinations_idx])
    print(max_safe_zone_count)

if __name__ == "__main__":
    main()