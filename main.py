import time

# Literally prints a horizontal line


def print_line():
    print("--------------------------------------")


def print_menu(menu):
    print_line()
    print("\n\n\nMenu")
    print_line()
    for foodName in menu:
        print("$"+str(menu[foodName][1])+" - "+menu[foodName][0])


# The menu, containing the food name, full food name to put on the menu and price
menu = {"burger": ("Kevin's *burger*", 15),
        "caesar salad": ("Kevin's *caesar salad*", 12),
        "pasta": ("Kevin's *pasta*", 10),
        "hotdog": ("Lil Kevin's *hotdog*", 5),
        "chicken strips": ("Lil Kevin's *chicken strips*", 7),
        "pop": ("*pop*", 2)}

# Printing welcome message before menu
print("Welcome to Kevin's Kusine!")


# Asking the user to order food
order = {}
while True:
    # Guiding the user to select a food item
    while True:
        # Delaying 2 seconds before displaying the menu again, leaving time for the user to read the previous message
        time.sleep(2)
        # Printing the menu
        print_menu(menu)
        try:
            print_line()
            food = input(
                "Please enter the simple name (Inside Stars) of the food item you would like to order\nOr if you have done ordering, just enter \"done\" to checkout\n")
        except:
            print_line()
            print(
                "Hmmm.. something's wrong, please enter ONE OF THE WORD(S) IN THE STARS IN THE MENU")
            continue
        if food == "done":
            break
        else:
            if food not in menu:
                print_line()
                print(
                    "Food item doesn't exist, try again? It's the word(s) in the stars!")
                continue
            else:
                break
    # Breaking the loop if the user wants to checkout and have ordered at least 1 item
    if food == "done":
        if len(order) < 1:
            print("You can't checkout yet, you havn't bought anything!")
            continue
        else:
            break
    # Guiding the user to enter an amount
    while True:
        if food in order:
            amountMessage = "You already ordered " + \
                str(order[food]) + " " + food + \
                "(s)\nYou can:\nChange this number by entering the new amount\nDelete this item from your order by entering 0\nOr go back by entering -1\n"
        else:
            amountMessage = "How many servings of " + food + \
                " would you like?\nOr if you chose the wrong food item, Just enter -1 to go back!\n"
        try:
            print_line()
            count = int(input(amountMessage))
        except:
            print_line()
            print("Please enter an integer that makes sense!")
            continue
        if count == -1:
            print_line()
            print("Restarting ordering sequence")
            break
        if food in order and count == 0:
            print("Succesfully removed all " + food + "(s) from your order")
            order.pop(food)
            break
        if count < 1 or count > 1000:
            print_line()
            print("Please enter a number that actually makes sense(1~1000)!")
            continue
        else:
            # Now I have the food item and count, I will add them to the order list
            print_line()
            print("Succesfully ordered " + str(count) +
                  " " + food + "(s)")
            order[food] = count
            break

print(order)

# Printing the receipt
print("\n\n")
print_line()
print("Your Order:")
print_line()
print("Item | Price | Quantity | Sub-Total")
print_line()
for item in order:
    print(item + " | $" + str(menu[item][1]) + " | " + str(order[item]) + " | $"+ str(menu[item][1]*order[item]))