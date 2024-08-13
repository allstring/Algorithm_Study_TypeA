def solution(people, limit):
    answer = 0
    start = 0
    end = len(people) - 1
    people.sort()  # 사람들의 몸무게를 정렬
    while start <= end:
        if start == end:  # 마지막 남은 사람이 혼자 남을 경우
            answer += 1
            break
        remain = limit - people[start]  # 가장 가벼운 사람을 태웠을 때 남은 무게
        while start < end and remain < people[end]:  # 남은 무게에 가장 무거운 사람이 탈 수 없는 경우
            end -= 1  # 무거운 사람 혼자 태움
            answer += 1
        if start < end and remain >= people[end]:  # 남은 무게에 무거운 사람이 탈 수 있는 경우
            end -= 1
        start += 1  # 가벼운 사람을 태우고 다음으로 이동
        answer += 1

    return answer
