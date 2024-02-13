import pyinputplus as pyip
import random
import time

# a program of 10 multiplication problems

number_of_questions = 10
correct_answers = 0

for question_number in range(number_of_questions):
    num_1 = random.randint(0, 9)
    num_2 = random.randint(0, 9)
    result = num_1 * num_2

    prompt = f"{question_number + 1}. Whats the result of multiplicating {num_1} and {num_2}? "

    try:
        # right answers are handled by allowRegexes
        # wrong answers are handled by blockRegexes with a custom message
        pyip.inputStr(
            prompt,
            allowRegexes=[rf"{result}"],
            blockRegexes=[(".*", "Incorrect!")],
            timeout=8,
            limit=3,
        )

    except pyip.TimeoutException:
        print("Out of time!")
    except pyip.RetryLimitException:
        print("You are out of tries")

    else:
        # This block runs if no exceptions were raised in the try block
        print("Correct!")
        correct_answers += 1

    time.sleep(1)  # brief pause to let user see the result

print(
    f"Score: {correct_answers} correct answers out of {number_of_questions} questions!"
)
