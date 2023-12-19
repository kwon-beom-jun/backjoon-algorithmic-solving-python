import sys

T = int(sys.stdin.readline().strip())
answer = []

for _ in range(T):
    A, B = map(int, sys.stdin.readline().split(","))
    answer.append(str(A+B))

print('\n'.join(answer))