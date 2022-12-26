specie_flowers = input()
count_flowers = int(input())
budget = int(input())

total_price = 0

if specie_flowers == "Roses":
    if count_flowers > 80:
        total_price = (count_flowers * 5) - (count_flowers * 5 * 0.1)
    else:
        total_price = count_flowers * 5
if specie_flowers == "Dahlias":
    if count_flowers > 90:
        total_price = (count_flowers * 3.8) - (count_flowers * 3.8 * 0.15)
    else:
        total_price = count_flowers * 3.8
if specie_flowers == "Tulips":
    if count_flowers > 80:
        total_price = (count_flowers * 2.8) - (count_flowers * 2.8 * 0.15)
    else:
        total_price = count_flowers * 2.8
if specie_flowers == "Narcissus":
    if count_flowers < 120:
        total_price = (count_flowers * 3) + (count_flowers * 3 * 0.15)
    else:
        total_price = count_flowers * 3
if specie_flowers == "Gladiolus":
    if count_flowers < 80:
        total_price = (count_flowers * 2.5) + (count_flowers * 2.5 * 0.2)
    else:
        total_price = count_flowers * 2.5

if budget >= total_price:
    print(f"Hey, you have a great garden with {count_flowers} {specie_flowers} and {budget - total_price:.2f} leva left.")
else:
    print(f"Not enough money, you need {total_price - budget:.2f} leva more.")
