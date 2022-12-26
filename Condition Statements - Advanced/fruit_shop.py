fruit = input()
day = input()
quantity = float(input())

total = 0

if day == "Monday"\
        or day == "Tuesday"\
        or day == "Wednesday"\
        or day == "Thursday"\
        or day == "Friday":
    if fruit == "banana":
        total = 2.5 * quantity
    elif fruit == "apple":
        total = 1.2 * quantity
    elif fruit == "orange":
        total = 0.85 * quantity
    elif fruit == "grapefruit":
        total = 1.45 * quantity
    elif fruit == "kiwi":
        total = 2.7 * quantity
    elif fruit == "pineapple":
        total = 5.5 * quantity
    elif fruit == "grapes":
        total = 3.85 * quantity
elif day == "Saturday"\
        or day == "Sunday":
    if fruit == "banana":
        total = 2.7 * quantity
    elif fruit == "apple":
        total = 1.25 * quantity
    elif fruit == "orange":
        total = 0.9 * quantity
    elif fruit == "grapefruit":
        total = 1.6 * quantity
    elif fruit == "kiwi":
        total = 3 * quantity
    elif fruit == "pineapple":
        total = 5.6 * quantity
    elif fruit == "grapes":
        total = 4.2 * quantity
if total == 0:
    print("error")
else:
    print(f"{total:.2f}")
