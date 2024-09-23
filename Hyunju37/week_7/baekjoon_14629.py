def main():
    MAX_NUM = 9876543210
    closest_r = -1
    closest_l = -1

    N = int(input())

    for i in range(N, MAX_NUM+1):
        if len(set(str(i))) == len(str(i)):
            closest_r = i
            break
    for i in range(N-1, -1, -1):
        if len(set(str(i))) == len(str(i)):
            closest_l = i
            break

    if abs(closest_r - N) < abs(closest_l - N):
        print(closest_r)
    else:
        print(closest_l)

if __name__ == "__main__":
    main()