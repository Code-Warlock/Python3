"""List Comprehensions """
odds = [x for x in range(10) if x % 2 != 0]
# odds = [x if x % 2 != 0 else x**2 for x in range(10)]


# for x in range(10):
#     if x % 2 != 0:
#         odds.append(x)
print(odds)
