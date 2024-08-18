# 주어진 수식을 계산하여 최대 값을 찾는 함수
answer = -float('inf')

# 세 개의 연속된 숫자와 연산자를 계산하는 함수
def checkThree(equation, N, index):
    if(index <= N-3):
        if equation[index+1] == '+': return int(equation[index]) + int(equation[index+2])
        if equation[index+1] == '-': return int(equation[index]) - int(equation[index+2])
        if equation[index+1] == '*': return int(equation[index]) * int(equation[index+2])
    return int(equation[index])

# 재귀적으로 수식을 계산하여 최대 값을 갱신하는 함수
def recursive(equation, N, sum, index):
    global answer
    if index >= N-1:
        answer = max(answer, sum)  # 계산된 값으로 최대 값 갱신
        return
    if equation[index+1] == '+':
        recursive(equation, N, sum+int(equation[index+2]), index+2)
        recursive(equation, N, sum+checkThree(equation,N,index+2), index+4)
        return
    if equation[index+1] == '-':
        recursive(equation, N, sum-int(equation[index+2]), index+2)
        recursive(equation, N, sum-checkThree(equation,N,index+2), index+4)
        return
    if equation[index+1] == '*':
        recursive(equation, N, sum*int(equation[index+2]), index+2)
        recursive(equation, N, sum*checkThree(equation,N,index+2), index+4)
        return

def main():
    N = int(input())  # 수식의 길이 입력
    equation = input()  # 수식 입력
    recursive(equation, N, int(equation[0]), 0)  # 수식의 첫 번째 문자로 재귀 시작
    recursive(equation, N, checkThree(equation, N, 0), 2)
    print(answer)  # 최대 값 출력

if __name__ == "__main__":
    main()
