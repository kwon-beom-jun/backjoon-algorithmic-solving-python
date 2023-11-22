A, B = map(int, input().split())
min = abs(A-B)

for _ in range(int(input())) :
    temp = int(input())
    min = abs(temp-B) + 1 if min > abs(temp-B) else min

print(min)