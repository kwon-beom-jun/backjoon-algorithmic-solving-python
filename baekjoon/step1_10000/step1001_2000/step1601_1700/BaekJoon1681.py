N, L = map(str, input().split(" "))
cnt = 0
answer = 0

while int(N) != cnt :
    answer += 1
    cnt += 0 if L in str(answer) else 1

print(answer)