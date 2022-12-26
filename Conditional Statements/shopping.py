peters_budget = float(input())
count_graphics_cards = int(input())
count_cpu = int(input())
count_ram = int(input())

total_price_graphic = count_graphics_cards * 250
price_cpu = total_price_graphic * 0.35
total_price_cpu = price_cpu * count_cpu
price_ram = total_price_graphic * 0.1
total_price_ram = price_ram * count_ram

discount = 0
if count_graphics_cards > count_cpu:
    discount = (total_price_graphic + total_price_ram + total_price_cpu) * 0.15

total_price_all = (total_price_graphic + total_price_ram + total_price_cpu) - discount
if peters_budget >= total_price_all:
    print(f"You have {peters_budget - total_price_all:.2f} leva left!")
else:
    print(f"Not enough money! You need {total_price_all - peters_budget:.2f} leva more!")
