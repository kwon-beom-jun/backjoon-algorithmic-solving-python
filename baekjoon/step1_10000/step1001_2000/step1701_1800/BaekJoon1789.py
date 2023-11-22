S = int(input())
N = 0
max = 0

for i in range(1, S+1) :
    max += i
    N += 1
    if max > S :
        N -= 1
        break

print(N)