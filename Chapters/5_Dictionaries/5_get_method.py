picnic_items = {"apples": 5, "cups": 2}

# get() method takes 2 arguments - the key of the value to retrieve and a fallback value if the key does not exist
print("I am bringing " + str(picnic_items.get("cups", 0)) + " cups.")

print("I am bringing " + str(picnic_items.get("eggs", 0)) + " eggs.")
