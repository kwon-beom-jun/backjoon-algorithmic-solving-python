# import sys
# a, b = map(int, sys.stdin.readline().split())
# data = [sys.stdin.readline().strip() for i in range(a)]
# arr = [[] for _ in range(10)] 

# # 이중배열로 생성
# # 첫번째 배열은 중복 수, 두번째 단어
# # 첫번째 오름차순 정렬, 두번째 길이로 정렬

# for i in data :
#     print(i)
#     arr[len(i)-1].append({i : 0})
#     print(arr[len(i)-1][i])
#     print("======================")
# # 0. 단어 길이 확인
# # 1. 자주나오는 단어
# # 2. 단어 길이순
# # 3. 사전순

# print(arr)

import sys

a, b = map(int, sys.stdin.readline().split())
data = [sys.stdin.readline().strip() for _ in range(a)]
word_count = {}  # 단어의 빈도를 저장할 딕셔너리
arr = [[] for _ in range(10)]  # 최대 단어 길이가 10이라고 가정

# 단어의 빈도 계산 및 길이별 그룹화
for word in data:
    word_count[word] = word_count.get(word, 0) + 1
    arr[len(word)-1].append(word)

# 각 그룹 내에서 정렬
for i in range(10):
    arr[i].sort(key=lambda x: (-word_count[x], len(x), x))

print("===================")

# 결과 출력
for group in arr:
    for word in group:
        print(word)
