import random

num_of_streaks = 0


# main program loop to run for 10000 times

for experiment_number in range(10000):
    # generating a list of values
    list_of_values = []

    for i in range(100):
        flip = random.randint(0, 1)
        if flip == 0:
            list_of_values.append("H")
        else:
            list_of_values.append("T")

    # counting streaks

    streak_counter = 0

    for index, item in enumerate(list_of_values):
        if item == list_of_values[index - 1]:
            streak_counter += 1
        else:
            streak_counter = 0  # "no match, counter reset to 0"

        if streak_counter == 5:
            # print(f"a streak found of {item}!")
            streak_counter = 0  # resetting streak counter
            num_of_streaks += 1
            break  # dont want to double count treaks, only one streak per 100 flips is important


print(f"found {num_of_streaks} streaks!")

print("Chance of streak: %s%%" % (num_of_streaks / 100))
