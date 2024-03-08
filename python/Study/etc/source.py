##############################
### 소수 판별
import math

def is_prime_number(x):
    # 2부터 x의 제곱근까지의 모든 수 확인
    for i in range(2, int(math.sqrt(x)) + 1):
        # x가 해당 수로 나누어 떨어진다면
        if x % i == 0:
            return False
    return True


##############################
### 에라토스테네스의 체 알고리즘
## 2 - N 범위 내의 소수 찾기

n = 1000 # 2부터 1000까지의 소수 판별
# 처음에는 모든 수가 소수(TRUE)인 것으로 초기화 _ 0, 1 제외
array = [True for _ in range(n + 1)]

# 2부터 n의 제곱근까지의 모든 수를 확인하며
for i in range(2, math.sqrt(n) + 1):
    if array[i] == True: # i가 소수인 경우(남은 수인 경우)
        # i를 제외한 모든 배수 지우기
        j = 2
        while i * j <= n:
            array[i * j] = False
            j += 1

# 모든 소수 출력
for i in range(2, n + 1):
    if array[i]:
        print(i, end=" ")


##############################
### 투 포인터 - 특정한 합을 가지는 부분 연속 수열 찾기

n = 5 # 데이터의 개수 N
m = 5 # 부분합 M
data = [1, 2, 3, 2, 5]

cnt = 0
interval_sum = 0
end = 0

# start를 차례대로 증가시키며 반복
for start in range(n):
    # end를 가능한 만큼 이동시키기
    while interval_sum < m and end < n:
        interval_sum += data[end]
        end += 1
    # 부분합이 m일 때 카운트 증가
    if interval_sum == m:
        cnt += 1
    interval_sum -= data[start]


##############################
### 구간 합
n = 5 # 데이터의 개수 N
data = [10, 20, 30, 40, 50]

# 접두사 합(Prefix Sum) 배열 계산
sum_value = 0
prefix_sum = [0]
for i in data:
    sum_value += i
    prefix_sum.append(sum_value)

# 구간 합 계산
left = 3
right = 4
print(prefix_sum[right] - prefix_sum[left - 1])