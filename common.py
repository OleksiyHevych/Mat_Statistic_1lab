import random
import time

from const import V, sum_limit

current_time = time.time()
random.seed(current_time)


def generation_x():
    a = V - 10
    sigma = 3 + V / 10
    r = sum(random.uniform(0, 1) for _ in range(sum_limit))
    return (r - 6) * sigma + a


n = 250


def generation_x_on_n():
    data = [generation_x() for _ in range(n)]
    data.sort()
    return data
