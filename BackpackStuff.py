import sys

itemsInBackpack = ["book", "computer", "keys", "travel mug"]

while True:
    # print(itemsInBackpack)
    print("Would you like to:")
    print("1. Add an item to the backpack?")
    print("2. Check if an item is in the backpack?")
    print("3. Quit")
    userChoice = input()

    if userChoice == "1":
        print("What item do you want to add to the backpack?")
        itemToAdd = input()

        itemsInBackpack.append(itemToAdd)
        # print(itemsInBackpack)
        print("You have added " + itemToAdd + " to the backpack. ")

    if userChoice == "2":
        print("What item do you want to check to see if it is in the backpack?")
        itemToCheck = input()

        # print(itemsInBackpack)
        if itemToCheck in itemsInBackpack:
            print("Yes, " + itemToCheck + " is in the backpack.")
        else:
            print("Sorry that item is not in the backpack.")

    if userChoice == "3":
        sys.exit()
