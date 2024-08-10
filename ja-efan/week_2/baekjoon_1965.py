# 상자 넣기

n = int(input())  # 상자 개수
boxes = list(map(int, input().split()))  # 상자 크기

box_cnt = [0 for _ in range(n)]  # 담을 수 있는 상자를 저장하는 리스트

for i in range(n):  # 모든 상자 순회
    box_cnt[i] = 1  # 현재 상자 기준 1개만 존재
    for j in range(i):  # 첫(idx:0) 상자 부터 i-1번째 상자까지 순회
        if boxes[j] < boxes[i]:  # j번째 상자가 i 번째 상자보다 작은 경우
            box_cnt[i] = max(box_cnt[j]+1, box_cnt[i])  # i번째 상자에 담을 수 있는 상자 개수 업데이트
# 최대 상자 개수 출력
print(max(box_cnt))