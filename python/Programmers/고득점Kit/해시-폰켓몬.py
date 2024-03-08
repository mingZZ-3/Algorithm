def solution(nums):
    poke = {}
    for item in nums:
        if not item in poke:
            poke[item] = 1
        else:
            poke[item] += 1
    if len(poke.keys()) >= len(nums)/2:
        return int(len(nums)/2)
    else:
        return int(len(poke.keys()))

def solution2(nums):
    return min(len(nums)/2, len(set(nums)))
print(solution([3, 1, 2, 3]))