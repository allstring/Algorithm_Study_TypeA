from itertools import permutations

def make_nums():
    numbers = set()
    for length in range(1, 11):  # 숫자는 최대 10자리
        for nums in permutations('0123456789', length):
            numbers.add(int(''.join(nums)))
    return sorted(numbers)  # 정렬

target = int(input())

numbers = make_nums()

ans = None
min_difference = float('inf')

for number in numbers:
    difference = abs(number - target)
    if difference < min_difference or (difference == min_difference and (ans is None or number < ans)):
        ans = number
        min_difference = difference

print(ans)
