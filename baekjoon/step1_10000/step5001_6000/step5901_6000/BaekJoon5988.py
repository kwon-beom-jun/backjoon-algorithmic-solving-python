import sys

N = int(sys.stdin.readline().rstrip())

print("\n".join(["even" if int(i) % 2 == 0 else "odd" for i in sys.stdin.readlines()]))