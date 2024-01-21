import sys

num = int(sys.stdin.readline())
arr = [sys.stdin.readline().strip().split() for _ in range(num)]

arr.sort(key=lambda x: (-int(x[1]), int(x[2]), -int(x[3]), x[0]))

answer = "\n".join(i[0] for i in arr)
print(answer)
