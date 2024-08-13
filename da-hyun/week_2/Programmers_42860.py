def solution(name):
    answer = 0
    for char in name:
        # 각 문자에 대해 'A'에서 해당 문자까지의 최소 이동 횟수를 계산
        answer += min((ord('Z') - ord(char)) + 1, ord(char) - ord('A'))
    
    tmpMove = len(name) - 1  # 기본적으로 오른쪽으로 쭉 이동하는 경우를 가정한 초기값 설정
    for index in range(len(name)):
        next = index + 1
        while next < len(name) and name[next] == 'A':  # 다음에 연속된 'A'가 있는지 확인
            next += 1
        # 현재 위치에서 연속된 'A'를 고려한 최소 이동 횟수 계산
        tmpMove = min(tmpMove, index + len(name) - next + min(index, len(name) - next))
    
    answer += tmpMove  # 이동 횟수를 답에 더함
    return answer
