import math

class Circle:
    def __init__(self, radius):
        self.radius = radius

    def calculate_diameter(self):
        return self.radius * 2

    def calculate_circumference(self):
        return 2 * math.pi * self.radius

    def calculate_area(self):
        return math.pi * self.radius ** 2

    def grow(self):
        self.radius *= 2

    def get_radius(self):
        return self.radius

# Validator class for data validation
class Validator:
    @staticmethod
    def validate_radius(user_input):
        try:
            radius = float(user_input)
            if radius <= 0:
                raise ValueError("Radius should be a positive number.")
            return radius
        except ValueError:
            raise ValueError("Invalid input. Please enter a valid radius.")

# Prompt the user to enter a radius
while True:
    try:
        user_input = input("Enter the radius of the circle: ")
        radius = Validator.validate_radius(user_input)
        break
    except ValueError as e:
        print(e)

# Create a Circle object and display the results
circle = Circle(radius)
print("Diameter:", circle.calculate_diameter())
print("Circumference:", circle.calculate_circumference())
print("Area:", circle.calculate_area())

# Ask the user if the circle should grow
while True:
    try:
        user_input = input("Should the circle grow? (yes/no): ")
        if user_input.lower() == "yes":
            circle.grow()
            print("New radius:", circle.get_radius())
            print("New diameter:", circle.calculate_diameter())
            print("New circumference:", circle.calculate_circumference())
            print("New area:", circle.calculate_area())
        elif user_input.lower() == "no":
            print("Goodbye!")
            break
        else:
            raise ValueError("Invalid input. Please enter 'yes' or 'no'.")
    except ValueError as e:
        print(e)
