#This program is intended to take manual input from a user and use it to calculate what a monthly payment on the
#Saving on a Valuable Education plan would be

#Establishing loop
while True:

    #The opening message
    print("Welcome to the SAVE Plan Payment Estimator!\n")

    #Taking user input for spousal information
    spouse = input("Are you currently single or married? Enter 's' for single or 'm' for married.\n")

    #Making sure input is correct
    while spouse.lower() != "s" and spouse.lower() != "m":
        print("Please enter 's' or 'm'.")
        spouse = input("Are you current single or married? Enter 's' for single or 'm' for married.\n")

    #Collecting tax filing status if necessary
    taxes = ""
    if spouse.lower() == "m":
        taxes = input("Do you file taxes separately or jointly. Enter 's' for separately or 'j' for jointly.\n")
        while taxes.lower() != "j" and taxes.lower() != "s" and taxes.lower() != "r":
            print("Please enter 's' or 'j'.\n")
            taxes = input("Do you file taxes separately or jointly? Enter 's' for separately or 'j' for jointly.\n")
    else:
        pass

    #Collecting number of child dependents
    children = ""
    while type(children) is not int:
        children = input("How many children do you provide more than half of their financial support to?\n")
        try:
            children = int(children)
        except ValueError:
            print("Please enter a number.\n")

    #Collecting number of non-child dependents
    o_dependents = ""
    while type(o_dependents) is not int:
        o_dependents = input("How many non-children dependents do you provide more than half of their financial support to?\n")
        try:
            o_dependents = int(o_dependents)
        except ValueError:
            print("Please enter a number.\n")

    #Collecting income
    income = ""
    while type(income) is not int:
        income = input("What is your current annual gross income?\n")
        try:
            income = int(income)
        except ValueError:
            print("Please enter a number.\n")

    #Converting input to usable integers
    num_spouse = 0
    if spouse.lower() == "s":
        num_spouse = 0
    else:
        if taxes.lower() == "s":
            num_spouse = 0
        else:
            num_spouse = 1

    #Calculating family size based on answers
    family = 1 + children + o_dependents + num_spouse

    #Producing the calculation and outputting the result

    payment = 0
    if family == 1:
        payment = round((income - 32805) / 120, 2)
        if payment <= 0:
            payment = 0
            print("Your estimated monthly payment on the SAVE Plan is $" + str(payment) + ".\n")
        else:
            print("Your estimated monthly payment on the SAVE Plan is $" + str(payment) + ".\n")
    elif family == 2:
        payment = round((income - 44370) / 120, 2)
        if payment <= 0:
            payment = 0
            print("Your estimated monthly payment on the SAVE Plan is $" + str(payment) + ".\n")
        else:
            print("Your estimated monthly payment on the SAVE Plan is $" + str(payment) + ".\n")
    elif family == 3:
        payment = round((income - 55935) / 120, 2)
        if payment <= 0:
            payment = 0
            print("Your estimated monthly payment on the SAVE Plan is $" + str(payment) + ".\n")
        else:
            print("Your estimated monthly payment on the SAVE Plan is $" + str(payment) + ".\n")
    elif family == 4:
        payment = round((income - 67500) / 120, 2)
        if payment <= 0:
            payment = 0
            print("Your estimated monthly payment on the SAVE Plan is $" + str(payment) + ".\n")
        else:
            print("Your estimated monthly payment on the SAVE Plan is $" + str(payment) + ".\n")
    elif family == 5:
        payment = round((income - 79065) / 120, 2)
        if payment <= 0:
            payment = 0
            print("Your estimated monthly payment on the SAVE Plan is $" + str(payment) + ".\n")
        else:
            print("Your estimated monthly payment on the SAVE Plan is $" + str(payment) + ".\n")
    elif family == 6:
        payment = round((income - 90630) / 120, 2)
        if payment <= 0:
            payment = 0
            print("Your estimated monthly payment on the SAVE Plan is $" + str(payment) + ".\n")
        else:
            print("Your estimated monthly payment on the SAVE Plan is $" + str(payment) + ".\n")
    elif family == 7:
        payment = round((income - 102195) / 120, 2)
        if payment <= 0:
            payment = 0
            print("Your estimated monthly payment on the SAVE Plan is $" + str(payment) + ".\n")
        else:
            print("Your estimated monthly payment on the SAVE Plan is $" + str(payment) + ".\n")
    elif family == 8:
        payment = round((income - 113760) / 120, 2)
        if payment <= 0:
            payment = 0
            print("Your estimated monthly payment on the SAVE Plan is $" + str(payment) + ".\n")
        else:
            print("Your estimated monthly payment on the SAVE Plan is $" + str(payment) + ".\n")
    elif family == 9:
        payment = round((income - 125325) / 120, 2)
        if payment <= 0:
            payment = 0
            print("Your estimated monthly payment on the SAVE Plan is $" + str(payment) + ".\n")
        else:
            print("Your estimated monthly payment on the SAVE Plan is $" + str(payment) + ".\n")
    elif family == 10:
        payment = round((income - 136890) / 120, 2)
        if payment <= 0:
            payment = 0
            print("Your estimated monthly payment on the SAVE Plan is $" + str(payment) + ".\n")
        else:
            print("Your estimated monthly payment on the SAVE Plan is $" + str(payment) + ".\n")
    elif family == 11:
        payment = round((income - 148455) / 120, 2)
        if payment <= 0:
            payment = 0
            print("Your estimated monthly payment on the SAVE Plan is $" + str(payment) + ".\n")
        else:
            print("Your estimated monthly payment on the SAVE Plan is $" + str(payment) + ".\n")
    elif family == 12:
        payment = round((income - 160020) / 120, 2)
        if payment <= 0:
            payment = 0
            print("Your estimated monthly payment on the SAVE Plan is $" + str(payment) + ".\n")
        else:
            print("Your estimated monthly payment on the SAVE Plan is $" + str(payment) + ".\n")