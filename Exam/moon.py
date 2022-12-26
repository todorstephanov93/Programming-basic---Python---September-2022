from math import ceil
average_speed = float(input())
liter_100 = float(input())

length = 384400
total_length = length * 2

time = ceil(total_length / average_speed)
total_time = time + 3

total_fuel = (liter_100 * total_length) / 100

print(total_time)
print(int(total_fuel))