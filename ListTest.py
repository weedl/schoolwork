names = [] # Creates an empty list
print("Please Enter 10 names \n")
for i in range(0, 10):
    name = input("Enter a name: ") # Creates a loops which asks for a name 10 times
    names.append(name) # Adds the names to the list "names"

names.sort() # Sorts the list alphabetically

search = input("Search for name in the list: ") # Asks user to search for a name in the list

if search in names:
    print("The name is indexed as " + str(names.index(search))) # Prints the index of the name in the list
else:
    print("The name is not in the list") # Tells the user that the name is not in the list

names.sort(reverse=True) # Reverses the list

length_names = len(names) # Finds the length of the list
middle_of_list = length_names//2 # Dividing the list's length by 2 to find out what half the list is
half_names = names[:middle_of_list] # Creates a new variable which contains the first half of the list

print(half_names)

last_name = input("Please enter one last name: ")
names.append(last_name) # Adds the last name given to the original list

print(names) # Prints the names of the original list to verify that it is working
