# 배열 돌리기 4
# Gold IV
# https://www.acmicpc.net/problem/17406

"""
풀이 설명 :
    알고리즘
        1. dfs(recursion)을 이용하여 회전 정보들로 순열을 구성
        2. 순열의 길이가 주어진 전체 회전 정보들의 길이와 동일하다면
        3. 구성 된 회전 순열로 배열을 회전시킨다.
        4. 하나의 회전 순열에 대하여 회전을 모두 마친 뒤, 배열의 값을 계산한다.
        5. 배열의 값을 기존의 최솟값과 비교해가며, 최종적인 최솟값을 찾는다.
"""
import copy

def cal_matrix_value(matrix:list) -> int:
    """
    "크기가 N×M 크기인 배열 A가 있을때, 배열 A의 값은 각 행에 있는 모든 수의 합 중 최솟값을 의미한다."
    문제에서 주어진 배열의 값을 구하는 함수
    :param matrix: 값을 구할 배열
    :return: 배열의 값
    """
    min_value = 100*50  # 각 행의 최대 값
    for row in matrix:
        min_value = min(min_value, sum(row))

    return min_value


def rotate_matrix(matrix:list, rotate:list)->list:
    """
    "회전 연산은 세 정수 (r, c, s)로 이루어져 있고,
    가장 왼쪽 윗 칸이 (r-s, c-s), 가장 오른쪽 아랫 칸이 (r+s, c+s)인 정사각형을
    시계 방향으로 한 칸씩 돌린다는 의미이다"
    주어진 배열(matrix)을 rotate에 기반하여 회전시키는 함수.
    :param matrix: 회전 될 배열(list)
    :param rotate: (r,c,s)로 구성 된 회전 정보
    :return: 회전된 함수
    """
    r, c, s = rotate
    left_top = (r-s-1, c-s-1)  # 회전 할 부분의 좌측 상단
    right_bottom = (r+s-1, c+s-1)  # 회전 할 부분의 우측 하단

    n = 2*s + 1  # submatrix 크기  (편의상 회전할 부분을 전체 matrix의 sub-matrix로 본다.)
    sub_matrix = [[0 for _ in range(n)] for _ in range(n)]  # sub-matrix 선언
    for i in range(n):
        for j in range(n):
            sub_matrix[i][j] = matrix[left_top[0]+i][left_top[1]+j]  # submatrix 초기화

    # sub-matrix를 회전시키는 반복문
    # 4개의 edge에 대해 나누어 회전
    # 왼쪽 edge부터 올라가면서 값을 대체하기 때문에 'L -> B -> R -> T' 순으로 회전
    for depth in range((n+1) // 2):
        tmp = sub_matrix[depth][depth]
        is_move = False
        # 왼쪽 엣지
        for i in range(depth, n-depth-1):
            sub_matrix[i][depth] = sub_matrix[i+1][depth]
            is_move = True
        # 아래쪽 엣지
        for j in range(depth, n-depth-1):
            sub_matrix[n-depth-1][j] = sub_matrix[n-depth-1][j+1]
            is_move = True
        # 오른쪽 엣지
        for i in range(n-depth-1, depth, -1):
            sub_matrix[i][n-depth-1] = sub_matrix[i-1][n-depth-1]
            is_move = True
        # 위쪽 엣지
        for j in range(n-depth-1, depth, -1):
            sub_matrix[depth][j] = sub_matrix[depth][j-1]
            is_move = True
        if is_move:
            sub_matrix[depth][depth+1] = tmp

    # 회전시킨 sub-matrix를 matrix에 병합시킨다. (부품 교체)
    for i, row in enumerate(range(left_top[0], right_bottom[0]+1)):
        for j, col in enumerate(range(left_top[1], right_bottom[1]+1)):
            matrix[row][col] = sub_matrix[i][j]

    return matrix


def recursion(matrix:list, rotates:list, used:list, is_used:list):
    """
    회전 정보들로 순열을 만들고, 만들어진 순열을 기반으로 회전 연산 수행 후 값을 계산하는 사실상 본체 함수
    :param matrix: 피연산자 (배열)
    :param rotates: 전체 회전 정보 리스트
    :param used: 사용 된(순열에 이미 포함된) 회전 정보
    :param is_used: 회전 정보가 사용 여부
                    (used를 set으로 두고, is_used를 없애도 되지만,
                    어차피 회전 정보가 6개 이하라 크게 영향을 주진 않을 것 같다.

    :return: None
    """
    global min_
    if len(used) == len(rotates):
        # matrix를 그대로 rotate_matrix함수에 넣거나, 얕은 복사(.copy())를 사용하게 되면
        # 리스트 주소에 접근해서 회전을 시켜버리기 때문에 제대로 회전이 되지 않는다. (다음 회전 순열에 영향을 미침)
        rotated = copy.deepcopy(matrix)
        for r in used:  # 만들어진 회전 순열을 순회
            rotated = rotate_matrix(rotated, rotates[r])  # 배열 회전 연산
        matrix_value = cal_matrix_value(rotated)  # 배열 값 계산
        min_ = min(min_, matrix_value)  # 글로벌 변수 min_ 과 값을 비교하고, 갱신
        return  # 함수 반환

    # 회전 순열을 만드는 코어 반복문
    for i in range(len(rotates)):
        if not is_used[i]:  # 사용되지 않은 회전 정보에 대하여
            is_used[i] = True  # 사용 표시
            used.append(i)  # 사용 리스트 추가
            recursion(matrix, rotates, used, is_used)  # 갱신된 정보들로 재귀 호출
            # 여기서 아래 두가지 원복 코드는 i+1번째 부터 시작하는 순열에 대하여
            # i 번째 회전 정보가 미리 들어가 있는 것을 방지 (사용한 적 없음을 표시하는 것)
            is_used[i] = False  # 사용 표시 원복
            used.pop()  # 사용 리스트 원복



def main():
    # N, M: 배열 크기, K: 회전 연산 개수
    N, M, K = map(int, input().split())
    matrix = [list(map(int, input().split())) for _ in range(N)]  # 배열 A
    rotates = [list(map(int, input().split())) for _ in range(K)]  # K개의 회전 연산 정보(r,c,s)
    is_used = [False for _ in range(K)]
    recursion(matrix=matrix, rotates=rotates, used=[], is_used=is_used)

    print(min_)

if __name__ == "__main__":
    min_ = 100*50  # 배열의 한 행이 가질 수 있는 최댓값
    main()
