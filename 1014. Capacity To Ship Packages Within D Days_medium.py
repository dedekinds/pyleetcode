class Solution(object):
    def check(self,weights,limit):
        nums = 0
        ans = []
        tempsum =0
        length = len(weights)
        i = 0
        while i<length:
            tempsum += weights[i]
            if tempsum > limit:
                ans.append(tempsum - weights[i])
                tempsum = 0
                continue
            i += 1
        if tempsum:
            ans.append(tempsum)
        return ans
    
    def shipWithinDays(self, weights, D):
        """
        :type weights: List[int]
        :type D: int
        :rtype: int
        """
        #https://www.cnblogs.com/wolf-yasen/p/6557729.html
        left = max(weights)
        right = sum(weights)
        res = 0xfffffff
        while left <= right:
            #print(left,right)
            mid = (left + right)>>1
            temp = self.check(weights,mid)
            if len(temp) <=D:
                right = mid -1
                res = min(res,max(temp))
            else:
                left = mid +1
        return res
        
        