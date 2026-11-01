
def calc():
    # OPERATIONS MENU
    print("-----CALCULATOR-----")
    print("1 - Addition")
    print("2 - Subtraction")
    print("3 - Multiplication")
    print("4 - Division")
    print("5 - EXIT")

    # TRY TO GET THE SELECTED OPERATION
    try:
        ope = int(input("Choose: "))
    except:
        print("Are you dumb? You have to enter one of the numbers above.")
        return

    # VALIDATE THE OPERATION, CHECK IF THE VALUE IS 1, 2, 3, 4 OR 5
    if ope < 1 or ope > 5:
        print("This operation is not available yet. Only the ones above.")
        return

    # PROGRAM EXIT
    if ope == 5:
        print("Program closed")
        return

    # NUMBER INPUT
    try:
        cont1 = float(input("Enter a number: "))
        cont2 = float(input("Enter another number: "))
    except:
        print("I can't believe you don't know what a number is.")
        return

    # VALIDATE DIVISION BY 0
    if ope == 4 and cont2 == 0:
        print("YOU CANNOT DIVIDE BY 0")
        return

    # EXECUTE THE SELECTED OPERATION
    if ope == 1:
        print("The result is", cont1 + cont2)
    elif ope == 2:
        print("The result is", cont1 - cont2)
    elif ope == 3:
        print("The result is", cont1 * cont2)
    elif ope == 4:
        print("The result is", cont1 / cont2)


# CALL THE FUNCTION TO RUN THE CALCULATOR
calc()
