S = input()
check = False
answer = []
temp = ""

for i in S :
    if i == "<" :
        answer.append(temp[::-1] + i)
        temp = ""
        check = True
        continue
    elif i == ">" :
        answer.append(i)
        check = False
        continue
    if check :
        answer.append(i)
    else :
        if i == " " :
            answer.append(temp[::-1] + i)
            temp = ""
        else :
            temp += i

answer.append(temp[::-1])

print("".join(answer))