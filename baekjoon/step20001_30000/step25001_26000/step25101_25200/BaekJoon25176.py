import sys

answer = 1

for i in range(1, int(sys.stdin.readline().strip())+1) :
  answer *= i

print(answer)