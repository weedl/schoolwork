txt = input("Please enter some text you would like to slice: ")

try:
    start = int(input("Please enter the index as to where you want the string to: "))

except Exception:
    print("That is not a number! Please run the script again,")
    exit(1)
else:
    if start < 0:
        start = 0  # if start is inputted as lower than 0 (will mess up string), it is set to 0.

try:
    end = int(input("Please enter the index where you would like to end the string: "))

except Exception:
    print("That is not a number! Please run the script again.")
    exit(1)
else:
    if end > len(txt):
        end = len(txt)  # makes sure that end is not longer than the input string
# try-except makes sure that the number typed is an int. If not, the string wil exit and tell the user that the input
# is invalid

start_end_txt = txt[start:end]  # creates a variable containing the txt input with a staring and ending point.
# both the start and end variable are determined by user-input from the try-except blocks.

print(start_end_txt)  # prints the results
