import itertools
from collections import deque

def main():
#enqueue 시점이 헷갈린다
    def spread_virus_bfs(x, y):
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        queue = deque([(x, y)])
        while queue:
            cx, cy = queue.popleft()
            for dx, dy in directions:
                nx, ny = cx + dx, cy + dy
                #queue.append((nx, ny))
                if 0 <= nx < N and 0 <= ny < M:
                    '''if map_copy[nx][ny] == 1:
                        break'''
                    if map_copy[nx][ny] == 0:
                        map_copy[nx][ny] = 2
                        queue.append((nx, ny)) #추가
                        #nx += dx #원래 이동하던 방향으로 한 칸 더
                        #ny += dy #원래 이동하던 방향으로 한 칸 더

    N, M = map(int, input().split())
    v_map = [list(map(int, input().split())) for _ in range(N)]
    empty_spaces = [(i, j) for i in range(N) for j in range(M) if v_map[i][j] == 0]
    possible_wall_combinations = tuple(itertools.combinations(empty_spaces, 3))
    #print(len(possible_wall_combinations))

    max_wall_combinations_idx = -1
    max_safe_zone_count = 0

    for idx, combination in enumerate(possible_wall_combinations):
        map_copy = [row[:] for row in v_map]
        for wall in combination:
            map_copy[wall[0]][wall[1]] = 1  # 벽 설치

        for i in range(N):
            for j in range(M):
                if map_copy[i][j] == 2:
                    spread_virus_bfs(i, j)
        safe_zone_count = sum(cell == 0 for row in map_copy for cell in row)
        if max_safe_zone_count < safe_zone_count:
            max_safe_zone_count = safe_zone_count
            max_wall_combinations_idx = idx
        #max_safe_zone_count = max(safe_zone_count, max_safe_zone_count)

    '''map_copy = [
        [0, 0, 0, 0, 1, 0],
        [1, 0, 0, 1, 0, 2],
        [1, 1, 1, 0, 0, 2],
        [0, 0, 0, 1, 0, 2]
    ]
    for i in range(4):
        for j in range(6):
            if map_copy[i][j] == 2:
                spread_virus_bfs(i, j)

    for row in map_copy:
        print(row)
    safe_zone_count = sum(cell == 0 for row in map_copy for cell in row)
    max_safe_zone_count = max(safe_zone_count, max_safe_zone_count)'''
    #print(possible_wall_combinations[max_wall_combinations_idx])
    print(max_safe_zone_count)

if __name__ == "__main__":
    main()