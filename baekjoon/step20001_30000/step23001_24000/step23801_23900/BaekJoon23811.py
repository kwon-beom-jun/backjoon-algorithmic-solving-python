N = int(input())

answer = []

for i in range(N):
    answer.append('@'*(5*N))

for i in range(N):
    answer.append('@'*N)

for i in range(N):
    answer.append('@'*(5*N))

for i in range(N):
    answer.append('@'*N)

for i in range(N):
    answer.append('@'*(5*N))

print('\n'.join(answer))