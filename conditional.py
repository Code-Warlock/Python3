age = int(input("Enter your age : "))
if age > 18:
    print("Elligible to vote.")
elif age == 18:
    print("Wait after 4 years.")
else:
    print("Too young to vote.")
