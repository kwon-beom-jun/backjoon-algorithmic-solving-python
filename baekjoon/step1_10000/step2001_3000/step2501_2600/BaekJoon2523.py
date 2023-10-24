num = int(input())
str_list = []

for i in range(num) :
    for _ in range(i+1) :
        str_list.append("*")
    str_list.append("\n")
    
for i in range(num) :
    for _ in range(num-i-1) :
        str_list.append("*")
    str_list.append("\n")

print(''.join(str_list))