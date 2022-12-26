from math import floor
record_sec = float(input())
distance = float(input())
time_in_sec_one_m = float(input())

all_time = distance * time_in_sec_one_m
water_resistence = floor((distance / 15)) * 12.5
total_time = all_time + water_resistence

if total_time < record_sec:
    print(f"Yes, he succeeded! The new world record is {total_time:.2f} seconds.")
else:
    print(f"No, he failed! He was {total_time - record_sec:.2f} seconds slower.")
