import sys

num = int(sys.stdin.readline().strip())
answer = []

answer.append(('@' * 3 * num + ' ' * num + '@' * num + '\n') * num)
answer.append(('@' * num + ' ' * num + '@' * num + ' ' * num + '@' * num + '\n') * 3 * num)
answer.append(('@' * num + ' ' * num + '@' * 3 * num + '\n') * num)

print(''.join(answer))