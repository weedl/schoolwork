def generate_letter():  # creates a function
    while 1:  # sets up a loop, will explain why later
        letters = "abcde"  # creates a string to loop through
        for x in letters:
            yield x
            # the 'for' statement is used to loop through the letter in the string. Yield makes sure that
            # the function 'remembers' which number it is at. This means that the next time you call
            # for the function as shown below. It will continue counting from where it left of.
            # a kind of savepoint
            if x == "e":
                break
                # lastly, we break the loop when we hit e, so that we can loop as many times as we want
                # if we don't break the loop, or create a loop to begin with, we can't loop through the string
                # more than once


incrementation = generate_letter()
# we set the generate_letter() function to = incrementation, so that we can
# create a new one later if we want to.
print(next(incrementation))
# this print statement will print the next return value, which in this case is a
print(next(incrementation))
# as the yield statement from earlier makes it so the function remembers which value
# it last returned, it will return the next value this time: b
print(next(incrementation))
print(next(incrementation))
print(next(incrementation))
print(next(incrementation))
print(next(incrementation))
print(next(incrementation))
print(next(incrementation))
print(next(incrementation))
# this script runs through the letters two times as this is what the task asked for
