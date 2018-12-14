不太合格的做法，全复杂度是 O(n+klog(k))
用快速选择加局部快速排序，感觉不太好



import random
class Solution:
    def find_k(self,tinput,k):
        if len(tinput) == 0 or len(tinput) < k:
            return 
        temp = random.choice(tinput)
        num1 = []
        num2 = []
        for i in tinput:
            if i < temp:num1.append(i)
            elif i > temp:num2.append(i)
        if k <= len(num1): 
            return self.find_k(num1, k)
        if k > len(tinput) - len(num2):
            return self.find_k(num2, k - (len(tinput) - len(num2)))
        return temp
    
    def GetLeastNumbers_Solution(self, tinput, k):
        # write code here
        if len(tinput) == 0 or len(tinput) < k:
            return []
        res = []
        check = self.find_k(tinput,k)
        for i in range(len(tinput)):
            if tinput[i] <= check:
                res.append(tinput[i])
        return sorted(res)[:k]



应该用快速选择的思路+在原来的数组上操作，这样的话，当找到第k小的数的时候他左边的显然都是最小的k个数
import random
class Solution:
    def partition(self,array,l,r):
        x = array[r]
        i = l-1
        for j in range(l,r):
            if array[j] <= x:
                i+=1
                array[i],array[j] = array[j],array[i]
        array[i+1],array[r] = array[r],array[i+1]
        return i+1
    

    def GetLeastNumbers_Solution(self, tinput, k):
        if len(tinput) == 0 or len(tinput) < k:
            return []
        left = 0
        right = len(tinput)-1
        temp = self.partition(tinput,left,right)
        while temp != k-1:
            print(temp)
            if temp >= k-1:
                right = temp - 1
                temp = self.partition(tinput,left,right)
            else:
                left = temp + 1
                temp = self.partition(tinput,left,right)
        print(temp)
        return tinput[:k]

tinput = [4,5,1,6,2,7,3,10]
k = 6#8
T = Solution()
print(T.GetLeastNumbers_Solution(tinput, k))
   