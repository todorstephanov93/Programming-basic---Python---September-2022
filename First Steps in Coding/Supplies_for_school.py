count_pen = int(input())
count_markers = int(input())
l_preparation = int(input())
discount = int(input()) / 100

price_pen = 5.80
price_markers = 7.20
price_preparation = 1.20

sum_without_discount = ((count_pen * price_pen) + (count_markers * price_markers) + (l_preparation * price_preparation))
total_sum = sum_without_discount - (sum_without_discount * discount)

print(total_sum)
