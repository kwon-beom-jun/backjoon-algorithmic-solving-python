import sys

T = int(sys.stdin.readline().strip())
answer = []

for _ in range(T):
    number = int(sys.stdin.readline().strip())
    cnt = 0
    
    if number < 10:
        answer.append(str(number))
    else:
        while number > 10:
            digit = number % 10
            number //= 10

            if digit >= 5:
                number += 1
            
            cnt += 1
        
        answer.append(str(number * (10 ** cnt)))

print('\n'.join(answer))