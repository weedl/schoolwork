import datetime, random


def create_time():
    x = datetime.datetime(2020, 5, 17)  # uses the datetime module to create return the date 17th of May 2020
    return x


def local_time():
    x = datetime.datetime.now()  # uses the datetime module to return the time at the computer it is being run at
    return x


def calculate_difference():
    try:
        x = int(input("Please enter a number: "))
        y = int(input("Please enter another number: "))

    except Exception:
        print("That is not a number pal!")
        exit(1)

    else:
        return str(x - y)  # uses try - except to make sure a number is being entered, otherwise, it is pretty straight


def generate_random(x):
    return random.randrange(0, x)  # the random module asks for x as input when run, and choses a random number in the
    # range between 0 and x

    except Exception:
        print("That is not a number pal!")
        exit(1)

    else:
        return str(x - y)


def generate_random(x):
    return random.randrange(0, x)
