budget = int(input())
season = input()
fishermen = int(input())

rent = 0
discount = 0
add_discount = 0

if season == "Spring":
    rent += 3000
    if fishermen < 7:
        discount = 10 / 100
    elif fishermen < 12:
        discount = 15 / 100
    else:
        discount = 25 / 100
if season == "Summer":
    rent += 4200
    if fishermen < 7:
        discount = 10 / 100
    elif fishermen < 12:
        discount = 15 / 100
    else:
        discount = 25 / 100
if season == "Autumn":
    rent += 4200
    if fishermen < 7:
        discount = 10 / 100
    elif fishermen < 12:
        discount = 15 / 100
    else:
        discount = 25 / 100
if season == "Winter":
    rent += 2600
    if fishermen < 7:
        discount = 10 / 100
    elif fishermen < 12:
        discount = 15 / 100
    else:
        discount = 25 / 100
if season != "Autumn":
    if fishermen % 2 == 0:
        add_discount = 5 / 100

money = rent - (rent * discount)
total = money - (money * add_discount)

if budget >= total:
    print(f"Yes! You have {budget - total:.2f} leva left.")
else:
    print(f"Not enough money! You need {total - budget:.2f} leva.")
