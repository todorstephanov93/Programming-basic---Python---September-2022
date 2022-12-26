from math import ceil
series = input()
time_episode = int(input())
time_break = int(input())

lunch_time = time_break / 8
recreation = time_break / 4

time_series = time_break - (lunch_time + recreation)

if time_series >= time_episode:
    print(f"You have enough time to watch {series} and left with {ceil(time_series - time_episode)} minutes free time.")
else:
    print(f"You don't have enough time to watch {series}, you need {ceil(time_episode - time_series)} more minutes.")
