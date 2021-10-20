# str = 'AABCA'
# save_word = []
# result = True
#
# for char in str:
#     print(char)
#
# for i in int(len(char)):
#     if char not in save_word:
#         if char[i] == char[i + 1]:
#             continue
#         else:
#             result = False
#     else:
#         save_word.append(char)
#
#
# print(save_word)
# print(result)

# https://www.acmicpc.net/problem/1316

# def isGroupString(str):
#     save_word = []
#     result = True
#     before_word = ''
#
#     for ch in str:
#         if not ch.isalpha():
#             continue
#
#         # 1. save_word 에 문자가 이미 등록되어있는지 검색
#         isExist = False
#         for word in save_word:
#             if ch == word:
#                 isExist = True
#                 break
#
#         # 2. save_word 에 이미 입력된 단어인지 조사
#         if not isExist:
#             # 전에 입력된 단어아닐때
#             save_word.append(ch)
#         else:
#             # 전에 이미 등록된 단어임
#             # 그런데 전과 입력된 단어일 경우는 무시
#             if before_word == ch:
#                 # result =True
#                 continue
#             else:
#                 # 전에 입력한 단어인데, 동시에 전과 입력된 단어와 다를 때
#                 result = False
#                 break
#         before_word = ch
#
#     # print("str: " + str)
#     # print("save_word: ", save_word)
#     #print("result: " , result)
#     return result
#
# number = int(input())
# # print("number : " , number)
#
# input_word = []
# count = 0
# for words in range(number):
#     input_str = str(input())
#     # print("input_str: " + input_str)
#     if isGroupString(input_str):
#         count += 1
# print(count)

n = int(input())

group_word = 0
for _ in range(n):
    word = input()
    error = 0
    for index in range(len(word)-1):  # 인덱스 범위 생성 : 0부터 단어개수 -1까지
        if word[index] != word[index+1]:  # 연달은 두 문자가 다른 때,
            new_word = word[index+1:]  # index+1 글자(현재글자) 이후 문자열을 새로운 단어로 생성
            if new_word.count(word[index]) > 0:  # 남은 문자열에서 현재글자가 있있다면
                error += 1  # error에 1씩 증가.
    if error == 0:
        group_word += 1  # error가 0이면 그룹단어
print(group_word)