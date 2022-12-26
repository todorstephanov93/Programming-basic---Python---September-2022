city = input()
sale = float(input())

commissions = 0
is_invalid_input = False

if city == "Sofia":
    if sale >= 0 and sale <= 500:
        commissions = sale * 0.05
    elif sale >=500 and sale <= 1000:
        commissions = sale * 0.07
    elif sale > 100 and sale <= 10000:
        commissions = sale * 0.08
    elif sale > 10000:
        commissions = sale * 0.12
    else:
        is_invalid_input = True
elif city == "Varna":
    if sale >= 0 and sale <= 500:
        commissions = sale * 0.045
    elif sale >=500 and sale <= 1000:
        commissions = sale * 0.075
    elif sale > 100 and sale <= 10000:
        commissions = sale * 0.1
    elif sale > 10000:
        commissions = sale * 0.13
    else:
        is_invalid_input = True
elif city == "Plovdiv":
    if sale >= 0 and sale <= 500:
        commissions = sale * 0.055
    elif sale >=500 and sale <= 1000:
        commissions = sale * 0.08
    elif sale > 100 and sale <= 10000:
        commissions = sale * 0.12
    elif sale > 10000:
        commissions = sale * 0.145
    else:
        is_invalid_input = True
else:
    is_invalid_input = True
if is_invalid_input:
    print("error")
else:
    print(f"{commissions:.2f}")


