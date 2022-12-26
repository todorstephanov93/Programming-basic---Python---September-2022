import sys
num = int(input())

max_value = -sys.maxsize
min_value = sys.maxsize

for i in range(0, num):
    number = int(input())

    if number > max_value:
        max_value = number
    if number < min_value:
        min_value = number

print(f"Max number: {max_value}")
print(f"Min number: {min_value}")