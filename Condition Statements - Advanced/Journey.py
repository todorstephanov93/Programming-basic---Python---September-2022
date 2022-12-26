budget = float(input())
season = input()

destination = None
rest = None
money = 0

if budget <= 100:
    destination = "Bulgaria"
    if season == "summer":
        rest = "Camp"
        money = budget * (30 / 100)
    elif season == "winter":
        rest = "Hotel"
        money = budget * (70 / 100)
elif budget <= 1000:
    destination = "Balkans"
    if season == "summer":
        rest = "Camp"
        money = budget * (40 / 100)
    elif season == "winter":
        rest = "Hotel"
        money = budget * (80 / 100)
else:
    destination = "Europe"
    rest = "Hotel"
    money = budget * (90 / 100)

print(f"Somewhere in {destination}")
print(f"{rest} - {money:.2f}")
