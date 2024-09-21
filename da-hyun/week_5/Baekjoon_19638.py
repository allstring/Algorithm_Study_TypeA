from queue import PriorityQueue

def main():
    # 입력값 받기: N(거인의 수), Hcenti(목표 키), T(횟수 제한)
    N, Hcenti, T = map(int, input().split())
    
    # 우선순위 큐 생성 (내림차순을 위해 음수 값으로 저장)
    queue = PriorityQueue()
    for _ in range(N):
        queue.put(-int(input()))  # 거인의 키를 음수로 저장
    
    # T번의 번개 사용 시도
    for count in range(T):
        tmpHeight = queue.get()  # 가장 큰 키의 거인 꺼내기
        if -tmpHeight < Hcenti:  # 거인의 키가 목표보다 작으면 종료
            print(f"YES\n{count}")
            return
        elif -tmpHeight == 1:  # 더 이상 줄일 수 없는 경우 종료
            print(f"NO\n{-tmpHeight}")
            return
        # 키를 반으로 줄여 다시 큐에 넣기
        queue.put(-(-tmpHeight // 2))
    
    # T번 이후 최종 검증
    tmpHeight = queue.get()
    if -tmpHeight < Hcenti:  # 거인의 키가 목표보다 작으면 성공
        print(f"YES\n{count+1}")
    else:  # 실패 시 가장 큰 거인의 키 출력
        print(f"NO\n{-tmpHeight}")

if __name__ == "__main__":
    main()