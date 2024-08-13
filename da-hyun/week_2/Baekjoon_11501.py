def binary_search(DP, target):
    # 이진 탐색을 통해 DP 리스트에서 target이 들어갈 위치를 찾는 함수
    x, y = 0, len(DP) - 1
    while x <= y:
        mid = (x + y) // 2  # 중간 인덱스 계산
        if DP[mid] < target:
            x = mid + 1  # target이 더 크면 오른쪽 부분 탐색
        else:
            y = mid - 1  # target이 작거나 같으면 왼쪽 부분 탐색
    return x  # 삽입할 위치 반환

def main():
    T = int(input())
    for test_case in range(T):
        N = int(input())
        nums = list(map(int, input().split())) 
        
        tmpMaxNum = -1  # 현재까지의 최대 숫자 초기화
        answer = 0  # 이익을 저장할 변수 초기화

        for index in range(N-1, -1, -1):  # 리스트를 역순으로 순회
            if nums[index] < tmpMaxNum:
                answer += tmpMaxNum - nums[index]  # 이익 계산
            elif nums[index] >= tmpMaxNum:
                tmpMaxNum = nums[index]  # 현재까지의 최대 숫자 갱신
        print(answer) 

if __name__ == "__main__":
    main()