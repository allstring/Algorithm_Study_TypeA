# Floyd_Warshall + Brute Force
def main():
    N = int(input())
    friends = [input().strip() for _ in range(N)]
    # 각 사람의 2-친구 수를 계산하기 위한 리스트
    max_two_friends = 0

    for i in range(N):
        # 중복된 계산 배제를 위한 Set 사용
        two_friends = set()
        for j in range(N):
            if friends[i][j] == 'Y':
                two_friends.add(j)
                # set method 중 update를 사용하면 여러개의 
                two_friends.update(k for k in range(N) if friends[j][k] == 'Y' and k != i)
        max_two_friends = max(max_two_friends, len(two_friends))
        
    print(max_two_friends)

if __name__ == "__main__":
    main()
