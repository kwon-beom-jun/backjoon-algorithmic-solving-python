import sys

N, L = map(int, sys.stdin.readline().split())
arr = sorted(list(map(int, sys.stdin.readline().split())))

for i in arr :
    if i > L :
        break
    elif i <= L :
        L += 1

print(L)