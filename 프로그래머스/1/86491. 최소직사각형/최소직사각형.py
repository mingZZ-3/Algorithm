def solution(sizes):
    w, h = 0, 0
    for x, y in sizes:
        if y > x:
            x, y = y, x
        w = max(w, x)
        h = max(h, y)
    return w * h