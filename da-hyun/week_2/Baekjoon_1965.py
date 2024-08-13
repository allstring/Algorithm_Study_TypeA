def binary_search(DP, target):
    # 이진 탐색으로 DP 리스트에서 target이 삽입될 위치를 찾는 함수
    x, y = 0, len(DP) - 1
    while x <= y:  
        mid = (x + y) // 2  # 중간 인덱스 계산
        if DP[mid] < target:
            x = mid + 1  # target이 더 크면 오른쪽 절반을 탐색
        else:
            y = mid - 1  # target이 작거나 같으면 왼쪽 절반을 탐색
    return x  # 삽입될 위치 반환

def main():
    N = int(input()) 
    boxes = list(map(int, input().split()))
    DP = []  # 최장 증가 부분 수열을 저장할 리스트
    
    # 상자 크기 리스트를 순회하며 DP 리스트를 업데이트
    for box in boxes:
        pos = binary_search(DP, box)  # box가 삽입될 위치 찾기
        if pos < len(DP):
            DP[pos] = box  # 기존 위치에 box 값으로 업데이트
        else:
            DP.append(box)

    print(len(DP))  # 최장 증가 부분 수열의 길이 출력

if __name__ == "__main__":
    main()