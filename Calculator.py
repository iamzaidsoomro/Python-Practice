def calc():
    choice = "y"
    while(choice == "y" or choice == "Y"):
        numb1 = input("Enter first number: ")
        numb2 = input("Enter second number: ")
        op = input("Enter operation: ")
        numb1 = int(numb1)
        numb2 = int(numb2)
        if op == '+': print("Sum = " + str(numb1 + numb2))
        elif op == '-': print("Difference = " + str(numb1 - numb2))
        elif op == '*': print("Product = " + str(numb1 * numb2))
        elif op == '/':
            if numb2 != 0: print("division = " + str(numb1 / numb2))
            else: print("Undefined")
        else: print("Invalid Data")
        choice = input("Would you like to perform again? Y/N: ")
calc()
