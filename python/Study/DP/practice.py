##################################
############### 1 - 개미 전사
n = int(input())
food = list(map(int, input().split()))

d = [0] * 100 # dp 테이블 최기화

# 바텀업 - DP
d[0] = food[0]
d[1] = max(food[0], food[1])
for i in range(2, n):
    d[i] = max(d[i-1], d[i-2] + food[i])

print(d[n-1])

##################################
############### 2 - 1로 만들기
x = int(input())
d = [0]*30001

# 바텀업
for i in range(2, x+1):
    # 현재 수에서 1을 빼는 경우
    d[i] = d[i-1] + 1
    if i % 2 == 0:
        d[i] = min(d[i], d[i//2] + 1)
    if i % 3 == 0:
        d[i] = min(d[i], d[i//3] + 1)
    if i % 5 == 0:
        d[i] = min(d[i], d[i//5] + 1)
print(d[x])

##################################
############### 3 - 효율적인 화폐 구성
n, m = map(int, input().split())
units = []
for i in range(n):
    units.append(int(input()))
d = [10001] * (m + 1)

d[0] = 0
for i in range(n):
    for j in range(units[i], m + 1):
        if d[j - units[i]] != 10001:
            d[j] = min(d[j], d[j - units[i]] + 1)

if d[m] == 10001:
    print(-1)
else:
    print(d[m])

##################################
############### 4 - 금광
for tc in range(int(input())):
    n, m = map(int, input().split())
    array = list(map(int, input().split()))

    dp = []
    index = 0
    for i in range(n):
        dp.append(array[index:index+m])
        index += m

    for j in range(1, m):
        for i in range(n):
            # 왼쪽 위
            if i == 0:
                left_up = 0
            else:
                left_up = dp[i-1][j-1]
            # 왼쪽
            left = dp[i][j-1]
            # 왼쪽 아래
            if i == n - 1:
                left_bottom = 0
            else:
                left_bottom = dp[i+1][j-1]
            dp[i][j] = dp[i][j] + max(left_up, left, left_bottom)
    result = 0
    for i in range(n):
        result = max(result, dp[i][m-1])
    print(result)

##################################
############### 5 - 병사 배치하기
# 가장 긴 증가하는 부분 수열을 가장 긴 감소하는 수열로 활용해서 푸는 문제
# LIS 점화식
n = int(input())
array = list(map(int, input().split()))
# 순서를 뒤집어 '최장 증가 부분 수열' 문제로 변환
array.reverse()

# dp를 위한 1차원 dp 테이블 초기화
dp = [1] * n

# 가장 긴 증가하는 부분 수열(LIS) 알고리즘 수행
for i in range(0, n):
    for j in range(0, i):
        if array[j] < array[i]:
            dp[i] = max(dp[i], dp[j] + 1)
# 열외해야 하는 병사의 최소 수를 출력
print(n - max(dp))