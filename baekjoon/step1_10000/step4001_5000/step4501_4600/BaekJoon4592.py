result = ""

while True :
    arr = input().split(" ")
    if(int(arr[0]) == 0) :
        break
    arr = arr[1:]
    next = ""
    for i in arr :
        if(next != i) :
            next = i
            result += i + " "
    result += "$\n"

print(result)