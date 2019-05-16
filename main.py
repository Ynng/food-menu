import time

# Literally prints a horizontal line


def print_line():
    print("--------------------------------------")

# Printing the receipt


def print_receipt(menu, order, tip=-1):
    print("\n\n\n")
    print_line()
    print("Your Order:")
    print_line()
    # Using the format specification thing to align text vertically https://docs.python.org/2/library/string.html#format-specification-mini-language
    # https://stackoverflow.com/questions/8450472/how-to-format-print-output-or-string-into-fixed-width#16047503
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
    print("{0: <50}".format("Sub-Total")+"$"+str(total))
    # Printing total with tax, rounded to 2 digits
    print("{0: <50}".format("HST(13%)")+"$"+str(round(total*0.13, 2)))
    final = total*1.13
    # if the tip is given, then do things about tax
    if tip > 0:
        print("{0: <50}".format(str(tip) + "% tip") +
              "$"+str(round(final*(tip/100)), 2))
        final = final*(1+(tip/100))
    if tip == 0:
        print("No tip at all :(")
    print("{0: <50}".format("Total")+"$"+str(round(final, 2)))
    return round(final, 2)


def print_menu(menu):
    print_line()
    print("\n\n\nMenu")
    print_line()
    for foodName in menu:
        print("{0: <50}".format(menu[foodName]
                                [0]+" -- ")+"$"+str(menu[foodName][1]))


# Getting the tipping information
# Choosing tip amount
def get_tip():
    print_line()
    while True:
        time.sleep(2)
        try:
            tipPercentage = int(input(
                "\nPlease choose the amount of tip you would like to give us\nYou can choose between 0% to 20%\nJust enter the number, for example, enter \"10\" for 10%\nWe recommand 10%, 15% or 20%\n"))
        except:
            print_line()
            print("Please enter an integer that makes sense!")
            continue
        if tipPercentage < 0 or tipPercentage > 20:
            print_line()
            print("Please enter an integer between 0 and 20!")
            continue
        else:
            return tipPercentage

# Getting the amount of a food needed and modifying the order list


def get_food_amount(menu, order, food):
    # Guiding the user to enter an amount
    while True:
        # Two different messages for new order or change order
        if food in order:
            amountMessage = "You already ordered " + \
                str(order[food]) + " " + food + \
                "(s)\nYou can:\nChange this number by entering the new amount\nDelete this item from your order by entering 0\nOr go back by entering -1\n"
        else:
            amountMessage = "How many servings of " + food + \
                " would you like?\nOr if you choose the wrong food item, Just enter -1 to go back!\n"
        try:
            print_line()
            count = int(input(amountMessage))
        # Lots of if states to make sure the error message makes sense and it always accurate and helpful
        except:
            print_line()
            print("Please enter an integer that makes sense!")
            continue
        if count == -1:
            print_line()
            print("Restarting ordering sequence")
            return
        if food in order and count == 0:
            print("Succesfully removed all " +
                  food + "(s) from your order")
            order.pop(food)
            return
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
            return

# Getting a food item choice


def get_food_item(menu):
    while True:
        # Delaying 2 seconds before displaying the menu again, leaving time for the user to read the previous message
        time.sleep(2)
        # Printing the menu
        print_menu(menu)
        try:
            print_line()
            food = input(
                "Please enter the simple name (Inside Stars) of the food item you would like to order or change\nOr if you have done ordering, just enter \"done\" to checkout\n")
        except:
            print_line()
            print(
                "Hmmm.. something's wrong, please enter ONE OF THE WORD(S) IN THE STARS IN THE MENU")
            continue
        # if user is done with ordering, exit
        if food == "done":
            return "done"
        else:
            # checking to see if the food item exist
            if food not in menu:
                print_line()
                print(
                    "Food item doesn't exist, try again? It's the word(s) in the stars!")
                continue
            else:
                return food


def get_order(menu, order):
    while True:
        # Guiding the user to select a food item
        food = get_food_item(menu)
        # Breaking the loop if the user wants to checkout and have ordered at least 1 item
        if food == "done":
            if len(order) < 1:
                print("You can't checkout yet, you havn't bought anything!")
                continue
            else:
                return
        get_food_amount(menu, order, food)


