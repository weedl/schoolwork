def calculate_area_of_shape():  # defines the function
    shape = input("Which of the following shapes would you like to calculate the are of:\nTriangle\nCircle\nSquare"
                  "\nPlease enter preferred shape: ")

    if shape.lower() == "triangle":  # converts all text to lowercase so that input format doesn't matter
        x = input("What is the height of the triangle in cm? \n")
        y = input("\nWhat is the baseline length of the triangle in cm? \n")
        area_of_triangle = int(x) * int(y) / 2  # the formulas ask for the necessary input needed in the formula
        print("The area of the triangle is " + str(area_of_triangle) + "cm" + "\u00b2")
        # it is important to turn the input into integer values, and thereafter back to string.
        # one can ask for integer values to start of to make the code simpler

    elif shape.lower() == "circle":
        x = input("What is the radius of the circle in cm?\n")
        area_of_circle = int(x) ** 2 * 3.14
        print("The area of the circle is " + str(area_of_circle) + "cm" + "\u00b2")

    elif shape.lower() == "square":
        x = input("What is the height of the square in cm?\n")
        area_of_square = int(x) ** 2
        print("The are of the shape is " + str(area_of_square) + "cm" + "\u00b2")

    else:
        print("Your value is invalid, please enter one of the supported shapes!")
        # if none of the entered shapes are in the code, the script will print this message


calculate_area_of_shape()  # calls the function

# I am unsure if this is how the task wanted us to do the task, though, this is a solution to crate what is requested
