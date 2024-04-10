def solution(sizes):
    w, h = 0, 0
    for i in sizes:
        x, y = map(int, i)
        if y > x:
            w = max(w, y)
            h = max(h, x)
        else:
            w = max(w, x)
            h = max(h, y)
    return w * h