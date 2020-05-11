import random

print("****WELCOME TO DICE STIMULATOR****")
#x=input("Enter y to roll again and N to quit:")
x="y"
while x=="y":
    n=random.randint(1,6)

    if n == 1:
        print("---------")
        print("|       |")
        print("|   0   |")
        print("|       |")
        print("---------")

    elif n == 2:
        print("---------")
        print("|   0   |")
        print("|       |")
        print("|   0   |")
        print("---------")
    elif n == 3:
        print("---------")
        print("|   0   |")
        print("|   0   |")
        print("|   0   |")
        print("---------")

    elif n == 4:
        print("---------")
        print("| 0   0 |")
        print("|       |")
        print("| 0   0 |")
        print("---------")

    elif n == 5:
        print("---------")
        print("| 0   0 |")
        print("|   0   |")
        print("| 0   0 |")
        print("---------")

    else:
        print("---------")
        print("| 0   0 |")
        print("| 0   0 |")
        print("| 0   0 |")
        print("---------")

    x=input("press y to continue and n to quit: ")


