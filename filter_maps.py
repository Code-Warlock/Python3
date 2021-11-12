""" Filters and Maps in Python"""

numbers = list(range(10))
def check_evens(num):
    return num % 2 == 0
def square(num):
    return num ** 2
squared = list(map(square , numbers))
# evens = list(filter(check_evens , numbers))

# for each in numbers:
#     squared.append(each**2)
#
# for each in numbers:
#     if each % 2 == 0:
#         evens.append(each)

print(squared)
# print(evens)
