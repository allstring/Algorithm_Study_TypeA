# 크로스워드
# Silver II
# https://www.acmicpc.net/problem/1706
"""
풀이 설명 :
    주어진 크로스워드의 가로방향 단어와 세로 방향 단어를 모두 탐색하여 set()객체로 관리해주고,
    set 객체를 list로 변환해 단순 정렬 후 결과 값 반환.

    낱말이 끝나는 조건을 명시하여 낱말이 끝나면,
    지금까지 모인 알파벳의 길이를 검사하여 최종적으로 낱말 set에 추가해준다.
"""

def main():
    R, C = map(int, input().split())  # 크로스워드 퍼즐 크기
    crosswords = [list(input().strip()) for _ in range(R)]
    words = set()  # 단어 수집 집합(중복 불가)

    # 가로 방향 단어 수집
    for r in range(R):  # 모든 행을 순회
        horizontal_words = ""  # 행의 초기 가로 단어
        for c in range(C):  # 가로 방향 순회
            if c == C or crosswords[r][c] == "#":  # 가로방향의 끝이거나, 금지된 칸인 경우 -> 이전까지의 단어가 끝난다.
                if len(horizontal_words) > 1:  # 단어의 길이가 1 이상 (낱말이기 때문에 1이상)
                    words.add(horizontal_words)  # 단어 집합에 추가
                horizontal_words = ""  # 단어 초기화
            else :
                horizontal_words += crosswords[r][c]  # 계속해서 알파벳 추가
        if len(horizontal_words) > 1:  # 가로 방향 순회 끝나면 길이 검사 후 단어 집합에 추가
            words.add(horizontal_words)

    # 세로 방향 단어 수집 : 가로 방향 단어 수집을 세로로 진행(행과 열 순회 순서(for 문 순서)만 변경)
    for c in range(C):
        vertical_words = ""
        for r in range(R):
            if r == R or crosswords[r][c] == "#":
                if len(vertical_words) > 1:
                    words.add(vertical_words)
                vertical_words = ""
            else :
                vertical_words += crosswords[r][c]
        if len(vertical_words) > 1:
            words.add(vertical_words)

    words = list(words)
    words.sort()
    print(words[0])


if __name__ == "__main__":
    main()