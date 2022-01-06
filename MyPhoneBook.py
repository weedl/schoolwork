business_phone = {
    "Telenor": "91 50 90 00",
    "Gjensidige": "91 50 31 00",
    "KID": "31 00 20 00",
    "VG": "22 00 00 00",
    "NRK": "23 04 70 00"
}
# Created a dictionary with contact information of some big corporations in Norway

company_name = input("Please enter the name of the company you want to add: ")
# Asks user to input the business
company_number = input("Please enter the phone number of the company: ")
# Asks user to input the phone number of the business

business_phone[company_name] = company_number
# Adds the business with the phone number to the dictionary

search_business = input("Please enter business to search for: ")

if search_business in business_phone.keys():
    print(search_business + "'s phone number is: " + business_phone.get(search_business))
    # If the variable "search_business" is in the dictionary, it will print the phone number related to the input
else:
    print("This business is not in the dictionary")
    # If the input is not found in the dictionary, the following will be printed

print("\nHere is an overview of the businesses referring to their phone numbers:")
for key in business_phone:
    print(key, " : ", business_phone[key])
# Loops through the business names in a clean manner

print("\nHere comes the business names alone:")  # Makes space to clean it up
for key in business_phone:
    print(key)
# Displays only the keys in the dictionary (Business names)
