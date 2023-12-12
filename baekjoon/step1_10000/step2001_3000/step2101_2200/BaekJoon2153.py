import sys, math

# ord("a") 97, ord("z") 112
# ord("A") 65, ord("Z") 90
# 95 이하면 -38 이상이면 -96

max = 1041
prime = [True for i in range(max + 1)]

for i in range(2, int(math.sqrt(max)) + 1) :
    if prime[i] == True :
        j = 2
        while i * j <= max :
            prime[i * j] = False
            j += 1

sum = 0
for i in sys.stdin.readline().strip() :
    sum += ord(i) - 38 if ord(i) < 95 else ord(i) - 96

print("It is a prime word." if prime[sum] else "It is not a prime word.")