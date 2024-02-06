import sys

T = int(sys.stdin.readline())
answer = []

for _ in range(T):
    sum = int(sys.stdin.readline())
    n = int(sys.stdin.readline())
    for _ in range(n):
        q, p = map(int, sys.stdin.readline().split())
        sum += q*p
    answer.append(str(sum))

print('\n'.join(answer))