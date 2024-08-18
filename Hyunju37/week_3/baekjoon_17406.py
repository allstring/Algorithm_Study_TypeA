def value_of_array(A, N):
    return max(sum(A[i]) for i in range(N))

def rotate_array(A, r, c, s):
    #(r-s, c-s) ~ (r+s, c+s) 까지의 영역 rotate
    #indices 순회
    for layer in range(1, s+1):
        #layer마다
        #시작지점
        indices = []
        pos = [r - layer - 1, c - layer - 1]
        #오른쪽으로
        for i in range(2 * layer + 1):
            indices.append(tuple(pos))
            pos[1] += 1
        pos[1] -= 1
        #아래쪽으로
        for i in range(2 * layer + 1):
            if i != 0:
                indices.append(tuple(pos))
            pos[0] += 1
        pos[0] -= 1
        #왼쪽으로
        for i in range(2 * layer + 1):
            if i != 0:
                indices.append(tuple(pos))
            pos[1] -= 1
        pos[1] += 1
        #위쪽으로
        for i in range(2 * layer + 1):
            if i != 0:
                indices.append(tuple(pos))
            pos[0] -= 1
        #indices = list(set(indices))
        indices.pop()
        #print(indices)

        #rotating
        tmp = A[indices[-1][0]][indices[-1][1]]
        for index in indices:
            next_temp = A[index[0]][index[1]]
            A[index[0]][index[1]] = tmp
            tmp = next_temp

        for i in range(len(A)):
            for j in range(len(A[0])):
                print(A[i][j], end= ' ')
            print()

    #return A





def main():
    N, M, K = list(map(int, input().split()))
    A = [list(map(int, input().split())) for _ in range(N)]
    ops = [tuple(map(int, input().split())) for _ in range(K)]

    rotate_array(A,3,4,2)
    #rotate_array()


if __name__ == '__main__':
    main()
