import sys

num = int(sys.stdin.readline().strip())
answer = []

answer.append(('@'*num + ' '*3*num + '@'*num + '\n') * num * 2)
answer.append(('@'*5*num + '\n') * num)
answer.append(('@'*num + ' '*3*num + '@'*num + '\n') * num)
answer.append(('@'*5*num + '\n') * num)


print(''.join(answer))