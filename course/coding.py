# student = list(list())
# n = int(input())
# for _ in range(n):
#     name = input()
#     score = float(input())
#     student.append((name,score))
# student.sort(key=lambda x:x[1])
# # print(student)
# low = student[0][1]
# # print(low)
# i = 0
# while student[i][1] == low:
#     i = i + 1
# second_low = student[i][1]
# # print(second_low)
# second_low_students = list()
# while student[i][1] == second_low:
#     second_low_students.append(student[i][0])
#     if i+1 <= n-1:
#         i = i + 1
#     else:
#         break
# second_low_students.sort()
# # print(second_low_students)
# for i in second_low_students:
#     print(i)
#
#
# n = int(input())
# score = list(map(int,input().split()))
# score.sort()
# i = n - 1
# high = score[n-1]
# while score[i] == high:
#     i = i - 1
# runner_up = score[i]
# print(runner_up)
#
# Dictionary of lists
# def minion_game(string):
#     score = dict()
#     vowel = dict()
#     consonants = dict()
#     score["Stuart"] = score["Kevin"] = 0
#     n = len(string)
#     for i in range(n):
#         if string[i] in ['A','E','I','O','U']:
#             score["Kevin"] = score["Kevin"] + 1
#             vowel.setdefault(string[i],[]).append(i)
#         else:
#             score["Stuart"] = score["Stuart"] + 1
#             consonants.setdefault(string[i],[]).append(i)
#     print(vowel)
#     print(consonants)
#
# if __name__ == '__main__':
#     s = input()
#     minion_game(s)
