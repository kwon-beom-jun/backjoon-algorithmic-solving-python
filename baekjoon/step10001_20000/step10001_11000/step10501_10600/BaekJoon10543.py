import sys

A = sys.stdin.readline().strip()
B = sys.stdin.readline().strip()

count = 0
i = 0

while i <= len(A) - len(B) :
    for j in range(len(B)) :
        if A[i+j] != B[j] :
            break
        if j == len(B) - 1 :
            count += 1
            i += len(B) - 1
    i += 1

print(count)