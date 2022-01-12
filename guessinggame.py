import mymodules

print(mymodules.create_time())
print(mymodules.local_time())
print(mymodules.calculate_difference())
print(mymodules.generate_random(100))
# print all the functions to verify that they work

x = int(mymodules.generate_random(10))  # sets the x value to 10 to create a random number between 0 and 10
while 1:  # creates a loop so that the user can keep on guessing
    try:
        y = int(input("Guess a number between 0 and 10 "))

    except Exception:
        print("That is not a number pal!")
        exit(1)
    # using a try - except loop to make sure the input is an integer
    else:
        if x == y:
            print("Yay, you guessed the right number!")
            break  # breaks the loop if the guess is successful
        elif 10 < x < 0:
            print("That's not a valid number!")  # if the number is over 10 or under 0, the number is deemed invalid
        else:
            print("Unfortunately, you are wrong :(")  # if the guess is wrong this message is printed
