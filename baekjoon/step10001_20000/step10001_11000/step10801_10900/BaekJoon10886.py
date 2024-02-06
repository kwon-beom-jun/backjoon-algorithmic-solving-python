import sys

N = int(sys.stdin.readline())

zero = 0
one = 0
for _ in range(N):
    if sys.stdin.readline().strip() == "1":
        one += 1
    else:
        zero += 1

print("Junhee is cute!" if one > zero else "Junhee is not cute!")