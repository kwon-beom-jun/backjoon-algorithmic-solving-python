N = int(input())
cnt = 1
answer = 0

while N != 0 :
    if N < cnt :
        cnt = 1
    N -= cnt
    cnt += 1
    answer += 1
    
print(answer)