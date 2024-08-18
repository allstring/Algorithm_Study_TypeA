# 퍼즐에서 가장 짧은 단어를 찾는 함수
def find_smallest_word(puzzle, R, C):
    words = []
    
    for row in puzzle:  # 행별로 #을 기준으로 단어 분리
        words.extend(row.split('#'))
    
    for col in range(C):  # 열별로 #을 기준으로 단어 분리
        column_word = []
        for row in range(R):
            column_word.append(puzzle[row][col])
        words.extend(''.join(column_word).split('#'))
    
    valid_words = [word for word in words if len(word) >= 2]  # 길이가 2 이상인 단어만 유효

    return min(valid_words)  # 사전순으로 가장 앞에 있는 단어 반환

def main():
    R, C = map(int, input().split())  # 퍼즐의 행과 열 입력
    puzzle = [input().strip() for _ in range(R)]  # 퍼즐 내용 입력
    
    print(find_smallest_word(puzzle, R, C))  # 가장 짧은 단어 출력

if __name__ == "__main__":
    main()
