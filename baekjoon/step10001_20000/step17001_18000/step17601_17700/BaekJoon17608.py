import sys

num = int(sys.stdin.readline().rstrip())
N = sys.stdin.readlines()
max = 0
cnt = 0

for item in reversed(N):
    if max < int(item):
        max = int(item)
        cnt += 1

print(cnt)