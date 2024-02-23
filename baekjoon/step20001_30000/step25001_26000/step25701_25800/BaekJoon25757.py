import sys

N, K = sys.stdin.readline().split()
name = set()

for _ in range(int(N)):
    name.add(sys.stdin.readline().rstrip())

size = len(name)

print(size if K == 'Y' else size//2 if K == 'F' else size//3)