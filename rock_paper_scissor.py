#Rock Paper Scissor game using python programming
import random2
while True:
    print("\n\t\t\tRock Paper Scissor Game\n")
    print("Select any one choice:\n1. Rock\n2. Paper\n3. Scissor\n4. Exit")
    choice = int(input("Enter your choice: "))
    rand_num = random2.randint(1,4)

    if choice == 1:
        if rand_num == 1:
            print("\nGame Draw!\nYou:Rock vs Computer:Rock\n")
        elif rand_num == 2:
            print("\nComputer Won!\nYou:Rock vs Computer:Paper\n")
        elif rand_num == 3:
            print("\nYou Won!\nYou:Rock vs Computer:Scissor\n")

    elif choice == 2:
        if rand_num == 1:
            print("\nYou Won!\nYou:Paper vs Computer:Rock\n")
        elif rand_num == 2:
            print("\nGame Draw!\nYou:Paper vs Computer:Paper\n")
        elif rand_num == 3:
            print("\nComputer Won!\nYou:Paper vs Computer:Scissor\n")

    elif choice == 3:
        if rand_num == 1:
            print("\nComputer Won!\nYou:Scissor vs Computer:Rock\n")
        elif rand_num == 2:
            print("\nYou Won!\nYou:Scissor vs Computer:Paper\n")
        elif rand_num == 3:
            print("\nGame Draw!\nYou:Scissor vs Computer:Scissor\n")

    elif choice == 4:
        exit()

    else:
        print("\nPlease enter valid choice!\n")