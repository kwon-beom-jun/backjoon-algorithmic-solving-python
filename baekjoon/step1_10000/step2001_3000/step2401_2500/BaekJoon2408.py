N = int(input())
number = []

for _ in range(2*N-1):
    n = input()
    number.append("//" if n == '/' else n)

print(eval(''.join(number)))