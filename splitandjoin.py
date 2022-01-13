txt = input("Please enter some text: ")  # asks the user for an input to use in the task

split_character = input("At which character would you like to split the text? " + txt + " ")  # creates an input
# variable where the user chooses where to split the string
result_split = txt.split(split_character)  # the split function allows a user to choose where the string should be split
print(result_split)  # prints the result


replace_character = input("Please enter a character to rejoin the string with: ")  # creates a variable with user input
# as to which character should be used to rejoin the split
replaces_split = txt.replace(split_character, replace_character)  # replace the character which is removed with the
# split function with the character inputted by the user. This gives the illusion of the character filling in the
# "split-spots"
print(replaces_split)  # prints the result
