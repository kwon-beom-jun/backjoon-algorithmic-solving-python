N, S = map(str, input().split())
arr = []

for i in range(int(N)):
    name, chat = map(str, input().split())
    if name == S:
        answer = chat
        break
    else:
        arr.append(chat)

cnt = 0
for i in arr:
    cnt += 1 if i == answer else 0

print(cnt)