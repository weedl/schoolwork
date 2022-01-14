
csv_reader = open("mycsv.csv", "r")  # opens the mycsv.csv file as the variable csv_reader

print(csv_reader.readable())  # checks whether the csv_reader variable is readable and prints the result

print(csv_reader.read())  # prints the csv file with the read method

csv_reader.close()  # closes the file so that we don't have an unecessary number of files open
