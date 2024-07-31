dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

def checkTeacher(classRoom, N):
    for i in range(N):
        for j in range(N):
            if(classRoom[i][j] == 'T'):
                for ddx, ddy in zip(dx, dy):
                    nx, ny = i, j
                    while True:
                        nx, ny = nx + ddx, ny + ddy
                        if(nx < 0 or nx >= N or ny < 0 or ny >= N or classRoom[nx][ny] == 'O'): break
                        if(classRoom[nx][ny] == 'S'): return False
    return True
def makeObstacle(N, classRoom):
    for i in range(N*N - 2):
        x1, y1 = i//N, i%N
        if(classRoom[x1][y1] != 'X'): continue
        classRoom[x1][y1] = 'O'
        for j in range(i+1, N*N -1):
            x2, y2 = j//N, j%N
            if(classRoom[x2][y2]!= 'X'): continue
            classRoom[x2][y2] = 'O'
            for k in range(j+1, N*N):
                x3, y3 = k//N, k%N
                if(classRoom[x3][y3]!= 'X'): continue
                classRoom[x3][y3] ='O'
                if(checkTeacher(classRoom, N)): return True
                classRoom[x3][y3] = 'X'
            classRoom[x2][y2] = 'X'
        classRoom[x1][y1] = 'X'

def main():
    N = int(input())
    classRoom = [input().split() for _ in range(N)]

    if makeObstacle(N, classRoom): print("YES")
    else: print("NO")
if __name__ == "__main__":
    main()