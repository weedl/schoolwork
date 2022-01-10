def summing_machine():
    values = []
    while 1:  # Creates a while loop so that the user can enter multiple numbers
        x = input("Please enter a numeric value: ")
        if x.isdigit():  # uses the isdigit method to check whether the input is a digit
            values.append(int(x))  # if the input is a number, it is altered into an integer
            print("\"" + x + "\" has been entered. Press \"s\" or \"S\" to stop")

        elif x == "s" or "S":
            print("You entered \"s/S\" to stop typing numbers. Now calculating your total...")
            print(sum(values))
            break  # this whole block makes sure that if "s/S" is typed to break the loop

        else:
            print("Your input is not allowed")  # Any other input is invalid, which is why "else" is used


summing_machine()  # Calls the function
