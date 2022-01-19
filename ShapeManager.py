class Shape:
    count = 0

    def __init__(self, description):
        self.description = description
        Shape.count += 1

    def __str__(self):
        return "{0}\nArea: {1}\nVolume: {2}".format(self.description, self.area(), self.volume())

    def area(self):
        return 0

    def volume(self):
        return 0



class two_dimensional(Shape):
    def __init__(self, description):
        super().__init__(description)

    def __str__(self):
        return "Two-dimensional shape\n{0}".format(super().__str__())


class three_dimensional(Shape):
    def __init__(self, description):
        super().__init__(description)

    def __str__(self):
        return "Three-dimensional shape\n{0}".format(super().__str__())


class square(two_dimensional):
    def __init__(self, description, length):
        super().__init__(description)
        self.length = length

    def area(self):
        return self.length * self.length

    def __str__(self):
        return "Square is a {0}".format(super().__str__())


class rectangle(two_dimensional):
    def __init__(self, description, height, length):
        super().__init__(description)
        self.length = length
        self.height = height

    def area(self):
        return self.height * self.length

    def __str__(self):
        return "Rectangle is a {0}".format(super().__str__())


class cube(three_dimensional):
    def __init__(self, description, length):
        super().__init__(description)
        self.length = length

    def area(self):
        return self.length * self.length * 6

    def volume(self):
        return self.length * self.length * self.length

    def __str__(self):
        return "Cube is a {0}".format(super().__str__())


class box(three_dimensional):
    def __init__(self, description, length, height, width):
        super().__init__(description)
        self.length = length
        self.height = height
        self.width = width

    def area(self):
        return self.height * self.width * 6

    def volume(self):
        return self.height * self.width * self.length

    def __str__(self):
        return "Box is a {0}".format(super().__str__())