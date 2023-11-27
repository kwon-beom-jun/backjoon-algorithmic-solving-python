while True :
    cnt = 0
    N = int(input())

    if N == 0 :
        break

    for i in range(N+1) :
        cnt += i * i

    print(cnt)