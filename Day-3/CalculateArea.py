# Defining a function to calculate area of a rectangle
def calculate_rect_area(length, width):
    area = length * width
    return area


length_in = float(input("Enter the length"))
width_in = float(input("Enter the width"))

area_result = calculate_rect_area(length_in, width_in)
print(f"Area of the rectangle is {area_result} square units")

