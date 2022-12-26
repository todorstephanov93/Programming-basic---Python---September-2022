tank_l = int(input()) / 10
tank_w = int(input()) / 10
tank_h = int(input()) / 10
percent = float(input()) / 100

volume = tank_h * tank_l * tank_w
seat_taken = volume * percent
water = volume - seat_taken

print(water)
