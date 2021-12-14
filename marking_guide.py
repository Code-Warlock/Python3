""" Marking Guide """
import random

"""
Students / Student took an exam of variable amount of questions.
==> Ask the student for the number of question he took.
==> Ask the student to type the answers to the questions he took.
==> Tell the user his result from the number of questions he answered
"""
while True:
    try:
        string_of_answers = "abcd"
        generated_answers = list() # a , b , c or d
        user_answers = []
        correct_answers = list()
        number_of_questions = int(input("Enter the number of questions you answered? : "))
        for x in range(number_of_questions):
            range_of_answers = random.randrange(4) # 0 - 3
            generated_answers.append(string_of_answers[range_of_answers])
        for each in range(number_of_questions):
            user_answers.append(input(f"Enter your answer for question {each + 1} : "))
        for x in range(number_of_questions):
            if generated_answers[x] == user_answers[x]:
                correct_answers.append(user_answers[x])
            else:
                continue
        result_message = f"You scored {len(correct_answers)} / {number_of_questions}"
        print(result_message)
    except ValueError:
        continue
    else:
        break
