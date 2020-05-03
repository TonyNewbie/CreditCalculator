from math import exp
number = int(input())
print(round(1 / (1 + exp(-number)), 2))
