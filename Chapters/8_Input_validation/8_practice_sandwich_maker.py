import pyinputplus as pyip
import time

bread_type = {"white bread": 2, "wheat bread": 2.5, "sourdough bread": 3}

protein_type = {"chicken": 5, "turkey": 7, "ham": 9, "tofu": 4}

cheese_type = {"cheddar cheese": 3, "swiss cheese": 4, "mozzarella cheese": 2}

condiment_type = {"mayo": 2, "mustard": 3, "lettuce": 1, "tomato": 1.5}


running_sum = 0

response_bread = pyip.inputMenu(
    list(bread_type.keys()), prompt=f"What type of bread would you like? \n"
)
running_sum += bread_type[response_bread]

response_protein = pyip.inputMenu(
    list(protein_type.keys()), prompt=f"What type of protein would you like? \n"
)
running_sum += protein_type[response_protein]

cheese_boolean = pyip.inputYesNo("Would you like cheese on your sandwich? ")

if cheese_boolean == "yes":
    response_cheese = pyip.inputMenu(
        list(cheese_type.keys()), prompt=f"What type of cheese would you like? \n"
    )
    running_sum += cheese_type[response_cheese]
else:
    response_cheese = "no cheese"

condiment_boolean = pyip.inputYesNo("Would you like any condiments on your sandwich? ")

if condiment_boolean == "yes":
    response_condiment = pyip.inputMenu(
        list(condiment_type.keys()), prompt=f"What type of condiment would you like? \n"
    )
    running_sum += condiment_type[response_condiment]
else:
    response_condiment = "no condiments"

count_sandwiches = pyip.inputInt(
    prompt="Please enter how many sandwiches you would like: \n", greaterThan=0
)
total_sum = count_sandwiches * running_sum

print(
    f"""Thank you for your order, you ordered {response_bread} 
sandwich with {response_protein}, {response_cheese} and {response_condiment}.\n
The total sum for your order is {total_sum} €"""
)
