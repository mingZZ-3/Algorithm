# 아스키값 비교로 풀이
def solution(numbers):
    nums = list(map(str, numbers))
    nums.sort(key=lambda x : x*3, reverse=True)
    return str(int(''.join(nums)))

print(solution([3, 30, 34, 5, 9]))

# 아스키값(문자)으로 비교하는 경우,
# 맨 앞자리의 문자를 기준으로 정렬
# ex) '3' > '20'
# 문제에서 숫자는 1000이하 였기 때문에 x*3을 해준 것
# --> 비교해야할 문자가 최대 3자리이기때문 (1000은 어차피 1-0이니 고려x)

# comparator 비교로 풀이
import functools
def comparator(a, b):
    t1 = a + b
    t2 = b + a
    return (int(t1) > int(t2)) - (int(t1) < int(t2))
    # t1이 크다면 1 // t2가 크다면 -1 // 같다면 0

def solution(numbers):
    n = list(map(str, numbers))
    n = sorted(n, key=functools.cmp_to_key(comparator), reverse=True)
    return str(int(''.join(n)))

print(solution([3, 30, 34, 5, 9]))