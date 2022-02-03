""" Creating a search engine in Python 3 """


# Let's dig in 


def create_grocery_list():
  """Function to create a grocery list """
  items = list()
  count = 1
  # Ask the user if he wants to continue after a 3 entry interval.
  while True:
    item = input("Enter the grocery you wanna add : ").lower()
    items.append(item)
    count += 1
    if count % 3 == 0:
      # Meaning the count is a multiple of 3 😊
      ans = input("Do you still wanna add more groceries !")
      if "y" in ans:
        break
  return items


# Test grocery list 

print(create_grocery_list())