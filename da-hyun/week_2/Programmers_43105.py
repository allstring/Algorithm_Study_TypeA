def solution(triangle):
    DPList = triangle[0]
    
    # 삼각형의 각 줄에 대해 반복
    for line in triangle[1:]:
        # 새로운 DP 리스트를 생성하여 값을 저장
        tmpDPList = [DPList[0] + line[0]]  # 첫 번째 요소는 항상 이전 줄의 첫 번째 요소와 더해짐
        
        # 중간 요소들은 이전 줄의 두 값 중 큰 값과 현재 값을 더함
        for index in range(1, len(line) - 1):
            tmpDPList.append(max(DPList[index], DPList[index - 1]) + line[index])
        
        # 마지막 요소는 이전 줄의 마지막 요소와 더해짐
        tmpDPList.append(DPList[-1] + line[-1])
        
        # DP 리스트를 현재 줄의 결과로 갱신
        DPList = tmpDPList
        
    return max(DPList)
