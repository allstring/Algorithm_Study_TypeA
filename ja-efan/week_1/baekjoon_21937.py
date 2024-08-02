# 작업
# Silver I
# https://www.acmicpc.net/problem/21937

from collections import defaultdict
import sys
sys.setrecursionlimit(10**4)


def dfs(task, task_dict, completed):
    global task_cnt
    if not task_dict[task]:
        return
    while task_dict[task]:
        a_task = task_dict[task].pop()
        if a_task not in completed:
            task_cnt += 1
            completed_task.add(a_task)
            dfs(a_task, task_dict, completed)


N, M = map(int, input().split())  # N : 민상이가 작업할 개수, M: 작업 순서 개수
tasks = defaultdict(list)
for _ in range(M):
    # task_B를 하기 위해서는 바로 이전에 작업 task_A를 먼저 해야 한다는 의미.
    # key, value : task_B : task_A
    task_A, task_B = map(int, input().split())
    tasks[task_B].append(task_A)

X = int(input())  # 민상이가 오늘 반드시 끝내야 하는 작업

# 민상이가 작업 X를 하기 위해 먼저 해야하는 일의 개수
task_cnt = 0
completed_task = set()
dfs(X, tasks, completed_task)
print(task_cnt)