def cash_checkout(total):
    while True:
        try:
            print_line()
            count = int(
                input("Please enter the amount of cash you are paying"))
        except:
            print_line()
            print("Please enter an integer that makes sense!")
            continue
        if count < total or count > 100000:
            print_line()
            print("Please enter a number that is no smaller than the total cost of your meal, but not completly ridiculous("+total+"~100000)!")
            continue
        else:
            # Now I have the amount of cash the user is paying, I need to calculate the change.
            print_line()
            print("Succesfully paid $" + str(count) + " in cash")
            print("Here's your change of $"str(count-total))
            print_line()
            print("Enjoy your meal :)")
            print_line()
            return


def credit_checkout(total):
    while True:
        try:
            print_line()
            cardType = int(
                input("Please enter the type of credit card you have\nWe accept *Visa*, *Mastercard* and *American Express*"))
        if checkoutVerification not in {"Visa", "Mastercard", "American Express"}:
            print_line()
            print("Sorry, we don't accept that card type, please try again with a different type of card")
            continue
        if paymentMethod == "cash":
            print("\n\n\n")
            print_line()
            print("\n")
            input(cardType + " SECURE LOGIN\nPlease enter your pin SECURELY here:")
            #Accepts the pin no matter what
            print_line()
            print("Contacting your bank....")
            time.sleep(1)
            print_line()
            print("Processing payment....")
            time.sleep(1)
            print_line()
            print("Succesfully paid $" + str(count) + " using a "+cardType+" Credit Card")
            print_line()
            print("Enjoy your meal :)")
            print_line()
            return

def checkout(total):
    while True:
        print_line()
        try:
            paymentMethod = input(
                "Please choose between *cash* and *credit card*")
        except:
            print_line()
            print("Hmmm.. something's wrong.... idk what happened!?!")
            continue
        if checkoutVerification not in {"cash", "credit card"}:
            print_line()
            print("Sorry, we don't accept that payment method")
            continue
        if paymentMethod == "cash":
            cash_checkout(total)
            return
        if paymentMethod == "credit card":
            credit_checkout(total)
            return

# returns -1 if not succesful, 1 is succesful


def checkout_verify(menu, order, tipPercentage):
    # First, verify that the user does actually want to checkout
    while True:
        # Prints the receit again for verification
        total = print_receipt(menu, order, tipPercentage)
        print_line()
        try:
            checkoutVerification = input(
                "Please DOUBLE CHECK your order, there is NO GOING BACK after this step!\nEnter \"sure\" to continue to checkout, or\nEnter \"not yet\" to go back")
        except:
            print_line()
            print("Hmmm.. something's wrong.... idk what happened!?!")
            continue
        if checkoutVerification not in {"sure", "not yet"}:
            print_line()
            print("You entered something that's not either \"sure\" or \"not yet\", please only enter one of these")
            continue
        if checkoutVerification == "sure":
            checkout(total)
            return 1
        if checkoutVerification == "not yet"
        return -1


def get_action(menu, order, tipPercentage):
    while True:
        time.sleep(2)
        # Printing the receipt again with tip information OR Just printing the receipt again after changing order/tip
        print_receipt(menu, order, tipPercentage)
        try:
            print_line()
            option = input("Options:\ncheckout | change order | change tip")
        except:
            print_line()
            print("Hmmm.. something's wrong, please enter ONE OF THE ABOVE OPTIONS")
            continue
        if option not in {"checkout", "change order", "change tip"}:
            print_line()
            print("You entered something that's not one of the three options\nplease enter ONE OF THE ABOVE OPTIONS")
            continue
        # Finally, if the user wants to change tip
        if option == "change tip":
            tipPercentage = get_tip()
            continue
        if option == "change order":
            get_order(menu, order)
            continue
        if option == "checkout":
            checkoutResponse = checkout_verify(menu, order, tipPercentage)
            if checkoutResponse == -1:
                continue
            if checkoutResponse == 1:
                return


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
get_order(menu, order)

# Print receipt without any tip information
print_receipt(menu, order)
# Now ask for tip information
time.sleep(1)
tipPercentage = get_tip()

# Guiding the user to select an action
get_action(menu, order, tipPercentage)
