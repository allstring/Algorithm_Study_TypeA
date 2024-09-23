# 숫자 조각
# Silver I

from collections import deque


def main():
    N = input()
    # print(list(N))
    K = len(N)
    if K > 9:
        print(9876543210)
        return
    int_N = int(N)
    list_N = list(N)
    list_N.reverse()

    q = deque([i for i in range(10)])
    used = set()
    result = ''
    while list_N:
        n = int(list_N.pop())
        if n not in used:
            used.add(n)
            result += str(n)
        else: # n in used:
            if n > 5:
                t = q.pop()
                result += str(t)
            else:
                t = q.popleft()
                result += str(t)

    print(int(result))
    return


if __name__ == "__main__":
    main()