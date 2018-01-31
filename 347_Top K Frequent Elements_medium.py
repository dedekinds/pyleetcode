'''
347. Top K Frequent Elements
2018.1.31
'''
import collections
class Solution:
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
    #http://blog.csdn.net/lilingyu520/article/details/51339878
    #hash，得到<元素，频次>键值对
    #因为频次小于n，建散列表，即新建大小为n+1的数组，数组下标为频次，数组内容为有相同频次的键值list，对散列表按下标由大到小遍历，找出k个键值

        temp=collections.Counter(nums)
        n=len(nums)
        freq=[[] for i in range(n+1)]
        
        for p in temp:
            freq[temp[p]]+=[p]
        ans=[]
        for p in range(n,0,-1):
            ans+=freq[p]
        return ans[:k]


______________________________________
用超级技术

import collections
c=collections.Counter(nums)
return [x[0] for x in c.most_common(k)]