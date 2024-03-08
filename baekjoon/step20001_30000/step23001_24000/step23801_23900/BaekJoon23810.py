import sys

num = int(sys.stdin.readline().strip())
answer = []

answer.append(('@' * num * 5 + '\n') * num)
answer.append(('@' * num + '\n') * num)
answer.append(('@' * num * 5 + '\n') * num)
answer.append(('@' * num + '\n') * num * 2)

print(''.join(answer))