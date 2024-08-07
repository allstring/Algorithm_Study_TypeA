# 가장 긴 감소하는 부분 수열

N = int(input())  # 수열의 크기
A = list(map(int, input().split()))  # 수열 A

LDS_cnt = [0 for _ in range(N)]  # Longest Decreasing Subsequence

for i in range(N):  # 배열 모든 원소 순회
    LDS_cnt[i] = 1  # 현재 원소 기준 LDS 길이를 1로 초기화
    for j in range(i):  # 배열 시작 부분 부터 i의 앞 부분까지 순회
        if A[j] > A[i]:
            # A의 j 번째 값이 i 번째 값보다 작은 경우에
            # A[j]가 마지막인 LDS에 A[i]를 더하면 LDS가 유지된다.
            # 따라서, i 번째 원소를 가지는 LDS를 갱신해준다.
            # j번째 원소를 가지는 LDS에 1을 더한 길이와,
            # 이전 까지 구해온 LDS(i가 들어가는) 길이를 비교하여 업데이트.
            LDS_cnt[i] = max(LDS_cnt[j] + 1, LDS_cnt[i])
# 최대값 출력
print(max(LDS_cnt))
