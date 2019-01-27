找到另一种策略：和样例不一样的（一种排序的既视感
从大到小找到当前的最大值的index，然后将这个数放在首位
[3 2 4 1]→[4 2 3 1]
然后将这个数放在本来应该的位置

class Solution(object):
    def pancakeSort(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """
        ans = []
        for i in range(len(A),0,-1):
            ind = A.index(i)

            if i != A[0]:#已经在第一位的话不用动
                A = A[:(ind+1)][::-1] + A[(1+ind):]
                #print(A)
                ans.append(ind+1)
            if A[0] == 1:break
            ans.append(A[0])
            A = A[:A[0]][::-1] + A[A[0]:]
            #print(A)
        return ans

        