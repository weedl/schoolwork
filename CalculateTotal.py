# We got to make a loop which loops through the script until it breaks
while 1:
    number = input("Which number am I thinking of? ")
    # Asks the user for a number, being looped until "break" statement is true

    if number == "-1":  # If the number is -1, run the following code
        print("Damn, you're right.\nHere is a cookie")
        break
        # This code will print a statement, and thereafter break the "while 1" loop

    else:
        print("Nope, try again")
    # This chunk of code ensures that as long as the input is any different from "-1", print a statement
