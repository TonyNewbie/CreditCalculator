from math import log


first_number = int(input())
second_number = int(input())
if second_number <= 0 or second_number == 1:
    print(round(log(first_number), 2))
else:
    print(round(log(first_number, second_number), 2))
