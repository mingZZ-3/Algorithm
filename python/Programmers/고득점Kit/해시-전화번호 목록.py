# 다시시도 해보기
def solution(phone_book):
    phone_book.sort()

    for i in range(len(phone_book)-1):
        if phone_book[i+1].startswith(phone_book[i]):
            return False
    return True

def solution2(phone_book):
    phone_book.sort()

    for p1, p2 in zip(phone_book, phone_book[1:]):
        if p2.startswith(p1):
            return False
    return True

# hash 풀이
def solution3(phone_book):
    hash_map = {}
    for number in phone_book:
        hash_map[number] = 1
    for number in phone_book:
        tmp = ""
        for n in number:
            tmp += n
            if tmp in hash_map and tmp != number:
                # 긴 숫자 입장에서 자신의 일부 값이 데이터로 있는지 확인
                return False
    return True


print(solution2(	["119", "97674223", "1195524421"]))