""" Shopping cart program in Python """
# =============================================VegWare==============================
name = input("Enter your name : ")
cart = dict()
items = ["Spinach","Carrot","Spring Onions","Lettuce","EggPlant","Turnip","Pumpkin","Cabbage"]
products = []
prices = [10000, 20000 , 9000 , 8000 , 30000 , 10000 , 12000 , 19000]
print(f"""================================Welcome {name} to VegWare====================================
_______________________________-The home to all kinds of Veggies-_____________________________
                                Select from the options below.

1.   Spinach (₦{prices[0]:,.2f})                                           5.   EggPlant (₦{prices[4]:,.2f})

2.   Carrot  (₦{prices[1]:,.2f})                                           6.   Turnip (₦{prices[5]:,.2f})

3.   Spring Onions (₦{prices[2]:,.2f})                                      7.   Pumpkin (₦{prices[6]:,.2f})

4.   Lettuce  (₦{prices[3]:,.2f})                                           8.   Cabbage (₦{prices[7]:,.2f})

""")
while True:
    selection = input("Enter your item : ").lower()
    if selection == "1" or "spi" in selection:
        no_of_items = int(input(f"How many spinach do you want to add to cart ==> (₦{10000:,.2f}) each : "))
        cart[items[0]] = [no_of_items,prices[0] * no_of_items]

    elif selection == "2" or "car" in selection:
        no_of_items = int(input(f"How many carrots do you want to add to cart ==> (₦{20000:,.2f}) each : "))
        cart[items[1]] = [no_of_items , prices[1] * no_of_items]

    elif selection == "3" or "spr" in selection or "onions" in selection:
        no_of_items = int(input(f"How many Spring Onions do you want to add to cart ==> (₦{9000:,.2f}) each : "))
        cart[items[2]] = [no_of_items , prices[2] * no_of_items]

    elif selection == "4" or "let" in selection:
        no_of_items = int(input(f"How many Lettuce do you want to add to cart ==> (₦{8000:,.2f}) each : "))
        cart[items[3]] = [no_of_items , prices[3] * no_of_items]

    elif selection == "5" or "egg" in selection:
        no_of_items = int(input(f"How many Egg Plants do you want to add to cart ==> (₦{30000:,.2f}) each : "))
        cart[items[4]] = [no_of_items , prices[4] * no_of_items]

    elif selection == "6" or "tur" in selection:
        no_of_items = int(input(f"How many Turnips do you want to add to cart ==> (₦{10000:,.2f}) each : "))
        cart[items[5]] = [no_of_items , prices[5] * no_of_items]

    elif selection == "7" or "pump" in selection:
        no_of_items = int(input(f"How many Pumpkin do you want to add to cart ==> (₦{12000:,.2f}) each : "))
        cart[items[6]] = [no_of_items , prices[6] * no_of_items]

    elif selection == "8" or "cabb" in selection:
        no_of_items = int(input(f"How many Cabbage do you want to add to cart ==> (₦{19000:,.2f}) each : "))
        cart[items[7]] = [no_of_items , prices[7] * no_of_items]
    continue_shopping = input("Do you want to add another? : y/n ")

    if "y" in continue_shopping or "" == continue_shopping:
        continue
    else:
        for each in cart.items():
            products.append(each)
        print(products)
        length = len(products)
        length_static = length
        print(f"""Vegetables     |     No of Individual item bought   |    Price
{products[length_static - length][0]}                 |     {products[length_static - length][1][0]}            |    {products[length_static - length][1][1]}
        """)
        break
print(cart)
