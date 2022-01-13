string = input("Please enter a string of characters: ")

while 1:
    option = input("\nChoose an option as to how you would you like to display the string?\n1: Uppercase\n2: Lowercase \n"
                   "3: Titlecase\n4: Remove the front and back whitespaces\ne: Exit program \n")
    if option == "1":
        print(string.upper())

    elif option == "2":
        print(string.lower())

    elif option == "3":
        print(string.title())

    elif option == "4":
        print(string.lstrip())

    elif option == "e":
        print("Exiting...")
        break

    else:
        print("The input is invalid, and an error occurred.")
