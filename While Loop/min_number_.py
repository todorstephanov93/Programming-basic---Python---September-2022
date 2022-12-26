small_num = int(input())

while True:
    user_input = input()
    if user_input == "Stop":
        break
    num = int(user_input)
    if num < small_num:
        small_num = num
print(small_num)