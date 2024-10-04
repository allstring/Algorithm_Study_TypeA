def main():

    def rotate(dice_nums, dir):
        temp = dice_nums[:]
        if dir == 1: #동쪽방향으로 회전
            # 동쪽 -> 바닥면, 윗면 -> 동쪽, 서쪽 -> 윗면, 바닥면 -> 서쪽
            temp[0], temp[2], temp[5], temp[4] = temp[2], temp[5], temp[4], temp[0]
        elif dir == 2: #서쪽방향으로 회전
            # 서쪽 -> 바닥면, 윗면 -> 서쪽, 동쪽 -> 윗면, 바닥면 -> 동쪽
            temp[0], temp[4], temp[5], temp[2] = temp[4], temp[5], temp[2], temp[0]
        elif dir == 3: #북쪽방향으로 회전
            # 윗면 -> 북쪽, 남쪽 -> 윗면, 바닥면 -> 남쪽, 북쪽 -> 바닥면
            temp[1], temp[5], temp[3], temp[0] = temp[5], temp[3], temp[0], temp[1]
        elif dir == 4: #남쪽방향으로 회전
            # 윗면 -> 남쪽, 북쪽 -> 윗면, 바닥면 -> 북쪽, 남쪽 -> 바닥면
            temp[3], temp[5], temp[1], temp[0] = temp[5], temp[1], temp[0], temp[3]
        return temp


    N, M, x, y, K = list(map(int, input().split()))
    map_num = []
    for i in range(N):
        map_num.append(list(map(int, input().split())))

    command = list(map(int, input().split()))

    # 바닥면(0) 북쪽(1) 동쪽(2) 남쪽(3) 서쪽(4) 윗면(5)
    dice_nums = [0, 0, 0, 0, 0, 0]

    cur_x = x
    cur_y = y
    if map_num[cur_x][cur_y] == 0:
        map_num[cur_x][cur_y] = dice_nums[0]
    else:
        dice_nums[0] = map_num[cur_x][cur_y]
        map_num[cur_x][cur_y] = 0
    for cmd in command:
        flag = 0
        if cmd == 1:
            if cur_y < M - 1:
                flag = 1
                cur_y += 1
                dice_nums = rotate(dice_nums, cmd)
        elif cmd == 2:
            if cur_y > 0:
                flag = 1
                cur_y -= 1
                dice_nums = rotate(dice_nums, cmd)
        elif cmd == 3:
            if cur_x > 0:
                flag = 1
                cur_x -= 1
                dice_nums = rotate(dice_nums, cmd)
        elif cmd == 4:
            if cur_x < N - 1:
                flag = 1
                cur_x += 1
                dice_nums = rotate(dice_nums, cmd)
        if flag == 1:
            if map_num[cur_x][cur_y] == 0:
                map_num[cur_x][cur_y] = dice_nums[0]
            else:
                dice_nums[0] = map_num[cur_x][cur_y]
                map_num[cur_x][cur_y] = 0
            print(dice_nums[5])

if __name__ == "__main__":
    main()