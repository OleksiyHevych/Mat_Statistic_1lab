import matplotlib.pyplot as plt
import numpy as np

from common import generation_x_on_n, make_intervals_from_n
from const import max_value, min_value


data = generation_x_on_n()

bins = make_intervals_from_n( maximum=max_value, minimum=min_value, rounder=1)

hist, _ = np.histogram(data, bins=bins)
relative_frequencies = hist / np.sum(hist)

plt.bar(range(len(relative_frequencies)), relative_frequencies,
        tick_label=[f"{i}-{j}" for i, j in zip(bins[:-1], bins[1:])])

plt.xlabel('Інтервали')
plt.ylabel('Відносна частота')
plt.xticks(rotation=30)

plt.show()
