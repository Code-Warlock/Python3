""" Functions in Python """
def hello(name):
    return "Hello" + " " + name

def maths(num1 , num2):
    x = 45
    return num1 * num2

def palindrome(word):
    """ Palindrome Funtion """
    # if word == word[::-1]:
    #     return True
    # else:
    #     return False
    return word == word[::-1]


user_word = input("Enter your word : ").lower()
if palindrome(user_word):
    print("Palidronme")
else:
    print("Not a palindrome")
# func = input("hello or maths : ").lower()
# if "ll" in func:
#     hello("Michael")
# else:
#     maths(3,4)
# res = maths(5,6)
# print(res * 12)
# print(x)
