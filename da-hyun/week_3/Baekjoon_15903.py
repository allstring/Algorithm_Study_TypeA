from queue import PriorityQueue

# 주어진 숫자들을 우선순위 큐에 넣고 두 개씩 꺼내 더한 후 큐에 다시 넣어 반복하는 함수
def main():
    n, m = map(int, input().split())  # 숫자의 개수 n과 연산 횟수 m 입력
    numbers = list(map(int, input().split()))  # 숫자들 입력
    answer = sum(numbers)  # 처음에 주어진 숫자들의 합
    que = PriorityQueue()  # 우선순위 큐 생성
    for num in numbers:
        que.put(num)  # 모든 숫자를 큐에 삽입
    for _ in range(m):  # m번 연산 수행
        a, b = que.get(), que.get()  # 큐에서 가장 작은 두 숫자 꺼내기
        answer += a + b  # 더한 값을 총합에 추가
        que.put(a + b)  # 더한 값을 큐에 두 번 삽입
        que.put(a + b)
    print(answer)  # 최종 결과 출력

if __name__ == "__main__":
    main()
