import sys
input = sys.stdin.readline

def main():
    N = int(input()) 
    maxNum = -1  # 최대 숫자 초기화
    count = 0  # 연속된 숫자의 수 초기화
    for _ in range(N):
        num = int(input()) 
        if num > maxNum:
            if num > maxNum + 1: 
                count = 0  # 연속된 숫자가 아닌 경우 카운트 초기화
            maxNum = num  # 최대 숫자 갱신
            count += 1  # 연속된 숫자 수 증가
    print(N - count)

if __name__ == "__main__":
    main()