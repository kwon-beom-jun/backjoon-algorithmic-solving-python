import sys

N, I = map(int, sys.stdin.readline().split())
N_arr = []

for i in range(N) :
    N_arr.append(sys.stdin.readline().rstrip())

N_arr.sort()

print(N_arr[I-1])