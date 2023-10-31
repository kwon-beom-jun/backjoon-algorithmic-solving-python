M = int(input())
N = int(input())
sum = 0
min = 0
count = 1

while(True) :
    square = count * count
    if square > N :
        break
    if M <= square & square <= N :
        if min == 0 :
            min = square
        sum += square
    count += 1

print(-1 if min == 0 else str(sum) + "\n" + str(min))