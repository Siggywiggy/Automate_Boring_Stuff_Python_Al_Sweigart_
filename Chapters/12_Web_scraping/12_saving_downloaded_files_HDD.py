import requests
import pprint

res = requests.get("https://automatetheboringstuff.com/files/rj.txt")
try:
    res.raise_for_status()
except Exception as exc:
    print(f"There was a problem: {exc}")

play_file = open("Romeo_and_Juliet.txt", "wb")  # write binary

for chunk in res.iter_content(
    100000
):  # iter_content() returns chunks (byte data type) - specify how many bytes per chunk
    print(play_file.write(chunk))

print(res.headers)
play_file.close()


