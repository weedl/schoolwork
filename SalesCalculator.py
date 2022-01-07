# The description for this code was very vague, and therefore,
# the script might not be as you anticipated.
list_of_sales = []
for i in range(10):
    x = int(input("Please enter a sales value: "))  # A loop which will ask the user for 10 sales values
    if x < 5000:  # Breaks if input is under 5 000
        break

    elif 5000 <= x <= 10000:  # Prints the value if between 5 000 and 10 000
        print(x)
        list_of_sales.append(x)  # Adds the input to a list

    elif x > 10000:  # Prints a messages and breaks if the input is over 10 000
        print("A possible data error seems to have occurred.")
        break

# Here we are finding the total amount of sales and printing them out
total_sales = sum(list_of_sales)
print("The total sales are " + str(total_sales))

# Now we are finding the average sales price, and then printing it
averege_sales = total_sales / len(list_of_sales)
print("\nThe average sales price is " + str(averege_sales))
