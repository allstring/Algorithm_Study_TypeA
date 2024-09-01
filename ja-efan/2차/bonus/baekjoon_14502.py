# 연구소
# Gold IV
# https://www.acmicpc.net/problem/14502

# swea 감시 피하기와 문제가 동일 한 것 같다.

from itertools import combinations


def safe_space(lab, n, m):
    cnt = 0
    for r in range(n):
        for c in range(m):
            if lab[r][c] == 0:
                cnt += 1
    return cnt


def bfs(lab, n, m, viruses):
    directions = [[1, 0], [0, 1], [-1, 0], [0, -1]]
    # visited = [[False for _ in range(m)] for _ in range(n)]
    for virus in viruses:
        stack = [virus]
        # visited[virus[0]][virus[1]] = True
        while stack:
            r, c = stack.pop()
            for dr, dc in directions:
                nr = r + dr
                nc = c + dc
                if 0 <= nr < n and 0 <= nc < m and not lab[nr][nc]:
                    lab[nr][nc] = 2
                    stack.append((nr, nc))
    # print(lab)
    return lab


def main():
    N, M = map(int, input().split())  # 연구소 크기
    lab = [list(map(int, input().split())) for _ in range(N)]
    empty_space = []
    viruses = []
    for r in range(N):
        for c in range(M):
            if lab[r][c] == 0:
                empty_space.append((r,c))
            elif lab[r][c] == 2:
                viruses.append((r,c))
    candidate_poses = list(combinations(empty_space, 3))

    max_safe = 0
    for poses in candidate_poses:
        tmp_lab = [row[:] for row in lab]  # deepcopy using slicing
        for r, c in poses:
            tmp_lab[r][c] = 1

        tmp_lab = bfs(tmp_lab, N, M, viruses)
        safes = safe_space(tmp_lab, N, M)
        max_safe = max(max_safe, safes)

    print(max_safe)


if __name__ == "__main__":
    main()