postal = {
    "6859": "Slinde",
    "5828": "Bergen",
    "8611": "Mo i Rana",
    "7207": "Ytre Snillefjord",
    "8682": "Trofors",
    "9528": "Alta",
    "0349": "Oslo",
    "1300": "Sandvika",
    "1604": "Råde",
    "1786": "Halden"
}
# Creates a dictionary storing all postal numbers and their correlating values

while 1:  # Creates a loop to ensure that a valid postal number is put
    post = input("Please enter a norwegian postal number: ")  # Asks user for a postal code

    if post in postal:
        print(postal.get(post))
        break
    # If input is in the dictionary, it will print the value related to it and break the loop.

    else:
        print("That is an invalid postal number! Please enter a valid one.")
    # If the input is not in the list, print message will be displayed, and it will loop back to input.
