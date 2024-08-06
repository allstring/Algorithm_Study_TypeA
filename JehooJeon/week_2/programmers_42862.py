def solution(n, lost, reserve):
    
    # lost와 reserve 순서대로 정렬
    lost.sort()
    reserve.sort()
    
    # reserve와 lost의 공통된 번호 제거
    for i in reserve[:]:
        if i in lost:
            reserve.remove(i)
            lost.remove(i)
    
    # 체육복 여벌 있는 학생이 도난당한 학생 빌려주기
    for i in reserve:
        # 앞쪽에 있는 학생부터 빌려주기
        if i-1 in lost:
            lost.remove(i-1)
        # 앞쪽에 있는 학생이 도난당한 학생이 아니면 뒤쪽에 있는 학생 빌려주기
        elif i+1 in lost:
            lost.remove(i+1)    
    
    answer = n - len(lost)
    return answer