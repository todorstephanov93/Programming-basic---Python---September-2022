bigger_number = int(input())

while True:
    user_input = input()
    if user_input == "Stop":
        break
    num = int(user_input)
    if num > bigger_number:
        bigger_number = num
print(bigger_number)
