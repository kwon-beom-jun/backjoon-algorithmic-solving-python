arr = list(input())

Hex = {
    "0" : 0, "1" : 1, "2" : 2, "3" : 3, "4" : 4,
    "5" : 5, "6" : 6, "7" : 7, "8" : 8, "9" : 9, 
    "A" : 10, "B" : 11, "C" : 12, "D" : 13, "E" : 14, "F" : 15
}

cnt = 0
answer = 0

for i in reversed(arr) :
    answer += Hex.get(i) * pow(16, cnt)
    cnt += 1

print(answer)