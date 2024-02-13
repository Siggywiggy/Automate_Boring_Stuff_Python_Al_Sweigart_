import pprint

message = "It was a bright cold day in April, and the clocks were striking thirteen."

count = {}

for character in message:
    count.setdefault(character, 0)
    count[character] += 1

pprint.pprint(count)

# pprint.pformat() returns prettified text as string value instead of displaying it on the screen
print(pprint.pformat(count))
