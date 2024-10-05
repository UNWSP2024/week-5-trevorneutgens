# Program #2: Math Quiz
# Write a program that gives simple math quizzes.  The program should display two random numbers to be added, such as
import random

def give_problem():
    # Generate two random numbers between 1 and 1000
    first_addition = random.randint(1, 1000)
    second_addition = random.randint(1, 1000)

    # Prompt the user for an answer with a clear message
    answer = int(input(f"   {first_addition}\n + {second_addition}\n _______\n "))
    calculate_answer(answer, first_addition, second_addition)

def calculate_answer(answer, first_addition, second_addition):
    correct_answer = first_addition + second_addition  # Correctly calculate the answer
    if answer == correct_answer:
        print("congratulations")
    else:
        print(f"The correct answer is: {correct_answer}")  # Print the correct answer

    # Ask the user if they want to continue
    if input("Do you want to try another problem? (enter 'y' for yes): ") == 'y':
        give_problem()
    else:
        print("Thanks for playing!")
give_problem()
# The program should allow the student to enter the answer.  
# If the answer is correct, a message of congratulations should be displayed.  
# If the answer is incorrect a message showing the correct answer should be displayed.  
# The program must use a function that accomplishes part of the needed tasks.