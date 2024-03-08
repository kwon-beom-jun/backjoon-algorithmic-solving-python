import sys

num = int(sys.stdin.readline().strip())
answer = []

answer.append(('@' * num + '\n') * 4 * num)
answer.append(('@' * 5 * num + '\n') * num)

print(''.join(answer))