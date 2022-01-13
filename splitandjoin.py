txt = input("Please enter some text: ")  # asks the user for an input to use in the task

split_character = input("At which character would you like to split the text? " + txt + " ")  # creates an input
# variable where the user chooses where to split the string
result_split = txt.split(split_character)  # the split function allows a user to choose where the string should be split
print(result_split)  # prints the result


combine_character = input("Please enter a character to rejoin the string with: ")  # creates a variable with user input
# as to which character should be used to rejoin the split
combine_split = combine_character.join(result_split)  # the combnie function combines the string where it was split by using the chosen character
print(combine_split)  # prints the result
