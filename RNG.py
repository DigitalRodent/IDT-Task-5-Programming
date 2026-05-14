# Let your ideas run wild!
import random

score = 0
question_count = 0

print("Answer the maths questions.")
print("Enter x to exit the quiz early.")

# Quiz loop
while question_count < 10:

    # Generate random numbers
    num1 = random.randint(0, 10)
    num2 = random.randint(0, 10)

    # Choose random operation
    operation = random.choice(["+", "-", "*", "/"])

    # Stop division by zero
    if operation == "/":
        while num2 == 0:
            num2 = random.randint(1, 10)

    # Calculate correct answer
    if operation == "+":
        correct_answer = num1 + num2

    elif operation == "-":
        correct_answer = num1 - num2

    elif operation == "*":
        correct_answer = num1 * num2

    else:
        correct_answer = float(num1) / num2
        correct_answer = round(correct_answer, 2)

    # Ask question
    user_answer = input(
        f"Question {question_count + 1}: "
        f"{num1} {operation} {num2} = "
    )

    if user_answer.lower() == "x":
        print("You have exited the quiz early.")
        break

    try:
        user_answer = float(user_answer)

        if user_answer == correct_answer:
            print("Correct!")
            score = score + 1
        else:
            print(f"Incorrect. The correct answer was {correct_answer}")

    except ValueError:
        print(f"Invalid answer. The correct answer was {correct_answer}")

    question_count = question_count + 1

print(f"Your final score is {score}/10")
input("Press Enter to exit.")