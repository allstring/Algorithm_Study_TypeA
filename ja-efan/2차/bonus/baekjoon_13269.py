# boj_13269.py
# 쌓기 나무

def main():
    N, M = map(int, input().split())
    top_view = [list(map(int, input().split())) for _ in range(N)]  # 위에서 바라본 모양
    front_view = list(map(int, input().split()))  # 앞에서 바라본 모양
    right_view = list(map(int, input().split()))  # 오른쪽 옆에서 바라본 모양

    for r in range(N):
        for c in range(M):
            if top_view[r][c] == 0:
                continue
            top_view[r][c] = min(front_view[c], right_view[-(r+1)])

    for i, row in enumerate(top_view):
        if max(row) != right_view[-(i+1)]:
            print(-1)
            return

    for c in range(M):
        col = []
        for r in range(N):
            col.append(top_view[r][c])
        if max(col) != front_view[c]:
            print(-1)
            return

    for row in top_view:
        print(*row)
    return


if __name__ == "__main__":
    main()
