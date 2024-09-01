# 친구
# Silver II

"""
풀이 설명 :
    문제에서 제시하는 '2-친구'는 본인과 직접 친구이거나, 한 다리 건너 아는 친구까지 포함한다.
    사람의 수 N만큼 돌며, 직접적인 친구인 수를 세고, 친구의 친구까지만 세면 각각의 2-친구를 구할 수 있다.
    한 사람의 2-친구를 모두 구했으면, most_famous값과 비교하며 최대값으로 갱신해준다.
"""
def main():
    N = int(input())
    adj_matrix = [list(input().rstrip()) for _ in range(N)]  # 인접 행렬
    most_famous = 0  # 가장 유명한 사람의 2-친구 수
    for i in range(N):
        friends = set()  # i번째 사람의 친구 목록
        for j, is_friend in enumerate(adj_matrix[i]):
            if is_friend == "N": continue  # 친구가 아닌 경우 스킵
            friends.add(j)  # 친구 목록에 추가
        for friend in list(friends):  # 친구들
            for k, is_friend in enumerate(adj_matrix[friend]):  # 친구의 친구 리스트
                if k == i: continue  # 자신인 경우 스킵
                if is_friend == "N": continue  # 친구가 아닌 경우 스킵
                friends.add(k)  # i의 친구 목록에 추가
        most_famous = max(most_famous, len(friends))  # 최댓값 갱신

    print(most_famous)  # 결과 출력


if __name__ == "__main__":
    main()