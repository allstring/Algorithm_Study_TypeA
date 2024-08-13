import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**8)  # 재귀 한도를 높여 깊은 재귀 호출을 허용
threshold = 1000000  # 모듈러 연산을 위한 상수 값

def recursive(A, DP):
    if A in DP:  # 이미 계산된 값이 DP에 있으면 그 값을 반환
        return DP[A]
    if(A[0] == '0'):  # 숫자가 0으로 시작하면 올바르지 않은 암호이므로 0 반환
        return 0 
    
    # 첫 번째 문자로 시작하는 부분과 그 나머지 문자열을 재귀적으로 계산하여 답을 구함
    tmpAnswer = (recursive(A[0:1], DP) * recursive(A[1:], DP)) % threshold
    
    if len(A) == 2:  # 문자열 길이가 2일 경우, 계산된 답을 DP에 저장하고 반환
        DP[A] = tmpAnswer
        return tmpAnswer
    
    if tmpAnswer == 0:  
        # 첫 번째 부분이 0일 경우, 두 자리 수를 기준으로 다시 계산
        tmpAnswer += (recursive(A[0:2], DP) * recursive(A[2:], DP)) % threshold
    else:  
        # 두 자리 수와 한 자리 수의 조합을 고려하여 답을 계산
        tmpAnswer += ((recursive(A[0:2], DP) - (recursive(A[0:1], DP) * recursive(A[1:2], DP))) * recursive(A[2:], DP)) % threshold
    
    DP[A] = tmpAnswer % threshold  # 결과를 DP에 저장
    return DP[A]

def main():
    S = input().strip()  # 입력된 문자열에서 공백을 제거
    DP = {"0": 0, "10": 1, "20": 1}  # 기본적인 DP 초기값 설정
    
    for i in range(1, 10):
        DP[str(i)] = 1  # 1부터 9까지는 모두 1로 초기화
    
    for i in range(11, 20):
        DP[str(i)] = 2  # 11부터 19까지는 모두 2로 초기화
    
    for i in range(21, 27):
        DP[str(i)] = 2  # 21부터 27까지는 모두 2로 초기화
    
    print(recursive(S, DP))  # 결과 출력

if __name__ == "__main__":
    main()  # 메인 함수 실행