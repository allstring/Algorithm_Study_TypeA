import sys
sys.setrecursionlimit(10**8)
input = sys.stdin.readline

def recursive(DP, index):
    if index in DP:  # 이미 계산된 값이 있으면 반환
        return DP[index]
    if index < 0:  # 인덱스가 음수일 경우 0 반환
        return 0
    # 점화식에 따라 재귀적으로 계산
    DP[index] = recursive(DP, index-1) + 2 * recursive(DP, index-2)
    return DP[index]  # 계산된 값을 반환

def main():
    DP = {0: 1, 1: 1, 2: 3}  # 기본 값 설정
    while True:
        try:
            n = int(input())  # 입력값 읽기
        except:
            break  
        print(recursive(DP, n))  # 재귀 함수 호출 후 결과 출력

if __name__ == "__main__":
    main() 