import math
name = input()
budget = float(input())
count_beers = int(input())
count_chips = int(input())

total_price_beers = count_beers * 1.2
price_chips = total_price_beers * (45 / 100)
total_price_chips = math.ceil(count_chips * price_chips)

total_sum = total_price_chips + total_price_beers
if budget >= total_sum:
    print(f"{name} bought a snack and has {budget - total_sum:.2f} leva left.")
else:
    print(f"{name} needs {total_sum - budget:.2f} more leva!")


