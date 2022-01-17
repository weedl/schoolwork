class fireman:
    count = 0

    def __init__(self, name, surname, staff_number, age):
        self.name = name
        self.surname = surname
        self.staff_number = staff_number
        self.age = age
        fireman.count += 1
        self.total = fireman.count

    def display(self):
        return "One fireman is called {} {}, he is {} years old, and his staff number is {} \n".format(self.name, self.
                                                                                                  surname, self.age,
                                                                                                  self.staff_number)


fireman1 = fireman("Steve", "Davis", 101, 27)

fireman2 = fireman("Gregor", "Kalsovic", 102, 38)

fireman3 = fireman("Peter", "Parker", 103, 21)

print(fireman.display(fireman1))
print(fireman.display(fireman2))
print(fireman.display(fireman3))
print("\nTotal number of firemen:", fireman.count)
