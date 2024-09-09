def bfs(A, B, C):
    result = set()  # 결과를 저장할 집합
    visited = set()  # 방문한 상태를 저장할 집합
    queue = [(0,0,C)]  # 초기 상태: A와 B는 비어 있고, C는 가득 참
    while queue:
        a, b, c = queue.pop()  # 큐에서 상태를 꺼냄
        if a == 0 : result.add(c)  # A가 비어 있을 때 C의 양을 결과에 추가
        for da, db, dc in [
            # A에서 B로 물을 옮김
            (max(a - (B - b), 0), min(B, a + b), c),
            # A에서 C로 물을 옮김
            (max(a - (C - c), 0), b, min(C, a + c)),
            # B에서 A로 물을 옮김
            (min(A, a + b), max(b - (A - a), 0), c),
            # B에서 C로 물을 옮김
            (a, max(b - (C - c), 0), min(C, b + c)),
            # C에서 A로 물을 옮김
            (min(A, a + c), b, max(c - (A - a), 0)),
            # C에서 B로 물을 옮김
            (a, min(B, b + c), max(c - (B - b), 0))
        ]:
            # 새로운 상태를 아직 방문하지 않았으면 큐에 추가
            if (da, db, dc) not in visited:
                visited.add((da,db,dc))  # 방문 처리
                queue.append((da,db,dc))  # 큐에 추가
    return sorted(result)  # 결과를 정렬하여 반환

def main():
    print(*bfs(*(map(int, input().split()))))  # 입력값을 받아 bfs 함수 호출 후 결과 출력

if __name__ == "__main__": main()  # 메인 함수 호출
