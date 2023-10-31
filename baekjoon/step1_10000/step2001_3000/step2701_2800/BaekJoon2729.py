num = int(input())

for _ in range(num):
    arr = input().split(" ")
    print(bin(int(arr[0],2) + int(arr[1],2))[2:])