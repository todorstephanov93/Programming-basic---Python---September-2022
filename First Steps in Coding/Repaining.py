quantity_nylon = int(input())
quantity_paint = int(input())
quantity_thinner = int(input())
work_hours = int(input())

price_nylon = 1.50
price_paint = 14.50
price_thinner = 5

add_paint = quantity_paint * (10/100)
add_nylon = 2
bags = 0.40

price_materials = (((add_nylon + quantity_nylon) * price_nylon) + ((add_paint + quantity_paint) * price_paint) + (price_thinner * quantity_thinner) + bags)
price_work_one_hour = price_materials * (30/100) * work_hours
price_total = price_materials + price_work_one_hour

print(price_total)
