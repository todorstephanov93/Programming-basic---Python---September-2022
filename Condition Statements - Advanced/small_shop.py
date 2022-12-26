product = input()
city = input()
quantity = float(input())

total = 0

if product == "coffee":
    if city == "Sofia":
        total = quantity * 0.5
    elif city == "Plovdiv":
        total = quantity * 0.4
    elif city == "Varna":
        total = quantity * 0.45

if product == "water":
    if city == "Sofia":
        total = quantity * 0.8
    elif city == "Plovdiv":
        total = quantity * 0.7
    elif city == "Varna":
        total = quantity * 0.7

if product == "beer":
    if city == "Sofia":
        total = quantity * 1.2
    elif city == "Plovdiv":
        total = quantity * 1.15
    elif city == "Varna":
        total = quantity * 1.1

if product == "sweets":
    if city == "Sofia":
        total = quantity * 1.45
    elif city == "Plovdiv":
        total = quantity * 1.30
    elif city == "Varna":
        total = quantity * 1.35

if product == "peanuts":
    if city == "Sofia":
        total = quantity * 1.60
    elif city == "Plovdiv":
        total = quantity * 1.50
    elif city == "Varna":
        total = quantity * 1.55

print(total)