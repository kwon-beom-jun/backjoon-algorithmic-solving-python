
num = int(input())
N = list(map(int, input().split()))
view = list(map(int, input().split()))

answer1 = 0
answer2 = 0
for i in range(num):
    answer1 += N[i]
    if view[i] == 0:
        answer2 += N[i]

print(str(answer1) + "\n" + str(answer2))