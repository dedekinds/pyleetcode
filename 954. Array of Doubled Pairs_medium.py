标准解答
import collections
class Solution(object):     
    def canReorderDoubled(self, A):
        count = collections.Counter(A)
        for x in sorted(A, key = abs):
            if count[x] == 0: continue
            if count[2*x] == 0: return False
            count[x] -= 1
            count[2*x] -= 1

        return True




_________________________________________________
暴力做法

class Solution(object):
    def check(self,nums):
        if len(nums)%2 == 1:return False
        if len(nums)==0:return True
        length = len(nums)
        if nums[0]>0:
            while nums:
                u = nums.pop(0)
                if not u*2 in nums:
                    return False
                else:
                    v = nums.index(u*2)
                    nums.pop(v)
            return True
        if nums[0]<0:
            while nums:
                u = nums.pop()
                if not u*2 in nums:
                    return False
                else:
                    v = nums.index(u*2)
                    nums.pop(v)
            return True
        else:
            return len(nums)%2 == 0
        
    def canReorderDoubled(self, A):
        """
        :type A: List[int]
        :rtype: bool
        """
        temp = sorted(A)
        neg = []
        zeros = []
        pos = []
        for tmp in temp:
            if tmp < 0:neg.append(tmp)
            if tmp > 0:pos.append(tmp)
            if tmp == 0:zeros.append(tmp)
        #print(neg)
        #print(zeros)
        #print(pos)
        return self.check(neg) and self.check(zeros) and self.check(pos)