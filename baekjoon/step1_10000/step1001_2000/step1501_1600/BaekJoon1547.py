num = int(input())
now = '1'

for _ in range(num) :
    temp = input()
    if temp[0] == now :
        now = temp[2]
    elif temp[2] == now :
        now = temp[0]

print(now)