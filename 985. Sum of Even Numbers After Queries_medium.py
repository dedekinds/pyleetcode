class Solution(object):
    def sumeven(self,nums):
        ans = 0
        for i in range(len(nums)):
            if nums[i]%2 == 0:
                ans += nums[i]
        return ans
    
    def sumEvenAfterQueries(self, A, queries):
        """
        :type A: List[int]
        :type queries: List[List[int]]
        :rtype: List[int]
        """
        ans = []
        even = self.sumeven(A)
        for temp in queries:
            check = A[temp[1]] + temp[0]
            if A[temp[1]] % 2 == 0:
                if check %2 ==0:
                    tempres = even - A[temp[1]] + check
                else:
                    tempres = even - A[temp[1]]
            else:
                if check%2 == 0:tempres = even + check
                else:tempres = even
            ans.append(tempres)
            even = tempres
            A[temp[1]] = check
                

        return ans