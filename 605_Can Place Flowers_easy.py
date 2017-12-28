'''
605. Can Place Flowers
2017.12.28
'''
遍历一次贪心（下次可以尝试一下DP
class Solution:
    def canPlaceFlowers(self, flowerbed, n):
        """
        :type flowerbed: List[int]
        :type n: int
        :rtype: bool
        """
        length=len(flowerbed)
        flowerbed.append(0)
        cnt=0
        for x in range(length):
            if flowerbed[x]==0 and flowerbed[x-1]==0 and flowerbed[x+1]==0:
                cnt+=1
                flowerbed[x]=1
        if cnt>=n:
            return True
        else:
            return False
