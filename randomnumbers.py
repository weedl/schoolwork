from random import *  # imports all the functions in the random module

file = open("randomnumbers.txt", "w")  # opens the file which I would like to write to, and use the 'w' keyword to write
# and adds open file to the 'file' variable

for i in range(100):  # make a loop to create 100 numbers
    rnum = randrange(501)  # generate a number between 1 and 500 (not including 501)
    file.write(str(rnum) + "\n")  # write the random number as a string to the randomnumbers file

file.close()  # close the file to event unecessary amount of open files
