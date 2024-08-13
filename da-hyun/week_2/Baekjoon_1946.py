import sys
input = sys.stdin.readline

def main():
    T = int(input().strip()) 

    for _ in range(T):
        N = int(input().strip())
        applicants = []
        for _ in range(N):
            a, b = map(int, input().strip().split()) 
            applicants.append((a, b))  # 지원자 점수 리스트에 추가
        applicants.sort()  # 첫 번째 점수 기준으로 정렬
        answer = 0  # 선택된 지원자 수 초기화
        tmpB = N + 1  # 두 번째 점수의 기준 초기화 (최대값 + 1로 설정)
        
        for _, b in applicants:
            if b < tmpB:  # 두 번째 점수가 현재 기준보다 작으면
                answer += 1  # 선택된 지원자 수 증가
                tmpB = b  # 기준 점수 갱신
        
        print(answer)

if __name__ == "__main__":
    main()