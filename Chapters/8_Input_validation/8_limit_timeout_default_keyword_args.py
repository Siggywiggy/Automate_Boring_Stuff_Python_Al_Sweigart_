import pyinputplus as pypi

# If the user fails to enter valid input, these keyword arguments
# will cause the function to raise a RetryLimitException or TimeoutException, respectively.

response = pypi.inputNum(
    "Input number, you have 2 tries: ", limit=2
)  # limit of 2 entries, will raise RetryLimitException

response = pypi.inputNum(
    "Input number, you have 10 seconds: ", timeout=10
)  # 10 second time limit, will raise TimeoutException

# default keyword - function returns default value instead of raising an exception

response = pypi.inputNum(
    "Enter a number, you have 2 tries: ",
    limit=2,
    default="You went over the limit of 2",
)
