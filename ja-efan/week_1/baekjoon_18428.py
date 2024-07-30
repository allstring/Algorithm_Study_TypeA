# 감시 피하기
# Gold V
# https://www.acmicpc.net/problem/18428

N = int(input())  # 복도(행렬) 크기, 3 <= N <= 6

hall = []
teachers = []  # 선생님 좌표 리스트
students = []  # 학생 좌표 리스트

# 복도 정보
for i in range(N):
    row = list(input().split())
    hall.append(row)
    for j in range(len(row)):
        if row[j] == "T":  # 선생님 좌표 (i, j)
            teachers.append([i, j])
        elif row[j] == "S":  # 학생 좌표 (i, j)
            students.append([i, j])
