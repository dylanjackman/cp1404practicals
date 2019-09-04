import random
MAX = 45
MIN = 1

quick_pick_count = int(input("How many quick picks would you like? "))
numbers = []
for i in range(quick_pick_count):
    for m in range(0, 6):
        quick_pick = random.randint(MIN, MAX)
        while quick_pick in numbers:
            quick_pick = random.randint(MIN, MAX)
        numbers.append(quick_pick)
    print(*numbers, sep=" ")
    numbers.clear()
