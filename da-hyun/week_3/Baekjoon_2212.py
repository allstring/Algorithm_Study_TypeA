# 센서들의 위치를 정렬하고 가장 큰 간격을 제외하여 전체 거리를 최소화하는 함수
def main():
    N = int(input())  # 센서의 개수
    K = int(input())  # 집중국의 개수
    sensors = list(map(int, input().split()))  # 센서 위치 입력
    sensors.sort()  # 센서 위치 정렬
    distances = []
    for index in range(N-1):  # 센서 간의 거리 계산
        distances.append(sensors[index+1] - sensors[index])
    whole_distance = sum(distances)  # 전체 거리 계산
    distances.sort()  # 거리 오름차순 정렬
    for _ in range(K-1):  # 집중국의 개수에 맞춰 가장 큰 간격 제거
        if not distances: break
        whole_distance -= distances.pop()
    print(whole_distance)  # 최소화된 전체 거리 출력

if __name__ == "__main__":
    main()