max = 0
enter = 0

for _ in range(10) :
    temp = input().split(" ")
    enter += int(temp[1]) - int(temp[0])
    max = enter if max < enter else max

print(max)