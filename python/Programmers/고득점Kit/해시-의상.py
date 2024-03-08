def solution(clothes):
    hash_map = {}
    for item in clothes:
        if not item[1] in hash_map:
            hash_map[item[1]] = 1
        else:
            hash_map[item[1]] += 1

    result = 1
    for i in hash_map.values():
        result *= (i+1)
    return result - 1

print(solution([["crow_mask", "face"], ["blue_sunglasses", "face"], ["smoky_makeup", "face"]]))