arr = []

while True:
    temp = str(input()).lower()
    if temp == "#" :
        break
    arr.append(str(
            temp.count("a")+
            temp.count("e")+
            temp.count("i")+
            temp.count("o")+
            temp.count("u"))+"\n")

print("".join(arr))