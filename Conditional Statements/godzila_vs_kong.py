budget = float(input())
extras = int(input())
price_clothes = float(input())

if extras > 150:
    price_clothes = price_clothes - (price_clothes * 0.1)

all_clothes_price = price_clothes * extras
decor = budget * 0.1

total = all_clothes_price + decor

if total > budget:
    print("Not enough money!")
    print(f"Wingard needs {total - budget:.2f} leva more.")
else:
    print("Action!")
    print(f"Wingard starts filming with {budget - total:.2f} leva left.")
