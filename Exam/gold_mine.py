for i in range(int(input())):
    average_gold_day = float(input())
    count_day = int(input())
    gold_day_location = 0
    average_day_location = 0
    average = average_day_location / count_day
    for j in range(count_day):
        gold = float(input())
        gold_day_location += gold
        average_day_location += gold_day_location

    if average_day_location >= average_gold_day:
        print(f"Good job! Average gold per day: {average_day_location:.2f}.")
    else:
        print(f"You need {average_gold_day - average_day_location:.2f} gold.")
        break
