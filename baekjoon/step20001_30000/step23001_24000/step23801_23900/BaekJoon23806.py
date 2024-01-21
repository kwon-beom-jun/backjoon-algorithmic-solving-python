import sys

num = int(sys.stdin.readline().strip())
answer = []

answer.append(('@'*num*5+'\n')*num)
answer.append((('@'*num)+(' '*num*3)+('@'*num)+'\n')*num*3)
answer.append(('@'*num*5+'\n')*num)

print(''.join(answer))