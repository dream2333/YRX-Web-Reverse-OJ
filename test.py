

import numpy as np
import matplotlib.pyplot as plt
import random


# 生成一百万个随机数
nums = np.random.randint(1, 10000000, 1000000)
nums = [random.randint(1,1000000) for i in range(10000000)]

plt.hist(nums, bins=100)
plt.show()