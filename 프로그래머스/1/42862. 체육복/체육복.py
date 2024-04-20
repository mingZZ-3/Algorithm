def solution(n, lost, reserve):
    student = [True] * (n + 1)
    
    for i in lost:
        if i in reserve:
            reserve.remove(i)
        else:
            student[i] = False
    
    reserve.sort()
    for i in reserve:
        if i == 1:
            student[i+1] = True
        elif i == n:
            student[i-1] = True
        elif not student[i-1]:
            student[i-1] = True
        elif not student[i+1]:
            student[i+1] = True

    return (student.count(True)-1)