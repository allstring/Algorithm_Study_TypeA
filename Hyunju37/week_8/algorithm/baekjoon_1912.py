import sys

def main():
    def max_subarray_sum(arr):
        max_ending_here = arr[0]
        max_so_far = arr[0]
        for n in arr[1:]:
            # n alone vs n까지 이어지는 부분수열
            max_ending_here = max(n, n+max_ending_here)
            # 지금까지의 최대 부분수열합 값 갱신
            max_so_far = max(max_so_far, max_ending_here)
        return max_so_far

    n = int(sys.stdin.readline())
    arr = list(map(int,sys.stdin.readline().split()))

    print(max_subarray_sum(arr))

if __name__ == "__main__":
    main()