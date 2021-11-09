""" Loops in Python """
import random
name = input("Enter your name : ")
cgp = random.randint(1233,1235)
print(f"""Welcome {name}
Your pin is {cgp}
Now Login with your details""")

# for x in range(12):
#     if x == 5:
#         break
#     print(x)
pin = int(input("Enter your PIN : "))
count = 1
while True:
    if pin == cgp:
        print("Login Successful!")
        break
    else:
        if count == 3:
            print("Three unsuccessful trials\nYour Card has been blocked!")
            break
        else:
            pin = int(input("Wrong Input!\nEnter your PIN : "))
            count += 1
