import sys

A = sorted([int(sys.stdin.readline().strip()) for _ in range(10)], reverse=True)[:3]
B = sorted([int(sys.stdin.readline().strip()) for _ in range(10)], reverse=True)[:3]

sum_A = sum_B = 0

for i in range(3) :
    sum_A += int(A[i])
    sum_B += int(B[i])


print(str(sum_A) + " " + str(sum_B))