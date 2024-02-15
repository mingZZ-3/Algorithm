# 2753 - 윤년
# 윤년이란 연도가 4의 배수이면서, 100의 배수가 아닐때  or  400의 배수일때이다.
year = int(input())
if year % 400 == 0:
    print('1')
elif year % 4 == 0 and year % 100 != 0:
    print('1')
else:
    print('0')