import sys

num = int(sys.stdin.readline())
lines = [int(sys.stdin.readline().strip()) for _ in range(num)]
print("\n".join(map(str, sorted(lines, reverse=True))))