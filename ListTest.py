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

print(names) # Prints the names of the list to verify that it is working
