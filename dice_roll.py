#Roll Dice Game in Python
import random2
a = 'y'

print("\t\tDice Roll")
while a == 'y' or a == 'Y':
    rand_num = random2.randint(1,6)

    if rand_num == 1:
        print("-----------")
        print("|         |")
        print("|    0    |")
        print("|         |")
        print("-----------")

    if rand_num == 2:
        print("-----------")
        print("| 0       |")
        print("|         |")
        print("|       0 |")
        print("-----------")

    if rand_num == 3:
        print("-----------")
        print("| 0       |")
        print("|    0    |")
        print("|       0 |")
        print("-----------")

    if rand_num == 4:
        print("-----------")
        print("| 0     0 |")
        print("|         |")
        print("| 0     0 |")
        print("-----------")

    if rand_num == 5:
        print("-----------")
        print("| 0     0 |")
        print("|    0    |")
        print("| 0     0 |")
        print("-----------")

    if rand_num == 6:
        print("-----------")
        print("| 0     0 |")
        print("| 0     0 |")
        print("| 0     0 |")
        print("-----------")

    a = input("\nWould you like to roll one more time?(y/n): ")
    