from math import pow
number = int(input())

for i in range(0, number + 1, 2):
    print(int(pow(2, i)))
