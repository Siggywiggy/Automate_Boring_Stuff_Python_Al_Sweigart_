import re

# re.IGNORECASE as second argument in re.compile()

robocop = re.compile(r"robocop", re.IGNORECASE)
print(robocop.search("RoboCop is part man, part machine, all cop.").group())
print(robocop.search("ROBOCOP protects the innocent.").group())
print(
    robocop.search(
        "Al, why does your programming book talk about robocop so much?"
    ).group()
)
