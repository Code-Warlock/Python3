"""String formatting in Python."""
# x = 8
# y = 9
# z = 10
# values = f"""The value of x is : {x}
# ________|_______________|____________
# The value of y is : {y}
# ________|_______________|____________
# The value of z is : {z}
# ________|_______________|____________
# """
# print(values)
name = input("Enter your name : ")
stock = input("What are you purchasing : ")
amount = float(input("How much are you gonna to pay : "))

print(f"""
              |              |              |
Customer name |     STOCK    |       AMOUNT |
______________|______________|______________|
{name}       |{stock:>7}       |   \u20A6{amount:^10,.2f}   |
 """)
# number = float(input("Enter an amount : "))
# name = "Desmond"
# test = f"""{name} The amount you entered was
#  #{number:^}"""
# print(test)
