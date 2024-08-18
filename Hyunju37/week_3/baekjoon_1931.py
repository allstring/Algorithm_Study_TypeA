import sys
input = sys.stdin.readline
N = int(input())
meetings = [list(map(int, input().split())) for _ in range(N)]
meetings.sort(key=lambda x:(x[1],x[0])) #끝나는 시간 기준으로 정렬, 같으면 시작시간 빠른순서대로
count = 1
end_time = meetings[0][1] #가장 먼저 끝나는 회의의 끝나는 시간
for start, end in meetings[1:]:
    if start >= end_time:
        count += 1
        end_time = end
print(count)
