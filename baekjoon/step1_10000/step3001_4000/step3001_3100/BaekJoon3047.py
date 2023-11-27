arr = map(int, input().split())
answer = ""

arr = sorted(arr)

for i in input() :
    if i == "A" :
        answer += str(arr[0]) + " "
    elif i == "B" :
        answer += str(arr[1]) + " "
    else :
        answer += str(arr[2]) + " "

print(answer)