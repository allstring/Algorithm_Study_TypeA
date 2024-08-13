# 1706. 크로스워드

import sys

sys.stdin = open('input.txt', 'r')

'''
    풀이방법 : 가로와 세로로 연속되어 있는 단어를 추출하는 문제이기 때문에 단어의 출발 지점을 파악하는 것이 중요하다고 생각함
    가로의 경우에는 가장 왼쪽에 있는 알파벳부터 돌아가면서 #이 아닌 경우 word의 시작지점으로 판단하고 초기화된 word에 하나씩 붙이기 시작
    만약 #을 만나면, 2개 이상의 알파벳이 붙은 단어일 경우 가능한 단어 list에 추가함
    #을 만난 뒤에도 다시 단어가 시작될 수 있기 때문에 word를 초기화 해주고 다시 진행
    세로의 경우에는 가로와 마찬가지로 진행하되 위에서 아래 순서대로 진행함
    가능한 모든 단어 list를 형성하고난 뒤에, sort()를 통해 정렬하고 결과를 출력

    문제파악 : 행과 열이 2이상 20이하이기 때문에 충분히 모든 경우의 수를 파악할 수 있다고 생각함
    bfs를 사용하고자 해보았는데, 단어의 시작지점을 파악하기 어렵다고 생각해서 pass -> 가능한지 여부 궁금함
    def main() 사용하니까 시간이 112ms -> 108ms로 미세하게 줄어듦

    단점 : 메모리를 많이 잡아먹고, 코드가 복잡하기 때문에 단순화가 필요하다고 생각됨
'''


def main():
    # R: 퍼즐의 줄 개수, C: 각 줄의 개수
    # 2 <= R, C <= 20
    R, C = map(int, input().split())
    crosswords = [list(input()) for _ in range(R)]

    # word_list: 가능한 모든 단어를 담아낼 리스트
    word_list = []

    # 가로로 되어있는 단어 추출
    for crossword in crosswords:
        # 단어를 만들기 위한 word 초기화
        word = ''
        # 가로 알파벳을 돌면서 확인
        for alphabet in crossword:
            # 만약 #이 나타나는 경우
            if alphabet == '#':
                # 지금까지 만들어진 단어가 2자리 이상일 경우 list에 추가
                if len(word) >= 2:
                    word_list.append(word)
                # #을 지나고 다시 word를 초기화
                word = ''
                continue
            # 만약 #이 아닌 경우에는 word에 알파벳 더해서 단어 형성
            word += alphabet
        # 만들어진 단어가 2자리 이상일 경우 list에 추가
        if len(word) >= 2:
            word_list.append(word)

    # 세로로 되어있는 단어 추출
    # 가로와 마찬가지로 진행하되, 행이 아니라 열 순서로 진행
    for i in range(C):
        word = ''
        for j in range(R):
            if crosswords[j][i] == '#':
                if len(word) >= 2:
                    word_list.append(word)
                word = ''
                continue
            word += crosswords[j][i]
        if len(word) >= 2:
            word_list.append(word)

    # 가능한 모든 단어를 사전순서대로 정렬
    word_list.sort()
    print(word_list[0])


if __name__ == "__main__":
    main()