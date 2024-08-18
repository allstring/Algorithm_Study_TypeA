def main():
    R, C = list(map(int, input().split()))

    puzzle = [list(input()) for _ in range(R)]
    words = []
    for r in range(R): #가로방향 단어들
        cross_h = ''.join(puzzle[r]) #배열 -> 문자열
        words_h = cross_h.split('#')
        for word in words_h: #길이가 2이상인 것들만 단어 취급
            if len(word) > 1:
                words.append(word)
    for c in range(C):
        cross = [puzzle[r][c] for r in range(R)]
        cross_v = ''.join(cross) #배열 -> 문자열
        words_v = cross_v.split('#')
        for word in words_v:
            if len(word) > 1:
                words.append(word)

    words.sort()
    print(words[0])

if __name__ == '__main__':
    main()