answer = [];

while True :
    try :
        n, k = map(int, input().split())
        temp = n
        while n // k :
            temp += n // k
            n = n // k + n % k
        answer.append(str(temp))
    except :
        break

print('\n'.join(answer))