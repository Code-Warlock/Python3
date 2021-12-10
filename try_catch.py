""" Handling Errors and Exception in Python """
""" try """
import time
# try:
#     # age = int(input("Enter your age : "))
#     # time.sleep(3)
#     # print(age , end=" ")
#     # print("Hello World") #Hello Wor
#     with open("files.txt" , "r") as f:
#         f.write("I just created this file!")
    # print(2 / 0)
# except ValueError:
#     print("Error > Expected a Number  e.g 12 ,23 ...")
# except ZeroDivisionError:
#     print("Cannot divide by 0")
# except KeyboardInterrupt:
#     time.sleep(.5)
#     print("Closing Program!")
#     time.sleep(.5)
#     print("Program Closed!")
# except(FileExistsError,FileNotFoundError,OSError):
#     print("This file based on your choice has either been created or does not exist")


# try:

# except:
# try:
#     print(x/1)
# except ZeroDivisionError:
#     print("Cannot divide by 0")
# except Exception as e:
#     print(e)
#     # raise e
#
# else:
#     print("Good maths")

# finally:
#     print("Hello")
#     print("Hello")
#     print("Hello")
#     print("Hello")
#     print("Hello")
#     print("Hello")


try:
    age = int(input("Enter your age : "))

    if age > 30:
        raise ValueError("Age above 30 is invalid")
    else:
        print("Welcome")
except ValueError:
    print("You are too old!")
