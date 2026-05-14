# IMPORTS
import os
import random
import time


PAST_HIGH_SCORES_FILE = "past_high_scores.txt"
today_high_scores = []


def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")


def display_menu():
    os.system("cls" if os.name == "nt" else "clear")
    print("Welcome to the Maths Quiz game. Please choose from the menu below:")
    print("--------------------------------------------------------------------")
    print("(A) New Game")
    print("(B) View Today's High Scores")
    print("(C) View Past High Sores")
    print("(D) Exit")


def get_menu_choice():
    choice = input("What would you like to do? Enter the letter option. ")
    choice = choice.upper()
    return choice


def generate_question():
    number_one = random.randint(0, 10)
    number_two = random.randint(0, 10)
    operation = random.choice(["+", "-", "*", "/"])

    if operation == "+":
        answer = number_one + number_two
        question = str(number_one) + " + " + str(number_two)

    elif operation == "-":
        answer = number_one - number_two
        question = str(number_one) + " - " + str(number_two)

    elif operation == "*":
        answer = number_one * number_two
        question = str(number_one) + " x " + str(number_two)

    else:
        while number_two == 0:
            number_two = random.randint(1, 10)

        answer = number_one / number_two
        answer = round(answer, 2)
        question = str(number_one) + " / " + str(number_two)

    return question, answer


def save_score_to_file(student_name, score):
    high_scores_file = open(PAST_HIGH_SCORES_FILE, "a")
    high_scores_file.write(student_name + " - " + str(score) + "/10\n")
    high_scores_file.close()


def play_quiz():
    score = 0
    student_name = input("Enter your name: ")
    student_name = student_name.title()

    print()
    print("Welcome", student_name)
    print("You will be asked 10 maths questions.")
    print("Enter x at any time to exit the quiz early.")
    print()

    for question_number in range(1, 11):
        question, correct_answer = generate_question()

        print("Question", question_number)
        user_answer = input(question + " = ")

        if user_answer.lower() == "x":
            print("You have exited the quiz early.")
            time.sleep(1)
            print()
            return

        try:
            user_answer = float(user_answer)

            if user_answer == correct_answer:
                print("Correct!")
                score = score + 1
            else:
                print("Incorrect. The correct answer was", correct_answer)

        except ValueError:
            print("Invalid answer. The correct answer was", correct_answer)

        print()

    print(student_name + ", your final score is " + str(score) + "/10")
    print()

    today_high_scores.append([student_name, score])
    save_score_to_file(student_name, score)

    input("Press Enter to return to the main menu.")
    print()


def view_today_high_scores():
    print()
    print("Today's High Scores")
    print("-------------------")

    if len(today_high_scores) == 0:
        print("No scores have been recorded today.")
    else:
        for high_score in today_high_scores:
            print(high_score[0] + " - " + str(high_score[1]) + "/10")

    print()


def view_past_high_scores():
    print()
    print("Past High Scores")
    print("----------------")

    try:
        high_scores_file = open(PAST_HIGH_SCORES_FILE, "r")
        high_scores = high_scores_file.readlines()
        high_scores_file.close()

        if len(high_scores) == 0:
            print("No past scores have been recorded.")
        else:
            for high_score in high_scores:
                print(high_score.strip())

    except FileNotFoundError:
        print("No past scores have been recorded.")

    print()


def main():
    running = True

    while running:
        display_menu()
        choice = get_menu_choice()
        print()

        if choice == "A":
            play_quiz()

        elif choice == "B":
            view_today_high_scores()

        elif choice == "C":
            view_past_high_scores()

        elif choice == "D":
            print("Thank you for playing Maths Quiz.")
            running = False

        else:
            print("Invalid option. Please enter A, B, C or D.")
            print()


main()