import time

# Literally prints a horizontal line


def print_line():
    print("--------------------------------------")


def print_menu(menu):
    print_line()
    print("\n\n\nMenu")
    print_line()
    for foodName in menu:
        print("{0: <50}".format(menu[foodName]
                                [0]+" -- ")+"$"+str(menu[foodName][1]))


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


# Printing the receipt
print("\n\n\n")
print_line()
print("Your Order:")
print_line()
# Using the format specification thing to align text vertically https://docs.python.org/2/library/string.html#format-specification-mini-language
print("{0: <20}".format("Item") + " | " + "{0: <11}".format("Price") + " | " +
      "{0: <10}".format("Quantity") + " | " + "Sub-Total")
print_line()
total = 0
for item in order:
    print("{0: <20}".format(item) + " | $" + "{0: <10}".format(str(menu[item][1])) + " | " + "{0: <10}".format(
        str(order[item])) + " | $" + "{0: <10}".format(str(menu[item][1]*order[item])))
    # Adding up the total price
    total += menu[item][1]*order[item]
print_line()
# Printing the totals
print("{0: <60}".format("Sub-Total")+"$"+str(total))
# Printing total with tax, rounded to 2 digits
print("{0: <60}".format("HST(13%)")+"$"+str(round(total*0.13, 2)))


#Choosing tip amount
