
为何直接将SET换成B就不行呢，set这个数据结构复杂度有多牛？
经过测试，确实很牛

import time
import random as rd

test = []
for i in range(1000000):
    test.append(rd.randint(1,30))



time_start=time.time()
for t in test:
    pass
time_end=time.time()
r = set(test)
for t in r:
    pass

time_end2 = time.time()
print('loop',time_end-time_start)
print('sett',time_end2-time_end)

loop 0.02008676528930664
sett 0.00899052619934082


——————————————————————————————————————————————————

class Solution(object):
    def fairCandySwap(self, A, B):
        """
        :type A: List[int]
        :type B: List[int]
        :rtype: List[int]
        """
        diff = int((sum(A) - sum(B))/2)
        SET = set(B)
        for i in A:
            if i - diff in SET:
                return [i,i-diff]