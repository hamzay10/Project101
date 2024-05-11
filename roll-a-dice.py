import random
response = "y"

while response == "y":
    no = random.randint(1,6)
    if no == 1:
        print("The number on the dice is 1")
    elif no == 2:
        print("The number is 2")
    elif no == 3:
        print("The number is 3")
    elif no == 4:
        print("The number is 4")
    elif no == 5:
        print("The number is 5")
    else:
        print("The number is 6")

    response = input("press y to roll again and n to exit: ")
    print("\n")
