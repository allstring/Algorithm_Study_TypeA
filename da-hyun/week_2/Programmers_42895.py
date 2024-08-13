def generate_combinations(N, count, memo, results):
    # 다양한 연산 결과의 고유한 조합을 저장할 집합
    current_set = set()
    # N을 count번 반복하여 만든 숫자 추가
    current_set.add(int(str(N) * count))
    
    # 'count'를 나눌 수 있는 모든 부분 집합에 대해 반복
    for i in range(1, count // 2 + 1):
        # 두 부분 집합의 결과가 미리 계산되지 않았다면 계산
        if i not in memo:
            generate_combinations(N, i, memo, results)
        if count - i not in memo:
            generate_combinations(N, count - i, memo, results)
        
        # 두 부분 집합의 숫자를 조합하여 다양한 연산 수행
        for num1 in memo[i]:
            for num2 in memo[count - i]:
                # 덧셈, 뺄셈, 곱셈, 나눗셈(유효한 경우) 결과를 추가
                current_set.add(num1 + num2)
                current_set.add(num1 - num2)
                current_set.add(num2 - num1)
                current_set.add(num1 * num2)
                if num2 != 0:
                    current_set.add(num1 // num2)
                if num1 != 0:
                    current_set.add(num2 // num1)
    
    # 현재 집합의 결과로 `results` 업데이트, 각 숫자를 만드는데 필요한 최소 연산 횟수 기록
    for num in current_set:
        if num in results:
            results[num] = min(count, results[num])
        else:
            results[num] = count
    
    # 현재 집합을 `memo`에 저장하여 나중에 재사용
    memo[count] = current_set

def solution(N, number):
    memo = {}
    results = {}
    
    # N을 최대 8번까지 사용하여 만들 수 있는 모든 숫자 조합 계산
    generate_combinations(N, 8, memo, results)
    
    # 목표 숫자 `number`가 `results`에 있으면 그 값을 반환, 없으면 -1 반환
    return results.get(number, -1)
