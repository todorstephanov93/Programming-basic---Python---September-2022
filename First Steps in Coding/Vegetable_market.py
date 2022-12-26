vegetables_price = float(input())
fruits_price = float(input())
vegetables_kilo = int(input())
fruits_kilo = int(input())

total_lev = (vegetables_kilo * vegetables_price) + (fruits_kilo * fruits_price)
total_euro = total_lev / 1.94

print(f'{total_euro:.2f}')
