def solution(arr):
    arr.reverse()
    result = [arr.pop()]

    while arr:
        now = result.pop()
        data = arr.pop()

        if now != data:
            result.append(now)
            result.append(data)
        else:
            result.append(now)

    return result


print(solution([1,1,3,3,0,1,1]))