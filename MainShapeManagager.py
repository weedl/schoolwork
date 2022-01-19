from ShapeManager import *

shapes = []

shapes.append(square("square1", 4))
shapes.append(rectangle("rectangle1", 6, 8))
shapes.append(cube("cube1", 3))
shapes.append(box("box1", 4, 2, 5))

print("Number of shapes:", Shape.count)
print("-" * 50)

for current in shapes:
    print(current)
    print("-" * 50)

