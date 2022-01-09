def metric_converter():  # Creates a function without a variable
    x = int(input("Enter a amount of inches you would\nlike to convert to centimeters: "))
    # Asks the user to input an amount of inches to convert. The script turns the input into an integer

    print("You entered " + str(x) + " inches, which equals to " + str(x * 0.393700787) + " centimeters")
    # Tells the user information, and adds the formula for converting inches into centimeters,
    # and thereafter turning the result into string


metric_converter()  # Calls the function

