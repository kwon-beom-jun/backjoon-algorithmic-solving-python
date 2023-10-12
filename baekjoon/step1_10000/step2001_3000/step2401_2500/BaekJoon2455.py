temp = input().split(" ")
num = int(temp[1])
max = int(temp[1])

for _ in range(3) :
    temp = input().split(" ")
    num += int(temp[1]) - int(temp[0])
    max = max if max > num else num

print(max)