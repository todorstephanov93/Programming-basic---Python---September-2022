chicken_menu = int(input())
fish_menu = int(input())
vegan_menu = int(input())

chicken_price = 10.35
fish_price = 12.40
vegan_price = 8.15
delivery = 2.50

price_food = ((chicken_menu * chicken_price) + (fish_menu * fish_price) + (vegan_menu * vegan_price))
price_desert = (price_food * 20 / 100)
total_price = price_food + price_desert + delivery

print(total_price)
