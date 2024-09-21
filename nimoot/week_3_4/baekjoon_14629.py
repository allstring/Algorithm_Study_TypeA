from itertools import permutations

def make_nums():
    numbers = set()
    for length in range(1, 11):  # 숫자는 최대 10자리
        for nums in permutations('0123456789', length):
            numbers.add(int(''.join(nums)))
    return sorted(numbers)  # 정렬해야 작은 수 반환 가능

target = int(input())

numbers = make_nums()

ans = -1
min_difference = float('inf')

for number in numbers:
    difference = abs(number - target)
    if difference < min_difference:
        ans = number
        min_difference = difference

print(ans)
