import sys

T = int(sys.stdin.readline())
arr = []

for _ in range(T):
    a, b, c = map(int, sys.stdin.readline().split())
    arr.append(str(min(a, min(b, c))))

print('\n'.join(arr))