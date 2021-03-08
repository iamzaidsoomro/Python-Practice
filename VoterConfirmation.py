def foo():
    name = str(input("Enter your name: "))
    age = int(input("Enter your age: "))
    if age >= 18:
         print(f"Mr {name.title()} you are eligible to vote.")
    else:
         remaining_age = 18 - age
         print(f"Mr {name.title()}, you will be eligible to vote after {remaining_age} years.")

    exit_confirmation = input("Would you like to check another name? Y/N")
    if exit_confirmation == 'y' or 'Y':
        return foo()
foo()

