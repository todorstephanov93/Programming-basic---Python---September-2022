country_team = input()
souvenir = input()
count_souvenirs = int(input())

price = 0

if country_team == "Argentina":
    if souvenir == "flags":
        price = 3.25
    elif souvenir == "caps":
        price = 7.20
    elif souvenir == "posters":
        price = 5.10
    elif souvenir == "stickers":
        price = 1.25

elif country_team == "Brazil":
    if souvenir == "flags":
        price = 4.20
    elif souvenir == "caps":
        price = 8.50
    elif souvenir == "posters":
        price = 5.35
    elif souvenir == "stickers":
        price = 1.20

elif country_team == "Croatia":
    if souvenir == "flags":
        price = 2.75
    elif souvenir == "caps":
        price = 6.90
    elif souvenir == "posters":
        price = 4.95
    elif souvenir == "stickers":
        price = 1.10

elif country_team == "Denmark":
    if souvenir == "flags":
        price = 3.10
    elif souvenir == "caps":
        price = 6.50
    elif souvenir == "posters":
        price = 4.80
    elif souvenir == "stickers":
        price = 0.90

total_price = price * count_souvenirs

if country_team != "Argentina" and country_team != "Brazil" and country_team != "Croatia" and country_team != "Denmark":
    print("Invalid country!")
elif souvenir != "flags" and souvenir != "caps" and souvenir != "posters" and souvenir != "stickers":
    print("Invalid stock!")
else:
    print(f"Pepi bought {count_souvenirs} {souvenir} of {country_team} for {total_price:.2f} lv.")
