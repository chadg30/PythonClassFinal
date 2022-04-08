# Python Final Project - Part 1
# Elijah McClymonds, Mike Elias, Chad Green

from time import perf_counter


def main():
    print("Pain\n")
    while True:
        first_name = input("Enter your First Name: ")
        last_name = input("Enter your Last Name: ")
        student_id = input("Enter your Student ID: ")

        # finishing
        user_input = input("Do you want to quit or start again? (q/s): ").lower()
        if user_input == "q":
            break
        elif user_input == "s":
            print("Restarting...")
        # exception for input?
    print("Bye!")


#chad man dude bro
def validate_data(first_name, last_name, student_id):
    # 3 attempts max to validate
    pass


#elijah md
def generate_questions():
    # randomly pick 10 questions from csv file
    pass


#mike man
def display_question():
    #check for input validation for answers
    pass


#chad man dude bro
def toggle_timer():
    #toggle between start and stop timer
    pass


#mike man
def record_data():
    #write statistics to text file
    pass


if __name__ == "__main__":
    main()
