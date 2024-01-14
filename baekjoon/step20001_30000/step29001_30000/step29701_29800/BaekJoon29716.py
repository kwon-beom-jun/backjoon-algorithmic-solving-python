import sys

arr = sys.stdin.readline().split()
answer = 0

for i in range(int(arr[1])):
    temp = sys.stdin.readline().strip()
    cnt = 0
    for j in temp:
        if ' ' == j:
            cnt += 1
        elif 'A' <= j <= 'Z':
            cnt += 4
        else:
            cnt += 2
    if cnt <= int(arr[0]):
        answer += 1

print(answer)