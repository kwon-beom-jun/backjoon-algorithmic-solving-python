result = ""

while True:
    word = input()
    if word == "***":
        break
    result += "".join(reversed(word)) + "\n"

print(result)