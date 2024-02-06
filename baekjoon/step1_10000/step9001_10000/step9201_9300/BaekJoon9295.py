import sys

T = int(sys.stdin.readline())
answer = []

for i in range(1, T+1):
    a, b = map(int, sys.stdin.readline().split())
    answer.append('Case ' + str(i) + ': ' + str(a+b))

print('\n'.join(answer))