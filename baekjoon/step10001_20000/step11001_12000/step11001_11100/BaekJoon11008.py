import sys

T = int(sys.stdin.readline().strip())
answer = []

for _ in range(T):
    s, p = map(str, sys.stdin.readline().split())
    answer.append(str(len(s.replace(p, '.'))))

print('\n'.join(answer))