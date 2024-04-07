# 8979
import sys

n, k = map(int, sys.stdin.readline().rstrip().split())
grade = [0] * (n + 1)   # 국가별 등수

gold = [-1 * (n + 1)]
silver = [-1 * (n + 1)]
bronze = [-1 * (n + 1)]
done = [[False] * (n + 1)]

for i in range(n):
    country, g, s, b = map(int, sys.stdin.readline().rstrip().split())
    gold[country] = g
    silver[country] = s
    bronze[country] = b

num = 1
while done.count(False) <= n-1:
    gold_max = max(gold)
    if gold_max != 0:
        gold_index = [i for i in range(gold) if gold[i] == gold_max]
        if len(gold_index) == 1:    # 금메달 수 혼자
            grade[gold_index] = num
            gold[gold_index] = 0
        else:   # 금메달 여러개
            # 실버 개수 비교
            silver_index = gold_index

# print(grade[k])