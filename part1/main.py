# Python Final Project - Part 1
# Elijah McClymonds, Mike Elias, Chad Green
import csv
import random
import time
import os


def main():
    # initializing data
    first_name = ''
    last_name = ''
    student_id = ''
    data_is_valid = False
    num_attempts = 0

    # program start
    print("Python Quiz")

    # continuously run program unless data is not valid OR user quits at the end
    while True:
        # get and validate user's first/last name and ID
        # user gets 3 attempts to enter data correctly
        while not data_is_valid and num_attempts < 3:
            first_name = input("\nEnter your First Name: ")
            last_name = input("Enter your Last Name: ")
            student_id = input("Enter your Student ID: ")
            data_is_valid = validate_data(first_name, last_name, student_id)
            num_attempts += 1

        # exit program if user does not enter data correctly in 3 attempts
        if num_attempts == 3:
            print("\nToo Many Login Attempts")
            break

        # randomly generate quiz questions if user-entered data is valid
        questions, num_questions = generate_questions()

        # take the quiz using randomized questions
        score, time_taken, answers = take_quiz(questions, num_questions)

        # record data to a text file based on the individual
        record_data(student_id, first_name, last_name, score, time_taken, questions, answers)

        # ask user if they want to take another quiz or exit program
        user_input = input("\n\nDo you want to quit or start again? (q/s): ").lower()
        if user_input == "q":
            break
        elif user_input == "s":
            clear_console()
            data_is_valid = False
            num_attempts = 0

    # program is complete; can terminate
    print("Bye!")


# code written by Chad Green
def validate_data(first_name, last_name, student_id):
    if not first_name.strip().isalpha():  # check if name is alpha
        print("Invalid Name Entered, Try Again.")
        return False
    if not last_name.strip().isalpha():  # check if last name is alpha
        print("Invalid Name Entered, Try Again.")
        return False
    if not len(student_id) == 6:  # check student ID length
        print("Student ID incorrect length, Try Again.")
        return False
    if not student_id[0] == 'A':  # check if student ID starts with A
        print("Student ID incorrect, Try Again.")
        return False
    if int(student_id[1:5].isdigit()):  # check if end of ID is numerical
        for char in student_id[1:5]:  # check if each digit in end of ID is between 1 and 9
            if 1 <= int(char) <= 9:
                return True
            else:
                print("Invalid Student ID, Try Again")
                return False


# code written by Mike Elias
def clear_console():
    print("Clearing screen...")
    time.sleep(2)  # waits 2 seconds before proceeding to illustrate clearing process
    print("\n" * 50)
    if os.name == 'nt':  # windows OS
        _ = os.system("cls")
    else:  # linux or macOS
        _ = os.system("clear")


# code written by Elijah McClymonds and Mike Elias
def generate_questions():
    # read TestBank file for questions
    with open("CPSC 236 TestBank - Sheet1.csv", "r") as file:
        reader = csv.reader(file)
        next(reader)  # skips context row from csv file
        rows = list(reader)
        quiz_questions = []
        question_count = 0

    # Get number of desired questions (10 or 20) from user
    while True:
        try:
            num_questions = int(input("\nHow many questions? (10 or 20): "))
            if not num_questions == 10 and not num_questions == 20:
                print("Incorrect question value.")
            else:
                if num_questions == 10:
                    print("Questions are worth 1 point each.\n")
                else:
                    print("Questions are worth 0.5 point each.\n")
                break
        except ValueError:
            print("Must be an integer")

    # add random questions to list from csv reader
    for content in rows:
        content.pop(0)  # skips first value in row (group number, not relevant to quiz)
        random_question = random.randint(0, 71)

        # check if question is already in questions list and if the max questions has already been reached
        if not rows[random_question] in quiz_questions and len(quiz_questions) < num_questions:
            quiz_questions.append(rows[random_question])
            question_count += 1
    return quiz_questions, num_questions


# code written by Mike Elias
def take_quiz(quiz_questions, num_questions):
    start_time = time.time()  # start a timer to keep track of elapsed time
    elapsed = 0
    question_num = 1  # for displaying the question number to the console
    score = 0  # user's score on the quiz
    valid_answers = ["A", "B", "C"]  # valid answers for input when taking the quiz
    student_answers = []  # keep track of student's responses

    # display one question at a time
    for value in quiz_questions:
        if elapsed < 60 * 10:  # if the elapsed time goes over 10 minutes, next question will not appear
            print("Question " + str(question_num) + ":")
            question = value[0]
            answer_a = value[1]
            answer_b = value[2]
            answer_c = value[3]
            correct_answer = value[4]
            print(question)
            print("A: " + str(answer_a))
            print("B: " + str(answer_b))
            print("C: " + str(answer_c))
            answer = input("\nWhich is the correct answer (a/b/c)?: ").upper()

            # validate answers given by user (can't be numerical and must be in the valid answers list)
            while answer not in valid_answers:
                print("Invalid answer. Try again.")
                answer = input("\nWhich is the correct answer (a/b/c)?: ").upper()
            student_answers.append(answer)
            if answer == correct_answer:
                print("Correct!\n")
                score += 1
            else:
                print("That's incorrect!\n")
            question_num += 1
            elapsed = time.time() - start_time
        else:
            print("You've run out of time. Quiz is ending.")
            break

    if num_questions == 10:
        print("\nFinal Score: " + str(score) + "/10")
    else:
        print("\nFinal Score: %1.0f" + str(score * 0.5) + "/10.0")
    time_taken = conversion(elapsed)
    print("Time taken: " + time_taken)

    return score, time_taken, student_answers


# code written by Chad Green
def conversion(seconds):
    # This function takes the time that it took the student to complete the quiz and
    # converts it from seconds to minutes and seconds
    seconds = seconds % (24 * 3600)
    minutes = seconds // 60
    seconds %= 60

    return "%02d:%02d" % (minutes, seconds)


# code written by Chad Green and Mike Elias
def record_data(student_id, firstname, lastname, score, elapsed_time, questions, answers):
    filename = student_id + "_" + firstname + "_" + lastname  # creates format: A12345_Raed_Seetan.txt
    with open("responses/%s.txt" % filename, "w") as file:
        file.write("Student ID:\t" + student_id + "\n")
        file.write("First Name:\t" + firstname + "\n")
        file.write("Last Name:\t" + lastname + "\n")
        file.write("Test Score:\t" + str(score) + "/10\n")
        file.write("Time Taken:\t" + str(elapsed_time) + "\n")
        file.write("\nQuestions:\n\n")
        question_num = 1  # keep track of question number for writing purposes
        for data in questions:
            question = str(question_num)+": "+data[0]  # the question being asked
            answer_a = "A) "+data[1]  # answer choice A
            answer_b = "B) "+data[2]  # answer choice B
            answer_c = "C) "+data[3]  # answer choice C
            submitted_answer = answers[question_num-1]  # answer chosen by user
            correct_answer = data[4]  # correct answer to question

            # write the data to individual text file
            file.write(question+"\n")
            file.write(answer_a+"\n")
            file.write(answer_b+"\n")
            file.write(answer_c+"\n")
            file.write("Submitted Answer:\t"+submitted_answer+"\n")
            file.write("Correct Answer:\t\t"+correct_answer+("\n" * 3))
            question_num += 1


if __name__ == "__main__":
    main()
