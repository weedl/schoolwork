import datetime, random


def create_time():
    x = datetime.datetime(2020, 5, 17)
    return x


def local_time():
    x = datetime.datetime.now()
    return x


def calculate_difference():
    try:
        x = int(input("Please enter a number: "))
        y = int(input("Please enter anohter number: "))

    except Exception:
        print("That is not a number pal!")
        exit(1)

    else:
        return str(x - y)


def generate_random():
    try:
        x = int(input("Please enter a maximum number for the generator: "))

    except Exception:
        print("That is not a number pal!")

    else:
        return random.randrange(0, x)

