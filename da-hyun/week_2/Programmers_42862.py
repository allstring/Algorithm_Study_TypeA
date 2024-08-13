def solution(n, _lost, _reserve):
    answer = n  # 총 학생 수를 기본값으로 설정
    index_reserve = 0
    
    reserve = [x for x in _reserve if x not in _lost]  # 잃어버리지 않은 여분 체육복 리스트
    lost = [x for x in _lost if x not in _reserve]  # 여분이 없는 잃어버린 체육복 리스트
    lost.sort()
    reserve.sort()
    
    for index_lost in range(len(lost)):
        while index_reserve < len(reserve) and reserve[index_reserve] < lost[index_lost] - 1:
            index_reserve += 1  # 잃어버린 학생 앞의 여분 체육복을 건너뜀
        if index_reserve < len(reserve) and lost[index_lost] - 1 <= reserve[index_reserve] <= lost[index_lost] + 1:
            index_reserve += 1  # 여분 체육복을 줄 수 있는 경우
        else:
            answer -= 1  # 체육복을 받지 못한 학생이 있을 경우
    
    return answer
