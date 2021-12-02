""" Decorations and 'Callbacks' in Python """

def area(length , breath):
    """Create Area Function """
    return length * breath

def volume(*args):
    if len(args) == 3:
        return args[0] * args[1] * args[2]
    elif len(args) == 2:
        return args[0] * args[1]
    elif len(args) == 4:
        return args[0](args[1] , args[2]) * args[3]

# print(volume(area , 3 , 2 , 4))
def print_val(func):
    print("============================================")
    # print(funcs[0]() + " " + funcs[1]())
    print(func())
    print("============================================")

@print_val
def sayName():
    return "Hello"

@print_val
def sayNamep():
    return "Desmond","Michael"
def sayName2():
    return "Samuel"


# print_val(sayName , sayName2)
