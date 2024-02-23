T = int(input())
answer = []

for _ in range(T) :
  N = int(input())
  school, alcohol = map(str, input().split())
  
  for _ in range(N - 1) :
    a, b = input().split()
    
    if int(alcohol) < int(b) :
      school = a
      alcohol = b
  
  answer.append(school)

print('\n'.join(answer))