# Python Final Project - Part 1
# Elijah McClymonds, Mike Elias, Chad Green

from time import perf_counter


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

        # finishing
        user_input = input("Do you want to quit or start again? (q/s): ").lower()
        if user_input == "q":
            break
        elif user_input == "s":
            print("Restarting...")
            valid = False
            count = 0
        # exception for input?
    print("Bye!")


# chad man dude bro
def validate_data(first_name, last_name, student_id, valid):
    # 3 attempts max to validate
    count = 0

    if first_name.strip().isalpha():  # check if name is alpha
        valid = True
    else:
        print("Invalid Name Entered, Try Again")
        return False
    if last_name.strip().isalpha():  # check if last name is alpha
        valid = True
    else:
        print("Invalid Name Entered, Try Again")
        return False
    if len(student_id) == 6:  # check student ID length
        valid = True
    else:
        print("Student ID incorrect length, Try Again")
        return False
    if student_id[0] == 'A':  # check if student ID starts with A
        valid = True
    else:
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
    pass


# mike man
def display_question():
    # check for input validation for answers
    pass


# chad man dude bro
def toggle_timer():
    # toggle between start and stop timer
    pass


# mike man
def record_data():
    # write statistics to text file
    pass


if __name__ == "__main__":
    main()
