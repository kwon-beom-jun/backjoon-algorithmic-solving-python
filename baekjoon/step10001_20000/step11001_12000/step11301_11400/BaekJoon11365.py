strings = []

while True:
    cipher = input()
    if cipher == "END":
        break
    else:
        strings.append(cipher[::-1]+"\n")

print(''.join(strings))