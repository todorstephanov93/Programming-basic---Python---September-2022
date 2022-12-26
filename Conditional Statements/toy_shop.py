price_excursion = float(input())
count_puzzles = int(input())
count_speak_dolls = int(input())
count_bears = int(input())
count_minions = int(input())
count_truck_toy = int(input())

puzzles_profit = count_puzzles * 2.6
dolls_profit = count_speak_dolls * 3
bears_profit = count_bears * 4.1
minions_profit = count_minions * 8.20
truck_profit = count_truck_toy * 2

count_toys = count_puzzles + count_speak_dolls + count_bears + count_minions + count_truck_toy

all_profit = puzzles_profit + dolls_profit + bears_profit + minions_profit + truck_profit


if count_toys >= 50:
    all_profit = all_profit - (all_profit * 0.25)

rent = all_profit * 0.1
all_profit_without_rent = all_profit - rent

if all_profit_without_rent >= price_excursion:
    print(f"Yes! {all_profit_without_rent - price_excursion:.2f} lv left.")
else:
    print(f"Not enough money! {price_excursion - all_profit_without_rent:.2f} lv needed.")
