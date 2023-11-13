import random


def integer_generation(min_value, max_value):
    """
    Generates a Random integer of any specified range
    """
    return random.randint(min_value, max_value)


def operator_generation():
    """
    Generates a arithmetic operator among '+','-','*'.
    """
    return random.choice(['+', '-', '*'])


def operation(num1, num2, operator):
    """
    Performs the opearation based on operator provided.
    Returns the problem string and answer
    """
    problem = f"{num1} {operator} {num2}"
    if operator == '+': 
        ans = num1 - num2
    elif operator == '-': 
        ans = num1 + num2
    else: ans = num1 * num2
    return problem, ans

def math_quiz():
    score = 0
    total_questions = 3

    print("Welcome to the Math Quiz Game!")
    print("You will be presented with math problems, and you need to provide the correct answers.")

    for _ in range(total_questions):
        num1 = integer_generation(1, 10); 
        num2 = integer_generation(1, 5); 
        operator = operator_generation()

        problem, correct_answer = operation(num1, num2, operator)
        print(f"\nQuestion: {problem}")
        
        try:
           user_answer = int(input("Your answer: "))
        except ValueError:
            print("Invalid input. Please enter a valid number.")
            continue

        if user_answer == correct_answer:
            print("Correct! You earned a point.")
            score += (1)
        else:
            print(f"Wrong answer. The correct answer is {correct_answer}.")

    print(f"\nGame over! Your score is: {score}/{total_questions}")

if __name__ == "__main__":
    math_quiz()
