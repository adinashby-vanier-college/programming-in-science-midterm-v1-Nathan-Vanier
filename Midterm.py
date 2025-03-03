import math

# Q1: Calculate the area of a circle
def area_of_circle(radius):
    area = math.pi * (radius ** 2)
    return round(area,2)

# Q2: Hollow Right Triangle
def hollow_right_triangle(n):
    result = ""
    if n > 4:
        result += "The triangle height should be at least 4."
    for i in range(1, n + 1):
        for j in range(1, i + 1):
            result += "*"
        result += "\n"
    return result.rstrip()
    


# Q3: Inverted Pyramid
def inverted_pyramid(n):
    result = ""
    for i in range(n, 0 , -1):
        spaces = "" * (i - 1)
        stars = "*" (2 * n - 2)
    result += spaces + stars + "\n"

    
    if n < 3: 
        result += "The pyramid height should be at least 3."
    
    return result.rstrip()

# ----------------------------------------------------------------
# print(area_of_circle(5))
# print()

#print(hollw_right_triangle(4))
n = 5
for i in range(1, n + 1):
    for j in range(1, i + 1):
        print("*", end="")
    print()

# print(hollow_right_triangle(5))
# print()

# print(inverted_pyramid(3))
# print()

# print(inverted_pyramid(4))
# print()

# print(inverted_pyramid(5))
# print()ow_right_triangle(3))
# print()







