import sys

W, H = map(int, sys.stdin.readline().split())

print("{:.1f}".format(W * H / 2))