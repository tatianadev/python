import math


def check_if_triangle_exists(a, b, c):
    if a < b + c and b < a + c and c < a + b:
        return True
    else:
        return False


def find_angle_of_triangle(a, b, c):
    # a**2 = b**2 +c**2 - 2*b*c*cosα
    cos_angle = (b ** 2 + c ** 2 - a ** 2) / (2 * b * c)  # cos of angle
    acos_angle = math.acos(cos_angle)  # acos, angle in radians
    degrees_angle = math.degrees(acos_angle)  # angle in degrees

    return degrees_angle


first_side = float(input("Enter value of fist side of triangle: "))
second_side = float(input("Enter value of second side of triangle: "))
third_side = float(input("Enter value of third side of triangle: "))

if check_if_triangle_exists(first_side, second_side, third_side):
    print("Triangle with such sides exists!")
    triangle_exists_flag = True
else:
    print("Triangle with such sides doesn't exist!")
    triangle_exists_flag = False

if triangle_exists_flag:
    first_angle = find_angle_of_triangle(first_side, second_side, third_side)
    second_angle = find_angle_of_triangle(second_side, first_side, third_side)
    third_angle = find_angle_of_triangle(third_side, second_side, first_side)
    print("First angle: {} degrees, "
          "second angle: {} degrees, "
          "third angle: {} degrees.".format(f'{first_angle:.2f}', f'{second_angle:.2f}', f'{third_angle:.2f}'))
