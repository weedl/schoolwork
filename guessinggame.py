import mymodules

print(mymodules.create_time())
print(mymodules.local_time())
print(mymodules.calculate_difference())
print(mymodules.generate_random())


x = int(mymodules.generate_random(10))
while 1:
    try:
        y = int(input("Guess a number between 0 and 10 "))

    except Exception:
        print("That is not a number pal!")
        exit(1)

    else:
        if x == y:
            print("Yay, you guessed the right number!")
            break
        elif 10 < x < 0:
            print("That's not a valid number!")
        else:
            print("Unfortunately, you are wrong :(")
