from math import floor
count_page = int(input())
pages_one_hour = int(input())
count_days = int(input())

count_page_one_day = count_page / count_days
count_day_hours = count_page_one_day / pages_one_hour

print(f'{floor(count_day_hours)}')
