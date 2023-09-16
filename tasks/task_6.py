from math import sqrt
from common import n, generation_x_on_n

data = generation_x_on_n()
Xv = sum(data) / n
s2 = sum([(data[i] - Xv) ** 2 for i in range(n)]) / n - 1
s = sqrt(s2)
print(f"Xv = {Xv}")
print(f"s = {s}")
