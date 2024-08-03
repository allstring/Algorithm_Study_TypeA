# 작업
# Silver I
# https://www.acmicpc.net/problem/21937

from collections import defaultdict
import sys

# recursion stack 제한을 작업의 개수만큼 늘려준다.
sys.setrecursionlimit(10**5)


def dfs(task, task_dict, completed):
    global task_cnt
    if not task_dict[task]:  # 더 이상 선행 작업이 없는 경우
        return  # 함수 리턴
    while task_dict[task]:  # 남은 선행 작업이 있는 경우
        a_task = task_dict[task].pop()  # 선행 작업 하나 겟
        if a_task not in completed:  # 선행 작업이 완료되지 않은 작업이라면
            task_cnt += 1  # 작업 카운트 + 1
            completed.add(a_task)  # 완료 작업 집합에 추가
            dfs(a_task, task_dict, completed)  # 선행 작업 기점으로 Recursion


N, M = map(int, input().split())  # N : 민상이가 작업할 개수, M: 작업 순서 개수
tasks = defaultdict(list)  # 리스트를 기본 값으로 가지는 dict 객체
for _ in range(M):
    # task_B를 하기 위해서는 바로 이전에 작업 task_A를 먼저 해야 한다는 의미.
    # key, value : task_B : task_A
    task_A, task_B = map(int, input().split())
    tasks[task_B].append(task_A)

X = int(input())  # 민상이가 오늘 반드시 끝내야 하는 작업

# 민상이가 작업 X를 하기 위해 먼저 해야하는 일의 개수
task_cnt = 0
# 완료한 일 집합 (in / not in 연산이 list에 비해 빠름)
completed_task = set()
# completed_task.add(X)
dfs(X, tasks, completed_task)
print(task_cnt)