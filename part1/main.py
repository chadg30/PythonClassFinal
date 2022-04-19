# Python Final Project - Part 1
# Elijah McClymonds, Mike Elias, Chad Green
import csv
import random
import time


def main():

    print("Python Quiz")
    valid = False
    count = 0
    while True:
        # get and validate user info, User gets 3 attempts
        while not valid and count < 3:
            first_name = input("\nEnter your First Name: ")
            last_name = input("Enter your Last Name: ")
            student_id = input("Enter your Student ID: ")
            valid = validate_data(first_name, last_name, student_id, valid)
            count += 1
        if count == 3:
            print("Too Many Login Attempts")
            break

        questions, num_questions = generate_questions()
        take_quiz(questions, num_questions)

        # finishing
        user_input = input("\n\nDo you want to quit or start again? (q/s): ").lower()
        if user_input == "q":
            break
        elif user_input == "s":
            valid = False
            count = 0
        # exception for input?
    print("Bye!")


# chad man dude bro
def validate_data(first_name, last_name, student_id, valid):
    # 3 attempts max to validate
    count = 0

    if not first_name.strip().isalpha():  # check if name is alpha
        print("Invalid Name Entered, Try Again")
        return False
    if not last_name.strip().isalpha():  # check if last name is alpha
        print("Invalid Name Entered, Try Again")
        return False
    if not len(student_id) == 6:  # check student ID length
        print("Student ID incorrect length, Try Again")
        return False
    if not student_id[0] == 'A':  # check if student ID starts with A
        print("Student ID incorrect, Try Again")
        return False
    if int(student_id[1:5].isdigit()):  # check if end of ID is numerical
        for char in student_id[1:5]:  # check if each digit in end of ID is between 1 and 9
            if 1 <= int(char) <= 9:
                valid = True
            else:
                print("Invalid Student ID, Try Again")
                return False
    else:
        print("Invalid Student ID, Try Again")

    return valid


# elijah MidClymonds
def generate_questions():
    # randomly pick 10 questions from csv file
    with open("CPSC 236 TestBank - Sheet1.csv", "r") as file:
        reader = csv.reader(file)
        rows = list(reader)
        quiz_questions = []
        question_count = 0
        while True:
            try:
                num_questions = int(input("How many questions? (10 or 20): "))
                if not num_questions == 10 and not num_questions == 20:
                    print("Incorrect question value.")
                else:
                    if num_questions == 10:
                        print("Questions are worth 1 point each.")
                    else:
                        print("Questions are worth 0.5 point each.")
                    break
            except ValueError:
                print("Must be an integer")
        for content in rows:
            # we don't need the group number
            content.pop(0)
            # avoid adding first row
            if content != rows[0] and question_count < num_questions:
                random_question = random.randint(1, 72)
                if not rows[random_question] in quiz_questions:
                    quiz_questions.append(rows[random_question])
                    question_count += 1
    # using this section to generate questions for my own test purposes
    return quiz_questions, num_questions


# mike man
def take_quiz(quiz_questions, num_questions):
    start_time = time.time()
    elapsed = 0
    question_num = 1
    score = 0
    valid_answers = ["A", "B", "C"]
    for value in quiz_questions:
        if elapsed < 60*10:
            print("Question " + str(question_num) + ":")
            print(value[0])
            print("A: " + str(value[1]))
            print("B: " + str(value[2]))
            print("C: " + str(value[3]))
            answer = input("\nWhich is the correct answer (a/b/c)?: ").upper()
            # validates answers (must be 'A', 'B', or 'C')
            # also avoids numerical answers
            while answer not in valid_answers:
                print("Invalid answer. Try again.")
                answer = input("\nWhich is the correct answer (a/b/c)?: ").upper()
            if answer == value[4]:
                print("Correct!\n")
                score += 1
            else:
                print("That's incorrect!\n")
            question_num += 1
            elapsed = time.time() - start_time
        else:
            print("You've run out of time")
            break

    if num_questions == 10:
        print("\nFinal Score: "+str(score)+"/10")
    else:
        print("\nFinal Score: %1.0f"+str(score*0.5)+"/10.0")
    print("Time taken: " + conversion(elapsed))


# chad man dude bro
def conversion(seconds):
    # toggle between start and stop timer
    seconds = seconds % (24 * 3600)
    minutes = seconds // 60
    seconds %= 60

    return "%02d:%02d" % (minutes, seconds)


# mike man
def record_data(student_id, firstname, lastname, score, elapsed_time, questions):
    # write statistics to text file
    pass


if __name__ == "__main__":
    main()
