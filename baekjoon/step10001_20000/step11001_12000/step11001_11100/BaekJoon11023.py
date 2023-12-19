import sys

answer = 0
arr = map(int, sys.stdin.readline().split())

for i in arr :
    answer += i

print(str(answer))