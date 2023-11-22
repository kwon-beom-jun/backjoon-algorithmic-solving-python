num = int(input())
answer = ""

for _ in range(num) :
    temp = ""
    for i in input() :
        if temp == i :
            continue
        else :
            temp = i
            answer += i
    answer += "\n"

print(answer)