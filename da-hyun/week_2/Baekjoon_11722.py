import sys
input = sys.stdin.readline

def upper_bound(nums, target):
    left, right = 0, len(nums)  # 이진 탐색의 시작(left)과 끝(right) 설정
    while left < right:
        mid = left + (right - left) // 2  # 중간 인덱스 계산
        if nums[mid] > target:  # 중간 값이 타겟보다 크면 왼쪽 구간으로 이동
            left = mid + 1
        else:  # 중간 값이 타겟보다 작거나 같으면 오른쪽 구간으로 이동
            right = mid
    return right  # 타겟 값 이상의 첫 번째 인덱스를 반환

def main():
    A = int(input())
    B = list(map(int, input().split()))  
    DP = []  # 증가하는 부분 수열을 저장할 리스트
    for num in B:
        if not DP or DP[-1] > num:  # DP가 비어 있거나 마지막 원소보다 num이 작을 경우
            DP.append(num)  # DP에 num 추가
        else:
            index = min(upper_bound(DP, num), len(DP) - 1)  # upper_bound로 위치 찾기
            DP[index] = num  # 해당 위치에 num을 삽입
    print(len(DP))  # DP의 길이(최종 증가 부분 수열의 길이)를 출력

if __name__ == "__main__":
    main()