A, B = input().split()

def validation(x, y) :
    max = 0
    for i in range(len(x)-len(y)+1) :
        cont = 0
        temp = x[i:i+len(y)]
        for i in range(len(temp)) :
            if temp[i] == y[i] :
                cont += 1
        max = cont if cont > max else max
    print(len(y)-max)

if len(A) >= len(B) :
    validation(A, B)
else :
    validation(B, A)