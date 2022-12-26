child = 0
human = 0

while True:
    user_input = input()
    if user_input == "Christmas":
        break
    years = int(user_input)
    if years <= 16:
        child += 1
    else:
        human += 1
price_toys = child * 5
price_human = human * 15
print(f"Number of adults: {human}")
print(f"Number of kids: {child}")
print(f"Money for toys: {price_toys}")
print(f"Money for sweaters: {price_human}")
