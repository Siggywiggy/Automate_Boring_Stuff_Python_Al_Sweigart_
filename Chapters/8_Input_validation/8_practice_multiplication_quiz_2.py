#! python 3

# multiplication quiz

import random
import time

num_of_questions = 10
correct_answers = 0

# outer loop for each question


for question in range(0, num_of_questions):
    num_tries = 3
    num_1 = random.randint(0, 9)
    num_2 = random.randint(0, 9)
    answer = 0
    correct_answer = 0
    print(f"Question number {question + 1}")

    print(f"Whats the result of multiplying {num_1} and {num_2}?")

    # take the start time

    start_time = time.time()

    while num_tries > 0:
        # inner loop to determine if user entered an integer or not
        while True:
            answer = input("Whats your answer? ")
            try:
                answer = int(answer)
                break
            except:
                continue

        # determine if answer is correct or not:

        if answer == (num_1 * num_2):
            print("Correct answer!")
            correct_answer = 1
            time.sleep(1)
            break
        else:
            print("Try again!")
            num_tries -= 1
            print(f"You have {num_tries} left!")

    # take the end time

    end_time = time.time()

    # determine if the player took too long to reply

    if end_time - start_time > 8:
        print(
            f"It took you too long to answer the question! {end_time - start_time} seconds!"
        )
    # add to correct answers if the answer was corrent and didnt take too long

    elif correct_answer == 1:
        correct_answers += 1
        print(f"You have {correct_answers} correct answers so far!")

print(
    f"You answered {correct_answers} answers correctly to {num_of_questions} questions"
)
