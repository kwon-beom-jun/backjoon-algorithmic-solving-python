num = int(input())
N = S = max = N_temp = S_temp = max_temp = 0
check = 'F'

for i in input() :
    if i == 'N' :
        if check != 'N' :
            max = max if max > max_temp else max_temp
            N, max_temp, check, S_temp = 0, 0, 'N', S
        if S_temp > 0 :
            S_temp -= 1
            max_temp += 2
        N += 1
    else :
        if check != 'S' :
            max = max if max > max_temp else max_temp
            S, max_temp, check, N_temp = 0, 0, 'S', N
        if N_temp > 0 :
            N_temp -= 1
            max_temp += 2
        S += 1

print(max if max > max_temp else max_temp)