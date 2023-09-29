#Instructions
#Determine if a triangle is equilateral, isosceles, or scalene.
#An equilateral triangle has all three sides the same length.
#An isosceles triangle has at least two sides the same length. (It is sometimes specified as having exactly two sides the same length, but for the purposes of this exercise we'll say at least two.)
#A scalene triangle has all sides of different lengths.

def my_triangle(a, b, c):
    contidion_1 = ((a + b) >= c)
    condition_2 = ((b + c) >= a)
    condition_3 = ((a + c) >= b)
    if (contidion_1 and condition_2 and condition_3) == True:
        print("\nThe conditions of the triangle are True.")
        if a == b == c:
            print("Your triangle is equilateral.")
        elif (a == b and a != c) or (b == c and c != a) or (c == a and a != b):
            print("Your triangle is isosceles.")
        else:
            print("Your triangle is scalene.")
    else:
        print("\nYour triangle doesn't follow the conditions.")

my_triangle(4, 4, 3) #should return isosceles
my_triangle(4, 3, 5) #should return scalene
my_triangle(3, 3, 3) #should return equilateral
my_triangle(3, 5, 20) #should return error