# ===== #1
import string


def solution1(id_list, report, k):
    answer = []
    a = list(set(report))
    dictionary2 = {name : 0 for name in id_list}
    dictionary = {name : [] for name in id_list}
    for i in a:
        dictionary[i.split()[1]].append(i.split()[0])

    for i in dictionary:
        if len(dictionary[i]) >= k:
            for j in dictionary[i]:
                dictionary2[j] += 1

    for i in dictionary2:
        answer.append(dictionary2[i])

    return answer

# ===== #2
# def solution(id_list, report, k):
#     answer = []
#     a = list(set(report))
#     dictionary2 = {name : 0 for name in id_list}
#     dictionary = {name : [] for name in id_list}
#     for i in a:
#         dictionary[i.split()[1]].append(i.split()[0])
#
#     for i in dictionary:
#         if len(dictionary[i]) >= k:
#             for j in dictionary[i]:
#                 dictionary2[j] += 1
#
#     for i in dictionary2:
#         answer.append(dictionary2[i])
#
#     return answer


#
    # set() - 중복 제거
def solution2(id_list, report, k):
    answer = []
    a = list(set(report))
    dic1 = {name : 0 for name in id_list}
    dic2 = {name : [] for name in id_list}

    for i in a:
        dic2[i.split()[1]].append(i.split()[0])

    for i in dic2:
        if len(dic2[i]) >= k:
            for j in dic2[i]:
                dic1[j] += 1

    for i in dic1:
        answer.append(dic1[i])

    return answer


#ㅇㅏ이디 추천
new_id = "...!@BaT#*..y.abcdefghijklm"

new_id.lower()
new_id.replace("~!@#$%^&*()=+[{]}:?,<>/", "")
new_id.replace("..", ".")
new_id.strip(".")

if len(new_id) == 0 :
    new_id += 'a'
elif len(new_id) >= 16:
    new_id = new_id[:14]
    new_id.strip(".")

if len(new_id) <= 2 :
    a = new_id[-1]
    while len(new_id) == 3 :
        new_id += a



#체육복
n = 3
lost = [2,4]
reserve = [2,2,3]

def solution(n, lost, reserve):
    answer = 0
    lost_set = set(lost) - set(reserve)
    reserve_set = set(reserve) - set(reserve)

    if len(reserve_set) != 0:
        for i in reserve_set:
            if i-1 in lost_set:
                lost_set.remove(i-1)
            elif i+1 in lost_set:
                lost_set.remove(i+1)

    answer = n - len(lost_set)
    return answer

arr1 = [9, 20, 28, 18, 11]
arr2 = [30, 1, 21, 17, 28]
n = 5


def solution(n, arr1, arr2):
    answer = []
    for i in range(n):
        tmp = bin(arr1[i] | arr2[i])

        tmp = tmp[2:].zfill(n)
        tmp = tmp.replace('1', '#')
        tmp = tmp.replace('0', ' ')
        answer.append(tmp)

    return answer

import sys

#N, K = map(int, sys.stdin.readlin().split())
#
# N = 25
# K = 4
# cnt = 0
#
# for i in range(1, N+1):
#     if N % i == 0:
#         cnt += 1
#         if K == cnt:
#             print(i)
#             break
#         else:
#             continue
#     else:
#         continue
#
# if cnt < K:
#     print(0)

from itertools import combinations
import sys

# N = 200
# dataset = list(range(1, N))
#
# for i in range(1, N):
#     list_set = list(combinations(dataset, i))
#     print(list_set)
#     if len(list_set) == 0:
#         print(i-1)

# N = int(input())
# word1 = list(input())
# word1_num = len(word1)
#
# for i in range(N - 1):
#     other_words = list(input())
#     for j in range(word1_num):
#         if word1[j] != other_words[j]:
#             word1[j] = '?'
#
# print(''.join(word1))

# 백준
# N = int(sys.stdin.readline())
# list_n = list(map(int, sys.stdin.readline().split()))
# list_n.sort()
# print(list_n[0]*list_n[-1])

#백준 1094
# X = int(sys.stdin.readline())
# cnt = 0
# while X != 0:
#     if X % 2 == 1:
#         cnt += 1
#     X = X // 2
# print(cnt)

#백준 1181
#import sys, string
#N = int(sys.stdin.readline())
#word_list = list(map(string, sys.stdin.readline().split()))
# word_list = ['but', 'i', 'wont', 'hesitate', 'no','more','no','more','it','cannot','wait','im','yours']
# word_set = set(word_list)
# word_list = list(word_set)
# word_list.sort()
# word_list.sort(key=len)
#
# for i in word_list:
#     print(i)


# 백준 1620
# N, M = map(int, input().split())
# mon_dic = {}
#
# for i in range(1, N+1) :
#     mon = input().rstrip()
#     mon_dic[i] = mon
#     mon_dic[mon] = i
#
# for _ in range(M) :
#     Q = input().rstrip()
#     if Q.isdigit():
#         print(mon_dic[int(Q)])
#     else :
#         print(mon_dic[Q])


#2257
chemical = input()
atom_mass = {'H':1, 'C':12, 'O': 16}
stack = []

for atom in chemical:
    if atom == 'H' or atom == 'C' or atom == 'O':
        stack.append(atom_mass[atom])
    elif atom == '(':
        atom.append(atom)
    elif atom == ')':
        cnt = 0
        while True:
            if stack[-1] == '(':
                stack.pop()
                stack.append(cnt)
                break
            else:
                cnt += stack.pop()
    else:
        stack.append(stack.pop()*int(atom))
# print(sum(stack))




