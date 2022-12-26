import sys

input_count = int(input())

max_number = -sys.maxsize
sum_other = 0
for _ in range(input_count):
    num = int(input())

    if num > max_number:
        max_number = num

    sum_other += num

if max_number == sum_other - max_number:
    print("Yes")
    print(f"Sum = {max_number}")
else:
    print("No")
    print(f"Diff = {abs(max_number - (sum_other - max_number))}")
