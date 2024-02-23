N = int(input())

answer = []

for i in range(N+2):
    answer.append('@')
answer.append('\n')

for i in range(N):
    answer.append('@'+(' '*N)+'@')
    answer.append('\n')

for i in range(N+2):
    answer.append('@')

print(''.join(answer))