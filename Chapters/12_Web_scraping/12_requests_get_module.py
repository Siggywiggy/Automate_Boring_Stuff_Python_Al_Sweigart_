import requests

res = requests.get("https://automatetheboringstuff.com/files/rj.txt")
print(type(res))
print(res.status_code == requests.codes.ok)
print(len(res.text))
print(res.text[:250])

res = requests.get("https://inventwithpython.com/page_that_does_not_exist")

# raise_for_status() will raise an exception if there was an error downloading the file
try:
    res.raise_for_status()
except Exception as exc:
    print(f"there was a problem {exc}")
