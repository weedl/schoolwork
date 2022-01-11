list_values = []  # creates a list where the sales values can be added
while 1:  # starts a while loop so that the user can add values until it breaks
    values = input("Type 'STOP' to move on to next step.\nPlease enter a sales value in 'kr.øre' format: ")
    if values.isdigit():  # checks whether the value is a digit or string
        list_values.append(float(values))  # if it is a value it is added to the 'list_values' list
        print("\nInput added to the list\n")

    elif values == "STOP":
        print("\nStopping...")
        break  # if the user enters 'STOP' the loop is broken

    else:
        print("\nThat input is invalid!\n")

        
try:
    number = int(input("Please enter how many values you would like to add together: "))
    if type(number) is int:
        print("Calculating")
    else:
        raise ValueError("Ouch, bad choice, that is not a number")
except ValueError as e:
    print(e)
    exit(1)
# asks the user how many of the values he or she wants to add together
 
    
sales_list = list_values[:number]  # creates a new list with the values the user wants to add together
sales_total = sum(sales_list)  # creates a sales total consisting of the sum of 'sales_list' values
print(str(sales_total) + "kr")  # displays the sales total to the user
