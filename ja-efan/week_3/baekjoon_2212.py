# 센서
# Gold V
# https://www.acmicpc.net/problem/2212

def main():
    N = int(input())  # 센서의 개수 (1이상 10,000이하)
    K = int(input())  # 집중국의 개수 (1이상 1,000이하)
    sensor_poses = list(map(int, input().split()))  # N개의 센서의 좌표 (각 좌표의 절대값은 1,000,000이하)
    # 절대값이 주어진다 -> 센서 위치가 원점(0) 기준 왼쪽(음수)일 수 도 있다?

    # 좌표 순(원점 기준 거리)으로 정렬
    sensor_poses.sort()
    # 센서 간 거리 계산
    sensor_diffs = []
    for i in range(N-1):
        sensor_diffs.append(abs(sensor_poses[i+1] - sensor_poses[i]))
    # 센서 간 거리 정렬
    sensor_diffs.sort()
    result = sum(sensor_diffs[:N-K])
    # 왜 sum(sensor_diffs[:-K+1]은 안될까?
    # 결국엔 똑같이 가장 거리가 먼 K-1개를 제외시켜주는 건데 ...
    # K의 범위가 1이상 1,000 이하이기 때문에
    # K가 1인 경우를 생각해보면 제대로 계산이 되지 않는다.

    print(result)


if __name__ == "__main__":
    main()