""" A palindrome programm in python """
# while True:
#     word = input("Enter your word : ").lower()
#     characters = list(word)
#     characters.reverse()
#     reversed_word = "".join(characters)
#     if word == reversed_word:
#         print("Word is a palindrome!")
#     else:
#         print("Word is not a palindrome!")
#     answer = input("Do you want to continue? y/n : ")
#     if answer == "y":
#         continue
#     else:
#         break
while True:
    word = input("Enter your word : ").lower()
    if word == word[::-1]:
        print("Word is a palindrome!")
    else:
        print("Word is not a palindrome!")
    answer = input("Do you want to continue? yes/no : ")
    if answer == "yes":
        continue
    else:
        break
