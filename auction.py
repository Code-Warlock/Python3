def auction(price , year):
    this_year = 2021
    diff = this_year - year
    rate = 0.2
    return f"#{(price * (1 - rate)) ** diff}"

initial_price = float(input("Enter the initial price of the car : "))
year_of_purchase = int(input("Enter the year of purchase : "))

print(auction(initial_price , year_of_purchase))
