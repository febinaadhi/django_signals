class Rectangle:
    def __init__(self, length: int, width: int):
        self.length = length
        self.width = width

    # Defining the __iter__ method to make the class iterable
    def __iter__(self):
        yield {'length': self.length}
        yield {'width': self.width}

# Get user input for length and width
length = int(input("Enter the length of the rectangle: "))
width = int(input("Enter the width of the rectangle: "))

# Create a Rectangle instance using user input
rectangle = Rectangle(length, width)

# Iterate over the instance
for dimension in rectangle:
    print(dimension)