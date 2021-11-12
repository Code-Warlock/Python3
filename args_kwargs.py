""" *args & **kwargs """

# Arbitary arguments and Keyword arguments in Python
# Default parameters
# def area(G = 9.8 , M , m , r = 8):
#     return (G * M * m) / r**2




def volume(*args):
    if len(args) == 2:
        return args[0] * args[1]
    elif len(args) == 3:
        return args[0] * args[1] * args[2]
    else:
        return False
def food(**kwargs):
    return kwargs

print(food(fname = input("Enter your first name : ") , lname = input("Enter your last name : ")))

# cuboid_length = float(input("Enter the length : "))
# cuboid_breadth = float(input("Enter the breadth : "))
# cuboid_height = float(input("Enter the height : "))
# cuboid_area = area(cuboid_length , cuboid_breadth)
# cuboid_volume = volume(12 , 3 ,5)
# print(f"Cuboid Area(m2) : {cuboid_area}\nCuboid Volume(m3) : {cuboid_volume}")

# while volume(3,4,5) == False:
#     print("Invalid number of arguments")
