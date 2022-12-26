type_projection = input()
r = int(input())
c = int(input())

full_hall = r * c
price_ticket = 0

if type_projection == "Premiere":
    price_ticket = 12
elif type_projection == "Normal":
    price_ticket = 7.5
elif type_projection == "Discount":
    price_ticket = 5

all_profit = full_hall * price_ticket

print(f"{all_profit:.2f}")
