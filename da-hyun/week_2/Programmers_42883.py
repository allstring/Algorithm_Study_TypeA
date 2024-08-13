def solution(number, k):
    stack = []
    
    for num in number:
        while stack and k > 0 and stack[-1] < num:  # 현재 숫자가 스택의 마지막 숫자보다 크면
            stack.pop()  # 스택에서 제거
            k -= 1  # 제거한 만큼 k 감소
        stack.append(num)  # 현재 숫자를 스택에 추가
    if k > 0:  # 남은 k가 있다면
        stack = stack[:-k]  # 남은 k만큼 뒤에서 제거
    
    return ''.join(stack)  # 스택을 문자열로 변환하여 반환
