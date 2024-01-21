N = []

line = input().split()[1:]

for num in line :
    N.append(int(num[::-1]))

while True :
    try :
        line = input().split()
        for num in line:
            N.append(int(num[::-1]))
    except :
        break

print("\n".join(map(str, sorted(N))))