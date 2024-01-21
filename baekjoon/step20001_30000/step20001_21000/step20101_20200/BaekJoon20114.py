import sys

N, H, W = map(int, sys.stdin.readline().split())

arr = []

for _ in range(H) :
    arr.append(sys.stdin.readline().strip())

answer = ['?' for _ in range(N)]

for i in range(N) :
    temp = ''
    check = False
    for j in range(H) :
        for k in range(i*W, (i+1)*W) :
            if arr[j][k] != '?' :
                answer[i] = arr[j][k]
                check = True
                break
        if check :
            break

print(''.join(answer))