""" Marking guide problem with Files"""
import random
answer_file = input("Enter the text file name of your answers : ")

if ".txt" in answer_file:
    print("file name successful!")
else:
    answer_file = "".join(list(answer_file) + list(".txt"))
    # listed = list(answer_file)
    # extension_list = list(".txt")
    # full_filename = listed + extension_list
    # answer_file = "".join(full_filename)


with open(answer_file , "a+") as f:
    try:
        ref_user_answers = []
        correct_answers = []
        if f.read == "":
            raise OSError()
        else:
            f.seek(0)
            user_answers = f.readlines()
        for each in user_answers:
            ref_user_answers.append(each[0].lower())
        for x in range(len(user_answers)):
            generated_answers = ["abcd"[random.randrange(4)] for x in range(len(user_answers))] #List Comprehension
        for x in range(len(user_answers)):
            if generated_answers[x] == ref_user_answers[x]:
                correct_answers.append(user_answers[x])
            else:
                continue
        result_message = f"You scored {len(correct_answers)} / {len(user_answers)}"
        print(result_message)
        print(generated_answers)
    except OSError:
        print("The file name does not exist or the file is empty!")
