import random
import time
from fractions import Fraction

OPERATORS = ['+', '-', '*', '/']    # list of operators
MIN_OPERAND = 1                     # minimum value of an operand
MAX_OPERAND = 10                    # maximum value of an operand
TOTAL_PROBLEMS = 10                 # total number of problems

def generate_problem():
    left = random.randint(MIN_OPERAND, MAX_OPERAND)
    right = random.randint(MIN_OPERAND, MAX_OPERAND)
    operator = random.choice(OPERATORS)

    if operator == '/':
        while right == 0 or left % right != 0:
            right = random.randint(MIN_OPERAND, MAX_OPERAND)

    expr = str(left) + " " + operator + " " + str(right)
    answer = eval(expr)
    if operator == '/':
        answer = Fraction(left, right)
    return expr, answer

score = 0
problems_attempted = 0
start_time = time.time()

while problems_attempted < TOTAL_PROBLEMS:
    expr, answer = generate_problem()
    while True:
        guess = input(f"Problem #{problems_attempted + 1}: {expr} = ")
        try:
            guess_float = float(guess)
            if abs(guess_float - float(answer)) < 0.001:
                print("Correct!")
                score += 1
                problems_attempted += 1
                break
            else:
                print("Incorrect. Deducting a point and giving you an extra question.")
                score -= 1  # Deduct a point for incorrect answer
                TOTAL_PROBLEMS += 1  # Add an extra question
                problems_attempted += 1
                break
        except ValueError:
            print("Invalid input. Please enter a number.")
    
end_time = time.time()
total_time = end_time - start_time

print(f"\nYour score: {score} out of {TOTAL_PROBLEMS}")
print(f"You were lied to and got {TOTAL_PROBLEMS - score} wrong.")
print(f"Total time taken: {total_time:.2f} seconds")
