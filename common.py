import random
import time
import math

from const import V, sum_limit

current_time = time.time()
random.seed(current_time)

n = 350


def generation_x():
    a = V - 10
    sigma = 3 + V / 10
    r = sum(random.uniform(0, 1) for _ in range(sum_limit))
    return (r - 6) * sigma + a


def generation_x_on_n():
    data = [generation_x() for _ in range(n)]
    data.sort()
    return data


def make_intervals_from_n(minimum, maximum, rounder):
    count_intervals = int(1 + 1.44 * math.log(n)) + 1
    step = (maximum - minimum) / count_intervals
    intervals = [round(minimum + step * i, rounder) for i in range(count_intervals + 1)]
    return intervals


def make_interval_labels(intervals: list):
    labels = [f"[{intervals[i]};{intervals[i + 1]}]" for i in range(len(intervals) - 1)]
    return labels
