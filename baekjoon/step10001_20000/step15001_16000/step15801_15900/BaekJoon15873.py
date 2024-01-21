
num = input()

if len(num) == 4 : 
    print(20)
elif len(num) == 3 : 
    print(int(num.replace("10","")) + 10)
else :
    print((int(num[0])+int(num[1])))
