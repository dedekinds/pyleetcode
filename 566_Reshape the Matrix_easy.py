'''566.Reshape the Matrix   
   2017.5.15
   438ms
   beats 0.76%=。=
'''
class Solution(object):
    def matrixReshape(self, nums, r, c):
        temp=[-1]
        last=[[-1]]
        for x in nums:
            for y in x:
                temp.append(y)
                temp2=temp[1:]
                #temp=[num for row in nums for num in row]#展开成一维数组
        #print(temp)
        if (r*c)==len(temp2):
            L=[c*x for x in range(int(len(temp2)/c))]
            for t in L:
                last.append(temp2[t:(t+c)])
            return(last[1:])
        else:
            return(nums)
'''
The best code
95ms
'''
import numpy as np

class Solution(object):
    def matrixReshape(self, nums, r, c):
        return map(list, np.array(nums, dtype=object).reshape(r, c)) if r >= 0 <= c and r * c == sum(map(len, nums)) else nums

'''
Other code

'''
import numpy as np

class Solution(object):
    def matrixReshape(self, nums, r, c):
        try:
            return np.reshape(nums, (r, c)).tolist()
        except:
            return nums

'''
Other code

'''
def matrixReshape(self, A, nR, nC):
    if len(A) * len(A[0]) != nR * nC:
        return A
        
    vals = (val for row in A for val in row)
    return [[vals.next() for c in xrange(nC)] for r in xrange(nR)]