def main():

    N = int(input())
    K = int(input())
    sensors = list(map(int, input().split()))
    sensors.sort()
    if K > N:
        print(0)
        return
    '''
    배열을 K개의 subarray로 split하기 위해서
    K-1 개의 split 지점(인덱스)들을 선택해야 한다.
    만약에 K=5일 때 split할 지점인 4개의 인덱스 a,b,c,d가 선택되었다고 가정해 보자
    우리가 최소화 해야 할 값은
     (arr[a] - arr[0])
    +(arr[b] - arr[a+1])
    +(arr[c] - arr[b+1])
    +(arr[d] - arr[c+1])
    +(arr[N-1] - arr[d+1])
    이다
    이를 헤쳐서 다시쓰면
     (arr[N-1] - arr[0])
    +(arr[a] - arr[a+1])
    +(arr[b] - arr[b+1])
    +(arr[c] - arr[c+1])
    +(arr[d] - arr[d+1])
    이게 우리가 최소화해야할 값이다
    맨 위인 (arr[N-1] - arr[0]) 은 고정된 값(우리가 바꿀 수 없는 값)
    이고 나머지 값들만 조정 가능하다.
    
    '''
    diff = [0] * (N-1)
    for i in range(N-1):
        diff[i] = sensors[i] - sensors[i+1] #음수 값
    diff.sort()

    ans = sensors[N-1] - sensors[0] #고정된 값
    #나머지 최소 diff들 더해주기
    for i in range(K-1):
        ans += diff[i]

    print(ans)
if __name__ == '__main__':
    main()