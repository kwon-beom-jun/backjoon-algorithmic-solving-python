num = int(input())
answer = []

for _ in range(num) :
    temp = input()
    sqrt_num = int(len(temp) ** 0.5)

    if sqrt_num == 1 :
        answer.append(temp)
    else :
        for i in range(sqrt_num) :
            for j in range(1, sqrt_num+1) :
                answer.append(temp[sqrt_num*j-i-1])
    
    answer.append("\n")

print(''.join(answer))